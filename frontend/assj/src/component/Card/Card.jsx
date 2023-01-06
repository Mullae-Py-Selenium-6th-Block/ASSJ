import React, { useState } from "react";
import "./Card.css";
import { motion, AnimateSharedLayout } from "framer-motion";
import { UilTimes } from "@iconscout/react-unicons";
import Chart from "react-apexcharts";

const Card = (props) => {
 const [expanded, setExpanded] = useState(false);

 return (
  <AnimateSharedLayout>
   {expanded ? (
    <ExpandedCard param={props} setExpanded={() => setExpanded(false)} />
   ) : (
    <CompactCard param={props} setExpanded={() => setExpanded(true)} />
   )}
  </AnimateSharedLayout>
 );
};

// CompactCard
function CompactCard({ param, setExpanded }) {
 return (
  <motion.div
   className="CompactCard"
   style={{
    background: param.color.backGround,
    boxShadow: param.color.boxShadow,
   }}
   onClick={setExpanded}
   layoutId="expandableCard"
  >
   <div className="detail">
    <div className="Name">{param.title}</div>
    <div className="Percent">
     <div>증감율</div>
     <div>10.4%</div>
    </div>
    <div className="Price">
     <div>평균매매가</div>
     <div>100,000</div>
    </div>
    <div className="Signal">
     <div>통계신호등</div>
     <div>
      <img src="" />
     </div>
    </div>
   </div>
  </motion.div>
 );
}

// ExpandedCard
function ExpandedCard({ param, setExpanded }) {
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
    background: param.color.backGround,
    boxShadow: param.color.boxShadow,
   }}
   layoutId="expandableCard"
  >
   <div>
    <UilTimes onClick={setExpanded} />
   </div>
   <span>{param.title}</span>
   <div className="chartContainer">
    <Chart series={param.series} type="area" options={data.option} />
   </div>
   <span>Last 24 hours</span>
  </motion.div>
 );
}
export default Card;
