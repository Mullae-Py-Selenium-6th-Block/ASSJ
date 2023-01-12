import "./DetailChart.css";

import React, { useEffect, useState } from "react";
import { Line, LineChart, XAxis, YAxis } from "recharts";

const Chart = ({
  tabButtonKey,
  price,
  predictprice,
  tradingvolume,
  totalhousenums,
  convertrate,
}) => {
  var dataTemp = price;
  var dataDomain = [];
  var dataUnit = "";
  var datainfo = "";
  const [usageStatus, setUsageStatus] = useState([]);
  const [domain, setDomain] = useState([]);
  const [unit, setUnit] = useState("");
  const [infoText, setInfoText] = useState("");

  useEffect(() => {
    if (tabButtonKey == 0) {
      dataTemp = predictprice;
      dataDomain = ["dataMin", "dataMax"];
      dataUnit = "단위: (천원)";
      datainfo =
        "한 달간 해당 자치구에 올라온 아파트 매물의 매매 가격을 모두 더한 뒤에 전체 매물의 수로 나눈 값";
    } else if (tabButtonKey === 1) {
      dataTemp = tradingvolume;
      dataDomain = ["dataMin", "dataMax"];
      dataUnit = "단위: (호)";
      datainfo = "한 달간 해당 자치구에서 거래된 아파트 매물의 수";
    } else if (tabButtonKey === 2) {
      dataTemp = convertrate;
      dataDomain = ["dataMin", "dataMax"];
      dataUnit = "단위: (%)";
      datainfo =
        "한 달간 평균적으로 해당 권역에서 전세 보증금을 월세로 전환했을 때 적용하는 비율";
    } else if (tabButtonKey === 3) {
      dataTemp = totalhousenums;
      dataDomain = ["dataMin", "dataMax"];
      dataUnit = "단위: (세대)";
      datainfo = "자치구별 세대 수";
    } else {
      dataTemp = price;
      dataDomain = ["dataMin", "dataMax"];
      dataUnit = "단위: (천원)";
      datainfo = "해당 자치구의 예측 평균 가격";
    }

    setUsageStatus(dataTemp);
    setDomain(dataDomain);
    setUnit(dataUnit);
    setInfoText(datainfo);
  }, [tabButtonKey]);

  return (
    <>
      <div className="info-text">{infoText}</div>
      <div className="unit-chart">
        <div className="unit">{unit}</div>
        <LineChart width={600} height={400} data={usageStatus}>
          <XAxis dataKey="x" style={{ width: "100%" }} />
          <YAxis domain={domain} />
          {/* <CartesianGrid stroke="#eee" strokeDasharray="5 5" /> */}
          <Line type="monotone" dataKey="y" stroke="#6D8B74" />
        </LineChart>
        <div className="unit"></div>
      </div>
    </>
  );
};

export default Chart;
