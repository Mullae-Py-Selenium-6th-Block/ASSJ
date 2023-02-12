import RankingPage from "../Pages/rankingPage";
import Main from "../Pages/main";
import { Route, Routes } from "react-router-dom";

const Routers = ({
  selectedGu,
  setSelectedGu,
  modalOpen,
  closeModal,
  graphData,
  economics,
  isClicked,
  setIsClicked,
  rankingData,
  setDetailGu,
  DetailOpen,
  closeDetail,
  detailGu,
  detailData,
  detailDataList,
}) => {
  return (
    <Routes>
      <Route
        path="/*"
        element={
          <Main
            selectedGu={selectedGu}
            setSelectedGu={setSelectedGu}
            modalOpen={modalOpen}
            closeModal={closeModal}
            graphData={graphData}
          />
        }
      ></Route>
      <Route
        path="/rank"
        element={
          <RankingPage
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
        }
      ></Route>
    </Routes>
  );
};

export default Routers;
