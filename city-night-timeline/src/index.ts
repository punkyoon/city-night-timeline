import Vue from "vue";
import Vuex from 'vuex'
import VueRouter from 'vue-router';
import axios from 'axios';

import App from './App.vue';

import Timeline from './components/Timeline.vue';
import Search from './components/Search.vue';
import Info from './components/Info.vue';


Vue.use(Vuex)
Vue.use(VueRouter);
Vue.config.productionTip = false;

axios.defaults.baseURL = 'http://localhost:8000';
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

const router = new VueRouter({
    mode: 'history',
    routes: [
        {path: '/', name: 'timeline', component: Timeline},
        {path: '/search', name: 'search', component: Search},
        {path: '/info', name: 'info', component: Info}
    ]
});

let v = new Vue({
    el: '#app',
    render: h => h(App),
    router: router
}); //.$mount('#app');