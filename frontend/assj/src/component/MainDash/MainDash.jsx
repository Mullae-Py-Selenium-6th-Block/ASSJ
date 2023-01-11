import React from "react";
import { useEffect } from "react";
import "./MainDash.css";
import Card from "../Card/Card";
import Switch from "../Switch/Switch";
import Red from "../../img/Red.png";
import Green from "../../img/Green.png";
import Yellow from "../../img/Yellow.png";
import image from "../../img/Background.png";

const MainDash = ({ isClicked, setIsClicked, rankingData }) => {
  console.log(rankingData);
  return (
    <div className="MainDash">
      <div className="Top3">
        <Card rankingData={rankingData ? rankingData.slice(0, 3) : []} />
      </div>

      <div className="Ranklist">
        <div className="RankingList">
          <div className="titbox">
            자치구 랭킹
            <Switch isClicked={isClicked} setIsClicked={setIsClicked} />
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
            {rankingData
              ? rankingData.slice(3).map(function (data, idx) {
                  return (
                    <div className="listheader">
                      <span className="column">{4 + idx}</span>
                      <span className="column">{data[1]}</span>
                      <span className="column">
                        <div className="column3">
                          {data[2] > 0 ? "+" + data[2] : data[2]}
                        </div>
                      </span>
                      <span className="column">{data[3]}</span>
                      <span className="column">{data[4]}</span>
                      <span className="column">
                        <img
                          src={data[2] > 0 ? Green : data[2] < 0 ? Red : Yellow}
                          alt=""
                        />
                      </span>
                    </div>
                  );
                })
              : "없음"}
          </div>
        </div>
      </div>
    </div>
  );
};

export default MainDash;
