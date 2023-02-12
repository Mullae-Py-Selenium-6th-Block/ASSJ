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
import { formatter } from "../../assets/React_Data/Data";

const CustomTooltip = ({ active, payload, label }) => {
  // console.log("payload", payload); //you check payload
  if (active) {
    return (
      <div>
        <p>{payload[0].payload.date} </p>
        <p>Price : ₩{formatter.format(payload[0].payload.price * 1000)}</p>
      </div>
    );
  }
  return null;
};

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
      <Tooltip content={<CustomTooltip />} />
      <Area type="monotone" dataKey="price" stroke="#6D8B74" fill="#6D8B74" />
    </AreaChart>
  );
}
