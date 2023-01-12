import React from "react";
import "./MainDash.css";
import Card from "../Card/Card";

import { useState } from "react";
import RankingList from "../RankingList/RankingList";
const MainDash = ({
  isClicked,
  setIsClicked,
  rankingData,
  detailGu,
  setDetail,
}) => {
  return (
    <div className="MainDash">
      <div className="Top3">
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
          rankingData={rankingData ? rankingData.slice(3) : []}
          setIsClicked={setIsClicked}
          isClicked={isClicked}
        />
      </div>
    </div>
  );
};

export default MainDash;
