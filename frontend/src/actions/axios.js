import axios from "axios";

const instance = axios.create({
  baseURL: "https://animestore-7b7f.onrender.com",
});

export default instance;
