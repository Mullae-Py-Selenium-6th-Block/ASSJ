import React from "react";
import "./Switch.css";

const Switch = ({ isClicked, setIsClicked }) => {
  return (
    <>
      <input
        className="react-switch-checkbox"
        id={`react-switch-new`}
        type="checkbox"
      />
      <label
        className="react-switch-label"
        htmlFor={`react-switch-new`}
        onClick={() => setIsClicked(!isClicked)}
      >
        <span className={`react-switch-button`} />
      </label>
    </>
  );
};

export default Switch;
