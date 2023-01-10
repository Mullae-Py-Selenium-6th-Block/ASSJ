import React from "react";
import RankingList from "../RankingList/RankingList";
import Top3 from "../Top3/Top3";
import "./MainDash.css";

const MainDash = ({ isClicked, setIsClicked }) => {
  return (
    <div className="MainDash">
      <Top3 isClicked={isClicked} setIsClicked={setIsClicked} />
      <RankingList isClicked={isClicked} setIsClicked={setIsClicked} />
    </div>
  );
};

export default MainDash;
