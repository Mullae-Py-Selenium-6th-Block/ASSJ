import {
  LineChart,
  Line,
  CartesianGrid,
  XAxis,
  YAxis,
  Tooltip,
} from "recharts";

const Chart = (index) => {
  const data = [{ name: "Page A", uv: 400, pv: 2400, amt: 2400 }];
  return (
    <div>
      <LineChart
        width={300}
        height={100}
        // data={data[index]}
        data={data}
        margin={{ top: 5, right: 20, bottom: 5, left: 0 }}
      >
        <Line type="monotone" dataKey="uv" stroke="#8884d8" />
        <CartesianGrid stroke="#ccc" strokeDasharray="5 5" />
        <XAxis dataKey="name" />
        <YAxis />
        <Tooltip />
      </LineChart>
    </div>
  );
};

export default Chart;
