import React, { useState } from "react";
import Logo from "../../img/Logo.png";
import "./Sidebar.css";
import pic from "./yoon.png";
import { SidebarData } from "../../Data/Data";

const Sidebar = () => {
  const [selected, setSelected] = useState(0);

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
            <div
              className={selected === index ? "menuItem active" : "menuItem"}
              key={index}
              onClick={() => setSelected(index)}
            >
              <item.icon />
              <span>{item.heading}</span>
            </div>
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
