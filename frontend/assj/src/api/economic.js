//경제 지표 api
import axios from "axios";
import { serverEndPoint } from "../utils/axios";
export async function getEconomicInfo() {
  const response = await axios
    .get(`${serverEndPoint}assj/economics/`)
    .then((res) => res.data.data[0]);

  return response;
}
