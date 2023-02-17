// Sidebar imports
import { UilMap, UilChart } from "@iconscout/react-unicons";

export const SidebarData = [
  {
    icon: UilMap,
    heading: "자치구 지도",
    to: "/",
  },
  {
    icon: UilChart,
    heading: "자치구 랭킹",
    to: "/rank",
  },
];
// Sidebar imports

export const color = {
  backGround: "#f2f2f2",
  boxShadow: "0px 5px 5px 0px #909090",
};

export const formatter = new Intl.NumberFormat("ko-KR");
