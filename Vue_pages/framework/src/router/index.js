import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/profile',
    name: 'profile',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "profile" */ '../views/ProfileView.vue'),
    children:[
      {
        path:'posts',
        name:'posts',
        component: () => import(/* webpackChunkName: "posts" */ '../components/profileComponents/MyPost.vue')
      },
      {
        path:'favourite',
        name:'favourite',
        component: () => import(/* webpackChunkName: "favourite" */ '../components/profileComponents/MyFavourite.vue')
      }
    ]
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
