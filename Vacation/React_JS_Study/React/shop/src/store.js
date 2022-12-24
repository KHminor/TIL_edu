import { configureStore, createSlice } from '@reduxjs/toolkit'
import user from './store/userSlice'

// let watch = createSlice({
//   name: 'watch',
//   initialState: {'watched':[]},
//   reducers: {
//     changeWatch(state,action) {
//       console.log(action.payload);
      
//     }
//   }
// })
// export let {changeWatch} = watch.actions

let stock = createSlice({
  name: 'stock',
  initialState: [10, 11, 12]
})

let cartData = createSlice({
  name: 'cartData',
  initialState: [
    {id : 0, name : 'White and Black', count : 2},
    {id : 2, name : 'Grey Yordan', count : 1}
    ],
  reducers: {
    changeCartData(state,action) {
      let data = state.filter((data)=> {
        return data.id === action.payload 
      })
      console.log('24번줄의 데이터는 ',data[0])
      data[0].count += 1 
    },
    addCartData(state,action) {
      let data ={id:action.payload.id, name:action.payload.title, count:0}
      let check = state.find((i)=> {
        return i.id === data.id
      })
      console.log(check);
      if (typeof check !== 'undefined' ) {
        alert('이미 장바구니에 해당 상품이 있습니다.')
      }
      else {
        alert('장바구니에 추가했습니다.')
        state.push(data)
      }
    },
    deleteData(state,action) {
      console.log(action.payload);
      let newarray = state.filter((data)=> {
        return data.id !== action.payload
      })

      console.log('array?',newarray);
      return newarray
    }
  }
})

export let {changeCartData,addCartData,deleteData} = cartData.actions 


export default configureStore({
  reducer: { 
    user: user.reducer,
    stock: stock.reducer,
    cartData: cartData.reducer,
    // watch: watch.reducer,
  }
}) 