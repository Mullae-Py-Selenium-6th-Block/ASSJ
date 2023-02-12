//경제 지표 api
import axios from "axios";

export async function getEconomicInfo() {
  const response = await axios
    .get("http://127.0.0.1:8000/assj/economics/")
    .then((res) => res.data.data[0]);

  return response;
}
