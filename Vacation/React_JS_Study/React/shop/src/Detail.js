import { useParams } from "react-router-dom"
import {datas} from './data'

function Detail(props) {

  let {id} = useParams()
  
  return (
    <div className="contain">
      <div style={{marginRight:'4px'}}>
        <img className='items' src="https://images.pexels.com/photos/4602025/pexels-photo-4602025.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2" alt="" />
        <p style={{marginTop:'7px'}}>{datas[id].title}</p>
        <p>{datas[id].content}</p>
      </div>
    </div>
  )
}

export default Detail