import "./App.css";
import Sidebar from "./component/Sidebar/Sidebar";

import { useEffect, useState } from "react";
import MainDash from "./component/MainDash/MainDash";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Web from "./Pages/Web";

import axios from "axios";
function App() {
  const [selectedGu, setSelectedGu] = useState(-1);
  const [graphData, setGraphData] = useState({});

  useEffect(() => {
    if (selectedGu === -1) {
      return;
    }
    axios
      .get("http://localhost:8000/assj/" + String(selectedGu) + "/")
      .then((response) => {
        setGraphData(response.data);
      });
  }, [selectedGu]);

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
