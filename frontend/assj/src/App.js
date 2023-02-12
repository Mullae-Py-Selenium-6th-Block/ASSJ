import "./App.css";
import Sidebar from "./component/Sidebar/Sidebar";
import { useEffect, useState } from "react";
import { BrowserRouter } from "react-router-dom";
import { rankingDetailInfo, rankingInfo } from "./api/ranking";
import { getEconomicInfo } from "./api/economic";
import { getGuInfo } from "./api/gu-info";
import Routers from "./routes/routers";

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

  const [sideSelected, setSideSelected] = useState(
    document.location.href === "http://localhost:3000/" ? 0 : 1
  );
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
    if (link === "http://localhost:3000/") {
      setSideSelected(0);
    } else {
      setSideSelected(1);
      getEconomicInfo().then((result) => setEconomics(result));
      console.log(economics);
    }
  }, [document.location.href]);

  useEffect(() => {
    if (selectedGu[0] === -1) {
      return;
    }
    getGuInfo(selectedGu[0]).then((result) => setGraphData(result));
    openModal();
  }, [selectedGu]);

  useEffect(() => {
    isClicked
      ? rankingInfo(0).then((result) => setRankingData(result))
      : rankingInfo(1).then((result) => setRankingData(result));
  }, [isClicked]);

  useEffect(() => {
    if (detailGu[0] === -1) {
      return;
    }
    console.log(detailGu[0]);
    rankingDetailInfo(detailGu[0]).then((res) => {
      setDetail(res[4]);
      setDetailList([res[0], res[1], res[2], res[3]]);
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
          <Routers
            selectedGu={selectedGu}
            setSelectedGu={setSelectedGu}
            modalOpen={modalOpen}
            closeModal={closeModal}
            graphData={graphData}
            economics={economics}
            isClicked={isClicked}
            setIsClicked={setIsClicked}
            rankingData={rankingData}
            setDetailGu={setDetailGu}
            DetailOpen={DetailOpen}
            closeDetail={closeDetail}
            detailGu={detailGu}
            detailData={detailData}
            detailDataList={detailDataList}
          />
        </div>
      </div>
    </BrowserRouter>
  );
}

export default App;
