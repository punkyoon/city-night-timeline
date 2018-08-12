import Vue from "vue";
import VueRouter from 'vue-router';

import App from './App.vue';

import { router_config } from './router/router';


Vue.use(VueRouter);
Vue.config.productionTip = false

const router = new VueRouter({
    mode: 'history',
    routes: router_config
});

let v = new Vue({
    el: '#app',
    render: h => h(App),
    router: router
}); //.$mount('#app');