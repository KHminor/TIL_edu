import {Table} from 'react-bootstrap';
import { useSelector } from 'react-redux';


function Cart(props) {

  let cartData = useSelector((state)=> { return state.cartData })
  // console.log(cartData);
  return (
    <div>
      <Table>
        <thead>
          <tr>
            <th>#</th>
            <th>상품번호</th>
            <th>상품명</th>
            {/* <th>변경하기</th> */}
          </tr>
        </thead>
        {
          cartData.map((data, idx)=> {
            let index = idx+1
            return (
              <tbody>
                <tr>
                  <td>{index}</td>
                  <td>{data.id}</td>
                  <td>{data.name}</td>
                </tr>
              </tbody>
            )
          })
        }
        
        
      </Table> 
    </div>
  )
}

export default Cart