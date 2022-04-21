# 0421 django api

$ python -m venv venv

$ source venv/Scripts/activate

$ pip install django django-seed djangorestframework django-extensions ipython

$ pip freeze > requirements.txt

$ django-admin startproject my_api .

$ python manage.py startapp articles



settings.py

```python
INSTALLED_APPS = [
    'articles',
    'django_seed',
    'django-extensions',
    'rest_framework',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```



my_api/urls.py

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('articles.urls')),
]
```



app_name 사용 이유가 redirect인데, 이거는 html보여주지 않고 data만 보여주기 때문에, 쓸 일이 없음

```python
from django.urls import path
from . import views

urlpatterns = [
    
]
```



articles/models.py

```python
from django.urls import path
from . import views

urlpatterns = [
]

```



articles/models.py

```python
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100) # CharField 최대 길이 필수
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)    # create니까 add가 붙음
    updated_at = models.DateTimeField(auto_now=True)
```



articles/serializers.py

```python
# articles/serializers.py

from rest_framework import serializers
from .models import Article

class ArticleListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields = '__all__'
```



urls.py

```python
from django.urls import path
from . import views

urlpatterns = [
    path('json-3/', views.article_json_3),
]
```



views.py

```python
from django.shortcuts import render
from .models import Article
from .serializers import ArticleListSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view  
# Create your views here.

@api_view(['GET']) # get방식으로만 응답하도록 처리
def article_json_3(request):
    articles = Article.objects.all()
    serializers = ArticleListSerializer(articles, many=True)
    return Response(serializers.data)
```



runserver

POSTMAN

![image-20220421093707555](C:\Users\baekh\AppData\Roaming\Typora\typora-user-images\image-20220421093707555.png)



사용자에게 보여줄 필드 수정하려면 serializers.py에서 필드 수정

```python
# articles/serializers.py

from rest_framework import serializers
from .models import Article

class ArticleListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields = ('title', 'content',)
```

![image-20220421093807456](C:\Users\baekh\AppData\Roaming\Typora\typora-user-images\image-20220421093807456.png)

serializers 쓰면 db에서 바꿔주네

---

[추가 참고사항]

python manage.py shell_plus

- ArticleListSerializer 불러오기

In [1]: from articles.serializers import ArticleListSerializer        

In [2]: serializer = ArticleListSerializer()	

(아티클리스트시리얼라이저를 인스턴스화)

In [3]: serializer
Out[3]: 
ArticleListSerializer():
    title = CharField(max_length=100)
    content = CharField(style={'base_template': 'textarea.html'})  

- 하나의 데이터를 불러와서(1번게시글) 직렬화 하기

In [4]: article = Article.objects.get(pk=1)

In [5]: article
Out[5]: <Article: Article object (1)>

In [6]: serializer = ArticleListSerializer(article)	# 재료(article)을 넣어서 도장찍기

In [7]: serializer
Out[7]: 
ArticleListSerializer(<Article: Article object (1)>):
    title = CharField(max_length=100)
    content = CharField(style={'base_template': 'textarea.html'}) 

In [8]: serializer.data
Out[8]: {'title': 'Born trouble head.', 'content': 'Score suddenly bag system parent citizen. Point ahead establish mention tell sea various. Old local name nearly enter scene prove.'}

- 여러 개의 데이터를 직렬화하기

In [9]: articles = Article.objects.all()

In [10]: serializer = ArticleListSerializer(articles, many=True)  # 여러 개 직렬화 시 many=True 옵션 필수

In [14]: serializer
Out[14]: 
ArticleListSerializer(<QuerySet [<Article: Article object (1)>, <Article: Article object (2)>, <Article: Article object (3)>, <Article: Article object (4)>, <Article: Article object (5)>, <Article: Article object (6)>, <Article: Article object (7)>, <Article: Article object (8)>, <Article: Article object (9)>, <Article: Article object (10)>, <Article: Article object (11)>, <Article: Article object (12)>, <Article: Article object (13)>, <Article: Article object (14)>, <Article: Article object (15)>, <Article: Article object (16)>, <Article: Article object (17)>, <Article: Article object (18)>, <Article: Article object (19)>, <Article: Article object (20)>]>, many=True):
    title = CharField(max_length=100)
    content = CharField(style={'base_template': 'textarea.html'})     

In [15]: serializer.data
Out[15]: [OrderedDict([('title', 'Born trouble head.'), ('content', 'Score suddenly bag system parent citizen. Point ahead establish mention tell sea various. Old local name nearly enter scene prove.')]), OrderedDict([('title', 'Available heart condition college interview should treatment.'), ('content', 'Morning miss no idea surface product lose family. Bill newspaper upon interest father.\nLose foot break outside. Middle moment degree body rather.')]), OrderedDict([('title', 'Civil throw look policy main reveal you near.'), ('content', 'Fight drop require. Fly different range book catch. Recent sound put fear reveal.\nWar certain avoid these some effort. Land look citizen easy.')]), OrderedDict([('title', 'Something tonight interview old six as attack.'), ('content', 'Who possible mother will ground group need. Offer give certain response. Science stay attack official that kind happen. Officer rather send become wife us.')]), OrderedDict([('title', 'Can whether create need blue increase share.'), ('content', 'Against face reveal job.\nSouth understand price sell. Add operation case actually defense.')]), OrderedDict([('title', 'Fast case nice sign.'), ('content', 'Toward TV technology tough democratic need everything mother.\nTown study of treat child exactly exactly. Shoulder investment which financial.')]), OrderedDict([('title', 'Go wife half central though policy student.'), ('content', 'Film try give risk suggest hot. Social travel particular human marriage. Ground along name nice air year add age.')]), OrderedDict([('title', 'Still executive body three.'), ('content', 'Vote blood week subject apply. Force thank dream population.\nBoy identify country two top. Theory story Mr resource.')]), OrderedDict([('title', 'Something store issue six growth him black.'), ('content', 'Already open environment. Sort boy think throughout. Economy against heart.\nOpen station trip guess shoulder. Later produce whom stuff pass decade.\nOr along wall. Go sound usually use.')]), OrderedDict([('title', 'Base wonder generation less blue.'), ('content', 'Draw explain arrive always show shoulder coach front. Drug resource way raise end training.')]), OrderedDict([('title', 'Assume idea surface under arm popular.'), ('content', 'Individual serious indicate themselves check fast. Bad vote community they.')]), OrderedDict([('title', 'Long make early seat whatever represent.'), ('content', 'Within feel marriage girl plan later baby.\nCommon some most production. Nor away exist official model although learn. Quickly item scene few continue.')]), OrderedDict([('title', 'Training company table.'), ('content', 'Its civil base international city recently food sort. Court open nearly.\nTask someone sell major hospital area player. Say just involve. Small since every ok have take.')]), OrderedDict([('title', 'News PM family own worry claim.'), ('content', 'Lose class guy despite people treat. Energy particularly risk party keep different. Trouble already seat glass.\nStandard and walk safe.')]), OrderedDict([('title', 'Three set over song teacher allow tree.'), ('content', 'Positive apply Mr relationship born. Until including option stay speak body.\nPerhaps few capital nice. Wrong worker western maybe say heart enough.')]), OrderedDict([('title', 'Four bad when character.'), ('content', 'Occur wrong manage. Nation view mention. Finish side put.\nPick face deep above follow push responsibility. Peace case development during do possible. Its ready shoulder than work safe research try.')]), OrderedDict([('title', 'Sometimes per live history keep affect.'), ('content', 'Bar recognize just whether forward. Whatever bag owner baby material response detail.\nDuring it production anyone woman young matter. Parent finish through. Easy student south.')]), OrderedDict([('title', 'Dinner central family this artist here pass.'), ('content', 'Assume marriage exist practice seat. Data seat then investment.\nEat audience clearly involve order argue attack. Home role modern special test well throughout. Require environment everyone.')]), OrderedDict([('title', 'Heavy hold book black carry.'), ('content', 'Detail population physical worry area. Major stage star about single impact. Political keep process.\nType like behind painting ago fill bill. Network better consumer son continue evening walk.')]), OrderedDict([('title', 'Chance red conference pay this boy act.'), ('content', 'Store door condition cause resource in. Teacher I either thought order. Its customer state live arm paper everybody third.\nHimself skin wife member simply each. Growth camera several.')])]

---

