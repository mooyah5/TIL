# 0508 TIL Vue2

### 목차

- SFC (Single File Component)
- Vue CLI
- Pass props & Emit event
- Vue Router
- Youtube Project





## SFC

- Component (컴포넌트)
  - 기본 HTML 엘리먼트를 확장하여 재사용 가능한 코드를 캡슐화 하는데 도움
  - CS에서는 재사용 범용성을 위해 개발된 SW 구성요소를 의미함
  - 즉, 유지보수 Easier, 재사용성 good 기능 제공
  - Vue 컴포넌트 = Vue 인스턴스
- SFC (single File Component)
  - Vue의 컴포넌트 기반 개발의 핵심 특징
  - 하나의 컴포넌트는 .vue 확장자를 가진 하나의 파일 안에서 작성되는 코드의 결과물
  - 화면의 특정 영역에대한 HTML, CSS, JS 코드를 하나의 파일(.vue)에서 관리
  - 즉, `.vue` 확장자를 가진 싱글 파일 컴포넌트를 통해 개발하는 방식
  - Vue 컴포넌트 = Vue 인스턴스 = .vue 파일



- 단일 파일 관리
  - 첫 개발 시작 시 크게 신경쓸 게 없어 쉽게 개발 가능하지만,
  - 코드 양이 많아지면 변수관리, 유지보수가 힘들어지고 비용발생
- 따라서 한 화면을 구성하는 여러 컴포넌트를 기능별로 파일을 나누어 개발
  - 첫 개발 준비단계에서 시간 소요가 증가하지만
  - 이후의 변수 관리가 용이하며, 기능별 유지, 보수 비용 감소



- Vue Component 구조 예시
  - 한 화면 안에서 기능 별 각기 다른 컴포넌트가 존재
    - 하나의 컴포넌트는 여러 개의 하위 컴포넌트를 가질 수 있음
    - Vue는 컴포넌트 기반의 개발 환경을 제공
  - Vue 컴포넌트는 Const app = new Vue({...}) 의 app을 의미함.
    - 반드시 파일 단위로 구분되어야 한다는 게 아님
    - 단일 .html 파일 안에서도 여러 개의 컴포넌트를 만들어 개발 가능



- 정리
  - Vue 컴포넌트는 Vue 인스턴스 (new Vue({..}))이기도 하다.
  - Vue 인스턴스는 .vue 파일 안에 작성된 코드의 집합
  - HTML, CSS, JS를 `.vue` 확장자를 가진 파일 안에서 관리하며 개발



## Vue CLI



#### Vue CLI

- Vue.js 개발을 위한 표준 도구
- 프로젝트의 구성을 도와주는 역할
- Vue 개발 생태계에서 표준 도구 기준을 목표로 함
- 확장 플러그인, GUI, Babel 등 다양한 tool 제공



#### Node.js

- JS를 브라우저가 아닌 환경에서도 구동할 수 있도록 하는 JS 런타임 환경
  - 브라우저 밖을 벗어 날 수 없던 JS 언어의 태생적 한계 해결
- 크롬 V8 엔진을 제공하여 여러 OS 환경에서 실행할 수 있는 환경 제공
- 단순히 브라우저만 조작가능하던 JS를 SSR 아키텍처에서도 사용 가능하도록 함



#### NPM (Node Package Manage)

- JS 언어를 위한 패키지 관리자
  - 파이썬에 pip이 있다면, Node.js에는 NPM
  - pip 처럼 다양한 의존성 패키지를 관리함
- Node.js의 기본 패키지 관리자
- Node.js 설치 시 함께 설치됨



#### Vue CLI Quick Start

- 설치

  ` npm install -g @vue/cli`

- 버전 확인

  `vue --version`

- 프로젝트 생성

  `vue create {app name}`

- npm 레지스트리 변경 (환경따라 등장하지 않을 수도)

  `? Your connection to the default npm registry seems to be slow.`

  `Use https://registry.npm.taobao.org for faster installation? Yes`

- Vue 버전 선택 (Vue 2)

  ```bash
  Vue CLI v5.0.4
  ? Please pick a preset: (User arrow keys)
  > Default ([Vue 3] babel, eslint)
    Default ([Vue 2] babel, eslint)
    Manually select features
  ```

- 프로젝트 생성 성공

  ```bash
  Successfully created project {app name}
  Get started with the following commands:
  ```

- 프로젝트 디렉토리 이동

  `cd {app name}`

- 서버 실행

  `npm run serve`





## Babel & Webpack

#### Vue 프로젝트 구조

![image-20220508175254683](0508 TIL Vue2 (예습).assets/image-20220508175254683.png)



#### Babel

"JS compiler"

- JS의 ECMAScript 2015+ 코드를 이전 버전으로 번역/변환해 주는 도구
- 과거 JS의 파편화, 표준화의 영향으로 코드 스펙트럼이 매우 다양
  -  때문에 최신 문법을 사용해도 이전 브라우저, 환경에서 동작하지 않는 상황 발생
- 원시 코드(최신 버전)를 목적 코드(구 버전)로 옮기는 번역기의 등장 => 개발자는 더 이상 내 코드가 특정 브라우저에서 동작하지 않는 상황에 대해 크게 고민하지 않을 수 있게 됨



#### Babel 동작 예시

![image-20220508175504753](0508 TIL Vue2 (예습).assets/image-20220508175504753.png)



#### Webpack

"static module bundler"

모듈 간 의존성 문제 해결 도구

프로젝트에 필요한 모든 모듈을 매핑하고 내부적으로 종속성 그래프를 빌드함



#### Static Module Bundler

- 모듈은 단지 파일 하나를 의미 (ex. js 파일 하나 = 모듈 하나)
- 배경
  - 브라우저만 조작 가능하던 시기의 JS는 모듈 관련 문법 없이 사용됨
  - BUT, JS와 app이 복잡해지고 크기가 커지면서, 전역 스코프를 공유하는 기존 개발 방식의 한계점이 드러남
  - SO, 라이브러리를 생성하여 필요 모듈을 언제든 불러오거나 코드를 모듈 단위로 작성하는 등의 다양한 시도가 이루어짐
- 여러 모듈 시스템
  - ESM (ECMA Script Module)
  - AMD (Asynchronous Module Definition)
  - CommonJS
  - UMD (Universal Module Definition)



- 모듈 의존성 문제

  - 모듈 수 증가로 라이브러리 or 모듈 간 의존성(연결성)이 깊어짐

    => 특정한 곳애서 발생한 문제가 어떤 모듈 간 문제인지 파악이 어려움

    즉, Webpack은 이 모듈 간 의존성 문제 해결을 위해 등장함

- Bundling : 모듈 의존성 문제를 해결해주는 작업
- Budler : 이러한 일을 해주는 도구
- Webpack : 다양한 Bundler 중 하나
  - 여러 모듈을 하나로 묶어주고, 묶인 파일은 하나 혹은 여러 개로 합쳐진다
  - Bundling 된 결과물은 더 이상 순서에 영향 받지 않고 동작
  - snowpack, parcel, rollup.ks 등의 webpack 이외에도 다양한 모듈 번들러 존재



- Vue CLI는 이러한 Babel, Webpack에 대한 초기 설정이 자동으로 되어 있음



#### node_module 의 의존성 깊이

![image-20220508175952547](0508 TIL Vue2 (예습).assets/image-20220508175952547.png)



#### Webpack

![image-20220508180011142](0508 TIL Vue2 (예습).assets/image-20220508180011142.png)





#### 정리

- Node.js
  - JS Runtime Environment
  - JS를 브라우저 밖에서 실행할 수 있는 새로운 환경
- Babel
  - Complier
  - ES2015+ JS 코드를 구 버전의 JS로 바꿔주는 도구
- Webpack
  - Module Bundler
  - 모듈 간 의존성 문제 해결 도구



#### Vue 프로젝트 구조

- `node_modules` : node.js 환경의 여러 의존성 모듈 (venv같은 것)
- `public/index.htm`l : Vue 앱의 뼈대 파일, 실제 제공되는 단일 html 파일
- `src/assets` : webpack에 의해 빌드 된 정적 파일
- `src/components` : 하위 컴포넌트들이 위치
- `src/App.vue` : 최상위 컴포넌트
- `src/main.js`
  - webpack이 빌드 시작 시 가장 먼저 불러오는 entry point
  - 실제 단일 파일에서 DOM과 data를 연결 했던 것과 동일한 작업이 이루어지는 공간
  - Vue 전역에서 활용 할 모듈을 등록할 수 있는 파일
- `babel.config.js` : babel 관련 설정이 작성된 파일
- `package.json` : 프로젝트 종속성 목록, 지원되는 브라우저에 대한 구성 옵션 포함 (requirements.txt 같은 것)
- `package-lock.json`  ( package.json과 세트)
  - node_modules에 설치되는 모듈과 관련된 모든 의존성을 설정, 관리
  - 팀원, 배포환경에서 정확하게 동일한 종속성을 설치하도록 보장하는 표현
  - 사용 할 패키지 버전 고정
  - 개발 과정 간 의존성 패키지 충돌 방지



---





## Pass Props & Emit Events



#### 컴포넌트 작성

- Vue app은 자연스럽게 중첩된 컴포넌트 트리로 구성
- 컴포넌트간 부모-자식 관계까 구성되며 이들 사이 필연적으로 의사소통 필요
- 부모는 자식에게 데이터를 전달(Pass props)
- 자식은 자신에게 일어난 일을 부모에게 알림 (Emit Event)
- 부모, 자식이 명확하게 정의된 인터페이스를 통해 격리 상태 유지 가능
- props는 아래로, events는 위로
- 부모는 props를 통해 자식에게 '데이터'를 전달
- 자식은 events를 통해 부모에게 '메시지'를 보냄

![image-20220508180840371](0508 TIL Vue2 (예습).assets/image-20220508180840371.png)



#### 컴포넌트 구조

<img src="0508 TIL Vue2 (예습).assets/image-20220509143651875.png" alt="image-20220509143651875" style="zoom:67%;" />

(vue 작성 후 enter : vetur가 작성해줌 ㅎㅎ)

1. 템플릿 (HTML)
2. 스크립트 (Javascript)
3. 스타일 (CSS)



##### 템플릿

- HTML의 body 부분
- 각 컴포넌트를 작성



##### 스크립트

- JS 작성구간
- 컴포넌트 정보, 데이터, 메서드 등 vue 인스턴스를 구성하는 대부분이 작성 됨



##### 스타일

- CSS 작성됨. 컴포넌트의 스타일을 담당

---



#### 컴포넌트 등록 3단계

1. 불러오기 (import)
2. 등록하기 (register)
3. 보여주기 (print)



#### props

- 부모(상위) 컴포넌트의 정보를 전달하기 위한 사용자 지정 특성
- 자식(하위) 컴포넌트는 props 옵션을 사용하여 수신하는 props를 명시적으로 선언해야 함
- 즉, 데이터는 props 옵션을 사용하여 자식 컴포넌트로 전달됨
- 주의
  - 모든 컴포넌트 인스턴스에는 자체 격리된 범위가 있음
  - 즉, 자식 컴포넌트의 템플릿에서 상위 데이터를 직접 참조할 수 없음



#### Static Props 작성

- 자식 컴포넌트(About.vue)에 보낼 prop 데이터 선언

- 작성법 `prop-data-name="value"`

  ![image-20220508181040646](0508 TIL Vue2 (예습).assets/image-20220508181040646.png)

- 수신 할 prop 데이터를 명시적으로 선언 후 사용

  ![image-20220508181055016](0508 TIL Vue2 (예습).assets/image-20220508181055016.png)



#### Dynamic Props 작성

- v-bind directive를 사용해 부모 데이터의 props를 동적으로 바인딩

- 부모에서 데이터가 업뎃 될 때마다 자식 데이터로도 전달 됨

  ![image-20220508181137148](0508 TIL Vue2 (예습).assets/image-20220508181137148.png)

- 마찬가지로 수신 할 prop 데이터를 명시적 선언 후 사용

![image-20220508181229949](0508 TIL Vue2 (예습).assets/image-20220508181229949.png)



#### Props 이름 컨벤션

- During Declaration (선언 시)
  - camel case
- in template (HTML)
  - kebab-case



#### 컴포넌트의 'data'는 반드시 함수여야 함

- 기본적으로 각 인스턴스는 모두 같은 data 객체를 공유하므로 새로운 data 객체를 반환(return)해야 함

​	![image-20220508181342921](0508 TIL Vue2 (예습).assets/image-20220508181342921.png)

![image-20220509150927356](0508 TIL Vue2 (예습).assets/image-20220509150927356.png)

컴포넌트를 재사용하다보니 전부 오른쪽을 사용하는데, 다같이 하나를 공유해버림. 각각이 형제라고 한다면, 

#### Props 시 자주하는 실수

- Static 구문을 사용하여 숫자를 전달하려고 시도하는 것

- 실제 JS 숫자를 전달하려면 값이 JS 표현식으로 평가되도록 **v-bind**를 사용해야 함

  ![image-20220508181428095](0508 TIL Vue2 (예습).assets/image-20220508181428095.png)



#### 단방향 데이터 흐름 (부모님께 말하기)

- 모든 props는 하위 속성과 상위 속성 사이 **단방향** 바인딩을 형성
- 부모 속성이 변경되면 자식 속성에게 전달되지만, 반대 방향으로는 안 됨
  - 자식 요소가 의도치 않게 부모 요소 상태를 변경하여 앱 데이터 흐름을 이해하기 어렵게 만드는 일을 방지
- 부모 컴포넌트가 업뎃될 때마다 자식 요소의 모든 prop들이 최신 값으로 업뎃 됨



#### Emit event (이벤트를 발신하다)

> Listening to Child Components Events

- $emit (eventName) = **발송하다.**
  - 현재 인스턴스에서 이벤트를 트리거
  - 추가 인자는 리스터의 콜백 함수로 전달

- **부모 컴포넌트는** 자식이 사용되는 템플릿에서 **v-on**을 사용하여 자식이 보낸 **이벤트를 청취**



#### Emit event 작성

- 현재 인스턴스에서 $emit 인스턴스 메서드를 사용해 `child-input-change` 이벤트를 트리거

  ![image-20220508181732954](0508 TIL Vue2 (예습).assets/image-20220508181732954.png)

- 부모는 자식이 사용되는 템플릿에서 v-on directive를 사용하여 자식이 보낸 이벤트를 청취

  ![image-20220508181743356](0508 TIL Vue2 (예습).assets/image-20220508181743356.png)



#### event 이름 컨벤션

- 컴포넌트 및 props와는 달리, 이벤트는 자동 대소문자 변환을 제공하지 않음

- HTML의 대소문자 구분을 위해 DOM 템플릿의 v-on 이벤트 리스너는 항상 자동으로 소문자 변환되기 때문에 v-on:myEvent는 자동으로 v-on:myevent로 변환

- 이런 이유로, 이벤트 이름에는 항상 kebab-case 권장

  ![image-20220508181850728](0508 TIL Vue2 (예습).assets/image-20220508181850728.png)





## Vue Router



#### Vue Router

- Vue.js 공식 라우터
- 라우트에 **컴포넌트**를 매핑한 후, 어떤 주소에서 렌더링할 지 알려줌
- **컴포넌트와 주소를 매핑함** (실제 새로고침, 화면전환, url변화가 없는데 눈속임함)
- SPA 상에서 라우팅을 쉽게 개발할 수 있는 기능을 제공
- router
  - 위치에 대한 최적 경로를 지정하며, 이 경로를 따라 데이터를 다음 장치로 전향시키는 장치



#### Vue Router 시작하기

1. 프로젝트 생성, 이동

   `vue create my-router-app`

   `cd my-router-app`

2. Vue Router plugin 설치 (Vue CLI 환경)

   `vue add router`

   - 주의: 기존 프로젝트를 진행하던 중 추가하면 App vue를 덮어쓰므로, 실행 전 파일 백업(커밋)해야 함

3. Commit 여부 (Yes)

   ```
   WARN There are unccommited changes in the current repository. it's recommended to commit or stash them first.
   ? Still proceed? Yes```
   ```

4. History mode 사용 여부 (Yes)

   ```
   ? Use history mode for router? (Requires proper server setup for index fallback in production) (Y/n)
   Yes
   ```



#### Vue Router로 인한 변화

1. App.vue 코드

2. router/index.js 생성

   ![image-20220508182358465](0508 TIL Vue2 (예습).assets/image-20220508182358465.png)

3. views 디렉토리 생성

   ![image-20220508182350649](0508 TIL Vue2 (예습).assets/image-20220508182350649.png)



##### index.js

- 라우트 관련 정보, 설정이 작성되는 곳

##### router-link

- `<router-link>`
  - 사용자 네비게이션을 가능케하는 컴포넌트
  - 목표 경로는 `to` prop으로 지정
  - html5 히스토리 모드에서 router-link는 클릭 이벤트를 차단, 브라우저가 페이지를 재로드하지 않도록 함
  - a 태그지만, 우리가 알던 GET 요청을 보내는 a태그와는 좀 다르게, 기본 GET요청을 보내는 이벤트를 제거한 형태로 구성
- `<router-view>`
  - 주어진 라우트에 대해 일치하는 컴포넌트를 렌더링하는 컴포넌트
  - 실제 컴포넌트가 DOM에 부착되어 보이는 자리를 의미
  - router-link를 클릭하면 해당 경로와 연결된 index.js에 정의한 컴포넌트가 위치



#### History Mode

- tml History API를 사용해서 router를 구현한 것
- 브라우저의 히스토리는 남기지만, 실제 페이지는 이동하지 않는 기능을 지원
- 페이지 재로드 없이 URL 탐색 가능 (SPA의 단점 중 하나인 URL이 변경되지 않음을 해결)
- 긍게, URL은 바뀌는 것처럼 보이는데, 새로고침은 되지 않고 있다는 뜻



##### History API

- DOM 의 Window 객체는 history 객체를 통해 브라우저의 세션 기록에 접근할 수 있는 방법을 제공
- 히스토리 객체는 사용자를 자신의 방문 기록 앞, 뒤로 보내거나, 
- 기록의 특정 지점으로 이동하는 등 유용한 메서드, 속성을 가진다.



#### 1. Named Routes

- 이름을 가지는 라우트
- 명명된 경로로 이동하려면 객체를 vue-router 컴포넌트 요소의 prop에 전달

#### 2. 프로그래밍 방식 네비게이션

- `<router-lick>`를 사용하여 선언적 탐색을 위한 a태그를 만드는 것 외에도, router의 인스턴스 메서드를 사용하여 프로그래밍 방식으로 같은 작업 수행 가능

  - 선언적 방식 : `<router-lick to="...">`
  - 프로그래밍 방식 : `$router.push()`

- Vue 인스턴스 내부에서 라우터 인스턴스에 `$router`로 접근 가능

- SO, 다른 url로 이동하려면, `this.$router.push`로 호출 가능

  - 이 메서드는 새 항목을 history stack에 넣으므로, 사용자가 브라우저 뒤로가기 버튼을 클릭할 시 이전 url로 이동하게 됨

- `<router-link>`를 클릭할 때 내부적으로 호출되는 메서드이므로

  - `<router-lick : to="...">`를 클릭하면 `router.push(...)`를 호출하는 것과 같음

- 작성 가능 인자 예시

  ```javascript
  // literal string path
  router.push('home')
  
  // object
  router.push({ path: 'home' })
  
  // named route
  router.push({ name: 'user', params: {userId: '123'} })
  
  // with query, resulting in /register?plan=private
  router.push({ path: 'register', query: { plan: 'private' } })
  ```

- About에서 Home으로 이동하는 로직 작성

  ```html
  <template>
      <div class="about">
          <h1>이것은 어바웃 페이지</h1>
          <button @click="moveToHome">Home으로 이동</button>
      </div>
  </template>
  
  <script>
  	export default {
          name: 'AboutView',
          methods: {
              moveToHome: function () {
                  // this.$router.push('/')
                  this.$router.push({ name: 'home' })
              },
          },
      }
  </script>
  ```



#### 3. Dynamic Route Matching

- 동적 인자 전달

- 주어진 패턴을 가진 라우트를 동일한 컴포넌트에 매핑해야 하는 경우

- 예) 모든 User에 대해 동일 레이아웃을 가지지만, 다른 User ID로 렌더링 되어야하는 User 컴포넌트

  ```javascript
  const routes = [
      {
          path: '/user/:userId'
          name: 'User',
          component: User
      },
  ]
  ```

- 동적인자는 콜론( : )으로 시작함

- 컴포넌트에서 `this.$rout.params`로 사용가능



#### components 와 views

- 기본적으로 작성된 구조에서 컴포넌츠 폴더와 뷰스 폴더 안에 각기 다른 컴포넌트가 존재
- 컴포넌트를 작성해 갈 때 정해진 구조가 있는 건 아니고, 주로 아래처럼 구조화
- `App.vue`
  - 최상위 컴포넌트
- `views/`
  - router(index.js)에 매핑되는 컴포넌트를 모아두는 폴더
  - 예) App 컴포넌트 내부에 AboutView & HomeView 컴포넌트 등록
- `components/`
  - router에 매핑된 컴포넌트 내부에 작성하는 컴포넌트를 모아두는 폴더
  - 예) Home 컴포넌트 내부에 HelloWorld 컴포넌트 등록



#### view router 필요성

1. SPA 등장 전

   - 서버가 모든 라우팅을 통제
   - 요청 경로에 맞는 html 제공

2. SPA 등장 후

   - 서버는 index.js 하나만 제공
   - 이후 모든 처리는 html 위에서 js코드 활용하여 진행
     - 요청 처리를 더이상 서버가 할 필요가 없어짐(하지 않음)

3. 라우팅 처리 차이

   1. SSR
      - 라우팅 결정권을 서버가 가짐
   2. CSR
      - 라우팅 결정권을 클라이언트가 가짐
        - 클라이언트가 더 이상 서버로 요청을 보내지 않고
        - 응답받은 html 문서 안에서 주소가 변경되면
        - 특정 주소에 맞는 컴포넌트를 렌더링

   - 결국 Vue Router는 라우팅 결정권을 가진 Vue.js에서 라우팅을 편리하게 할 수 있는 Tool을 제공해주는 라이브러리

---



## Youtube Project



#### 컴포넌트 관계



![image-20220510022936891](0508 TIL Vue2 (예습).assets/image-20220510022936891.png)



#### 1. 프로젝트 준비

- 프로젝트 생성 및 lodash 설치

  ```bash
  $ vue create youtube-project
  $ cd youtube-project
  $ npm i lodash
  ```

#### 2. 유트브 검색 데이터 (TheSearchBar.vue)

##### 1) 컴포넌트 등록

```html
// App.vue
<template>
	<div id="app">
        <h1>My first Youtube Project</h1>
        <the-search-bar></the-search-bar>
    </div>
</template>

<script>
import TheSearchBar from '@/components/TheSearchBar'
    
export default {
    name: 'App',
    components: {
        TheSearchBar,
    },
    ...
}
</script>
```

##### 2) Emit Event (TheSearchBar.vue => App.vue)

```html
// TheSearchBar.vue

<template>
	<div>
        <input @keyup.enter="onInputKeyWord" type="text">
    </div>
</template>

<script>
export default {
    name: 'searchBar',
    methods: {
        onInputKeyword: function (event) {
            this.$emit('input-change', event.target.value)
        }
    }
}
</script>
```

##### 3) 이벤트 청취 후 함께 전달 된 데이터 할당

```html
// App.vue
<template>
	<div id="app">
        <h1>My first Youtube Project</h1>
        <the-search-bar @input-change="onInputChange"></the-search-bar>
    </div>
</template>

<script>
import TheSearchBar from '@/components/TheSearchBar'
    
export default {
    
    name: 'App',
    components: {
        TheSearchBar,
    },
    ...
    data: function () {
        return {
            inputValue: null,
        }
    },
    methods: {
        onInputChange: function (inputText) {
            // console.log(this) -> Vue instance
            this.inputvalue = inputText
            // console.log(this.inputValue)
        }
    }
}
</script>
```



#### 3. 유튜브 요청 & 응답 데이터 처리 (App.vue)

##### 1) API_KEY, API_URL 할당

​	https://developers.google.com/youtube/v3/docs/search/list?hi=ko

##### 2) Youtube API 요청 & 응답 데이터를 변수에 할당

```html
// App.vue
<template>
	<div id="app">
        <h1>My first Youtube Project</h1>
        <the-search-bar @input-change="onInputChange"></the-search-bar>
    </div>
</template>

<script>
import TheSearchBar from '@/components/TheSearchBar'
import axios from 'axios'
import TheSearchBar from './components/TheSearchBar.vue'

const API_KEY = 'AIzaSyBDCH20EbGZ0Rid-FEbHkFgP9SBktV6I48'
const API_URL = 'https://www.googleapis.com/youtube/v3/search'
    
export default {
    name: 'App',
    data: function () {
        return {
            inputValue: null,
            videos: [],
        }
    },
    components: {
        TheSearchBar,
    },
    methods: {
        onInputChange: function (inputText) {
            // console.log(this) -> Vue instance
            this.inputvalue = inputText
            // console.log(this.inputValue)
            
            const params = {
                key: API_KEY,
                part: 'snippet',
                type: 'video',
                q: this.inputValue,
            }
            axios({
                method: 'get',
                url: API_URL,
                params,
            })
            .then(res => {
                console.log(res)
                this.videos = res.data.items
            })
            .catch(err => {
                console.log(err)
            })
        }
    }
}
</script>
```

##### 3) Pass props (App.vue => VideoList.vue)

할당한 응답 데이터를 하위 컴포넌트로 전달

![image-20220510024441031](0508 TIL Vue2 (예습).assets/image-20220510024441031.png)

```html
// App.vue
<template>
	<div id="app">
        <h1>My first Youtube Project</h1>
        <header>
        	<the-search-bar @input-change="onInputChange"></the-search-bar>
        </header>
        <section>
        	<video-list :videos="videos"></video-list>
        </section>
    </div>
</template>
```

##### 4) 내려받은 prop 데이터 선언 후 사용

```html
// VideoList.vue

<template>
	<ul>
        <li v-for="video in videos" :key="video.id.videoId">
        {{ video.snippet.title }}
        </li>
    </ul>
</template>

<script>
export default {
    name: 'VideoList',
    props: {
        videos: {
            type: Array,
            required: true,
        }
    }
}
</script>
```

##### 5) Pass props (VideoList.vue => VideoListItem.vue)

```html
// VideoList.vue

<template>
	<ul>
        <li v-for="video in videos"
            :key="video.id.videoId"
            :video="video">
        {{ video.snippet.title }}
        </li>
    </ul>
</template>

<script>
export default {
    name: 'VideoList',
    props: {
        videos: {
            type: Array,
            required: true,
        }
    }
}
</script>
```

##### 6) 내려받은 prop 데이터 (개별 비디오 객체) 선언 후 사용

```html
// VideoListItem.vue

<template>
	<ul>
        <li>
            <img :src="video.snippet.thumbnails.default.url" alt="youtube-thumbnail-image">{{ video.snippet.title }}
        </li>
    </ul>
</template>

<script>
export default {
    name: 'VideoListItem',
    props: {
        videos: {
            type: Object,
            required: true,
        }
    }
}
</script>
```



#### 4. 유튜브 상세 영상 정보 - VideoDetail.vue

##### 1) 유튜브 상세 영상 정보 알리기

- VideoListItem.vue => VideoList.vue

  ```html
  // VideoListItem.vue
  
  <template>
  	<ul>
          <li @click="selectVideo">
              <img :src="video.snippet.thumbnails.default.url" alt="youtube-thumbnail-image">{{ video.snippet.title }}
          </li>
      </ul>
  </template>
  
  <script>
  export default {
      name: 'VideoListItem',
      props: {
          videos: {
              type: Object,
              required: true,
          }
      },
      methods: {
          selectVideo: function () {
              this.$emit{'select-video', this.video}
          }
      },
  }
  </script>
  ```

  ```html
  // VideoList.vue
  
  <template>
  	<ul>
          <li v-for="video in videos"
              :key="video.id.videoId"
              :video="video"
              @select-video="onSelectVideo">
          {{ video.snippet.title }}
          </li>
      </ul>
  </template>
  
  <script>
  export default {
      name: 'VideoList',
      props: {
          videos: {
              type: Array,
              required: true,
          }
      },
      methods: {
          onSelectVideo: function (video) {
              // console.log(video)
              this.$emit('select-video', video)
          }
      }
  }
  </script>
  ```

- VideoList.vue => App.vue

  ```html
  // App.vue
  <template>
  	<div id="app">
          <h1>My first Youtube Project</h1>
          <header>
          	<the-search-bar @input-change="onInputChange"></the-search-bar>
          </header>
          <section>
          	<video-list :videos="videos" @select-video="onVideoSelect"></video-list>
          </section>
      </div>
  </template>
  
  <script>
  import TheSearchBar from '@/components/TheSearchBar'
  import axios from 'axios'
  import TheSearchBar from './components/TheSearchBar.vue'
  
  const API_KEY = ???
  const API_URL = 'https://www.googleapis.com/youtube/v3/search'
      
  export default {
      name: 'App',
      data: function () {
          return {
              inputValue: null,
              videos: [],
              selectedVideo: null,
          }
      },
      components: {
          TheSearchBar,
      },
      methods: {
          onInputChange: function (inputText) {
              // console.log(this) -> Vue instance
              this.inputvalue = inputText
              // console.log(this.inputValue)
              
              const params = {
                  key: API_KEY,
                  part: 'snippet',
                  type: 'video',
                  q: this.inputValue,
              }
              axios({
                  method: 'get',
                  url: API_URL,
                  params,
              })
              .then(res => {
                  console.log(res)
                  this.videos = res.data.items
              })
              .catch(err => {
                  console.log(err)
              })
          },
          onVideoSelect: function (video) {
              this.selectedVideo = video
          }
      },
  }
  </script>
  ```

- App 컴포넌트에서 내린 데이터가 VideoDetail에 전달 되었는지 확인

  ```html
  // App.vue
  <template>
  	<div id="app">
          <h1>My first Youtube Project</h1>
          <header>
          	<the-search-bar @input-change="onInputChange"></the-search-bar>
          </header>
          <section>
              <video-detail :video="selectedVideo"></video-detail>
          	<video-list :videos="videos" @select-video="onVideoSelect"></video-list>
          </section>
      </div>
  </template>
  
  <script>
  import TheSearchBar from '@/components/TheSearchBar'
  import axios from 'axios'
  import TheSearchBar from './components/TheSearchBar.vue'
  
  const API_KEY = ???
  const API_URL = 'https://www.googleapis.com/youtube/v3/search'
      
  export default {
      name: 'App',
      data: function () {
          return {
              inputValue: null,
              videos: [],
              selectedVideo: null,
          }
      },
      components: {
          SearchBar,
          VideoList,
          VideoDetail,
      },
      methods: {
          onInputChange: function (inputText) {
              // console.log(this) -> Vue instance
              this.inputvalue = inputText
              // console.log(this.inputValue)
              
              const params = {
                  key: API_KEY,
                  part: 'snippet',
                  type: 'video',
                  q: this.inputValue,
              }
              axios({
                  method: 'get',
                  url: API_URL,
                  params,
              })
              .then(res => {
                  console.log(res)
                  this.videos = res.data.items
              })
              .catch(err => {
                  console.log(err)
              })
          },
          onVideoSelect: function (video) {
              this.selectedVideo = video
          }
      },
  }
  </script>
  ```

- App.vue => VideoDetail.vue

  ```html
  // VideoDetail.vue
  
  <template>
  	<div>
          {{ video }}
      </div>
  </template>
  
  <script>
  export default {
      name: 'VideoDetail',
      props: {
          video: {
              type: Object,
          }
      }
  }
  </script>
  ```

- VideoDetail 컴포넌트 마무리

- Youtuve iframe 문서를 참고하여 videoId 값 찾기

  - https://developers.google.com/youtuve/plater_parameters?hl=ko

```html
// VideoDetail.vue

<template>
	<div v-if="video" class="video-detail">
        <iframe :src="videoURI" frameborder="0"></iframe>
    </div>
</template>

<script>
export default {
    name: 'VideoDetail',
    props: {
        video: {
            type: Object,
        }
    },
    computed: {
        videoURI: function () {
            const videoId = this.video.id.videoId
            return 'https://www.youtuve.com/embed/${videoId}'
        },
    },
}
</script>
```



#### 5. Environment Variable

- API 키 환경변수 설정

  ![image-20220510030301047](0508 TIL Vue2 (예습).assets/image-20220510030301047.png)

- 프로젝트 최상단에 배치하여 환경 변수 지정 가능

- `NODE_ENV`, `BASE_URL` 및 `VUE_APP_`로 시작하는 변수만 클라이언트 번들에 정적으로 포함됨

- `.env.local`에 작성하는 환경변수는 개발 단계에서 원격 저장소에 노출시키지 않기 위해 git에서 무시되며, 모든 경우에 로드하기 위해 사용

- 단, 환경 변수는 빌드에 포함되므로 누구나 앱 파일을 검사하여 볼 수 있으며, 실제 배포 단계에서는 배포 서비스에서 이러한 환경 변수를 설정할 수 있도록 환경을 제공함

  - 환경변수
    - 컴퓨터에서 동작하는 방식에 영향을 미치는, 동적인 값들의 모임
    - 시스템의 실행 파일이 놓여 있는 디렉터리의 경로 등 운영체제 상에서 동작하는 응용프로그램이 참조하기 위한 설정이 기록됨

---

![image-20220509150614358](0508 TIL Vue2 (예습).assets/image-20220509150614358.png)

---

<img src="0508 TIL Vue2 (예습).assets/image-20220509150405439.png" alt="image-20220509150405439" style="zoom:67%;" />

이렇게 하면 에러남. Component template should contain exactly one root element. If you are using v-if on multiple elements, use v-else-if to chain them instead.

템플릿 안에는 반드시 하나의 element만 있어야 한다.

그래서 div 태그 안에 다 넣어야 함..ㅋㅋㅋㅋ (그렇구나...)

<img src="0508 TIL Vue2 (예습).assets/image-20220509150509720.png" alt="image-20220509150509720" style="zoom:67%;" />



---

components랑 views의 차이

거대한 html 파일 안에 거의비슷하게 거대한 app.vue가 있는데, 그게 app이다.

그런데, router로 이동 가능한 공간이 두 가지 있음 (Home, About)

Home도 어느정도 큰 조각이라 새끼 하나 가지고 있음 (HelloWorld.vue)

views 폴더 안에는 '라우터 급'인 애들이 들어가는 게 좋다.

그럼 component 는? 그 밑 조그마한 조각들을 넣는 게 국룰

그런데, 더 큰 프로젝트를 하다보면 합의해서 바꿀 수 있는 문제임.

아무튼 바로 vue를 만들면 이렇게 짜져있다는 것

그래서, 지금은 일단, 마침 부모자식관계니까 Home으로 props emit으로 짜고, 

---

app.vue 안의 HomeView 안의 Helloworld에서 뒤 두개 emit 연결해주기

홈뷰에서 헬로월드는 내려주는거 (props)

헬로월드에서 홈뷰는 emit으로 커스..이벤트..올려주는거

---

![image-20220510031302344](0508 TIL Vue2 (예습).assets/image-20220510031302344.png)
