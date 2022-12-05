import React, { useState } from "react";
import "./App.css";

function App() {
  let [글제목, 글제목함수] = useState(["남자코트", "강남 우동맛집", "파이썬독학"]);
  let [글제목2, 글제목함수2] = useState(["221127", "221128", "221129"]);
  let [따봉, 따봉변경] = useState([0,0,0]);
  let [선택글제목,선택글제목변경] = useState(null)
  let [입력값, 입력값변경] = useState('')
  
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
              <h1 onClick={()=> {
                let title = article
                선택글제목변경(title)
                setModal(true)
              }}>{article} <span style={{cursor: 'pointer'}} onClick={(e)=> {
                e.stopPropagation()
                let thumb = [...따봉]
                thumb[i] = 따봉[i] +1
                따봉변경(thumb)
              }}>👍</span>{따봉[i]}</h1>
              <div>{글제목2[i]} <button onClick={(e)=>{
                let title = [...글제목].filter((t) => {
                  return t != article
                })  
                글제목함수(title)
              }}>삭제</button></div>
            </div>
          )
        })
      }
      <br /><br />

      <input id="input" onChange={(e)=> {
        입력값변경(e.target.value)
        console.log(입력값);
      }} onKeyDown={(e)=> {
        if (e.key === 'Enter') {
          console.log(e.key);
          if (입력값 === ''){
            alert('경고')
          }
          else {
            let title = [입력값,...글제목]
            let inp = document.getElementById('input')
            inp.value = ''
            글제목함수(title)
          }
        }
      }} />
      
      <button onClick={()=> {
        if (입력값 === ''){
          alert('경고')
        }
        else {
          let title = [입력값,...글제목]
          let inp = document.getElementById('input')
          inp.value = ''
          글제목함수(title)
        }
        
      }}>저장</button>

      {
        modal == true ? <Modal 선택글제목={선택글제목} 글수정버튼={글제목함수} color="skyblue" bgc={'yellow'} 글제목={글제목}  /> : null
      }

    </div>
  );
}

function Modal(props) {
  return (
    <div className="modal" style={{backgroundColor:props.color}}>
      <h2 id="title">{props.선택글제목}</h2>
      <p>날짜</p>
      <p>상세내용</p>
    </div>
  );
}

export default App;
