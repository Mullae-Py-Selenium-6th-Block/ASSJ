import "./chart.css";
import React from "react";
import {
  AreaChart,
  Area,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
} from "recharts";

export default function Chart({ graphData }) {
  return (
    <AreaChart
      width={700}
      height={400}
      viewBox={"0 -10 600 400"}
      data={graphData}
    >
      <CartesianGrid strokeDasharray="5 5" />
      <XAxis dataKey="date" />
      <YAxis />
      <Tooltip />
      <Area
        type="monotone"
        dataKey="price"
        stroke="#6D8B74"
        fill="#6D8B74"
      />
    </AreaChart>
  );
}
