import { createRouter, createWebHashHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import Signup from '../views/Signup.vue'
import CitizenSignupForm from '../views/CitizenSignup.vue';
import InvestorSignupForm from '../views/InvestorSignup.vue';
import InvestorLogin from '../views/InvestorLogin.vue';
import CitizenLogin from '../views/CitizenLogin.vue';
// import CitizenDashboard from '../views/CitizenDashboard.vue';
// import CitizenDashboard from '../views/CitizenDashboard.vue';


const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/signup',
    name: 'Signup',
    component: Signup
  },
  {
    path: '/signup/citizen',
    name: 'CitizenSignup',
    component: CitizenSignupForm
  },
  {
    path: '/signup/investor',
    name: 'InvestorSignup',
    component: InvestorSignupForm
  },
  {
    path: '/login/citizen',
    name: 'CitizenLogin',
    component: CitizenLogin
  },
  {
    path: '/login/investor',
    name: 'InvestoLogin',
    component: InvestorLogin
  },
  // {
  //   path: '/dashboard/citizen',
  //   name: 'CitizenDashboard',
  //   component: CitizenDashboard
  // },

]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
