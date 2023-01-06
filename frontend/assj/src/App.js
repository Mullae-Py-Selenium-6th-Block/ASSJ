import "./App.css";
import Sidebar from "./component/Sidebar/Sidebar";

import { useState } from "react";
import MainDash from "./component/MainDash/MainDash";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Web from "./Pages/Web";

function App() {
  const url = "http://localhost:8000/assj/";
  fetch(url)
    .then((res) => res.json())
    .then((data) => console.log(data));
  const [selectedGu, setSelectedGu] = useState(-1);
  return (
    <BrowserRouter>
      <div className="App">
        <div className="AppGlass">
          <Sidebar />
          <Routes>
            <Route
              path="/*"
              element={
                <Web setSelectedGu={setSelectedGu} selectedGu={selectedGu} />
              }
            ></Route>
            <Route path="/rank" element={<MainDash />}></Route>
          </Routes>
        </div>
      </div>
    </BrowserRouter>
  );
}

export default App;
