# JS 정리

Vanilla JavaScrip: 웹 브라우저에서 바로 실행할 수 있는 JS문법, 즉 순수한 JS 라는 의미

```markdown
Node.js 설치

$ node -v
$ npm -v

JavaScript 파일 실행해 보기
$ node hello.js
```

---

## JS 기초 코드 작성법

들여쓰기 2칸

```javascript
if (조건) {
  
}

for (one in many) or (one of many) {
  
}

```



JS에도 Python의 코드 스타일 가이드인 PEP8과 같이 여러 코드 스타일 가이드가 있지만 수업에선 Airbnb Style Guide.

단일 주석 : // 

여러 줄 주석 : /* */

---

## 변수와 식별자

식별자 정의와 특징

- 카멜 케이스

  - 변수, 객체, 함수에 사용

  ```javascript
  // 변수
  let dog
  let variableName
  
  // 객체
  const userInfo = { name: 'Tom', age: 20}
  
  // 함수
  function add() {}
  function getName() {}
  ```

  

- 파스칼 케이스

  - 클래스, 생성자에 사용

  ```javascript
  // 클래스
  class User{
      constructor(options) {
          this.name = options.name
      }
  }
  
  // 생성자 함수
  function User(options) {
      this.name = options.name
  }
  
  ```

  

- 대문자 스네이크 케이스

  - 상수(constants)에 사용
  - 상수: 개발자의 의도와 상관없이 변경될 가능성이 없는 값을 의미

  ```javascript
  // 값이 바꾸지 않을 상수
  const API_KEY = 'my-key'
  const PI = Math.PI
  
  // 재할당이 일어나지 않는 변수
  const NUMBERS = [1,2,3]
  ```

  

함수 스코프(function scope)

- 함수의 중괄호 내부를 가리킴
- 함수 스코프를 가지는 변수는 함수 바깥에서 접근 불가능



변수 선언 키워드 정리

- Airbnb 스타일 가이드에서는 기본적으로 const 사용을 권장
  - 재할당해야 하는 경우에만 let을 사용

---

## 데이터 타입

- Number
  - 정수 또는 실수형 숫자를 표현하는 자료형
  - NaN
    - Not-A-Number(숫자가 아님)를 나타냄
    - Number.isNaN()의 경우 주어진 값의 유형이 Number이고 NaN이면 true, 아니면 false를 반환
- Sting
  - 문자열을 표현하는 자료형
  - 곱셈, 나눗셈, 뺄셈은 안되지만 덧셈을 통해 문자열을 붙일 수 있다.
  - 개행 문자 \n 을 넣어 다음 줄로 넘어갈 수 있다.
  - 백틱(`)사이에 문자를 입력하고 가변 변수를 넣고 싶을 경우 ${{변수명}} 해주면 파이썬의 f-string과 유사.
- null
  - 변수의 `값이 없음을 의도적으로 표현할 때` 사용하는 데이터 타입
- nudefined
  - 값이 정의되어 있지 않음을 표현하는 값
  - 변수 선언 이후 직접 값을 할당하지 않으면 자동으로 할당됨
- null vs undefined
  - 차이점은 typeof 연산자를 통해 확인을 해보면
    - null: object
    - nudefined: undefined

---

## 연산자

- 할당 연산자

```javascript
let c = 0

c += 10
c -= 3
c*= 10
c++
c--
```

- 비교 연산자

```java
3 > 2
'A' < 'B'
'Z' < 'a'
```

- 동등 연산자(==)

  - 두 피연산자가 같은 값으로 평가되는지 비교 후 boolean 값을 반환	

  - 비교할 때 `암묵적 타입 변환`을 통해 타입을 일치시킨 후 같은 값인지 비교\

- 일치 연산자(===)

  - 두 피연산자의 값과 타입이 모두 같은 경우 true를 반환
  - 엄격한 비교가 이뤄지며 `암묵적 타입 변환이 발생하지 않음`

- 논리 연산자

  - &&
  - ||
  - !

- 삼항 연산자

  - 3개의 피연산자를 사용하여 조건에 따라 값을 반환하는 연산자
  - 가장 앞의 조건식이 참이면 : 앞의 값이 반환되며, 그 반대읠 경우: 뒤의 값이 반환되는 연산자.

  ```javascript
  true ? 1:2 //1
  false ? 1:2 //2
  
  const result = Math.PI > 4 ? 'Yep' : 'Nope' // Nope
  ```

  

---

## 조건문

조건문의 종류

- if

  ```javascript
  const name = 'manager'
  
  if (name === 'admin') {
      consol.log('관리자님 환영합니다.')
  }
  else if (name === 'manager') {
      consol.log('매니저님 환영합니다.')
  }
  else {
      consol.log(`${name}님 환영합니다.`)
  }
  ```

  

- switch

```javascript
switch(expression) {
    case 'first value': {
        // do something
        [break]
    }
    case 'second value': {
        // do something
        [break]
    }
    [default: {
     // do something
     }]
}

// break문이 없는 경우 break문을 만나거나 default문을 실행할 때까지 다음 조건문 실행 
```

---

## 반복문

반복문의 종류

- while

  - 조건문이 참이기만 하면 문장을 계속해서 수행

    ```javascript
    while (조건문) {
        // do something
    }
    
    let i = 0
    
    while (i<6) {
        console.log(i)
        i += 1
    }
    ```

    

- for

  - 특정한 조건이 거짓으로 판별될 때까지 반복

    ```javascript
    for ([초기문];[조건문];[증감문]) {
        // do something
    }
    
    for (let i=0; i<6; i++) {
        console.log(i)
    }
    ```

    

- for ...in

  - 객체(object)의 속성을 순회할 때 사용

  - 배열도 순회 가능하지만 인덱스 순으로 순회한다는 보장이 없으므로 권장하지 않음

    ```javascript
    for (variable in object) {
        statements
    }
    
    const fruits = {a:'apple', b:'banana'} 
    
    for (const key in fruits) {
        console.log(key) // a, b
        console.log(fruits[key]) // apple, banna
    }
    ```

    

- for ...of

  - 반복 가능한 객체를 순회할 때 사용
  - 반복 가능한(iterable)객체의 종류: Array, Set, String 등

  ```javascript
  for (variable of object) {
      statements
  }
  
  const numbers = [0, 1, 2, 3]
  
  for (const number of numbers) {
      console.log(number) // 0, 1, 2, 3 
  }
  ```

  

- for ...in 과 for ...of의 차이

  - for ...in은 `속성 이름`을 통해 반복 (객체 순회 적합)
  - for ...of는 `속성 값`을 통해 반복   (iterable 순회 적합)

  ```javascript
  // Array
  
  const numbers = [10, 20, 30]
  
  // for ...in
  for (const number in numbers) {
      console.log(number) // 0 1 2
  }
  
  // for ...of
  for (const number of numbers) {
      console.log(number) // 10 20 30
  }
  ```

  ```javascript
  // Object
  
  
  const capitals = {
      korea: '서울',
      france: '파리',
      japan: '도쿄'
  }
  
  // for ...in
  for (const capital in capitals) {
      console.log(capital) // korea france japan
  }
  
  // for ...of
  for (const capital of capitals) {
      console.log(capital) // TypeError: capitals is not iterable (객체를 접근하는 타입도 아니고 iterable 하지 못해서 에러)
  }
  ```

  

  - const [참고]
    - for문 
      - for (let i=0; i<6; i++) {...} 의 경우에는 최초 정의한 i를 재할당 하면서 사용하기 떄문에 const를 사용시 에러
    - for ...in, for ...of
      - 재할당이 아닌, 매 반복 시 해당 변수를 새로 정의하여 사용하므로 에러가 발생하지 않음



---

## 함수

JS에서 함수를 정의하는 주로 사용하는 2가지 방법

- 함수 선언식 (function declaration)

  ```javascript
  // 일반적인 프로그래밍 언어의 함수 정의 방식
  function 함수명() {
      // do something
  }
  
  function add(num1,num2) {
      return num1 + num2
  }
  add(2,7)  // 9
  ```

  

- 함수 표현식 (function expression)

  ```javascript
  // 표현식 내에서 함수를 정의하는 방식
  // 함수 표현식은 함수의 이름을 생략한 익명 함수로 정의 가능
  
  변수키워드 함수명 = function() {
      // do something
  }
  
  const sub = function(num1,num2) {
      return num1 + num2
  }
  
  위의 코드와 아래의 코드들은 같다.
  
  const sub = (num1,num2) =>{
      return num1 + num2
  }
  
  const sub = (num1,num2) => num1 + num2
  
  sub(2,7)  // 9
  ```

  ```javascript
  // 표현식에서는 함수 이름을 명시하는 것도 가능하다
  // 다만 이 경우 함수 이름은 호출에 사용되지 못하고 디버깅 용도로 사용됨
  
  const mySub = function namedSub(num1,num2) {
      return num1 - num2
  }
  
  mySub(1, 2) // -1
  namedSub(1,2) // ReferenceError: namedSub is not defined
  ```

  

- 기본 인자
  - 인자 작성 시 '=' 문자 뒤 기본 인자 선언 가능하다.
  - ex) const greeting = function(name='Anoymous') 



103page부터 정리 다시 하기