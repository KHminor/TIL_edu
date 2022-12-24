import { useEffect, useState } from "react"
import { useParams } from "react-router-dom"
import {datas} from './data'
import Nav from 'react-bootstrap/Nav';
import { useDispatch } from "react-redux";
import { addCartData } from "./store";

function Detail(props) {
  let dispatch = useDispatch()
  let [alertcheck, setAlert] = useState(true) 
  let [inText,setInText] = useState(0)
  let [탭, 탭변경] = useState(0)
  let [fade,setFade] = useState('')

  useEffect(()=> {
    setTimeout(() => {
      setAlert(false)}, 2000);
  }, [])

  useEffect(()=> {
    if (isNaN(inText)) {
      alert('문자입력 ㄴㄴ')
    }
  }, [inText])

  
  useEffect(()=> {
    let a = setTimeout(() => {
      setFade('end')
    }, 250);
    return ()=> {
      clearTimeout(a)
      setFade('')
    }
  }, [탭])

  let {id} = useParams()
  let [num, setNum] = useState(0)
  let data = props.datas.find((data)=> {
    // console.log(data);
    return data.id === Number(id)
  })

  let dataId = data.id+1

  return (
    <div className={"start" + fade}>
      {
        alertcheck === true 
        ? <div id="sale" className="alert alert-warning">
            2초이내 구매시 할인
          </div>
        : null
      }
      <div style={{marginRight:'4px', display:'flex', justifyContent:'center',alignItems:'center'}}>
        <div>
          <img className='items' style={{height:'50%'}} src={'https://codingapple1.github.io/shop/shoes' + dataId +'.jpg'} alt="" />
          {/* <div>
            <input onKeyDown={(e)=> {
              setInText(e.target.value);
            }} type="text" />
          </div> */}
          <p style={{marginTop:'7px'}}>{datas[data.id].title}</p>
          <p>{datas[data.id].content}</p>
          <div>
            <button onClick={()=> {
              // console.log(data);
              dispatch(addCartData(data))
              // dispatch(addCartData({id : 3, name : 'Test', count : 1}))
            }}>주문하기</button>
          </div>
        </div>  
      </div>

      <div style={{display:'grid', gridTemplateColumns:'1fr'}}>
        <div style={{display:'flex', justifyContent:'center',alignItems:'center'}}>
          <Nav variant="tabs" defaultActiveKey="link0">
            <Nav.Item>
              <Nav.Link onClick={()=> {탭변경(0)}} eventKey="link0">버튼0</Nav.Link>
            </Nav.Item>
            <Nav.Item>
              <Nav.Link onClick={()=> {탭변경(1)}} eventKey="link1">버튼1</Nav.Link>
            </Nav.Item>
            <Nav.Item>
              <Nav.Link onClick={()=> {탭변경(2)}} eventKey="link2">버튼2</Nav.Link>
            </Nav.Item>
          </Nav>
        </div>
        <div style={{display:'flex', justifyContent:'center',alignItems:'center'}}>
          <TabContent 탭={탭} datas={props.datas}/>
        </div>
      </div>
      
    </div>
  )
}

function TabContent({탭,datas}) {
  let [fade,setFade] = useState('')
  useEffect(()=> {
    let a = setTimeout(() => {
      setFade('end')
    }, 100);
    return ()=> {
      clearTimeout(a)
      setFade('')
    }
  }, [탭])

  return (
    <div className={'start '+ fade}>
      { [<div>{datas[0].title}</div>,<div>내용1</div>,<div>내용2</div>][탭] }
    </div>
  )
}

export default Detail