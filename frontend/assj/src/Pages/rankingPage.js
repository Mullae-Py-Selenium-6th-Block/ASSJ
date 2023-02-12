import DetailModal from "../component/DetailModal/DetailModal";
import React from "react";
import "./rankingPage.css";
import Card from "../component/Card/Card";
import RankingList from "../component/RankingList/RankingList";

const RankingPage = ({
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
    <>
      <div className="MainDash">
        <div className="economic-info">
          <div className="infoeco baserate">기준금리: {economics[2]}</div>
          <div className="infoeco exchagerate">
            원/달러 환율: {economics[1]}
          </div>
          <div className="infoeco m2">M2통화량: {economics[0]}</div>
        </div>
        <div className="Top3">
          <Card
            setDetail={setDetailGu}
            rankingData={rankingData ? rankingData.slice(0, 3) : []}
            setIsClicked={setIsClicked}
            isClicked={isClicked}
          />
        </div>
        <div>
          <RankingList
            setDetail={setDetailGu}
            rankingData={rankingData ? rankingData : []}
            setIsClicked={setIsClicked}
            isClicked={isClicked}
          />
        </div>
      </div>
      <DetailModal
        open={DetailOpen}
        close={closeDetail}
        detailGu={detailGu}
        detailData={detailData}
        detailDataList={detailDataList}
      />
    </>
  );
};

export default RankingPage;
