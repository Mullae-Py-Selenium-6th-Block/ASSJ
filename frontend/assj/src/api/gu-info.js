//구별 정보 api
import axios from "axios";
import { serverEndPoint } from "../utils/axios";
export async function getGuInfo(guId) {
  const data = await axios
    .get(`${serverEndPoint}assj/${String(guId)}/`)
    .then((res) => res.data);
  return data;
}
