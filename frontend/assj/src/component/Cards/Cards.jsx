import React from "react";
import "./Cards.css";
import { CardsData } from "../../React_Data/Data";
import Card from "../Card/Card";
import image from "../../img/Background.png";

const Cards = () => {
 return (
  <div
   style={{
    backgroundImage: `url(${image})`,
    backgroundPosition: "bottom",
    backgroundRepeat: "no-repeat",
    backgroundSize: "contain",
   }}
   className="Cards"
  >
   {CardsData.map((card, id) => {
    return (
     <div className="parentContainer">
      <Card title={card.title} color={card.color} series={card.series} />
     </div>
    );
   })}
  </div>
 );
};

export default Cards;
