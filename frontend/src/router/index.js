import {
  createRouter,
  createWebHashHistory,
  createWebHistory,
} from "vue-router";
import Home from "../views/Home.vue";
import Login from "../views/Login.vue";
import Signup from "../views/Signup.vue";
import CitizenSignupForm from "../views/CitizenSignup.vue";
import InvestorSignupForm from "../views/InvestorSignup.vue";
import InvestorLogin from "../views/InvestorLogin.vue";
import CitizenLogin from "../views/CitizenLogin.vue";
import CitizenDashboard from "../views/CitizenDashboard.vue";
import authGuard from "../guards/AuthGuard";
import authService from "../services/AuthService";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/auth/login",
    name: "Login",
    component: Login,
  },
  {
    path: "/auth/signup",
    name: "Signup",
    component: Signup,
  },
  {
    path: "/auth/signup/citizen",
    name: "CitizenSignup",
    component: CitizenSignupForm,
  },
  {
    path: "/auth/signup/investor",
    name: "InvestorSignup",
    component: InvestorSignupForm,
  },
  {
    path: "/auth/login/citizen",
    name: "CitizenLogin",
    component: CitizenLogin,
  },
  {
    path: "/auth/login/investor",
    name: "InvestoLogin",
    component: InvestorLogin,
  },
  {
    path: "/citizen/dashboard",
    name: "CitizenDashboard",
    component: CitizenDashboard,
    beforeEnter: authGuard,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
