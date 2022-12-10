import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import {Navbar,Nav} from 'react-bootstrap';



function App() {
  return (
    <div className="App">
      <Navbar id='navbar' variant="dark">
        <div className="grid subfont">
          <div className=''></div>
          <Nav style={{color:'black',justifyContent: 'center',alignItems: 'center' }} href="#home"><span class="material-symbols-outlined" style={{marginRight:'3px'}}>menu</span>메뉴</Nav>
          <div></div>
          <Nav style={{color:'black',justifyContent: 'center',alignItems: 'center' }}  href="#features"><span class="material-symbols-outlined">search</span>검색</Nav>
          <div></div>
          <Nav className='mainfont' style={{color:'black',justifyContent: 'center',alignItems: 'center', fontSize:'2rem', letterSpacing:'5px'}}  href="#home" >LOUIS VUITTON</Nav>
          <div></div>
          <Nav style={{color:'black',justifyContent: 'center',alignItems: 'center' }}  href="#home" >위시리스트</Nav>
          <div></div>
          <Nav style={{color:'black',justifyContent: 'center',alignItems: 'center' }}  href="#pricing">My lv</Nav>
          <div></div>
          <Nav style={{color:'black',justifyContent: 'center',alignItems: 'center' }}  href="#pricing"><span class="material-symbols-outlined">shopping_cart_checkout</span></Nav>
        </div>
      </Navbar>
      
      <div className='main-bg'>
        {/* 배경사진 */}
      </div>

      <div className='contain'>
        <div></div>
        <div style={{marginRight:'4px'}}>
          <img className='items' src="https://images.pexels.com/photos/4602025/pexels-photo-4602025.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2" alt="" />
          <p style={{marginTop:'7px'}}>의류</p>
          <p>상품설명</p>
        </div>
        <div style={{marginRight:'4px', marginLeft:'2px'}}>
          <img className='items' src="https://images.pexels.com/photos/4276653/pexels-photo-4276653.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2" alt="" />
          <p style={{marginTop:'7px'}}>백</p>
          <p>상품설명</p>
        </div>
        <div style={{marginLeft:'4px'}}>
          <img className='items' src="https://images.pexels.com/photos/4061385/pexels-photo-4061385.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2" alt="" />
          <p style={{marginTop:'7px'}}>신발</p>
          <p>상품설명</p>
        </div>
        <div></div>
      </div>
    </div>
  );
}

export default App;
