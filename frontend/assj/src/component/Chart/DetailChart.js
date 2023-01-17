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

const Chart = ({ unit, usageStatus, domain }) => {
  return (
    <>
      <div className="unit-chart">
        <div className="unit">{unit}</div>
        <LineChart width={600} height={400} data={usageStatus}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="x" style={{ width: "100%" }} />
          <YAxis domain={domain} />
          <Tooltip />
          <Line
            type="monotone"
            dataKey="y"
            stroke="#6D8B74"
            activeDot={{ r: 8 }}
          />
          <Line type="monotone" dataKey="y1" stroke="#FB5753" />
        </LineChart>
        <div className="unit"></div>
      </div>
    </>
  );
};

export default Chart;
