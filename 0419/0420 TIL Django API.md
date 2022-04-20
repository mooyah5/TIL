# 0420 TIL Django API





## API

Application PRogramming Interface



프로그래밍 언어가 제공하는 기능을 수행할 수 있게 만든 인터페이스

프로그램을 연결시킬 수 있는 **다리**를 만드는 역할

남들이 만들어놓은 모듈을 사용할 수 있음

"바퀴를 다시 만들지 마라" = 남들이 만들어 놓은 거 재활용 해라(프로그래밍의 강력함을 나타내는 단어)

- 네이버 지도, 카카오페이, SNS 로그인, youtuveAPI (추후 vue.js로 유튜브 따라만들기 할 것)

CLI 커맨드(명령어)

GUI 그래픽(마우스)

API 어플리케이션





## REST

- REpresentational State Transfer

- API 서버 개발을 위한 일종의 SW 설계 방법론 (라면 끓일 때 면부터 넣어, 스프부터 넣어)
- 네트워크 구조 원리의 모음
  - 자원 정의, 자원에 대한 주소 지정
- REST 원리를 따라는 시스템을 RESTful이라는 용어로 지칭함
- 자원 정의 방법(어디에 위치 시킬 것인가 등) 주소체계 정의 방법 중 하나?

진짜 restful한 거는, 실제로 그렇게 엄격하게 지켜지지는 않음.

그런 REST API로 괜찮은가(naver d2) [(17) Day1, 2-2. 그런 REST API로 괜찮은가 - YouTube](https://www.youtube.com/watch?v=RP_f5dMoHFc)



- 자원과 주소의 지정 방법
  1. 자원 : URI(자원이 어디에 있는지에 대한 정보를 표현)
  2. 행위 : HTTP method(자원에 뭘 할지)
  3. 표현 : 결과물
     - 자원과 행위를 통해 궁극적으로 표현되는 결과물
     - JSON으로 표현된 데이터를 제공



## HTTP

요청과 응답

이거 이해하면 됨

요청을 이렇게 보내고 응답을 이렇게 받음

GEt, path이렇게 있고 header가 따로 있음



HTTP method : GET, POST, DELETE, UPDATE 있는데 회사마다 다르기도 함



### HTTP response status codes (중요)

1. 정보제공
2. 성공
3. redirect
4. 사용자 탓 (니탓)
5. 서버 탓 (내탓, I'm sorry)



### 웹에서의 리소스 식별

- HTTP 요청 대상을 자원이라고 하는데, 
- 어쩌구
- 사실 URI는 수업자료에 URI vs URL vs URN
- W3C 웹표준만드는 단체인데, 보통 URI 잘 안쓰고, URI라는 체계 안에 URL, URC, URN, DATA URI l있는데, 
- ![image-20220420125820618](C:\Users\baekh\AppData\Roaming\Typora\typora-user-images\image-20220420125820618.png)
- 전부 다 URI고 부분적으로 나뉨
- Protocol            // HOST                 :PORT     /PATH             QueryString                            Fragment
- https                  ://127.0.0.1           :8000      /articles/3      ?q="검색어"&title="제목"      #content



- Protocol (https)
  - 브라우저가 사용해야 하는 프로토콜(규칙)
- HOST (://)
  - 요청을 받는 웹 서버
- PORT (:)
  - 웹 서버 안 리소스에 접근하는데 사용되는 기술적인 문(door) 번호
  - 예) 장고 서버 안에 여러 개가 있으면 그중에 어디로 갈지! (python manage.py runserver 8080로 포트번호 직접 지정 밑 동시 run 가능)
- PATH (/)
  - 웹 서버 상의 리소스 경로 (articles)
- Query String Parameter (?)
  - 웹 서버에 제공하는 추가적인 데이터
  - `&`로 구분되는 key-value 쌍
- Fragment (#)
  - HTML 문서의 특정 부분을 보여주기 위한 방법
  - 요청을 보내는 건 아니고, 페이지 내에서 가르키도록 되어 있는 것
  - **부분식별자**라고 불림





## Response

장고 시드로 더미데이터 만들고,

- JS response

- 직렬화



### 직렬화 (Serialization)

서버와 프로그램 간 다리가 API라고 했을 때,

우리 서버는 Python을 쓰는데, 저기는 Java를 쓸 때, 통신하고 싶을 경우

이때 쓰는 포맷이 JSON

왜냐하면 대부분의 언어에는 딕셔너리 같은 모양의 key-value로 되어있는 게 많기 때문임!

이러한 JSON을 하는 과정을 직렬화라고 함

python list나 queryset 들을 JSON으로 바꾸는 과정! (다른 언어와 통신하기 위해)



#### Serializers in Django

장고에는 이걸 통해 JSON모양으로 도장처럼 찍어누를 수 있음

model form 이랑 거의 비슷함



### DRF Django REST Framework

DRF를 통해서 RESTful한 API서버를 만들 수 있음

예시)![image-20220420132039716](C:\Users\baekh\AppData\Roaming\Typora\typora-user-images\image-20220420132039716.png)



#### 역직렬화

넣을 때는 직렬화라면, 뺄 때는 역직렬화

