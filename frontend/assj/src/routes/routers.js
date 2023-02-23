import RankingPage from "../Pages/rankingPage";
import Main from "../Pages/main";
import { Route, Routes } from "react-router-dom";

const Routers = ({}) => {
  return (
    <Routes>
      <Route path="/*" element={<Main />}></Route>
      <Route path="/rank" element={<RankingPage />}></Route>
    </Routes>
  );
};

export default Routers;
