import DetailModal from "../component/DetailModal/DetailModal";
import React from "react";
import "./rankingPage.css";
import Card from "../component/Card/Card";
import RankingList from "../component/RankingList/RankingList";
import { rankingDetailInfo, rankingInfo } from "../api/ranking";
import { getEconomicInfo } from "../api/economic";
import { useEffect, useState } from "react";

import { axiosClient } from "../utils/axios";
const RankingPage = ({}) => {
  const [isClicked, setIsClicked] = useState(false); //2번 페이지 랭킹 정렬 스위치 버튼
  const [rankingData, setRankingData] = useState([]); //2번 페이지 랭킹 데이터

  const [detailGu, setDetailGu] = useState([-1, ""]); //2번 페이지 클릭된 구
  const [detailData, setDetail] = useState([]); //2번 페이지 클릭된 구 데이터
  const [detailDataList, setDetailList] = useState([]); //2번 페이지 클릭된 구 데이터

  const [DetailOpen, setDetailiOpenState] = useState(false); //1번페이지 모달 창 state
  const [economics, setEconomics] = useState([]);

  const openDetail = () => {
    setDetailiOpenState(true);
  };
  const closeDetail = () => {
    setDetailiOpenState(false);
  };
  useEffect(() => {
    var link = document.location.href;
    if (link === `${axiosClient.frontUrl}`) {
    } else {
      getEconomicInfo().then((result) => setEconomics(result));
      console.log(economics);
    }
  }, [document.location.href]);

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
