경고창 alert

const 는 변수는 대문자로 선언하는 것이 좋다고 한다. (상수라는 것을 표현)



<img src="JS기초강좌.assets/image-20221025153623316.png" alt="image-20221025153623316" style="zoom:67%;" />



변수 타입은 

- var
- const
- let



문자열 사용

- 큰 따옴표 (" ")

- 작은 따옴표 (' ')
- 백틱 (``) : 파이썬의 f string 기능 구현
  - ex). `My name is ${name}'   



<img src="JS기초강좌.assets/image-20221025154404351.png" alt="image-20221025154404351" style="zoom:67%;" />

 

alert 와 comfirm 의 차이

alert 는 확인 창만 있고

confirm은 확인 버튼과 취소 버튼이  둘다 있다.





<img src="JS기초강좌.assets/image-20221025165536604.png" alt="image-20221025165536604" style="zoom:80%;" />



![image-20221025165617077](JS기초강좌.assets/image-20221025165617077.png)



함수에 리턴값이 없어도 리턴을 하게 된다.

그리고 파이썬 처럼 함수의 리턴값을 변수를 선언하여 담아서 출력도 가능하다



---

### 함수 선언문

<img src="JS기초강좌.assets/image-20221025223528757.png" alt="image-20221025223528757" style="zoom:50%;" /><img src="JS기초강좌.assets/image-20221025223556688.png" alt="image-20221025223556688" style="zoom:50%;" />

JS는 인터프리터 언어지만 위와 같은 함수 선언문의 경우 어디서든 호출이 가능한 이유로는

실행되기전 초기화 단계에서 코드의 모든 함수 선언문을 찾아서 선언된 함수 모임을 생성하기 때문이다. (호이스팅)



### 함수 표현식

<img src="JS기초강좌.assets/image-20221025223835748.png" alt="image-20221025223835748" style="zoom:50%;" />



### 화살표 함수

화살표 함수는 함수 표현식에서 사용하나봄

1. 우선 function을 제거할 경우엔 매개 변수 우측에 화살표를 넣어주고
2. return 을 제거할 경우 밖에 있던 중괄호를 소괄호로 변경우 제거
3.  여기서 리턴문이 한줄일 경우 소괄호 또한 없앨 수 있다.

<img src="JS기초강좌.assets/image-20221025224055018.png" alt="image-20221025224055018" style="zoom: 33%;" /><img src="JS기초강좌.assets/image-20221025224132440.png" alt="image-20221025224132440" style="zoom:33%;" /><img src="JS기초강좌.assets/image-20221025224151457.png" alt="image-20221025224151457" style="zoom:33%;" /><img src="JS기초강좌.assets/image-20221025224305050.png" alt="image-20221025224305050" style="zoom:33%;" />



---

### Object 생성

객체를 생성할 때는 중괄호로 감싼 뒤 key : value 형식으로 작성

<img src="JS기초강좌.assets/image-20221025230229907.png" alt="image-20221025230229907" style="zoom: 33%;" />

<img src="JS기초강좌.assets/image-20221025231502636.png" alt="image-20221025231502636" style="zoom: 50%;" />

객체 생성 후 값 변경 가능.



객체 속성 조회,추가, 삭제

<img src="JS기초강좌.assets/image-20221025231157521.png" alt="image-20221025231157521" style="zoom: 50%;" />



또 다른 객체 생성 방법(입력 값에 따른 생성)

<img src="JS기초강좌.assets/image-20221025233842627.png" alt="image-20221025233842627" style="zoom:50%;" />

for in 을 이용한 조회

<img src="JS기초강좌.assets/image-20221025231146610.png" alt="image-20221025231146610" style="zoom:33%;" />

<img src="JS기초강좌.assets/image-20221025233946668.png" alt="image-20221025233946668" style="zoom:50%;" />

<img src="JS기초강좌.assets/image-20221025233958117.png" alt="image-20221025233958117" style="zoom:50%;" />



<img src="JS기초강좌.assets/image-20221025234531877.png" alt="image-20221025234531877" style="zoom:50%;" />



Object의 key 값 가져오기

<img src="JS기초강좌.assets/image-20221025234639291.png" alt="image-20221025234639291" style="zoom:50%;" />



Object의 value 값 가져오기

<img src="JS기초강좌.assets/image-20221025234709544.png" alt="image-20221025234709544" style="zoom:50%;" />

---

### 객체 - method

<img src="JS기초강좌.assets/image-20221025234830103.png" alt="image-20221025234830103" style="zoom: 33%;" />

아래와 같이 줄여서 사용도 가능

<img src="JS기초강좌.assets/image-20221025234843849.png" alt="image-20221025234843849" style="zoom:33%;" />



<img src="JS기초강좌.assets/image-20221025235012305.png" alt="image-20221025235012305" style="zoom:33%;" />

그래서 객체 내부에서의 method 을 사용할 경우엔 this를 사용하지 말기

---

### Array

<img src="JS기초강좌.assets/image-20221025235516017.png" alt="image-20221025235516017" style="zoom:33%;" />





<img src="JS기초강좌.assets/image-20221025235540676.png" alt="image-20221025235540676" style="zoom:33%;" />



배열 메서드

<img src="JS기초강좌.assets/image-20221025235629151.png" alt="image-20221025235629151" style="zoom:33%;" />



<img src="JS기초강좌.assets/image-20221025235708228.png" alt="image-20221025235708228" style="zoom:33%;" />