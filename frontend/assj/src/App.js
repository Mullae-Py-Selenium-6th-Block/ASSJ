import "./App.css";
import Sidebar from "./component/Sidebar/Sidebar";
import { useEffect, useState } from "react";
import MainDash from "./component/MainDash/MainDash";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Web from "./Pages/Web";
import axios from "axios";
import Modal from "./component/kakaomap/modal";
import DetailModal from "./component/DetailModal/DetailModal";

function App() {
  const [selectedGu, setSelectedGu] = useState([-1, ""]); //1번 페이지 구 선택
  const [graphData, setGraphData] = useState({}); //1번 페이지 구 데이터

  const [isClicked, setIsClicked] = useState(false); //2번 페이지 랭킹 정렬 스위치 버튼
  const [rankingData, setRankingData] = useState([]); //2번 페이지 랭킹 데이터

  const [detailGu, setDetailGu] = useState([-1, ""]); //2번 페이지 클릭된 구
  const [detailData, setDetail] = useState([]); //2번 페이지 클릭된 구 데이터

  const [modalOpen, setState] = useState(false); //1번페이지 모달 창 state
  const [DetailOpen, setDetailiOpenState] = useState(false); //1번페이지 모달 창 state

  const openModal = () => {
    setState(true);
  };
  const closeModal = () => {
    setState(false);
  };
  const openDetail = () => {
    setDetailiOpenState(true);
  };
  const closeDetail = () => {
    setDetailiOpenState(false);
  };
  useEffect(() => {
    if (selectedGu[0] === -1) {
      return;
    }
    axios
      .get("http://127.0.0.1:8000/assj/" + String(selectedGu[0]) + "/")
      .then((response) => {
        setGraphData(response.data);
        response.data.map((elem, idx) => {
          if (idx === 119) {
            elem.price = response.data[118].nextprice;
          }
        });
      });
    openModal();
  }, [selectedGu]);

  useEffect(() => {
    console.log(isClicked);
    if (isClicked === false) {
      axios
        .get("http://127.0.0.1:8000/assj/ranking/order/1/")
        .then((response) => {
          setRankingData(response.data?.data);
        });
    } else if (isClicked === true) {
      axios
        .get("http://127.0.0.1:8000/assj/ranking/order/0/")
        .then((response) => {
          setRankingData(response.data?.data);
        });
    }
  }, [isClicked]);

  useEffect(() => {
    if (detailGu[0] === -1) {
      return;
    }
    axios
      .get(
        "http://127.0.0.1:8000/assj/ranking/" +
          String(detailGu[0]) +
          "/?format=json"
      )
      .then((response) => {
        setDetail(response.data);
        openDetail();
      });
  }, [detailGu]);

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
                <MainDash
                  isClicked={isClicked}
                  setIsClicked={setIsClicked}
                  rankingData={rankingData}
                  detailGu={detailGu}
                  setDetail={setDetailGu}
                />
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
        <DetailModal
          open={DetailOpen}
          close={closeDetail}
          detailGu={detailGu}
          detailData={detailData}
        />
      </div>
    </BrowserRouter>
  );
}

export default App;
