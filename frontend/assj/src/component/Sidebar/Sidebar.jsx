import React, { useState } from "react";
import Logo from "../../assets/img/Logo.png";
import "./Sidebar.css";
import pic from "./yoon.png";
import { SidebarData } from "../../assets/React_Data/Data";
import { Link } from "react-router-dom";
import { frontUrl } from "../../utils/axios";
const Sidebar = () => {
  const [sideSelected, setSideSelected] = useState(
    document.location.href === `${frontUrl}` ? 0 : 1
  );

  const sideSet = (e) => {
    if (e.target.outerText === "자치구 지도") {
      window.location.href = "/";
    } else {
      window.location.href = "/rank";
    }
  };

  return (
    <div className="Sidebar">
      <div className="logo">
        <img src={Logo} alt="" />
      </div>
      <div>알쓸신집</div>
      <div>Seoul Apartment Price Prediction Project</div>
      <hr></hr>
      {/*menu*/}
      <div className="menu">
        {SidebarData.map((item, index) => {
          return (
            <Link
              to={item.to}
              style={{ color: "inherit", textDecoration: "inherit" }}
              className={
                sideSelected === index ? "menuItem active" : "menuItem"
              }
              key={index}
              onClick={sideSet}
            >
              <item.icon />
              <span>{item.heading}</span>
            </Link>
          );
        })}
      </div>

      <div className="yoon">
        <img src={pic} alt="" />
      </div>
      <hr></hr>
      <div>문래 파이 셀레니움 6단지</div>
      <div>Mullae Py Selenium 6th Block</div>
    </div>
  );
};

export default Sidebar;
