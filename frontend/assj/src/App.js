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
  const [detailDataList, setDetailList] = useState([]); //2번 페이지 클릭된 구 데이터

  const [modalOpen, setState] = useState(false); //1번페이지 모달 창 state
  const [DetailOpen, setDetailiOpenState] = useState(false); //1번페이지 모달 창 state

  const [pageSide, setPageSide] = useState("http://localhost:3000/");
  const [sideSelected, setSideSelected] = useState(0);
  const [economics, setEconomics] = useState([]);
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
    var link = document.location.href;
    if (link === "http://43.201.96.246/") {
      setSideSelected(0);
    } else {
      axios.get("http://43.201.96.246/assj/economics/").then((response) => {
        setEconomics(response.data.data[0]);
      });
      setSideSelected(1);
    }
  }, [pageSide]);

  useEffect(() => {
    if (selectedGu[0] === -1) {
      return;
    }
    axios
      .get("http://43.201.96.246/assj/" + String(selectedGu[0]) + "/")
      .then((response) => {
        setGraphData(response.data);
        response.data.map((elem, idx) => {
          if (idx === 119) {
            elem.price = response.data[118].nextprice;
          }
        });
        openModal();
      });
  }, [selectedGu]);

  useEffect(() => {
    if (isClicked === false) {
      axios
        .get("http://43.201.96.246/assj/ranking/order/1/")
        .then((response) => {
          setRankingData(response.data?.data);
        });
    } else if (isClicked === true) {
      axios
        .get("http://43.201.96.246/assj/ranking/order/0/")
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
        "http://43.201.96.246/assj/ranking/" +
          String(detailGu[0]) +
          "/?format=json"
      )
      .then((response) => {
        const price = [];
        const totalhousenums = [];
        const tradingvolume = [];
        const convertrate = [];
        const responsedata = response.data;
        for (let i = 0; i < responsedata.length; i++) {
          price.push({
            x: responsedata[i].date,
            y: responsedata[i].price,
            y1: responsedata[i].price,
          });
          if (responsedata[i].totalhousenums !== null) {
            totalhousenums.push({
              x: responsedata[i].date,
              y: responsedata[i].totalhousenums,
            });
          }
          if (responsedata[i].tradingvolume !== null) {
            tradingvolume.push({
              x: responsedata[i].date,
              y: responsedata[i].tradingvolume,
            });
          }
          if (responsedata[i].tradingvolume !== null) {
            convertrate.push({
              x: responsedata[i].date,
              y: responsedata[i].convertrate,
            });
          }
        }

        price[price.length - 1].y1 =
          responsedata[responsedata.length - 2].nextprice;
        setDetail(responsedata);
        setDetailList([price, totalhousenums, tradingvolume, convertrate]);
        openDetail();
      });
  }, [detailGu]);

  return (
    <BrowserRouter>
      <div className="App">
        <div className="AppGlass">
          <Sidebar
            sideSelected={sideSelected}
            setSideSelected={setSideSelected}
          />
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
                  economics={economics}
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
          detailDataList={detailDataList}
        />
      </div>
    </BrowserRouter>
  );
}

export default App;
