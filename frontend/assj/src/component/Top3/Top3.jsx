import React from "react";
import "./Top3.css";
import Cards from "../Cards/Cards";

const Top3 = ({ isClicked, setIsClicked }) => {
  return <Cards isClicked={isClicked} setIsClicked={setIsClicked} />;
};

export default Top3;
