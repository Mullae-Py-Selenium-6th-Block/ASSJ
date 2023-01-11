import React, { useState } from "react";
import "./Card.css";
import { motion, AnimateSharedLayout } from "framer-motion";
import { UilTimes } from "@iconscout/react-unicons";
import Chart from "react-apexcharts";
import Red from "../../img/Red.png";
import Green from "../../img/Green.png";
import Yellow from "../../img/Yellow.png";

const Card = ({ rankingData }) => {
  const color = {
    backGround: "#f2f2f2",
    boxShadow: "0px 5px 5px 0px #909090",
  };

  console.log(rankingData, color);

  const [expanded, setExpanded] = useState(false);

  return (
    <AnimateSharedLayout>
      {expanded ? (
        <ExpandedCard
          rankingData={rankingData}
          color={color}
          setExpanded={() => setExpanded(false)}
        />
      ) : (
        <CompactCard
          rankingData={rankingData}
          color={color}
          setExpanded={() => setExpanded(true)}
        />
      )}
    </AnimateSharedLayout>
  );
};

// CompactCard
function CompactCard({ rankingData, color, setExpanded }) {
  const topList = rankingData.map((data, idx) => (
    <div
      key={idx + 1}
      className="CompactCard"
      style={{
        background: color.backGround,
        boxShadow: color.boxShadow,
      }}
      onClick={setExpanded}
      layoutId="expandableCard"
    >
      <div className="detail">
        <div className="Name">
          {idx + 1}등. {data[1]}
        </div>
        <div className="Percent info">
          <div>증감율</div>
          <div>{data[2]}</div>
        </div>
        <div className="Price info">
          <div>평균매매가</div>
          <div>{data[3]}</div>
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

// ExpandedCard
function ExpandedCard({ rankingData, color, setExpanded }) {
  const data = {
    options: {
      chart: {
        type: "area",
        height: "auto",
      },

      dropShadow: {
        enabled: false,
        enabledOnSeies: undefined,
        top: 0,
        left: 0,
        blur: 3,
        color: "#000",
        opacity: 0.35,
      },
      fill: {
        colors: ["#fff"],
        type: "gradient",
      },
      dataLabels: {
        enabled: false,
      },
      stroke: {
        curve: "smooth",
        colors: ["white"],
      },
      tooltips: {
        x: {
          format: "dd/MM/YY HH:mm",
        },
      },
      grid: {
        show: true,
      },
      xaxis: {
        type: "datatime",
        categories: [
          "2022-12-01T00:00:00.000z",
          "2022-12-01T01:00:00.000z",
          "2022-12-01T02:00:00.000z",
          "2022-12-01T03:00:00.000z",
          "2022-12-01T04:00:00.000z",
          "2022-12-01T05:00:00.000z",
          "2022-12-01T06:00:00.000z",
        ],
      },
    },
  };

  return (
    <motion.div
      className="ExpandedCard"
      style={{
        background: color.backGround,
        boxShadow: color.boxShadow,
      }}
      layoutId="expandableCard"
    >
      <div>
        <UilTimes onClick={setExpanded} />
      </div>
      <span>{rankingData[1]}</span>
      <div className="chartContainer"></div>
      <span>Last 24 hours</span>
    </motion.div>
  );
}
export default Card;
