import React, { useEffect, useState } from "react";
import Chart from "../Chart/DetailChart";
import "./DetailModal.css";
import { formatter } from "../../assets/React_Data/Data";

const DetailModal = ({ open, close, detailGu, detailData, detailDataList }) => {
  // 예측가격:predictprice
  // 평균매매가격: price
  // 미분양: unsold
  // 전월세전환율: convertrate
  //총인구수:
  //총세대 수: totalhousenums
  //매매거래량: tradingvolume
  const [category, setCategory] = useState(-1);
  const price = detailDataList[0];
  const totalhousenums = detailDataList[1];
  const tradingvolume = detailDataList[2];
  const convertrate = detailDataList[3];

  var dataTemp = price;
  var dataDomain = [];
  var dataUnit = "";
  var datainfo = "";
  var tableD = [];
  const [usageStatus, setUsageStatus] = useState([]);
  const [domain, setDomain] = useState([]);
  const [unit, setUnit] = useState("");
  const [infoText, setInfoText] = useState("");
  const [columns, setColumns] = useState([]);
  const [tableData, setTableData] = useState();

  useEffect(() => {
    if (category === 1) {
      dataTemp = tradingvolume;
      dataDomain = ["dataMin", "dataMax"];
      dataUnit = "단위: (호)";
      datainfo = "한 달간 해당 자치구에서 거래된 아파트 매물의 수";
      setColumns(["날짜", "매매거래량(호)"]);
      tableD = detailData.map((detail) => {
        return [detail.date, detail.tradingvolume];
      });
    } else if (category === 2) {
      dataTemp = convertrate;
      dataDomain = ["dataMin", "dataMax"];
      dataUnit = "단위: (%)";
      datainfo =
        "한 달간 평균적으로 해당 권역에서 전세 보증금을 월세로 전환했을 때 적용하는 비율";
      setColumns(["날짜", "전월세전환율(%)"]);
      tableD = detailData?.map((detail) => {
        return [detail.date, detail.convertrate];
      });
    } else if (category === 3) {
      dataTemp = totalhousenums;
      dataDomain = ["dataMin", "dataMax"];
      dataUnit = "단위: (세대)";
      datainfo = "자치구별 세대 수";
      setColumns(["날짜", "총 세대수(세대)"]);
      tableD = detailData.map((detail) => {
        return [detail.date, detail.totalhousenums];
      });
    } else if (category === -1) {
      datainfo = "확인하고 싶은 자료의 버튼을 클릭해주세요.";
    } else {
      dataTemp = price;
      dataDomain = [619500, 2312300];
      dataUnit = "단위: (천원)";
      datainfo =
        "한 달간 해당 자치구에 올라온 아파트 매물의 매매 가격을 모두 더한 뒤에 전체 매물의 수로 나눈 값";
      setColumns(["날짜", "평균 매매가"]);
      tableD = detailData.map((detail) => {
        return [detail.date, detail.price];
      });
    }
    setUsageStatus(dataTemp);
    setDomain(dataDomain);
    setUnit(dataUnit);
    setInfoText(datainfo);
    setTableData(tableD);
  }, [category]);

  return (
    // 모달이 열릴때 openModal 클래스가 생성된다.
    <div className={open ? "openDetailModal modalDetail" : "modalDetail"}>
      {open ? (
        <section>
          <header>
            <span>{detailGu[1]}</span>
            <button
              className="close"
              onClick={() => {
                close();
                setCategory(-1);
              }}
            >
              &times;
            </button>
          </header>
          <main>
            <div>
              <button
                className={
                  "cateButton" +
                  (category === 0
                    ? " activecate"
                    : category === -1
                    ? " init"
                    : "")
                }
                onClick={() => setCategory(0)}
                key={0}
              >
                예측가격
              </button>
              <button
                className={
                  "cateButton" +
                  (category === 1
                    ? " activecate"
                    : category === -1
                    ? " init"
                    : "")
                }
                onClick={() => setCategory(1)}
                key={1}
              >
                거래량
              </button>
              <button
                className={
                  "cateButton" +
                  (category === 3
                    ? " activecate"
                    : category === -1
                    ? " init"
                    : "")
                }
                onClick={() => setCategory(3)}
                key={3}
              >
                총 세대수
              </button>
              <button
                className={
                  "cateButton" +
                  (category === 2
                    ? " activecate"
                    : category === -1
                    ? " init"
                    : "")
                }
                onClick={() => setCategory(2)}
                key={2}
              >
                전월세전환율
              </button>
            </div>
            <div>
              {category === -1 ? (
                <div className="initial-button">
                  <div className="init-info">{infoText}</div>
                </div>
              ) : (
                <div className="info-box">
                  <div className="info-text">{infoText}</div>
                  <div className="month">최근 11개월</div>
                  <div className="table-chart">
                    <Table
                      className="table"
                      columns={columns}
                      tableData={tableData}
                      infoText={infoText}
                    />
                    <Chart
                      category={category}
                      className="chart"
                      unit={unit}
                      domain={domain}
                      usageStatus={usageStatus}
                    />
                  </div>
                </div>
              )}
            </div>
          </main>
          <footer>
            <button
              className="close"
              onClick={() => {
                close();
                setCategory(-1);
              }}
            >
              close
            </button>
          </footer>
        </section>
      ) : null}
    </div>
  );
};

function Table({ columns, tableData, infoText }) {
  // const reverse = [...tableData].reverse();
  return (
    <>
      <table className="table-container">
        <colgroup>
          <col width="100px" />
        </colgroup>
        <thead>
          <tr>
            {columns.map((column, idx) => (
              <th key={column}>{column}</th>
            ))}
          </tr>
        </thead>
        <tbody>
          {tableData.map((elem, idx) => {
            return (
              <tr key={idx}>
                {elem.map((item, idx) => {
                  if (idx === 0) {
                    return <td>{item}</td>;
                  } else {
                    return <td>{formatter.format(item)}</td>;
                  }
                })}
              </tr>
            );
          })}
        </tbody>
      </table>
    </>
  );
}
export default DetailModal;
