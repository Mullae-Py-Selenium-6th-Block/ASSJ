import React from "react";
import Chart from "./chart";
import "./modal.css";

const Modal = ({ open, close, selectedGu, setSelectedGu, graphData, set }) => {

  return (
    // 모달이 열릴때 openModal 클래스가 생성된다.
    <div className={open ? "openModal modal" : "modal"}>
      {open ? (
        <section>
          <header>
            <span>{selectedGu[1]}</span>
            <button className="close" onClick={close}>
              &times;
            </button>
          </header>
          <main>
            <Chart graphData={graphData} />
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

export default Modal;
