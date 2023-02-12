import SelectButton from "../component/SelectButton/SelectButton";
import MapContainer from "../component/kakaomap/mapContainer";
import Modal from "../component/kakaomap/modal";
import "./main.css";
const Main = ({
  modalOpen,
  closeModal,
  selectedGu,
  setSelectedGu,
  graphData,
}) => {
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
