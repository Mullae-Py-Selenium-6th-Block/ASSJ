import React from "react";
import RankingList from "../RankingList/RankingList";
import Top3 from "../Top3/Top3";
import "./MainDash.css";

const MainDash = () => {
 return (
  <div className="MainDash">
   <Top3 />
   <RankingList />
  </div>
 );
};

export default MainDash;
