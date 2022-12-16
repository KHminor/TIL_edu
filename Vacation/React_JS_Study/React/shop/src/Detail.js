import { useEffect, useState } from "react"
import { useParams } from "react-router-dom"
import {datas} from './data'

function Detail(props) {

  let [alert, setAlert] = useState(true) 

  useEffect(()=> {
    setTimeout(() => {
      setAlert(false)}, 2000);
  }, [])

  let {id} = useParams()
  let [num, setNum] = useState(0)
  let data = props.datas.find((data)=> {
    // console.log(data);
    return data.id === Number(id)
  })

  let dataId = data.id+1

  return (
    <div style={{display:'f lex', justifyContent:'center',alignItems:'center'}}>
      {
        alert === true 
        ? <div id="sale" className="alert alert-warning">
            2초이내 구매시 할인
          </div>
        : null
      }
      <button onClick={()=> {setNum(num+1)}}>{num}</button>
      <div style={{marginRight:'4px'}}>
        <img className='items' style={{height:'50%'}} src={'https://codingapple1.github.io/shop/shoes' + dataId +'.jpg'} alt="" />
        <p style={{marginTop:'7px'}}>{datas[data.id].title}</p>
        <p>{datas[data.id].content}</p>
      </div>
    </div>
  )
}

export default Detail