import Switch from "../Switch/Switch";
import Red from "../../assets/img/Red.png";
import Green from "../../assets/img/Green.png";
import Yellow from "../../assets/img/Yellow.png";
import { color } from "../../assets/React_Data/Data";
import { AnimateSharedLayout } from "framer-motion";
import { formatter } from "../../assets/React_Data/Data";
import "./RankingList.css";

const RankingList = ({ isClicked, setIsClicked, rankingData, setDetail }) => {
  return (
    <AnimateSharedLayout>
      <Guitems
        rankingData={rankingData}
        color={color}
        setDetail={setDetail}
        isClicked={isClicked}
        setIsClicked={setIsClicked}
      />
    </AnimateSharedLayout>
  );
};

function Guitems({ isClicked, setIsClicked, rankingData, setDetail }) {
  const detailbox = (data) => {
    console.log(data[0], data[1]);
    setDetail((current) => {
      return [data[0], data[1]];
    });
  };
  return (
    <div className="Ranklist">
      <div className="RankingList">
        <div className="titbox">
          자치구 랭킹
          <span className="switch-name">
            {isClicked ? " (증감율 낮은 순)" : " (증감율 높은 순)"}
          </span>
          <Switch isClicked={isClicked} setIsClicked={setIsClicked} />
        </div>
        <div className="listData">
          <div className="listheader">
            <span className="column">순위</span>
            <span className="column">자치구명</span>
            <span className="column">가격 증감율(%)</span>
            <span className="column">금월 매매가(천원)</span>
            <span className="column">익월 예측가(천원)</span>
            <span className="column">통계 신호등</span>
          </div>
          {rankingData
            ? rankingData.slice(3).map(function (data, idx) {
                return (
                  <div
                    className="listheader"
                    onClick={() => {
                      detailbox(data);
                    }}
                    key={idx}
                  >
                    <span className="column">{4 + idx}</span>
                    <span className="column">{data[1]}</span>
                    <span className="column">
                      <div
                        className={"column3" + (data[2] > 0 ? " red" : " blue")}
                      >
                        {data[2] > 0 ? "+" + data[2] : data[2]}
                      </div>
                    </span>
                    <span className="column">{formatter.format(data[3])}</span>
                    <span className="column">{formatter.format(data[4])}</span>
                    <span className="column">
                      <img
                        src={data[2] > 0 ? Green : data[2] < 0 ? Red : Yellow}
                        alt=""
                      />
                    </span>
                  </div>
                );
              })
            : "없음"}
        </div>
      </div>
    </div>
  );
}
export default RankingList;
