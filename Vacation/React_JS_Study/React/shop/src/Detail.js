import { useParams } from "react-router-dom"
import {datas} from './data'

function Detail(props) {

  let {id} = useParams()

  let data = props.datas.find((data)=> {
    console.log(data);
    return data.id === Number(id)
  })

  let dataId = data.id+1

  return (
    <div style={{display:'flex', justifyContent:'center',alignItems:'center'}}>
      <div style={{marginRight:'4px'}}>
        <img className='items' style={{height:'50%'}} src={'https://codingapple1.github.io/shop/shoes' + dataId +'.jpg'} alt="" />
        <p style={{marginTop:'7px'}}>{datas[data.id].title}</p>
        <p>{datas[data.id].content}</p>
      </div>
    </div>
  )
}

export default Detail