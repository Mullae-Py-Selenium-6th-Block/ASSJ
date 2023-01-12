import React, { useEffect, useState } from "react";
import Chart from "../Chart/DetailChart";
import "./DetailModal.css";
import { formatter } from "../../React_Data/Data";

const DetailModal = ({ open, close, detailGu, detailData }) => {
  // 예측가격:predictprice
  // 평균매매가격: price
  // 미분양: unsold
  // 전월세전환율: convertrate
  //총인구수:
  //총세대 수: totalhousenums
  //매매거래량: tradingvolume
  const [category, setCategory] = useState(-1);

  const columns = [
    "날짜",
    "가격(천원)",
    "예상 가격(천원)",
    // "총 인구수",
    "총 세대수(세대)",
    "매매거래량(호)",
    "전월세전환율(%)",
    // "미분양",
  ];
  const price = [];
  const predictprice = [];
  const totalhousenums = [];
  const tradingvolume = [];
  const convertrate = [];
  // const predictpricelist = [];
  for (let i = 0; i < detailData.length; i++) {
    price.push({ x: detailData[i].date, y: detailData[i].price });
    predictprice.push({ x: detailData[i].date, y: detailData[i].predictprice });
    totalhousenums.push({
      x: detailData[i].date,
      y: detailData[i].totalhousenums,
    });
    tradingvolume.push({
      x: detailData[i].date,
      y: detailData[i].tradingvolume,
    });
    convertrate.push({ x: detailData[i].date, y: detailData[i].convertrate });
  }
  // for (let i = 0; i < detailData.length; i++) {
  //   predictpricelist.push({
  //     date: detailData[i].date,
  //     districtname: detailData[i].districtname,
  //     predictprice: detailData[i].predictprice,
  //   });
  // }
  return (
    // 모달이 열릴때 openModal 클래스가 생성된다.
    <div className={open ? "openDetailModal modalDetail" : "modalDetail"}>
      {open ? (
        <section>
          <header>
            <span>{detailGu[1]}</span>
            <button className="close" onClick={close}>
              &times;
            </button>
          </header>
          <main>
            <div>
              <button
                className={"cateButton" + (category == 4 ? " activecate" : "")}
                onClick={() => setCategory(4)}
                key={4}
              >
                실가격
              </button>
              <button
                className={"cateButton" + (category == 0 ? " activecate" : "")}
                onClick={() => setCategory(0)}
                key={0}
              >
                예측가격
              </button>
              <button
                className={"cateButton" + (category == 1 ? " activecate" : "")}
                onClick={() => setCategory(1)}
                key={1}
              >
                거래량
              </button>
              <button
                className={"cateButton" + (category == 3 ? " active" : "")}
                onClick={() => setCategory(3)}
                key={3}
              >
                총 세대수
              </button>
              <button
                className={"cateButton" + (category == 2 ? " active" : "")}
                onClick={() => setCategory(2)}
                key={2}
              >
                전월세전환율
              </button>
            </div>

            <Chart
              tabButtonKey={category}
              className="chart"
              price={price}
              predictprice={predictprice}
              tradingvolume={tradingvolume}
              totalhousenums={totalhousenums}
              convertrate={convertrate}
            />

            <Table
              className="table"
              detailData={detailData}
              columns={columns}
            />
          </main>
          <footer>
            <button className="close" onClick={close}>
              close
            </button>
          </footer>
        </section>
      ) : null}
    </div>
  );
};

function Table({ detailData, columns }) {
  return (
    <table>
      <thead>
        <tr>
          {columns.map((column) => (
            <th key={column}>{column}</th>
          ))}
        </tr>
      </thead>
      <tbody>
        {detailData.map(
          (
            {
              date,
              price,
              predictprice,
              totalhousenums,
              tradingvolume,
              convertrate,
            },
            idx
          ) => (
            <tr key={idx}>
              <td>{date}</td>
              <td>{formatter.format(price)}</td>
              <td>{formatter.format(predictprice)}</td>
              <td>{formatter.format(totalhousenums)}</td>
              <td>{tradingvolume}</td>
              <td>{convertrate}</td>
            </tr>
          )
        )}
      </tbody>
    </table>
  );
}
export default DetailModal;
