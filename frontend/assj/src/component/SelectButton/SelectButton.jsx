import "./SelectButton.css";
import React from "react";

const SelectButton = ({ selectedGu, setSelectedGu }) => {
  let data = [
    "강남구",
    "강동구",
    "강북구",
    "강서구",
    "관악구",
    "광진구",
    "구로구",
    "금천구",
    "노원구",
    "도봉구",
    "동대문구",
    "동작구",
    "마포구",
    "서대문구",
    "서초구",
    "성동구",
    "성북구",
    "송파구",
    "양천구",
    "영등포구",
    "용산구",
    "은평구",
    "종로구",
    "중구",
    "중랑구",
  ];

  const toggleActive = (e) => {
    setSelectedGu((current) => {
      return [e.target.value, e.target.innerText];
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
                className={
                  "btn" + (idx === selectedGu[0] ? " buttonactive" : "")
                }
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
