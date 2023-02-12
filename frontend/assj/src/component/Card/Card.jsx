import React from "react";
import "./Card.css";
import { AnimateSharedLayout } from "framer-motion";
import Red from "../../assets/img/Red.png";
import Green from "../../assets/img/Green.png";
import Yellow from "../../assets/img/Yellow.png";
import first from "../../assets/img/first.png";
import second from "../../assets/img/second.png";
import third from "../../assets/img/third.png";

import { color } from "../../assets/React_Data/Data";
import { formatter } from "../../assets/React_Data/Data";

const Card = ({ rankingData, setDetail }) => {
  return (
    <AnimateSharedLayout>
      <CompactCard
        rankingData={rankingData}
        setDetail={setDetail}
        color={color}
      />
    </AnimateSharedLayout>
  );
};

// CompactCard
function CompactCard({ rankingData, color, setDetail }) {
  const detailbox = (data) => {
    console.log(data[0], data[1]);
    setDetail((current) => {
      return [data[0], data[1]];
    });
  };
  const topList = rankingData.map((data, idx) => (
    <div
      key={idx + 1}
      className="CompactCard"
      style={{
        background: color.backGround,
        boxShadow: color.boxShadow,
      }}
    >
      <div
        className="detail"
        onClick={() => {
          detailbox(data);
        }}
      >
        <div className="Name">
          <img
            className="rank-img"
            src={idx === 0 ? first : idx === 1 ? second : third}
          />
          {data[1]}
        </div>
        <div className="Percent info">
          <div>증감율</div>
          <div>{data[2]}</div>
        </div>
        <div className="Price info">
          <div>평균매매가</div>
          <div>{formatter.format(data[3])}</div>
        </div>
        <div className="Signal info">
          <div>통계신호등</div>
          <div>
            <img
              src={data[2] > 0 ? Green : data[2] < 0 ? Red : Yellow}
              alt=""
            />
          </div>
        </div>
      </div>
    </div>
  ));
  return <div className="top-container">{topList}</div>;
}
export default Card;
