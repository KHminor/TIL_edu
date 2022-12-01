import React, { useState } from "react";
import "./App.css";

function App() {
  let [글제목, 글제목함수] = useState(["코트", "아우터", "바지"]);
  let [글제목2, 글제목함수2] = useState(["221127", "221128", "221129"]);
  // let [따봉, 따봉변경] = useState([0,0,0]);
  let [따봉0, 따봉변경0] = useState(0);
  let [따봉1, 따봉변경1] = useState(0);
  let [따봉2, 따봉변경2] = useState(0);
  
  let [성별, 성별변경] = useState(["여자", "남자"]);
  let [modal, setModal] = useState(false)

  function 제목바꾸기() {
    let newArray = [...성별];
    newArray[0] = 성별[1];
    성별변경(newArray);
  }

  return (
    <div className="App">
      <div className="black-nav">개발 Blog</div>

      {
        글제목.map((article,i)=> {
          return (
            <div>
              <h1>{article} <span>👍</span>{따봉`${i}`}</h1>
              <div>{글제목2[i]}</div>
            </div>
          )
        })
      }

      {/* {
        글제목.map((article,i)=> {
          return (
            <div>
              <h1>{글제목[i]} <span onClick={()=> {
                let up = [...따봉]
                up[i] += 1
                따봉변경(up)
              }}>👍</span> {따봉[i]}</h1>
              {글제목2[i]}
            </div>
          )
        })
      } */}
    
      {/* {
        따봉.map((i)=> {return <div>{i}</div> })
      } */}

      {/* <div className="list">
        <button onClick={제목바꾸기}>👩‍🦰</button>
        <div style={{ textAlign: "start" }}>
          <p style={{ fontSize: "1.5rem" }}>{성별[0]}코트 추천</p>
          <p>2월 17일 발행</p>
        </div>
        <hr />
        <div>
          <button
            onClick={() => {
              let newArray = [...글제목];
              newArray[0] = 글제목[2];
              newArray[1] = 글제목[0];
              newArray[2] = 글제목[1];
              글제목함수(newArray);
            }}
          >
            🐱‍🏍
          </button>
          <h1>
            {글제목[0]}{" "}
            <button
              onClick={() => {
                return 따봉변경(따봉 + 1);
              }}
            >
              👍
            </button>
            {따봉}
          </h1>
          {글제목2[0]}
        </div>
        <hr />
        <div>
          <h1>{글제목[1]}</h1>
          {글제목2[1]}
        </div>
        <hr />
        <div>
          <h1 onClick={() => {
            modal == false ? setModal(true) : setModal(false)
            }}>{글제목[2]}</h1>
          {글제목2[2]}
        </div>
        <hr />
      </div>

      {
        modal== true ? <Modal/> : null
      } */}

    </div>
  );
}

function Modal() {
  return (
    <div className="modal">
      <h2>제목</h2>
      <p>날짜</p>
      <p>상세내용</p>
    </div>
  );
}

export default App;
