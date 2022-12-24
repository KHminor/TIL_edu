import {Table} from 'react-bootstrap';
import { useDispatch, useSelector } from 'react-redux';
import { upAge } from '../store/userSlice';
import { changeCartData, deleteData } from '../store'
import { useEffect } from 'react';


function Cart() {

  let dispatch = useDispatch()
  let user = useSelector((state)=> { return state.user })
  let cartData = useSelector((state)=> { return state.cartData })

  // useEffect(()=> {
  //   // alert('추가되었습니다')
  // },[cartData])

  // console.log(cartData);
  return (
    <div>
      <h6>{user.name} 장바구니 ({user.age}살)</h6>
      <button onClick={()=> {dispatch(upAge(10))}}>나이 증가 버튼</button>
      <Table>
        <thead>
          <tr>
            <th>#</th>
            <th>상품번호</th>
            <th>상품명</th>
            <th>수량</th>
            {/* <th>변경하기</th> */}
          </tr>
        </thead>
        <tbody>
          {  
            cartData.map((data, idx)=> {
              let index = idx+1
              console.log(data)
              return ( 
                <tr key={idx}>
                  <td>{index}</td>
                  <td>{data.id}</td>
                  <td>{data.name}</td>
                  <td>{data.count} </td>
                  <td>
                    <button onClick={()=> {
                      dispatch((changeCartData(data.id)))
                    }}>+</button>
                    <button onClick={()=> {
                      dispatch((deleteData(data.id)))
                    }}>제거</button>
                  </td>
                </tr>
              )
            })
          }
        </tbody>
        
        
      </Table> 
    </div>
  )
}

export default Cart