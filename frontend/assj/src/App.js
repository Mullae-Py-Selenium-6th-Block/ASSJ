import "./App.css";
import Sidebar from "./component/Sidebar/Sidebar";

import { useState } from "react";
import MainDash from "./component/MainDash/MainDash";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Web from "./Pages/Web";

function App() {
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
