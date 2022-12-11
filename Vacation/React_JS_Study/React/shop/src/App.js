import './App.css';
import React ,{useState} from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import {nav, items} from './data.js'


function App() {

  let [item, setItems] = useState(items)

  return (
    <div className="App">
      {/* navbar */}
      {nav}
      
      <div className='main-bg'>
        {/* 배경사진 */}
      </div>

      <div className='contain'>
        <div></div>
        {item.map((item) => {
          return item
        })}
        <div></div>
      </div>
    </div>
  );
}

export default App;