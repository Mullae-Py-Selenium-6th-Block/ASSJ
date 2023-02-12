//구별 정보 api
import axios from "axios";

export async function getGuInfo(guId) {
  const data = await axios
    .get("http://127.0.0.1:8000/assj/" + String(guId) + "/")
    .then((res) => res.data);
  return data;
}
