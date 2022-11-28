import React, { useState } from "react";
import "./App.css";

function App() {
  let [글제목, 글제목함수] = useState(["코트", "아우터", "바지"]);
  let [글제목2, 글제목함수2] = useState(["221127", "221128", "221129"]);
  return (
    <div className="App">
      <div className="black-nav">개발 Blog</div>

      <div className="list">
        <div style={{ textAlign: "start" }}>
          <p style={{ fontSize: "1.5rem" }}>남자 코트 추천</p>
          <p>2월 17일 발행</p>
        </div>
        <hr />
        <div>
          <h1>{글제목[0]}</h1>
          {글제목2[0]}
        </div>
        <hr />
        <div>
          <h1>{글제목[1]}</h1>
          {글제목2[1]}
        </div>
        <hr />
        <div>
          <h1>{글제목[2]}</h1>
          {글제목2[2]}
        </div>
        <hr />
      </div>
    </div>
  );
}

export default App;
