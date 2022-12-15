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
    <img className='items' style={{height:'70%'}} src="https://codingapple1.github.io/shop/shoes1.jpg" alt="" />
    <p style={{marginTop:'7px'}}>{datas[0].title}</p>
    <p>{datas[0].content}</p>
  </div>,
  <div style={{marginRight:'4px', marginLeft:'2px'}}>
    <img className='items' style={{height:'70%'}} src="https://codingapple1.github.io/shop/shoes2.jpg" alt="" />
    <p style={{marginTop:'7px'}}>{datas[1].title}</p>
    <p>{datas[1].content}</p>
  </div>,
  <div style={{marginLeft:'4px'}}>
    <img className='items' style={{height:'70%'}} src="https://codingapple1.github.io/shop/shoes3.jpg" alt="" />
    <p style={{marginTop:'7px'}}>{datas[2].title}</p>
    <p>{datas[2].content}</p>
  </div>
]

export {items, datas}