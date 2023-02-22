1. React 시작
   * npm create-react-app {{프로젝트명}} 



2. 리엑스에서 데이터 바인딩
   * {} 중괄호를 사용하여 바인딩 하기 (className과 같은 거의 모든 곳에서 사용이 가능)

```react
import './App.css';
import logo from './logo.svg'

function App() {
	// let post = "강남 고기 맛집"
	function 함수() {
		return 100
	}
 
  return (
	    <div className="App">
      <div className="black-nav">
        <div>개발 Blog</div>
      </div>
			<h4> {함수()} </h4>
      <img src={logo} alt="" />
    </div>
  );
}

export default App;

```



3. JSX에서 Style 속성을 집어넣을 때

   - Vue, Html에서 Style의 속성을 집어넣을 때처럼 style='font-size: 16px' 와 같이 하는 것이 아닌
   - style={스타일} 로 객체 성격을 나타낼 수 있도록 해야한다.

   ```react
   <div style={ 
           {font-size: 16px,
           color: 'blue'     
           } }>스타일</div>
   ```

   - 다수의 스타일을 집어넣을 경우 , 를 기준으로 작성하면 된다
   - 오른쪽의 value의 값은 항상 문자열로 작성
   - 또한 font-size와 같이 케밥케이스로 작성하는 것을 카멜케이스로 변경하여 작성해야한다. (이유는 js에서 -는 뺄셈이기 때문.)

   ```react
   <div style={ {color: 'black', fontSize: '16px'} }>스타일 복수 작성</div>
   ```

   * 여기서 해당 div들에 대해 계속 이렇게 작성하기 귀찮을 경우 바인딩을 사용하여 작성할 수 있다.

   ```react
   import './App.css';
   import logo from './logo.svg'
   
   function App() {
   
     let post = {color: 'blue', fontSize: '30px'}
    
     return (
   	<div className="App">
         <div className="black-nav">
           <div style={ post }>
               개발 Blog
           </div>
         </div>
       </div>
     );
   }
   
   export default App;
   
   ```

   

4. 리엑트에서 데이터 관리법

   1. 변수에 넣기

      * `변경이 자주 되지 않는 경우의 데이터의 경우 사용하기`
      * let data = '~~~~~~'

   2. State에 넣기

      * state에 데이터를 저장해놓고 사용하는 이유?
        * `state 안의 데이터가 변경되면 새로고침이 없어도 HTML이 자동으로 재랜더링이 되기 때문이다.`
        * 그래서 부드럽게 새로고침 없이 변경이 된다.
        * useState에서 S 대문자는 필수
      * state는 변수 대신 쓰는 데이터 저장공간

      1. 상단에 import React, { useState } from 'react' 추가

      2. useState(데이터)

         * ex) useState("남자 코트 추천");

         * 이렇게 작성을 하게 되면 [a,b] 이런 두개의 array에 생성이 된다.

         * a에는 남자 코트 추천

         * b에는 남자 코트 추천 state를 정정해주는 함수

         * 그래서 요즘에 작성하는 코드 방식은

           * let [a,b] = useState('남자 코트 추천')
           * ES6 destructuring 문법이다.
             * 파이썬에서는 익숙한 문법으로 파이썬에서는 a,b = 10,20 으로 사용되는데 
             * 리엑트에서는 let [a,b] = [10,20] 이렇게 사용된다.
             * 그래서 let [글제목,글제목변경] = useState('남자 코트 추천')

         * 또한 useState()안에는 문자, 숫자, array, object 모두 저장가능하다

           * ex.
           * let [글제목,글제목변경] = useState(['남자 코드 추천', '강남 우동 맛집'])

           ```react
           import React, { useState } from "react";
           import "./App.css";
           // import logo from "./logo.svg";
           
           function App() {
             let [글제목, 글제목변경] = useState(["남자 코드 추천", "강남 우동 맛집"]);
             let [글제목2, 글제목변경2] = useState("여자 코트 추천");
           
             // let posts = "연제 고기 맛집";
             return (
               <div className="App">
                 <div className="black-nav">
                   <div>개발 Blog</div>
                 </div>
                 <div className="list">
                   <h3> {글제목[0]} </h3>
                   <h3> {글제목[1]} </h3>
                   <p>11월 28일 발행</p>
                   <hr />
                 </div>
                 <div className="list">
                   <h3> {글제목2} </h3>
                   <p>11월 28일 발행</p>
                   <hr />
                 </div>
               </div>
             );
           }
           
           export default App;
           
           ```

           