import "./App.css";
import { Main } from "./Routes/Main";
import { Routes, Route, useNavigate } from "react-router-dom";
function App() {
  let navigate = useNavigate();
  return (
    <div className="App">
      <div
        onClick={() => {
          navigate("/main");
        }}
        style={{ height: "5vh", cursor: "pointer", backgroundColor: "skyblue" }}
      ></div>
      <Routes>
        <Route path="/main" element={<Main />} />
      </Routes>
    </div>
  );
}

export default App;
