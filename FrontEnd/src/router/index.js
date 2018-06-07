import Vue from 'vue'
import Router from 'vue-router'
import Login from '../components/login/login.vue'
import OCRAS from '../components/ocras/OCRAS.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'OCRAS',
      component: OCRAS
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '*',
      component: OCRAS
    }
  ]
})
