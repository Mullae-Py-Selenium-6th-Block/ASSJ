import React from "react";
import "./MainDash.css";
import Card from "../Card/Card";
import axios from "axios";

import RankingList from "../RankingList/RankingList";

const MainDash = ({
  isClicked,
  setIsClicked,
  rankingData,
  detailGu,
  setDetail,
}) => {
  // var economicData = {};
  // console.log(axios.get("http://43.201.96.246/assj/economics/"));
  return (
    <div className="MainDash">
      <div className="economic-info">
        <div className="infoeco baserate">기준금리</div>
        <div className="infoeco exchagerate">원/달러 환율</div>
        <div className="infoeco m2">M2통화량</div>
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
