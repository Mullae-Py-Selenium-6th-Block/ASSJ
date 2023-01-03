import "./App.css";
import Sidebar from "./component/Sidebar/Sidebar";
import SelectButton from "./component/SelectButton/SelectButton";

function App() {
  return (
    <div className="App">
      <div className="AppGlass">
        <Sidebar />
        <div style={{ display: "flex" }}>
          <SelectButton />
        </div>
      </div>
    </div>
  );
}

export default App;
