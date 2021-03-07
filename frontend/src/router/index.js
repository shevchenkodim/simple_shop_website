import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('../views/Home.vue')
  },
  {
    props: true,
    path: '/:category_code',
    name: 'Category',
    component: () => import('../views/Category.vue')
  },
  {
    path: '/*',
    name: 'Page404',
    component: () => import('../views/Page404.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  routes
})

export default router
