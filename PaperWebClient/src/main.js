import { createApp } from "vue";
import 'element-plus/theme-chalk/index.css'
import ElementPlus from 'element-plus'
import App from "./App.vue";
import axios from "axios";
import store from "@/store";
import router from "./router";

// Nucleo Icons
import "./assets/css/nucleo-icons.css";
import "./assets/css/nucleo-svg.css";

import materialKit from "./material-kit";

const app = createApp(App);

axios.defaults.baseURL = "http://localhost:8000/api/";
app.config.globalProperties.$http = axios;
app.use(store);
app.use(router);
app.use(materialKit);
app.use(ElementPlus);
app.mount("#app");
