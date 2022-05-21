import { createRouter, createWebHashHistory } from 'vue-router'
import store from '@/store/index.js'
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
    // redirect: to =>{
    //   return to.path + '/posts'
    // },
    children:[
      {
        path:'/profile/posts',
        name:'posts',
        component: () => import(/* webpackChunkName: "posts" */ '../components/profileComponents/MyPost.vue')
      },
      {
        path:'/profile/favourite',
        name:'favourite',
        component: () => import(/* webpackChunkName: "favourite" */ '../components/profileComponents/MyFavourite.vue')
      }
    ]
  },
  {
    path: '/forum',
    name: 'forum',
    component: () => import(/* webpackChunkName: "forum" */ '../views/ForumView.vue')
  },
  {
    path: '/create_post',
    name: 'createPost',
    component: () => import(/* webpackChunkName: "forum" */ '../views/CreatePostView.vue')
  },
  {
    path: '/course_schedule',
    name: 'courseSchedule',
    component: () => import(/* webpackChunkName: "forum" */ '../views/CourseScheduleView')
  },
  {
    path: "/sector",
    name: "sector",
    component: () => import(/* webpackChunkName: "sector" */ '../components/forumComponents/InSection.vue'),
    // redirect: to =>{
    //   return to.path + '/new'
    // },
    children: [
      {
        path:"/sector/new",
        name:"new",
        component: () => import(/* webpackChunkName: "new" */ '../components/forumComponents/NewPosts')
      },
      {
        path: "/sector/hot",
        name: "hot",
        component: () => import(/* webpackChunkName: "sector" */ '../components/forumComponents/HotPosts')
      }
    ]
  },
  {
    path: "/post",
    name: "post",
    component: () => import(/* webpackChunkName: "post" */ '../components/postComponents/InPost.vue')
  },
  {
    path: "/Classroom",
    name: "classroom",
    component: () => import(/* webpackChunkName: "classroom" */ '../views/ClassroomView.vue')
  },

  {
    path: "/control",
    name: "controlNavigator",
    component: () => import(/* webpackCHunkName: "control" */ '../components/controlComponents/controlNavigator.vue'),
    children: [
      {
        path: "/control/controlBoard",
        name: "controlBoard",
        component: () => import(/* webpackChunkName: "control" */ '../views/controlBoardView.vue')
      },
      {
        path: "/control/controlData",
        name: "controlData",
        component: () => import(/* webpackChunkName: "control" */ '../views/controlDataView.vue')
      }
    ]
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

router.afterEach((to, from) => {
  if (to.path === "/"){
    store.commit("changeMainFunctionsVisible");
  }else {
    store.commit("changeMainFunctionsInvisible")
  }

  from.path;
})



export default router
