import axios from "axios";
import { serverEndPoint } from "../utils/axios";
export async function rankingInfo(num) {
  console.log(num);
  const data = await axios
    .get(`${serverEndPoint}assj/ranking/order/${num}/`)
    .then((res) => res.data.data);
  return data;
}

export async function rankingDetailInfo(num) {
  const response = await axios
    .get(`${serverEndPoint}assj/ranking/${String(num)}/?format=json`)
    .then((res) => res.data);

  const price = [];
  const totalhousenums = [];
  const tradingvolume = [];
  const convertrate = [];
  const responsedata = response;
  for (let i = 0; i < responsedata.length; i++) {
    price.push({
      x: responsedata[i].date,
      y: responsedata[i].price,
      y1: responsedata[i].price,
    });
    if (responsedata[i].totalhousenums !== null) {
      totalhousenums.push({
        x: responsedata[i].date,
        y: responsedata[i].totalhousenums,
      });
    }
    if (responsedata[i].tradingvolume !== null) {
      tradingvolume.push({
        x: responsedata[i].date,
        y: responsedata[i].tradingvolume,
      });
    }
    if (responsedata[i].tradingvolume !== null) {
      convertrate.push({
        x: responsedata[i].date,
        y: responsedata[i].convertrate,
      });
    }
  }

  price[price.length - 1].y1 = responsedata[responsedata.length - 2].nextprice;
  return [price, totalhousenums, tradingvolume, convertrate, responsedata];
}
