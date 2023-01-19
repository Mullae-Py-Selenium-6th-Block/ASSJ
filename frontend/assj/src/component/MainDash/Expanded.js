import { motion, AnimateSharedLayout } from "framer-motion";
import { UilTimes } from "@iconscout/react-unicons";
import Chart from "react-apexcharts";

function ExpandedCard({ rankingData, color, setExpanded }) {
  return (
    <motion.div
      className="ExpandedCard"
      style={{
        background: color.backGround,
        boxShadow: color.boxShadow,
      }}
      layoutId="expandableCard"
    >
      <div>
        <UilTimes onClick={setExpanded} />
      </div>
      <span>{rankingData[1]}</span>
      <div className="chartContainer"></div>
      <span>Last 24 hours</span>
    </motion.div>
  );
}

export default ExpandedCard;
