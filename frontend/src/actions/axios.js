import axios from "axios";

const instance = axios.create({
  baseURL: "https://django-backend-3oer.onrender.com",
});

export default instance;
