import {Navbar,Nav} from 'react-bootstrap';

let nav = [
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
]


let datas = [
  {
    id : 0,
    title : "White and Black",
    content : "Born in France",
    price : 120000
  },

  {
    id : 1,
    title : "Red Knit",
    content : "Born in Seoul",
    price : 110000
  },

  {
    id : 2,
    title : "Grey Yordan",
    content : "Born in the States",
    price : 130000
  }
] 

let items = [
  <div style={{marginRight:'4px'}}>
    <img className='items' src="https://images.pexels.com/photos/4602025/pexels-photo-4602025.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2" alt="" />
    <p style={{marginTop:'7px'}}>{datas[0].title}</p>
    <p>{datas[0].content}</p>
  </div>,
  <div style={{marginRight:'4px', marginLeft:'2px'}}>
    <img className='items' src="https://images.pexels.com/photos/4276653/pexels-photo-4276653.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2" alt="" />
    <p style={{marginTop:'7px'}}>{datas[1].title}</p>
    <p>{datas[1].content}</p>
  </div>,
  <div style={{marginLeft:'4px'}}>
    <img className='items' src="https://images.pexels.com/photos/4061385/pexels-photo-4061385.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2" alt="" />
    <p style={{marginTop:'7px'}}>{datas[2].title}</p>
    <p>{datas[2].content}</p>
  </div>
]

export {nav, items, datas}