import React from "react";
import Chart from "./chart";
import "./modal.css";

const Modal = (props) => {
  const { open, close, index, name } = props;
  console.log("modal");
  console.log(props);
  return (
    // 모달이 열릴때 openModal 클래스가 생성된다.
    <div className={open ? "openModal modal" : "modal"}>
      {open ? (
        <section>
          <header>
            {name}
            <button className="close" onClick={close}>
              &times;
            </button>
          </header>
          <main>
            <Chart index={index} />
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
