import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";

import HighchartsVue from "highcharts-vue";

app = createApp(App);

app.use(store);
app.use(router);
app.use(HighchartsVue);

app.mount("#app");
