import "./App.css";
import Sidebar from "./component/Sidebar/Sidebar";
import { BrowserRouter } from "react-router-dom";
import Routers from "./routes/routers";

function App() {
  return (
    <BrowserRouter>
      <div className="App">
        <div className="AppGlass">
          <Sidebar />
          <Routers />
        </div>
      </div>
    </BrowserRouter>
  );
}

export default App;
