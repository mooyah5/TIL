

# 0425 TIL JavaScript (1)







---



- 자바 스크립트의 배열은 원시타입 아니고 참조타입임. 원시타입은 값을 저장, 참조타입은 주소를 저장.

---

## 함수

- 함수는 주소를 참조함
- 함수 생성 방식 - 선언식, 표현식
  - 선언식 : function name(args) { }
  - 표현식 : const name = function(args) { return ~ }

- 자바스크립트 : 1급객체(파이썬도) - 변수에 함수 삽입 가능



### JS 실행환경

1. 브라우저
2. 로컬 - node.js 설치 필요 (프레임워크 아님. 자바스크립트 실행환경)

엔진 차이가 있어서, IDE에서 작성하고 크롬에서 실행하는 식으로 배워보자



### 변수와 인자 개수 불일치 허용

- 기본 인자

  ```javascript
  const greeting = function(name = 'hanna') {
      console.log(`hi ${name}`)
  }
  greeting()
  ```

  => hi hanna

  

- 매개변수 < 인자

  ```javascript
  const noArgs = function () {
      return 0
  }
  noArgs(1, 2, 3)
  ```

  => 0 (오류가 안남)

  

- ddd

  ```javascript
  const threeArgs = function (arg1, arg2, arg3) {
      return 0
  }
  threeArgs() // [undifined, undifined, undifined]
  threeArgs(1) // [1, undifined, undifined, undifined]
  treeArgs(1, 2) // 
  threeArgs(1, 2, 3) // [1, 2, 3]
  threeArgs(1, 2, 3, 4) // [1, 2, 3]
  ```



### Rest Parameter

- 사용하면 함수가 정해지지 않은 수의 매개변수를 배열로 받음 (python의 *args와 유사)

```javascript
const rest = function (arg1, arg2, ...restPara) {
    return [arg1, arg2, restPara]
}

rest(1, 2, 3, 4, 5, 6)	// [1, 2, array(4)] => [3, 4, 5, 6] 
rest(1, 2)				// [1, 2, array(0)] => []
```



### spread operator

- 배열인자를 전개하여 전달 가능

```javascript
const spreadOpr = function(arg1, arg2, arg3) {
    return arg1 + arg2 + arg3
}
const numbers = [1, 2, 3, 4, 5]
console.log(spreadOpr(...numbers)) // 6
```

- 순서대로 하고 뒤에있는 값까지

```javascript
const spreadOpr = function(arg1, arg2, arg3, arg4) {
    return arg1 + arg2 + arg3 + arg4
}
const numbers = [1, 2, 3]
console.log(spreadOpr(...numbers, 4)) // 10
```





![image-20220426100233329](C:\Users\baekh\AppData\Roaming\Typora\typora-user-images\image-20220426100233329.png)

자스는 위에서 아래로 실행되는데, 이때 호이스팅이 안되는애들은 그대로 있고, 되는 애들은 맨 위로 올라감. 예상치 못한 결과를 나타낼 수 있음. 함수 순서가 바뀌니꺼. 에어비앤비에서는 함수표현식을 권장!



#### 호이스팅

```javascript
add(2, 7)
function add (num1, num2) {
	return num1 + num2
}
```





#### arrow 함수

- 함수를 간결하게 정의할 수 있다.

  ```javascript
  const arrow1 = function (name) {
  return `hello ${name}`
  }
  ```

  1. function 키워드 삭제

     ```javascript
     const arrow2 = (name) => {
     	return `hello ${name}`
     }
     ```

  2. ( ) 생략 가능

     ```javascript
     const arrow3 = name => {
     	return `hello, ${name}`
     }
     ```

  3. 함수의 바디({내용}) 표현식 1개(1줄) 경우에 { }, return 생략 가능

     ```javascript
     const arrow4 = name => `hello, ${name}`
     ```



---



## 문자열

깊게 다루지 않을 것.

쳐보면 됨



- includes 있는지 없는지 체크

```javascript
const str = 'a santa at nasa'
str.includes('santa')	// true
str.includes('asan')	// false
```



- split

  ```javascript
  const str = 'a cup'
  str.split() 		// ['a cup']
  str.aplit('') 		// ['a', ' ', 'c', 'u', 'p']
  str.aplit(' ') 		// ['a', 'cup']
  ```



- replace (다시)

  ```javascript
  const str = 'a b c d'
  str.replace(' ', '-') 	// 'a-b c d'
  
  const str = 'a b c d'
  str.replaceAll('', '-')	// 'a-b-c-d'
  ```

  

- trim

  ```javascript
  const str = '	hello	'
  str.trim()			// hello
  str.trimStart()		// hello    .
  str.trimEnd()		//    hello.
  ```





---





## 배열

### 배열의 정의와 특징

- 키, 속성들을 담고 있는 참조 타입의 **객체(object)** (딕셔너리 타입)
- 순서를 보장
- 대괄호로 생성, 0을 포함한 양의정수 인덱스로 접근 가능
- 배열 길이는 array.length로 접근
- 배열의 마지막 원소는 array.length -1로 접근([-1] 안됨)



### 배열 관련 주요 메서드

```javascript
const numbers = [1, 2, 3, 4, 5]
numbers[0]
numbers[-1]		// undifined (양의 정수 index만 가능)
numbers.length	// 5 (길이)
```

push  삽입

pop 뒤 빼기

unshift 왼쪽에 삽입

shift 왼쪽 빼기

includes 있는지 없는지 확인

indexOf 인덱스에 있는 값

indexOf(없는값) = -1

join() 그대로 출력 // 1,2,3,4,5

join('') 붙어서 출력 // '12345'

join('-') // [1-2-3-4-5]





### spread operator

```javascript
const array1 = [1, 2, 3]
const array2 = [5, 6, 7]
const array3 = [...array1, 4, ...array2] // (7) [1, 2, 3, 4, 5, 6, 7]

```

- 옛날에는 concat 메소드를 써야했는데 이제는 ㄱㅊ



### 강적 - Arrya 관련 주요 메드 심화편

![image-20220426103725503](C:\Users\baekh\AppData\Roaming\Typora\typora-user-images\image-20220426103725503.png)

Array Helper Method = item 한개씩 꺼내서 사용

- callback 함수를 받는 것이 특징
  - callback 함수 : [a, b, c]면, a를 꺼내서 특정행동을하는데, 그 행동이 함수인 것이고, 그 함수 이름을 callback 함수라고 부름 (함수에서 쓰는 함수)



#### forEach

- 하나씩 꺼내서 각각에 callback 함수를 적용시킴

- 반환값(return)이 없는 메소드
- 한 번 처리하면 끝나는 애

```javascript
const colors = ['red', 'green', 'blue']
const noresult = colors.forEach((color) => {
    // 할 일(작업) 콜백함수
    console.log(`색상은 ${color}`);
})
```

```javascript
// 1단계
const 함수명 = 배열.forEach(콜백함수)
// 2단계
const 함수명 = 배열.forEach(function (함수에서하나씩꺼낸애이름color) => {할일})
// 3단계
const 함수명 = 배열.forEach(재료) => {할일})
// 4단계
// 할 일이 많으면
const 함수명 = 배열.forEach(재료) => {
    // 할일들
}
```

- 콜백함수는 3가지 매개변수로 구성 (재료)

  - ```javascript
    const 함수명 = 배열.forEach((재료1, 재료2, 재료3) => {
    	할일
    })
    
    재료1은 배열 안에 1개씩 들고온거
    재료2는 재료1의 인덱스
    재료3은 전체배열(잘 안 씀)
    
    const 함수명 = 배열.forEach((재료, 인덱스, 전체배열) => {
    	할일
    })
    ```

  - ```javascript
    const colors = ['red', 'green', 'blue']
    const noresult = colors.forEach((color, index, list) => {
        // 할 일(작업) 콜백함수
        console.log(`${list} 중에서 ${index}번 색상은 ${color}`);
    })
    ```



#### map

- 배열 각 요소에 대해 콜백 함수를 한번씩 실행
- 새로운 거 만들고 싶을 때
- 기존 배열 전체를 다른 형태로 바꿀 때
- 콜백 **함수의 반환 값을 요소로 하는** 새로운 배열 반환
- 파이썬의 map처럼 요소 하나하나를 새로운 형태로 재탄생시킴

```javascript
const numbers = [1, 2, 3, 4, 5]
const doubleNumbers = numbers.map((number) => {
    return number * 2;
})
console.log(doubleNumbers)		// [2, 4, 6, 8, 10]
```



#### filter

조건

```javascript
const numbers = [1, 2, 3, 4, 5]
const oddNums = numbers.filter((num) => {
    return num > 2
})
console.log(oddNums)	// [3, 4, 5]



const numbers = [1, 2, 3, 4, 5]
const oddNums = numbers.filter((num) => {
    return num % 2 === 0
})
console.log(oddNums)	// [2, 4]
```



#### reduce

- 살짝 복잡함 (할일이)
- 하나씩 릴레이함
- 배열을 한 개의 값으로 만드는 것 (acc에 누적 후 반환)
- 주요 매개변수
  - acc 누적값 (accumulator)
    - 이전 콜백함수의 반환값이 누적되는 변수
  - initialValue(optional) 시작값
    - 최초 콜백함수 호출 시 

```javascript
const result = numbers.reduce(누적값, 요소 => {
리턴
}, 시작값)



arr = [1, 2, 3]
const result = arr.reduce((acc, element, index, array) => {
    return `바톤은 ${arr}, element는 ${element}`
}, 0)
result()
```





#### find

- 배열의 각 요소에 대해 콜백 함수를 한 번 씩 실행
- 하나씩 요소를 꺼내서 어벤저에 넣고 어벤저에 있는 것 중에서 이름이 토르인 것을 찾아옴
- 조건을 만족하는 애를 찾는데, 한 개만 찾으면 STOP (첫번째로 찾은 것 반환 후 끝냄)

```javascript
const avengers = [
    { name : "Tony Starks", age : 45},
    { name : 'Steve Rogers', age : 32},
    { name : 'Thor', age : 40000}
]
const findAvenger = avengers.find((avenger) => {
    return avenger.name == 'Thor'
})
console.log(findAvenger)
```



#### some

- every와 반대
- 배열 요소 중 하나라도 통과하면 참
- 모든 요소가 통과하지 못하면 거짓 반환
- 주로 에러 난 게 한 개라도 있는지 확인할 때 

```javascript
const numbers = [1, 2, 3, 4, 5]
const hasEvenNumber = numbers.some(number => {
    return number % 2 === 0
}) // arrow function에 의해 괄호 하나 뺄 수 있음
console.log(hasEvenNumber)		// true (짝수가 2, 4 존재하니까)

const numbers = [1, 3, 5, 7, 9]
const hasEvenNumber = numbers.some(number => {
    return number % 2 === 0
}) // arrow function에 의해 괄호 하나 뺄 수 있음
console.log(hasEvenNumber)		// false (짝수가 하나도 없으니까)
```



#### every

- 모든 게 통과해야 참
- 하나라도 없으면 거짓

```javascript
const numbers = [2, 4, 6, 8, 10]

const isEveryNumberEven = numbers.every( number => {
	return number % 2 === 0
})
console.log(isEveryNumberEven)	// true (전부 다 짝수니까)


const numbers = [2, 4, 6, 8, 10, 1]

const isEveryNumberEven = numbers.every( number => {
	return number % 2 === 0
})
console.log(isEveryNumberEven)	// false (1이라는 홀수가 하나라도 있으니까)
```





- for loop 인덱스 쓸 수 있는데 조금 불편
- for ...of 오래된 브라우저 환경에서 지원X
- forEach : 대부분의 브라우저 환경에서 지원(break, continue 사용 불가능) - Airbnb 권장



---



## 객체

### 객체



![image-20220426125332551](0425 TIL JavaScript (1).assets/image-20220426125332551-16509452156071.png)

- 파이썬의 딕셔너리처럼 생기고 실제로 그렇게 씀

- 나중에 나오는 JSON이랑 구분할 필요는 있음

- 객체는 속성의 집합이며, 중괄호 내부에 쌍으로 표현된다.

- 속성은 key, value 한 줄. 이것을 모아둔 게 객체. (정보+행동)

- **key는 문자열타입만 가능**

  띄어쓰기가 있으면 따옴표로 묶어서 표현

- value는 모든 타입(함수도) 가능 = 메소드

- 객체 요소의 접근은 점(.)이나 대괄호([])로 가능

  - 이름에 띄어쓰기 같은 구부낮가 있으면 대괄호 접근만 가능



### 메소드

![image-20220426125502298](0425 TIL JavaScript (1).assets/image-20220426125502298.png)

- 객체 안에 있는 함수
- `객체.메서드명()`으로 호출 가능
- 메서드의 안에 있는 this 키워드가 객체 (객체 안에 있는 함수의 안에 있는 this는 자기 자신을 가리킴. 파이썬에서는 self)
  - fullName 은 메서드가 아니라서 정상출력 안됨(NaN)
  - getFullName 은 

```javascript
const me = {
    firstName : 'Hanna',
    lastName : 'Baek',
    fullName: this.firstName + this.lastName,
    
    getFullName: function () {
        return this.firstName + this.lastName
    }
}

me.firstName
'Hanna'
me['firstName']
'Hanna'
me.lastName
'Baek'
me['lastName']
'Baek'
me.fullName
NaN				// window 객체(최상위객체)...?
me.getFullName()
'HannaBaek'
```



```javascript
const me = {
    firstName : 'Hanna',
    lastName : 'Baek',
    fullName: this.firstName + this.lastName,		//여기 this는 dynamic(변해서)
    
    getFullName: function () {
    	console.log(this)							//여기 this는 static
        return this.firstName + this.lastName
    }
}
```

![image-20220426130051582](0425 TIL JavaScript (1).assets/image-20220426130051582.png)





- 배열도 객체임. 배열의 키는 인덱스
  - 0 : data1
  - 1 : data2
  - 2 : data3
  - ...



객체가 이렇게 생기니까 다른 언어 하는 사람들이 훈수를 둔다. 자스 이렇게 하니까 너무 어렵다. Syntactic Sugar를 만듦

- ES6
  - 속성명 축약
  - 메서드명 축약
  - 계싼된 속성명 사용
  - 구조분해할당
  - ㅇㅇㅇ



1. **속성명 축약 (shorthand)**

   - 객체 정의 시 키와 할당하는 변수 이름이 같으면 예시처럼 축약 가능

   - **객체 정의 시 키 값과 키에 할당하는 값이 같으면 축약 가능**

     ![image-20220426130352461](0425 TIL JavaScript (1).assets/image-20220426130352461.png)

     books : books니까 줄여줌(생략)

     ```javascript
     // 과거
     var books = ['learning JS', 'Python']
     var magazines = ['vogue', 'math']
     
     var bookShop = {
         books : books,
         magazines : magazines,
     }
     
     console.log(bookShop)
     console.log(bookShop.books)
     
     // 최근
     const books = ['learning JS', 'Python']
     const magazines = ['vogue', 'math']
     
     const bookShop = {
         books,				// 생략
         magazines
     }
     
     console.log(bookShop)
     console.log(bookShop.books)
     ```

     



2. **메서드명 축약**

   메서드 선언 시 function 키워드 생략 가능

   ![image-20220426130436234](0425 TIL JavaScript (1).assets/image-20220426130436234.png)

   ```javascript
   let key = 'region'
   const value = ['광주', '서울', '부산']
   
   const ssafy = {
       [key] : value,
   }
   
   console.log(ssafy.region)		// ['광주', '서울', '부산']
   
   
   
   key = 'test'					// 계산된 속성(computed property name)
   console.log(ssafy.test)	
   ```

   



3. **계산된 속성 (computed property name)**

   객체 정의 시 key의 이름을 표현식을 이용하여 동적 생성 가능

   ![image-20220426130701876](0425 TIL JavaScript (1).assets/image-20220426130701876.png)

   ```javascript
   let key = 'region'
   const value = ['광주', '서울', '부산']
   
   const ssafy = {
       [key] : value,
   }
   
   key = 'test'	// 키 변경 - 계산된 속성(computed property name)
   console.log(ssafy.test)	
   ```

   

   동적으로? 연동돼서 변한다. 프로그래밍 세계에서 동적이다라는 말은 '변한다'

   key끼리 연결시켜놔서 regions 한쪽이 변하면 다른 쪽 값도 변한다.

   

4. **구조 분해 할당 (desrtucting assignment)**

   - 만약 자스 객체 속 요소가 뭐가 있는지 모를때, 3개만 쓰고 싶을 때 이런 식으로 들고 와서 쓰면 됨

   ![image-20220426130900315](0425 TIL JavaScript (1).assets/image-20220426130900315.png)

   ```javascript
   const userInfo = {
       name: 'ssafy kim',
       userId : 'ssafy1234',
       phoneNumber : '010-1234-1234',
       email : 'ewr@sfe.com'
   }
   
   // 과거
   const name = userInfo.name
   const userId = userInfo.userId
   const phoneNumber = userInfo.phoneNumber
   
   // 최근
   const {name, userId, phoneNumber} = userInfo
   console.log(name, userId, phoneNumber)
   
   
   function getUserInfo ({userId, email}) {
       console.log(`Userid:${userId}`)
       console.log(`User Email : ${email}`)
   }
   
   getUserInfo(userInfo)
   ```

   ---

   ![image-20220426134152576](0425 TIL JavaScript (1).assets/image-20220426134152576.png)

   ---

   ![image-20220426134612659](0425 TIL JavaScript (1).assets/image-20220426134612659.png)

   ---

   

5. **spread operator** 객체 내부 전개할 때~



### JSON (JavaScript Object Notatio)

자바스크립트 객체와 유사하지만, 실제로는 문자열타입 (타입이 다르다 = 사용 행동이 다름)

자스에서 JSON을 쓰려면, 얘는 딕셔너리처럼 생긴 문자열 덩어리여서, parse()를 써서 자바스크립트 객체로 만들어야 함(반대는 stringify())

- JSON.**parse**()
  - JSON => 자스 객체
- JSON.**stingify**()
  - 자스 객체 => JSON



serializer가 하는 걸 저렇게 하는 거임

![image-20220426131421739](0425 TIL JavaScript (1).assets/image-20220426131421739.png)



#### 참고 - 배열은 객체다

- 키와 속성들을 담고 있는 참조 탕ㅂ의 객체
- 배열은 인덱스를 키로 가지며 length 프로퍼티를 갖는 특수한 객체

![image-20220426131651219](0425 TIL JavaScript (1).assets/image-20220426131651219.png)



---

```javascript
// 과거
var obj = {
	gretting : function() {
        console.log('Hi')
    }
}

// 최근
const obj = {
    greeting() {
        console.log('Hi')
    }
}
```





---

## this

- 실행 문맥에 따라 다른 대상을 가리킴. 그래서 dynamic하다!
  1. 일반 함수
  2. 메소드 (객체 안의 함수)
  3. 생성자
  4. 간접호출 (몰라도 됨)



```javascript
// 1. 일반 함수에서 this
function myFunction() {
    console.log(this)
}
myFunction()		// window

// 2. 메소드에서 this
const myObject = {
    method() {
        console.log(this)
    }
}
myObject.method()	// {method: f}

// 3. 생성자에서 this
function myFunction() {
    console.log(this)
}
new MyFunction()		//

// Arrow Function
// 애로우 펑션에서는 항상 콜백에 쓰는데, 이거의 this와 바깥 함수의 this의 값이 항상 같다.

const myObject = {
    mymethod(items) {
        console.log(this)
        const callback = () => {
            console.log(this)		// myObject
        }
        items.forEach(callback)
    }
}

myObject.mymethod([1, 2, 3])

// 같아지는 이유

// 랙시컬 스코프 = 정적 스코프 (대부분의 프로그래밍 언어)
// 함수가 어디서 선언되었는지에 따라 this의 값이 결정되는 것을 의미함
// this의 값을 고정시키고 싶어서 쓴다..?

// 정적 스코프의 반댓말 = 다이나믹 스코프
// 함수를 어떻게 호출(사용)하는지에 따라 this의 값이 결정되는 것을 의미
```



---

```javascript
// 일반함수
// printArea는 radiuses 배열 안의 한 요소를 꺼내서 넓이를 구하는 메소드
const obj = {
    PI: 3.14,
    radiuses: [1, 2, 3, 4, 5],
    printArea: function() {
        this.radiuses.forEach(function (r) {
            console.log(this)
            console.log(this.PI * r * r)
        })
    }
}
obj.printArea()	// window, NaN

// arrow function
const obj = {
    PI: 3.14,
    radiuses: [1, 2, 3, 4, 5],
    printArea: function() {
        this.radiuses.forEach((r) => {
            console.log(this.PI * r * r)
        })
    }
}
obj.printArea()
```

![image-20220426142059665](0425 TIL JavaScript (1).assets/image-20220426142059665.png)

```javascript
// arrow function
const obj = {
    PI: 3.14,
    radiuses: [1, 2, 3, 4, 5],
    printArea: function() {
        this.radiuses.forEach((r) => {
            console.log(this.PI * r * r)
        }.bind(this)) // this가 window 객체를 가리키는 것을 방지하기 위해 사용
    }
}
obj.printArea()
```

근데 이거 에러남





---

https://lodash.com/

<script src="https://cdn.jsdelivr.net/npm/lodash@4.17.21/lodash.min.js"></script>

https://velog.io/@kysung95/%EC%A7%A4%EB%A7%89%EA%B8%80-lodash-%EC%95%8C%EA%B3%A0-%EC%93%B0%EC%9E%90



```javascript
<script src="https://cdn.jsdelivr.net/npm/lodash@4.17.21/lodash.min.js"></script>
  <script>
    // 위 CDN import 를 통해서 _ 식별자 이용 가능
    _.sample([1, 2, 3, 4, 5]) // 배열 중 랜덤으로 1개
    console.log(_.sample([1, 2, 3, 4, 5]))

    console.log(_.sampleSize([1, 2, 3, 4, 5], 2)) // 배열 중 랜덤으로 2개

    console.log(_.range(6))       // [0, 1, 2, 3, 4, 5]

    console.log(_.range(1, 4))    // [1, 2, 3]  <- 1은 미포함

    console.log(_.range(1, 10, 2)) // [1, 3, 5, 7, 9]



    // deepcopy
    const original = {a: {b:1}}

    const ref = original                // 얕은 복사

    const copy = _.cloneDeep(original)  // 깊은 복사

    console.lof(original.a.b, ref.a.b, copy.a.b)
    ref.a.b = 10
    console.lof(original.a.b, ref.a.b, copy.a.b)
    copy.a.b = 100  // 딥카피한 것을 100으로 바꿔보기
    console.lof(original.a.b, ref.a.b, copy.a.b)
  </script>
```

