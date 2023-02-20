import SelectButton from "../component/SelectButton/SelectButton";
import MapContainer from "../component/kakaomap/mapContainer";
import Modal from "../component/kakaomap/modal";
import "./main.css";
import { getGuInfo } from "../api/gu-info";

import { useState, useEffect } from "react";
const Main = () => {
  const [graphData, setGraphData] = useState({}); //1번 페이지 구 데이터
  const [selectedGu, setSelectedGu] = useState([-1, ""]); //1번 페이지 구 선택
  const [modalOpen, setState] = useState(false); //1번페이지 모달 창 state

  const openModal = () => {
    setState(true);
  };
  const closeModal = () => {
    setState(false);
  };

  useEffect(() => {
    if (selectedGu[0] === -1) {
      return;
    }
    getGuInfo(selectedGu[0]).then((result) => setGraphData(result));
    openModal();
  }, [selectedGu]);

  return (
    <>
      <div>
        <SelectButton selectedGu={selectedGu} setSelectedGu={setSelectedGu} />
        <div id="mapContainer">
          <MapContainer selectedGu={selectedGu} setSelectedGu={setSelectedGu} />
        </div>
      </div>
      <Modal
        open={modalOpen}
        close={closeModal}
        selectedGu={selectedGu}
        setSelectedGu={setSelectedGu}
        graphData={graphData}
      />
    </>
  );
};

export default Main;
