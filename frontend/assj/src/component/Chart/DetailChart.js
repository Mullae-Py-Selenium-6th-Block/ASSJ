import "./DetailChart.css";

import React from "react";

import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
} from "recharts";
import { formatter } from "../../assets/React_Data/Data";

const Chart = ({ unit, usageStatus, domain, category }) => {
  var name = "";
  var value = -1;
  const CustomTooltip = ({ active, payload, label }) => {
    // console.log("payload", payload); //you check payload
    if (active && payload) {
      if (category === 0) {
        name = "가격";
        value = "₩" + formatter.format(payload[0].payload.y * 1000);
      } else if (category === 1) {
        name = "거래량";
        value = payload[0].payload.y;
      } else if (category === 2) {
        name = "전월세 전환율";
        value = payload[0].payload.y;
      } else if (category === 3) {
        name = "총 세대 수";
        value = formatter.format(payload[0].payload.y);
      }
      return (
        <div className="tool-box">
          <p>날짜: {payload[0].payload.x} </p>
          <p>
            {name} : {value}
            {payload[0].payload.x !== "2022-12-01" ? (
              ""
            ) : (
              <p>예측가: {formatter.format(payload[0].payload.y1 * 1000)}</p>
            )}
          </p>
        </div>
      );
    } else {
      return null;
    }
  };
  return (
    <>
      <div className="unit-chart">
        <LineChart width={400} height={350} data={usageStatus}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="x" style={{ width: "100%" }} />
          <YAxis domain={domain} />
          <Tooltip content={<CustomTooltip />} />
          <Line
            type="monotone"
            dataKey="y"
            stroke="#6D8B74"
            activeDot={{ r: 8 }}
          />
          <Line type="monotone" dataKey="y1" stroke="#FB5753" />
        </LineChart>
        <div className="unit">{unit}</div>
      </div>
    </>
  );
};

export default Chart;
