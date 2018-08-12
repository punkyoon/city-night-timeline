import Timeline from '../components/Timeline.vue';
import Search from '../components/Search.vue';
import Info from '../components/Info.vue';


export const router_config = [
    {path: '/', component: Timeline},
    {path: '/search', component: Search},
    {path: '/info', component: Info}
];