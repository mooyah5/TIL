# 목차

- HTML
  - 기본구조
  - 문서 구조화
- CSS
- CSS Selectors
- CSS 단위
- Selectors 심화
- Box model
- Display
- Position



### 현재 웹 표준

웹 표준 : WWW(world wide web) 구현 위해 따라야 할 표준 또는 규격.

- W3C - 국제표준화기구, 월드 와이드 웹 컨소시엄
  - HTML5 - 하이퍼텍스트생성언어
- WHATWG - 웹 하이퍼텍스트 애플리케이션 테크놀로지 워킹 그룹 (이전에 HTML5로 알려진, 웹 어플리케이션1.0)
  - HTML Living Standard (apple, google, ms, mozilla)

→ 현재는 주도권 싸움에서 WHATWG 승리



### Browser

익스플로러X

크롬 O





## 개발 환경 설정

- VSCode
- 크롬 개발자 도구
  - Elements - DOM 탐색 및 CSS 확인 및 변경
    - Styles - 요소에 적용된 CSS 확인
    - Computed - 스타일이 계산된 최종 결과
    - Event Listners - 해당 요소에 적용된 이벤트 (JS)
  - Soueces, Network, Performence 등





## HTML

Hyper Text Markup Language

Hyper Text: 참조(하이퍼링크)를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트. 비 선형적.

Markup Language: 태그 등을 이용하여 문서, 데이터 구조를 명시하는 언어 (예. HTML, Markdown)



### HTML 기본 구조

- html : 문서 최상위(root) 요소
- head : 문서 메타데이터 요소
  - 문서 제목, 인코딩, 스타일, 외부 파일 로딩 등
  - 일반적으로 브라우저에 나타나지 않는 내용
- body : 문서 본문 요소
  - 실제 화면 구성 관련 내용



### DOM(Document Object Model) 트리

- 텍스트 파일인 HTML 문서를 브라우저에서 렌더링 하기 위한 구조
  - 문서 모델 구성
  - 문서 내 각 요소에 접근하고, 수정에 필요한 property와 method를 제공



### 요소 (element)

![Untitled.png (672×147)](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/4586e40d-ccd4-4469-a7b1-b9ec7e3a83ae/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220202T104647Z&X-Amz-Expires=86400&X-Amz-Signature=599564797aa81b0ca1d9665526448f959ceb989d7a8de258e34a434ea89a9885&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

HTML의 요소는 태그와 내용으로 구성됨

- HTML 요소는 시작, 종료태그, 태그 사이 내용으로 구성
  - 태그(요소)는 내용을 감싸는 것으로, 그 내용의 성격과 의미를 정의함
- 내용 없는 태그
  - br, hr, img, input, link, meta
- 요소는 중첩(nested)될 수 있다
  - 요소들이 다른 요소들을 포함할 수 있다
  - 요소 중첩으로 하나의 문서를 구조화
  - 여는, 닫는 태그의 ‘쌍’ 확인!
    - 오류 반환이 아니라, 걍 레이아웃이 깨져서 출력되므로, 디버깅 힘들어짐



### 속성(attribute)

![Untitled.png (1441×254)](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/73097f53-7c93-4a8f-ae27-b84221f5fbcf/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220202T104703Z&X-Amz-Expires=86400&X-Amz-Signature=1f57455cf1e52d927ad480885f52dcfff08f8040038a8e50abab4513fffd944e&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

태그별로 사용 가능한 속성이 다름

- 속성으로 태그의 부가정보 설정 가능
- 요소는 속성 가질 수 있음. 경로, 크기 등 추가정보 제공
- 요소 시작 태그에 작성. 보통 이름=값이 쌍으로 존재
- 태그 상관 없이 사용가능 속성도 있음 (HTML Global Attribute)
  - id : 문서 전체에서 유일한 고유 식별자 지정
  - class : 공백으로 구분된 해당 요소의 클래스 목록
  - data-* : 페이지에 개인 사용자 정의 데이터 저장 위해 사용
  - style - inline
  - title : 요소 추가 정보 지정
  - tabindex - 요소 탭 순서
- 속성 작성 방식 통일하기
  - 공백 X
  - 쌍따옴표

![Untitled.png (495×381)](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/cab1a2b7-2336-4e0c-a87d-597584914bbe/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220202T104715Z&X-Amz-Expires=86400&X-Amz-Signature=498bd118fe64995c2769d13134b40c5366fc8b544cfbca7035c9db6d8f1eb5ec&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)



### 시맨틱 태그

- HTML5에서 의미론적 요소를 담은 태그의 등장
  - 기존 영역을 의미하는 div 태그를 대체해서 사용
- 대표적인 태그 목록
  - header : 문서 전체나 섹션의 헤더(머리말)
  - nav : 네비
  - aside : 사이드에 위치한 공간, 메인 콘텐츠와 관련성 적은 콘텐츠
  - section : 문서의 일반적인 구분, 컨텐츠의 그룹을 표현
  - article : 문서, 페이지, 사이트 안에서 독립적으로 구분되는 영역
  - footer : 문서 전체나 섹션의 푸터(마지막)
- Non senmantic 요소는 div, span 등이 있음
- h1, table 태그들도 시맨틱 태그로 볼 수 있음
- 개발자, 사용자, 검색엔진 등에 의미있는 정보 그룹을 태그로 표현
- 단순 구역 구분 뿐 아니라 ‘의미’를 가지는 태그를 활용하기 위한 노오력
- 요소 의미 명확성, 코드가독성 증가, 유지보수 easy
- 검색엔진최적화(SEO)를 위해서 메타태그, 시맨틱 태그 등을 통한 마크업 효과적 활용해야 함





## HTML 문서 구조화



### 인라인/블록 요소

CSS에서 다룸



### 텍스트 요소

- <a></a> : **하이퍼링**크 생성. href 속성 활용
- <b></b> : **굵은** 글씨
- <strong></strong> : 강조 요소 (굵)
- <i></i> : **기울임** 글씨
- <em></em> : 강조요소(보통 기울임)
- <br> : 텍스트 내 **줄바꿈** 생성
- <img> : **이미지**. src 속성 활용
- <span></span> : 의미 없는 인라인 컨테이너



### 그룹 컨텐츠

- <p></p> : 하나의 문단

- <hr> : 수평선. 문단 분리

- <ol></ol> : 순서 有 (1, 2, 3)

- <ul></ul> : 순서 無 (-)

- <pre></pre> : 그대로. 고정폭 글꼴, 공백문자 유지

- <blockquote></blockuote> : 긴 인용문, 주로 들여쓰기

- <div></div> : 의미 없는 블록 레벨 컨테이너



### table

- table의 각 영역 명시를 위해 `<thead>` `<tbody>` `<tfoot>`요소 활용

![Untitled.png (602×327)](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/7133f871-9da6-4d39-b746-c0c07459f8a4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220202T104744Z&X-Amz-Expires=86400&X-Amz-Signature=c19fb760ebc401f6cdf73caff86852effae1f2097caf1225b6a9c68d59d17306&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

- `<tr>`으로 가로 줄 구성

- 내부에는 `<th>`, `<td>`로 셀 구성

  - thead : tr → th

  - tbody : tr → td

  - tfoot : tr → td

  - caption

    ![Untitled.png (711×335)](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/0e1c4450-7bcf-4237-a65a-0f320bacf9c7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220202T104752Z&X-Amz-Expires=86400&X-Amz-Signature=4589b7accc1ea4e7ff84334302530a734acdf58314945c673f44399ebb0ac216&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

- colspan, rowspan : 셀 병합

  ![Untitled.png (641×306)](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/dba89bde-541a-43c7-82dc-089b90333d5c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220202T104807Z&X-Amz-Expires=86400&X-Amz-Signature=6959a537284dd8fd975727e1e3cdbc20dc6d399233f211d5756a60b4bf9fec28&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

- <caption> : 설명, 제목

  ![Untitled.png (460×327)](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/8c73a246-d17d-456a-bce9-38c0c504e1db/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220202T104817Z&X-Amz-Expires=86400&X-Amz-Signature=2b5f4f0f81a743d8d4d200b1513b134606f2c488b44d04a8ea12c66d7514da9d&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)



### form

- `<form>`
- 정보(데이터)를 서버에 제출하는 영역
- 기본 속성
  - action : 처리 서버 URL
  - method : form 제출 시 사용할 HTTP 메서드(GET or POST)
  - enctype : method가 post인 경우 데이터 유형



### input

- 다양한 타입을 가지는 입력 데이터 유형, 위젯 제공
- 속성
  - name : form control에 적용되는 이름(이름/값 페어)
  - value : form control에 적용되는 값 (이름/값 페어)
  - required, readonly, autofocus, autocomplete, disabled

![Untitled.png (591×392)](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/a439920a-1f4a-4ba3-a08c-c155faef91b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220202T104929Z&X-Amz-Expires=86400&X-Amz-Signature=3288faa4f71219282f37acb2fbac2aca13aea36c3d0a43328e5088fbee8ae009&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)



### input label

- label을 클릭하여 input 자체의 초점을 맞추거나 활성화
  - 사용자는 선택 가능 영역 증가로 웹, 모바일 환경에서 편하게 사용 가능
  - label과 input 입력 관계가 시각적일 뿐만 아니라 화면 리더기에서도 라벨을 읽어 쉽게 내용 확인 가능하도록
- <input>← id 속성
- <label> ← for 속성
  - 상호 연관

![Untitled.png (725×119)](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/a383e33f-869e-40dc-aeea-06c85161960d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220202T104943Z&X-Amz-Expires=86400&X-Amz-Signature=e91962e088a88944b7763142b0bc269888caf80ce251459520f553ca6d2f0716&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

---



### input 유형 - 일반

- 일밙거으로 입력 받기 위해 제공됨
- 타입별로 HTML 기본 검증 or 추가 속성 활용 가능
  - text : 일반 텍스트 입력
  - password : 입력 시 값이 안 보이고 문자를 특수기호로 표현(*)
  - email : 이메일 형식 아니면 form 제출 불가
  - number : min, maxm step 속성으로 숫자 범위 설정 가능
  - file : accept 속성으로 파일 타입 지정



### input 유형 - 항목 중 선택

- label로 내용을 작성하여 항목 선택 가능
- 동일 항목에 대해서는 name을 지정해서 선택된 항목에 대한 value 지정 필요
  - checkbox - 다중선택
  - radio - 단일선택



### input 유형 - 기타

- 다양한 종류의 input을 위한 picker 제공
  - color
  - date
- hidden input으로 사용자 입력 안 받고 서버에 전송되어야 하는 값 설정
  - hidden : 사용자에게 안 보이는 input



### input 유형 - 종합

- `<input>` 요소의 동작은 타입 따라 달라지므로, 각 내용을 숙지해라
- [링크](https://developer.mozilla.org/ko/docs/Web/HTML/Element/Input)



### 마크업 해보기

test3.html (포기)

---



## CSS

Cascading Style Sheets

스타일 지정 언어

(선택, 스타일 지정)

![Untitled.png (629×292)](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/a37bd3bd-b8d9-485a-8769-02dad8b694fd/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220202T105043Z&X-Amz-Expires=86400&X-Amz-Signature=b27340f6662f020760bb4825caf945cdeeb68217913663f8935947c159556f5e&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

- 선택자 -  스타일 지정할 HTML 요소를 선택
- 중괄호 속 - 속성과 값, 하나의 쌍으로 선언
- 각 쌍은 선택한 요소의 속성과 속성에 부여할 값
  - 속성 (property) : 어떤 스타일 기능을 변경?
  - 값 (Value) : 어떻게 스타일 기능 변경?





일단 여기까지