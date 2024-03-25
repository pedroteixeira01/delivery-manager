import { createRouter, createWebHashHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import TrucksView from '../views/TrucksView.vue';
import CargosView from '../views/CargosView.vue';

const routes = [
  {
    path: '',
    name: 'home',
    component: HomeView
  },
  {
    path: '/trucks',
    name: 'trucks',
    component: TrucksView
  },
  {
    path: '/cargos',
    name: 'cargos',
    component: CargosView
  }
];

const router = createRouter({
    history: createWebHashHistory(),
    routes
});
  
export default router;