import Vue from 'vue'
import VueRouter from 'vue-router'
import resultComponent from "@/views/resultComponent";
import searchComponent from "@/views/searchComponent";

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: searchComponent
  },
  {
    path: '/search',
    name: 'result',
    component: resultComponent
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('@/views/LoginComponent')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
