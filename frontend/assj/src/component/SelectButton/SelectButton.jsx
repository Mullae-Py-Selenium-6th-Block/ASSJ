import "./SelectButton.css";
import React, { useState } from "react";

const SelectButton = () => {
  let data = [
    "은평구",
    "서대문구",
    "마포구",
    "종로구",
    "중구",
    "용산구",
    "강북구",
    "도봉구",
    "노원구",
    "중랑구",
    "동대문구",
    "성동구",
    "광진구",
    "성북구",
    "강서구",
    "양천구",
    "영등포구",
    "동작구",
    "구로구",
    "금천구",
    "관악구",
    "서초구",
    "강남구",
    "송파구",
    "강동구",
  ];

  let [btnActive, setBtnActive] = useState("");

  const toggleActive = (e) => {
    setBtnActive((current) => {
      return e.target.value;
    });
  };

  return (
    <div className="select-menu">
      <div id="map-logo">
        <i className="fa-solid fa-map-location-dot fa-2xl"></i>
      </div>
      <div id="set">
        <div className="select-box">
          <span className="jachigu">확인하고 싶은 자치구를 선택하세요.</span>
          <span className="ganada">(가나다 순)</span>
        </div>
        <div className="container">
          {data.map((item, idx) => {
            return (
              <button
                key={idx}
                value={idx}
                className={"btn" + (idx == btnActive ? " active" : "")}
                onClick={toggleActive}
              >
                {item}
              </button>
            );
          })}
        </div>
      </div>
    </div>
  );
};

export default SelectButton;
