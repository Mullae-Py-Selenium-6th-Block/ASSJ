import "./App.css";
import Sidebar from "./component/Sidebar/Sidebar";
import SelectButton from "./component/SelectButton/SelectButton";
import MapContainer from "./component/kakaomap/mapContainer";
import { useState } from "react";
import MainDash from "./component/MainDash/MainDash";

function App() {
  const [selectedGu, setSelectedGu] = useState(-1);
 return (
  <div className="App">
   <div className="AppGlass">
    <Sidebar />
        <div>
          <SelectButton selectedGu={selectedGu} setSelectedGu={setSelectedGu} />

          <div id="mapContainer">
            <MapContainer />
          </div>
        </div>
    <MainDash />
   </div>
  </div>
 );
}

export default App;
