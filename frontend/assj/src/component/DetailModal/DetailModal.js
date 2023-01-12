import React from "react";
// import Chart from "./chart";
// import "./DetailModal.css";

const DetailModal = ({ open, close, detailGu, detailData }) => {
  return (
    // 모달이 열릴때 openModal 클래스가 생성된다.
    <div className={open ? "openModal modal" : "modal"}>
      {open ? (
        <section>
          <header>
            <span>{detailGu[1]}</span>
            <button className="close" onClick={close}>
              &times;
            </button>
          </header>
          <main>{/* <Chart detailData={detailData} /> */}</main>
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

export default DetailModal;
