# 0515 TIL Vue.js (4) - Vue + API 서버



﻿

**목차**

- Server & Client
- CORS
- Authentication & Authorization
- JWT



---



## **Server & Client**



**Server**

클라이언트에게 정보, 서비스를 제공하는 컴퓨터 시스템

- 정보, 서비스
  - Django를 통해 응답한 template
  - DRF를 통해 응답한 JSON



**Client**

서버에게 그 서버가 제공하는 **서비스를 요청**하고

서비스 요청을 위해 필요한 인자를 **서버 요구 방식에 맞게 제공**하며

서버로부터 돌아오는 응답을 **사용자에게 적절하게 표현**하는 기능을 가진 시스템



**정리**

- **Server는 정보 제공**
  - DB와 통신하며 데이터를 CRUD
  - 요청을 보낸 Client에게 이러한 정보를 응답
- **Client는 정보 요청 & 표현**
  - Server에게 정보(데이터) 요청
  - 응답 받은 정보를 잘 가공하여 화면에 보여줌



## **CORS**



**Same-origin policy (SOP)**

**"동일 출처 정책"**

- 특정 출처(origin)에서 불러온 문서나 스크립트와 다른 출처에서 가져온 리소스와의 상초작용 제한 보안방식
- 잠재적 해로운 문서를 분리하여, 공격 경로를 줄임



**Origin (출처)**

두 url의 protocol, port, host가 모두 같아야 동일한 출처라 할 수 있음



**same-origin 예시**



<img src="https://blogfiles.pstatic.net/MjAyMjA1MTVfMjk3/MDAxNjUyNTY0NjIzNTMw.huxn0AJrIS2ipko4BJMBMEM_mfA87EgYlQbx8o7S7mIg.m6VOlC3xa8WE9pJX5QXlIkwNeiE6PiMavJ9in_5Yvy8g.PNG.baekhannah/image.png" alt="img" style="zoom:50%;" />





**Cross-Origin Resource Sharing (CORS)**

"교차 출처 리소스(자원) 공유"

- **추가 HTTP header를 사용**하여, 특정 출처에서 실행중인 웹 애플리케이션이 **다른 출처의 자원에 접근 할 수 있는 권한을 부여하도록 브라우저에 알려주는 체제**
- 리소스가 자신의 출처(도메인, 프로토콜, 포트)와 다를 때 교차출처 http 요청을 실행
- 보안상 이유로 브라우저는 교차출처 http 요청을 제한(SOP)
  - 예) XMLHttpRequest는 SOP를 따름
- 다른 출처의 리소스를 불러오려면 그 출처에서 올바른 CORS header를 포함한 응답을 반환해야 함



**CORS Policy**

교차 출처 리소스 공유 정책

다른 출처에서 온 자원공유에 대한 정책 <=> SOP



**교차 출처 접근 허용**

- CORS를 사용해 교차 출처 접근을 허용하기
- CORS는 HTTP의 일부로, 어떤 호스트에서 자신의 컨텐츠를 불러갈 수 있는지 서버에 지정할 수 있는 방법



**CORS 사용 이유**

**1. 브라우저와 웹 애플리케이션 보호**

- - 악의적인 사이트 데이터를 가져오지 않도록 사전 차단
  - 응답을 받는 자원에 대한 최소한의 검증
  - 서버는 정상 응답하지만 브라우저에서 차단

**2. 서버 자원 관리**

- - 누가 해당 자원에 접근할 수 있는지 관리 가능



**CORS 사용 방법**

- CORS 표준에 의해 추가된 HTTP Header를 통해 이를 통제



**Access-Control-Allow-Origin 응답 헤더**

- 이 응답이 주어진 출처로부터 요청코드와 공유될 수 있는지 나타냄
- 예
  - Access-Control-Allow-Origin: *
  - 브라우저 리소스에 접근하는 임의의 origin으로부터 요청을 허용한다고 알리는 응답에 포함
  - '*' 는 모든 도메인에서 접근 가능함을 의미
  - '*' 외에 특정 origin 하나를 명시할 수 있음



---

---



## **Authentication & Authorization**



**Authentication**

**인증, 입증**

- 자신이라고 주장하는 **사용자가 누구인지 확인**하는 행위
- 모든 보안 프로세스의 첫 단계 (가장 기본적인 요소)
- 즉 내가 누규? 인지 확인하는 과정
- **401 Unauthorized** **-** 비록 HTTP 표준에서는 미승인 하고 있지만, 의미상 이 응답은 **비인증**을 의미한다.



**Authorization**

**권한 부여, 허가**

- 사용자에게 특정 자원이나 기능 **액세스 권한 부여** 과정 (절차)
- 보안환경에서 권한 부여는 항상 인증 필요
  - 예) 사용자는 조직 액에스 권한 부여 받기 전에 먼저 자신의 ID가 진짜인지 확인 받아야 함
- 서류 등급, 웹페이지 CRUD 방법, 제한구역
  - 인증이 됐어도 모든 권한을 받는 건 아니잖아?
- **403 Forbidden** - 401과 다른 점은 서버는 클라이언트가 누군지 알고 있음





**정리**

- **Authentication (인증)**
  - 자신이라고 주장하는 유저 확인
  - Credentials (비번, 얼굴인식) 검증
  - 장고 -> 게시판 서비스 로그인
  - 인증 이후 권한 획득 (생성, 수정, 삭제)
- **Authorization (권한, 허가)**
  - 유저의 자원 접근 가능 여부 확인
  - 규칙/규정에 의해 접근할 수 있는지 확인
  - 장고 -> 일반유저 vs 관리자 유저
  - 인증 이후 권한 부여 (예: 로그인 후 글 작성 가능)





**Authentication & Authorization work together**

회원 가입 및 로그인 하면 할 수 있는 권한 생성

인증 이후 권한이 따라오는 경우가 많음

단, 모든 인증을 거쳐도 권한이 동일하게 부여되는 건 아님

장고에서 로그인했다고 해도, 다른 사람 글까지 수정/삭제는 안되잖아



세션, 토큰, 제3자를 활용하는 등 다양한 방식의 인증 방식이 존재

---



## **DRF Authentication**



**다양한 인증 방식**

1. **Session Based**
2. **Token Based** (Basic Token, JWT)
3. **Oauth** (google, facebook, github...)





---

---







**JWT**

JSON Web Token

- JSON 포맷을 활용하여 요소 간 안전하게 정보를 교환하기 위한 표준 포맷
- 암호화 알고리즘에 의한 디지털 서명이 되어 있으므로 JWT 자체로 검증 가능
- JWT 자체가 필요한 정보를 모두 갖기 때문에(self-contatined) 이를 검증하기 위한 다른 검증 수단이 노 필요
- 사용처 - Authentication, Information Exchange



**JWT 특징**

- JWT는 DB에서 유효성 검사가 필요 없음
- JWT 자체가 인증에 필요한 정보를 모두 갖기 때문 (Self-contained)
- 이것은 세션이나 기본 토큰 기반의 인증과의 핵심적인 차이점임
- 토큰을 탈취할 경우 서버 측에서 토큰 무효화 불가능 (블랙리스팅 테이블)
- 매우 짧은 유효기간(5분)과 Refrech 토큰을 활용하여 구현
- MSA (Micro Server Architecture) 구조에서 서버간 인증에 활용
- One Source (JWT) Multi Use 가능





## **dj-rest-auth & django-allauth 라이브러리**



```javascript
$ pip install django-allauth
$ pip install dj-rest-auth
```

**settings.py**



![img](0515 TIL Vue.js (4) - Vue + API 서버.assets/image-16525665414262.png)



**urls.py**



![img](0515 TIL Vue.js (4) - Vue + API 서버.assets/image-16525665580824.png)



﻿