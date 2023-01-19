import React from "react";
import "./MainDash.css";
import Card from "../Card/Card";
import axios from "axios";

import RankingList from "../RankingList/RankingList";

const MainDash = ({
  economics,
  isClicked,
  setIsClicked,
  rankingData,
  detailGu,
  setDetail,
}) => {
  return (
    <div className="MainDash">
      <div className="economic-info">
        <div className="infoeco baserate">기준금리: {economics[2]}</div>
        <div className="infoeco exchagerate">원/달러 환율: {economics[1]}</div>
        <div className="infoeco m2">M2통화량: {economics[0]}</div>
      </div>
      <div className="Top3">
        {/* <div>{economics}</div> */}

        <Card
          setDetail={setDetail}
          rankingData={rankingData ? rankingData.slice(0, 3) : []}
          setIsClicked={setIsClicked}
          isClicked={isClicked}
        />
      </div>
      <div>
        <RankingList
          setDetail={setDetail}
          rankingData={rankingData ? rankingData : []}
          setIsClicked={setIsClicked}
          isClicked={isClicked}
        />
      </div>
    </div>
  );
};

export default MainDash;
