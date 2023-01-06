import React, { useState } from "react";
import "./RankingList.css";
import Switch from "../Switch/Switch";
import Red from "../../img/Red.png";
import Green from "../../img/Green.png";
import Yellow from "../../img/Yellow.png";

const RankingList = () => {
 const [isToggled, setIsToggled] = useState(false);
 return (
  <div className="RankingList">
   <div className="titbox">
    자치구 랭킹
    <Switch isToggled={isToggled} onToggle={() => setIsToggled(!isToggled)} />
   </div>
   <div className="listData">
    <div className="listheader">
     <span className="column">순위</span>
     <span className="column">자치구명</span>
     <span className="column">가격 증감율(%)</span>
     <span className="column">현재 평균매매가(만원)</span>
     <span className="column">예상 평균매매가(만원)</span>
     <span className="column">통계 신호등</span>
    </div>

    <div className="listheader">
     <span className="column">1</span>
     <span className="column">강남구</span>
     <span className="column">
      <div className="column3">+1.04</div>
     </span>
     <span className="column">110,000</span>
     <span className="column">10,000</span>
     <span className="column">
      <img src={Green} alt="" />
     </span>
    </div>
    <div className="listheader">
     <span className="column">1</span>
     <span className="column">강남구</span>
     <span className="column">
      <div className="column3">+1.04</div>
     </span>
     <span className="column">110,000</span>
     <span className="column">10,000</span>
     <span className="column">
      <img src={Green} alt="" />
     </span>
    </div>
    <div className="listheader">
     <span className="column">1</span>
     <span className="column">강남구</span>
     <span className="column">
      <div className="column3">+1.04</div>
     </span>
     <span className="column">110,000</span>
     <span className="column">10,000</span>
     <span className="column">
      <img src={Green} alt="" />
     </span>
    </div>
    <div className="listheader">
     <span className="column">1</span>
     <span className="column">강남구</span>
     <span className="column">
      <div className="column3">+1.04</div>
     </span>
     <span className="column">110,000</span>
     <span className="column">10,000</span>
     <span className="column">
      <img src={Green} alt="" />
     </span>
    </div>
    <div className="listheader">
     <span className="column">1</span>
     <span className="column">강남구</span>
     <span className="column">
      <div className="column3">+1.04</div>
     </span>
     <span className="column">110,000</span>
     <span className="column">10,000</span>
     <span className="column">
      <img src={Green} alt="" />
     </span>
    </div>
    <div className="listheader">
     <span className="column">1</span>
     <span className="column">강남구</span>
     <span className="column">
      <div className="column3">+1.04</div>
     </span>
     <span className="column">110,000</span>
     <span className="column">10,000</span>
     <span className="column">
      <img src={Green} alt="" />
     </span>
    </div>
    <div className="listheader">
     <span className="column">1</span>
     <span className="column">강남구</span>
     <span className="column">
      <div className="column3">+1.04</div>
     </span>
     <span className="column">110,000</span>
     <span className="column">10,000</span>
     <span className="column">
      <img src={Green} alt="" />
     </span>
    </div>
    <div className="listheader">
     <span className="column">1</span>
     <span className="column">강남구</span>
     <span className="column">
      <div className="column3">+1.04</div>
     </span>
     <span className="column">110,000</span>
     <span className="column">10,000</span>
     <span className="column">
      <img src={Green} alt="" />
     </span>
    </div>
   </div>
  </div>
 );
};

export default RankingList;
