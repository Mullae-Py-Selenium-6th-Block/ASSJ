import axios from "axios";

export const isProduction = process.env.NODE_ENV === "production";

export const serverEndPoint = isProduction
  ? "http://43.201.96.246/"
  : "http://127.0.0.1:8000/";

export const frontUrl = isProduction
  ? "http://43.201.96.246/"
  : "http://localhost:3000/";

export const axiosClient = axios.create({
  baseURL: serverEndPoint,
  frontUrl: frontUrl,
  withCredentials: true,
});
