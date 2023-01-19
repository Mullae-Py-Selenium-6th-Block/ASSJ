import SelectButton from "../component/SelectButton/SelectButton";
import MapContainer from "../component/kakaomap/mapContainer";

const Web = ({ selectedGu, setSelectedGu }) => {
  return (
    <div>
      <SelectButton selectedGu={selectedGu} setSelectedGu={setSelectedGu} />
      <div id="mapContainer">
        <MapContainer selectedGu={selectedGu} setSelectedGu={setSelectedGu} />
      </div>
    </div>
  );
};

export default Web;
