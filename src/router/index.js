import Vue from 'vue'
import VueRouter from 'vue-router'
import resultComponent from "@/views/resultComponent";
import searchComponent from "@/views/searchComponent";
import Home from "@/views/Home";

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
    path: '/home',
    name: 'map',
    component: Home
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('@/views/LoginComponent')
  },
  {
    path: '/register',
    name: 'register',
    component: () => import('@/views/RegisterComponent')
  },
  {
    name: 'profile',
    path: '/profile',
    component: () => import('@/views/SearchRecordsComponent')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
