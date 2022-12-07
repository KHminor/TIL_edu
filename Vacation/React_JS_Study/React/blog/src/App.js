import React, { useState } from "react";
import "./App.css";

function App() {
  let [글제목, 글제목함수] = useState(["남자코트", "강남 우동맛집", "파이썬독학"]);


  return (
    <div className="App">
      <nav>
        <a href="https://www.naver.com/">Naver</a>
        <a href="https://github.com/KHminor">Git</a>
      </nav>
      <div className="black-nav">개발 Blog</div>
      <h1>Algorithm</h1>
      <div className="container">
        <div className="item"></div>
        <div id="code" className="item">
          <h2>[BOJ]2869-달팽이는 올라가고 싶다</h2><hr />
          <pre>
          import sys<br /><br />
          a,b,v = map(int,sys.stdin.readline().split()) <br />
          <br />
          if (v-a)%(a-b): <br />
          &nbsp;&nbsp;&nbsp;&nbsp;print(((v-a)//(a-b))+2)<br />
          else<br />
          &nbsp;&nbsp;&nbsp;&nbsp;print(((v-a)//(a-b))+1)<br />
          </pre>
        </div>
        <div className="item"></div>
      </div>
    </div>
  );
}

export default App;
