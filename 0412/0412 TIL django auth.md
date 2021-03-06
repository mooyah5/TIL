# 0412 TIL django auth



### 인증 vs 권한

- 인증 Authentication
  - 신원 확인
  - 자신이 누군가라고 주장하는 사람의 신원을 확인하는 것
  - 출입증, 민증, 회사사원증, 놀이동산 이용권처럼 이 사람이 그 사람인지 확인
- 권한, 허가 Authorization 
  - 권한에 따라 할 수 있는 행동 허가 범위가 달라진다.
  - 클라이언트가 하려는 작업이 해당 클라이언트에게 허가된 작업인지 확인
  - 미성년자 - 주류판매 X / 성인 - 주류판매 O
  - 1급 비밀, 2급비밀 등
- 인증 후 인증된 사용자에 대한 권한을 부여한다.

인증 + 권한 => 보안

이러한 인증을 하도록 만든 것이 **쿠키**와 **세션**



### 쿠키 vs 세션 vs 캐시

- 쿠키는 for 로그인
  - 웹페이지를 받을 때의 정보를 쿠키에 담아 로컬에 저장하고 다시 요청 보내면 서버에서 쿠키 속 정보를 확인한다. 업뎃할 게 있으면 http header에 포함시켜서 응답합
  - 민감한 내용은 넣지 않는 게 좋음
- 세션
  - 사이트, 브라우저 간 상태 유지
  - Django : 특정 session id를 포함하는 쿠키를 활용하여 각 브라우저와 사이트가 연결된 세션을 알아낸다.
  - 쿠키에는 session id만 포함되어 있으며, 실제 데이터는 서버 db에 저장됨
- 캐시
  - css, js, 이미지 파일을 브라우저나 서버 단의 캐시 메모리에 저장하여 사용
  - 빠른 시일 내 재사용될 만한 것을 임시 저장하여 재요청이 들어왔을 때, 빠르게 + 서버를 거치지 않고 응답할 수 있음
  - 한 번 캐싱이 되면 브라우저를 참고하므로, 서버에서 변경이 일어나도 사용자는 마치 변경되지 않은 것처럼 느낄 수 있다.

---

### HTTP

로그인(인증)을 하기 위해 쿠키와 세션을 써야하는 이유가 바로 http의 특징 때문

1. HTTP

   - hyper text transfer protocol
   - html 문서와 같은 자원들을 가져올 수 있게 해주는 클라이언트, 서버간 프로토콜
   - 웹에서 이루어지는 모든 데이터 교환의 기초
   - ex) 자동차 이동(transfer)을 위한 교통 법규(protocol)의 존재처럼, html이 전송(transfer)되기 위한 http 규칙이 존재!
     - 프로토콜 : 규칙, 규약

2. 요청, 응답

   - 요청 request
     - 클라이언트(브라우저)에 의해 전송되는 메시지
     - 서버로 보내서 원하는 것을 받음(서버인 이모님께 삼겹살 2인분을 요청)
   - 응답 response
     - 서버가 응답전송하는 메시지
     - 요청이 오면, 요청에 맞게 클라이언트가 원하는 것을 전송
       - 구글 페이지 보여줘 => html 문서 (자원) 전송

3. 특징

   1. 비연결지향 connectionless
      - 서버는 클라이언트의 요청에 대한 응답을 보낸 후 연결을 끊는다.
   2. 무상태 stateless
      - 연결을 끊는 순간 서버 간 통신이 끝나며, **상태 정보가 유지되지 않음**
      - 클라이언트-서버 간 주고 받는 메시지들은 서로 완전히 독립적
      - 통신이 끝난 순간 서로의 상태정보를 가지지 않는다.

   - 이러한 HTTP의 두 가지 특징에 의거하여 웹사이트에는 클라이언트-서버 간 관계를 지속하기 위한 **쿠키, 세션**이 존재한다!! (로그인, 장바구니, 자동완성 등)



---

### 쿠키

1. 쿠키
   - 클라이언트(브라우저)의 로컬에 저장되는 key-value 형태의 작은 데이터 파일
   - 상태가 없는(stateless) HTTP 프로토콜에서 상태 정보를 저장하여 세션을 만듦
   - 두 요청이 동일 브라우저에서 왔는지 판단할 때 주로 사용됨
   - 사용자 인증에 유효한 시간이 명시되어 있을 시, 브라우저 종료 시에도 인증이 유지될 수 있다.

2. 구성요소
   - 이름 - 쿠키 구분
   - 값 - 쿠키 이름 관련 값
   - 유효시간 - 쿠키 유지시간
   - 도메인 - 쿠키를 전송할 도메인
   - 경로 - 쿠키를 전송할 요청 경로
3. 동작방식
   - 클라이언트 요청
   - 서버의 쿠키 생성
   - 서버가 http header에 쿠키를 포함시켜 응답
   - 브라우저 종료 시에도 쿠키 만료 기간이 남았을 경우 클라이언트 로컬에 보관
   - 같은 사용자의 요청 시 http header에 쿠키를 함께 보냄
   - 서버에서 쿠키를 읽어, 상태정보를 업데이트하여 변경된 쿠키를 http header에 포함시켜 재응답 (장바구니에 새 상품 추가)
4. 사용목적
   1. 세션 관리 session management
      - 로그인, 아이디 자동완성, 팝업 여부, 장바구니, 공지 하루만 보기 등의 정보 관리
   2. 개인화 Personalization
      - 테마, 사용자 선호 설정
   3. 트래킹 Tracking
      - 사용자 행동 기록, 분석
5. 장바구니 예시
   - SW가 아니므로 프로그램처럼 실행은 어렵고, 악성코드도 설치할 수는 없지만, 사용자 행동추적이나 사용자 행동을 추적하여 쿠키를 훔쳐내어 해당 사용자의 계정 접근권한 획득 가능성이 있음
   - response header에 `set-cookie` 속성을 지정하면 클라이언트에 쿠키를 만들 수 있으나, 쿠키는 사용자가 따로 요청하지 않아도 브라우저가 서버에 요청을 보낼 때 `request header`에 넣어서 자동으로 서버에 전송함
   - 서버 자원을 사용하지 않아 속도는 빠른데 보안문제가 있음 (최근에는 jwt를 사용)
   - 쿠키는 웹 사이트에서 여러 번 트랜잭션을 만드는 사용자를 추적하는 데 사용함

---

### 세션

1. 세션

   - 사이트, 특정브라우저 간 상태 유지

2. 동작방식

   1. 클라이언트가 서버 접속, 로그인하면 session id를 발급받음
   2. 클라이언트는 session id를 쿠키에 보관하여 로컬에 저장함
   3. 서버에 요청할 때, session id가 담긴 쿠키를 서버에 전달함
   4. 서버는 쿠키에 저장된 session id를 받아서, 서버 측 세션의 클라이언트 정보를 가져와 일치 여부를 판단함
   5. 일치하면 클라이언트에게 응답함 (로그인 / 로그인유지)

3. 특징

   - 사용자 정보를 클라이언트 로컬이 아니라 서버에 두기 때문에 보안상 좋음.
   - 사용자가 늘어나면 서버 메모리를 많이 차지함 (동접자수에 성능 반비례)

   - 클라이언트에게 고유 session id를 부여함
   - 보안우수
   - 서버메모리 차지