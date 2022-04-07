# django form

1. Read (index)

   ![image-20220407114039051](Workshop.assets/image-20220407114039051.png)

2. CREATE

   ![image-20220407114142566](Workshop.assets/image-20220407114142566.png)

3. DETAIL

   ![image-20220407114206730](Workshop.assets/image-20220407114206730.png)

4. UPDATE

   ![image-20220407114241020](Workshop.assets/image-20220407114241020.png)

   ![image-20220407114249842](Workshop.assets/image-20220407114249842.png)

   ![image-20220407114258869](Workshop.assets/image-20220407114258869.png)

5. DELETE

   No.6 삭제하기

   ![image-20220407114325956](Workshop.assets/image-20220407114325956.png)

   삭제 확인

   ![image-20220407114337980](Workshop.assets/image-20220407114337980.png)

---

코드, 순서

- 가상환경 설정 및 활성화
- 필요 pip install
- django-admin startproject crud .
- python manage.py startapp articles
- settings.py  - app등록, ko-kr, Asia-Seoul, 템플릿dirs : [BASE_DIRS / 'templates']
- templates 폴더 생성 + base.html 작성

1. base.html

   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
     <meta charset="UTF-8">
     <meta http-equiv="X-UA-Compatible" content="IE=edge">
     <meta name="viewport" content="width=device-width, initial-scale=1.0">
     <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
     <title>Document</title>
   </head>
   <body>
     {% block content %}
     {% endblock content %}
     <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
   </body>
   </html>
   ```

   - ! + tab

   - head에 bootstrap 링크

   - body에 block content 지정

   - body 바닥에 bootstrap 링크

   

   - 서버동작 확인 python manage.py runserver 나가기는 ctrl+C

2. articles/models.py

   ```python
   from django.db import models
   
   # Create your models here.
   class Article(models.Model):
       title = models.CharField(max_length=10)
       content = models.TextField()
       created_at = models.DateTimeField(auto_now_add=True)
       updated_at = models.DateTimeField(auto_now=True)
   
   def __str__(self):
       return f'{self.pk} - {self.title}'
   ```

   - Article이라는 모델 생성(title, content, created_at, updated_at)
   - str형식으로 표현되도록

3. articles/admin.py

   ```python
   from django.contrib import admin
   from .models import Article
   
   # Register your models here.
   class ArticleAdmin(admin.ModelAdmin):
       list_display = ['pk', 'title', 'created_at', 'updated_at']
       
   admin.site.register(Article, ArticleAdmin)
   ```

   - 관리자 페이지 등록

   - list_display로 관리자 페이지에 드러낼 요소 등록(content 제외)

   - 관리자 계정 생성 python manage,py createsuperuser

     ![image-20220407120242541](Workshop.assets/image-20220407120242541-16493006457512.png)

4. crud/urls.py

   ```python
   from django.contrib import admin
   from django.urls import path, include
   
   urlpatterns = [
       path('admin/', admin.site.urls),
       path('articles/', include('articles.urls')),
   ]
   ```

   - articles/urls.py로 include

5. articles/urls.py 파일 생성

   ```python
   from django.urls import path
   from . import views
   
   app_name = 'articles'
   urlpatterns = [
       path('', views.index, name='index'),
       path('new', views.new, name='new'),
       path('<int:pk>/', views.detail, name='detail' ),
       path('<int:pk>/edit/', views.edit, name='edit'),
       path('<int:pk>/delete/', views.delete, name='delete'),
   ]
   ```

   - index 페이지는 메인페이지라서 따로 url 지정 X
   - detail, edit, delete는 한 게시물에 대한 내용을 담거나 db를 수정하므로 `<int:pk>`를 url에 지정

6. articles/views.py

   ```python
   from django.shortcuts import render, redirect
   from .models import Article
   from .forms import ArticleForm
   
   # Create your views here.
   def index(request):
       articles = Article.objects.order_by('-pk')
       context = {
           'articles' : articles
       }
       return render(request, 'articles/index.html', context)
   
   def new(request):
       if request.method == 'POST':
           form = ArticleForm(request.POST)
           if form.is_valid(): # 유효성 통과하면
               article = form.save()   # 저장하고
               return redirect('articles:detail', article.pk ) # 디테일 페이지 보여줘
       else:
           form = ArticleForm()
       context = {
           'form' : form,
       }
       return render(request, 'articles/new.html', context)
       
   def detail(request, pk):
       article = Article.objects.get(pk=pk)
       context = {
           'article' : article,
       }
       return render(request, 'articles/detail.html', context)
   
   def edit(request, pk):
       article = Article.objects.get(pk=pk)
       if request.method == 'POST':
           form = ArticleForm(request.POST, instance=article)
           if form.is_valid(): 
               article = form.save() 
               return redirect('articles:detail', article.pk )
       else:
           form = ArticleForm(instance=article)
       context = {
           'article' : article,
           'form' : form,
       }
       return render(request, 'articles/new.html', context)
       
   def delete(request, pk):
       article = Article.objects.get(pk=pk)
       if request.method == 'POST':
           article.delete()
           return redirect('articles:index')
       else:
           redirect('articles:detail', article.pk)
   ```

   - index는 새로 생성된 게시물이 상단에 보이도록 order_by('-pk') 으로 pk 내림차순 지정

   - new(create)는 원래 if POST에서

     ```python
     title = request.POST.get('title')
     content = request.POST.get('content')
     article = Article(title=title, content=content)
     article.save()
     ```

     으로 지정되었다가, forms.py로 형식이 변경되면서 냅다 form = ArticleForm(request.POST)으로 바꾸고 유효성 검사

   - edit에서는 new(create)와 다르게 article 변수에 pk 데이터를 담아서 instance=article을 지정

7. articles/forms.py 파일 생성

   ```python
   from django import forms
   from .models import Article
   
   class ArticleForm(forms.ModelForm):
       
       class Meta:
           model = Article
           fields = '__all__'
           # exclude = ['content', ] # content만 빼고 나머지 다
   ```

   django form형식으로 바꿔서 html에서 매번 동일 문구 중복 작성하지 않도록

8. templates/articles/

   1. index.html

      ```html
      {% extends 'base.html' %}
      
      {% block content %}
        <h1>INDEX</h1>
        <a href="{% url 'articles:new' %}">NEW</a>
        <hr>
        <ul>
          {% for article in articles %}
            <li>No.{{ article.pk }} - 제목: <a href="{% url 'articles:detail' article.pk %}">{{ article.title }}</a></li>
            <p> 내용 : {{ article.content }}</p>
          {% endfor %}
        </ul>
      {% endblock content %}
      ```

   2. new.html

      ```html
      {% extends 'base.html' %}
      
      {% block content %}
        <h1 class="text-center">CREATE</h1>
        <hr>
        <form action="" method='POST'>
          {% csrf_token %}
          {% comment %} 제목 : <input type="text" name="title"><br>
          내용 : <textarea name="content" id="" cols="30" rows="10"></textarea> {% endcomment %}
          {{ form.as_p }}
          <input type="submit" value="제출">
        </form>
        <hr>
        <a href="{% url 'articles:index' %}">목록으로</a>
      {% endblock content %}
      ```

   3. detail.html

      ```html
      {% extends 'base.html' %}
      
      {% block content %}
        <h1>DETAIL</h1>
        <hr>
          <h3>N.{{ article.pk }}번 게시글 - {{ article.title }}</h3>
          <p>내용: {{ article.content }}</p>
          <p>작성 : {{ article.created_at }}</p>
          <p>수정: {{ article.updated_at }}</p>
        <hr>
        <a href="{% url 'articles:edit' article.pk %}">수정하기</a>
        <form action="{% url 'articles:delete' article.pk %}" method='POST'>
          {% csrf_token %}
          <button class='btn btn-danger'>삭제하기</button>
        </form>
        <a href="{% url 'articles:index' %}">목록으로</a>
      {% endblock content %}
      ```

      삭제 버튼은 form으로 보내서 post - csrf토큰 검사 해줌

   4. edit.html

      ```html
      {% extends 'base.html' %}
      
      {% block content %}
        <h1 class="text-center">UPDATE</h1>
        <hr>
        <form action="" method='POST'>
          {% csrf_token %}
          {% comment %} 제목 : <input type="text" name="title" value="{{ article.title }}"><br>
          내용 : <textarea name="content" id="" cols="30" rows="10">{{ article.content }}</textarea> {% endcomment %}
          {{ form.as_p }}
          <input type="submit" value="제출">
        </form>
        <hr>
        <a href="{% url 'articles:detail' article.pk %}">목록으로</a>
      {% endblock content %}
      ```

      