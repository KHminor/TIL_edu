import './App.css';
import Main from './Routes/Main';
import {Routes,Route, useNavigate} from 'react-router-dom'
function App() {
  let navigator = useNavigate()
  return (
    <div className="App">
      <div onClick={()=> {
        navigator('/main')
      }} style={{height:'10vh', backgroundColor:'skyblue', cursor:'pointer'}}>고고</div>
      <Routes>
        <Route path='/main' element={<><Main/></>}/>
      </Routes> 
    </div>
  );
}

export default App;
