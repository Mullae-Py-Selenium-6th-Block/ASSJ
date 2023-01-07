import "./App.css";
import Sidebar from "./component/Sidebar/Sidebar";
import { useEffect, useState } from "react";
import MainDash from "./component/MainDash/MainDash";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Web from "./Pages/Web";
import axios from "axios";
import Modal from "./component/kakaomap/modal";

function App() {
  const [selectedGu, setSelectedGu] = useState([-1, ""]);
  const [graphData, setGraphData] = useState({});
  const [isClicked, setIsClicked] = useState(false);
  const [rankingdata, setRankingData] = useState({});

  const [modalOpen, setState] = useState(false);
  const openModal = () => {
    setState(true);
  };
  const closeModal = () => {
    setState(false);
  };

  useEffect(() => {
    if (selectedGu[0] === -1) {
      return;
    }
    axios
      .get("http://localhost:8000/assj/" + String(selectedGu[0]) + "/")
      .then((response) => {
        setGraphData(response.data);
      });
    openModal();
  }, [selectedGu]);

  useEffect(() => {
    console.log("useeffect");
    console.log(isClicked);
    if (isClicked === false) {
      axios
        .get("http://localhost:8000/assj/ranking/order/0/")
        .then((response) => {
          setRankingData(response.data);
        });
    } else if (isClicked === true) {
      axios
        .get("http://localhost:8000/assj/ranking/order/1/")
        .then((response) => {
          setRankingData(response.data);
        });
    }
  }, [isClicked]);

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
            <Route
              path="/rank"
              element={
                <MainDash isClicked={isClicked} setIsClicked={setIsClicked} />
              }
            ></Route>
          </Routes>
        </div>
        <Modal
          open={modalOpen}
          close={closeModal}
          selectedGu={selectedGu}
          setSelectedGu={setSelectedGu}
          graphData={graphData}
        />
        ;
      </div>
    </BrowserRouter>
  );
}

export default App;
