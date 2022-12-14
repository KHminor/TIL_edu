import './App.css';
import React ,{useState} from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import { items} from './data.js'
import { Routes, Route, Link, useNavigate, Outlet } from 'react-router-dom';
import comp from './newcomponent'
import {Navbar,Nav} from 'react-bootstrap';
import Detail from './Detail'

function App() {

  let [item, setItems] = useState(items)
  let navigate = useNavigate()

  return (
    <div className="App">

      {/* navbar */}
      <Navbar id='navbar' variant="dark">
        <div className="grid subfont">
          <div className=''></div>
          <Nav style={{color:'black',justifyContent: 'center',alignItems: 'center' }} href="#home"><span class="material-symbols-outlined" style={{marginRight:'3px'}}>menu</span>메뉴</Nav>
          <div></div>
          <Nav style={{color:'black',justifyContent: 'center',alignItems: 'center' }}  href="#features"><span class="material-symbols-outlined">search</span>검색</Nav>
          <div></div>
          <Nav className='mainfont' style={{color:'black',justifyContent: 'center',alignItems: 'center', fontSize:'2rem', letterSpacing:'5px', cursor: 'pointer' }} onClick={()=> {navigate('/')}}>LOUIS VUITTON</Nav>
          <div></div>
          <Nav style={{color:'black',justifyContent: 'center',alignItems: 'center', cursor: 'pointer' }}  onClick={()=> {navigate('/detail')}} >위시리스트</Nav>
          <div></div>
          <Nav style={{color:'black',justifyContent: 'center',alignItems: 'center', cursor: 'pointer' }}  onClick={()=>{navigate('/about')}}>My lv</Nav>
          <div></div>
          <Nav style={{color:'black',justifyContent: 'center',alignItems: 'center' }}  href="#pricing"><span class="material-symbols-outlined">shopping_cart_checkout</span></Nav>
        </div>
      </Navbar>

      {/* <Link style={{textDecoration: 'none', color:'black'}} to={'/'}>홈 </Link><br />
      <Link to={'/detail'}>상세페이지</Link><br />
      <Link to={'/comp'}>새로운 컴포넌트</Link> */}

      <Routes>
        <Route path='/' element={<>
        <div className='main-bg'>
        {/* 배경사진 */}
        </div></>} />
          
        <Route path='/detail/:id'  element={<Detail />}/>
        <Route path='/comp' element={<>
          {comp}
        </>}/>

          <Route path='event' element={<> <Event /></>}>
            <Route path='one' element={<><p>첫 주문시 양배추즙 서비스</p></>}/>
            <Route path='two' element={<><p>생일기념 쿠폰받기</p></>}/>
          </Route>

        <Route path='*' element={<>여긴 뭐하러 왔어?</>}/>
      </Routes>
      
      {/* <Items item={item} /> */}
    </div>
  );
}

function Event() {
  return (
    <div>
      <h4>오늘의 이벤트</h4>
      <Outlet></Outlet>
    </div>
  )
}

function Items(props) {
  return (
    <div className='contain'>
      <div></div>
      {props.item.map((item) => {
        return item})}
      <div></div>
    </div>
  )
}

export default App;