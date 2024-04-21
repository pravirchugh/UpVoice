import {
  createRouter,
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
import InvestorDashboard from "../views/InvestorDashboard.vue";
import CitizenVisualization from "../views/CitizenVisualization.vue";
import InvestorVisualization from "../views/InvestorVisualization.vue";
import authGuard from "../guards/AuthGuard";
import { isUserLoggedIn } from "../utils";

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
    meta: { requiresGuest: true }
  },
  {
    path: "/auth/signup",
    name: "Signup",
    component: Signup,
    meta: { requiresGuest: true }
  },
  {
    path: "/auth/signup/citizen",
    name: "CitizenSignup",
    component: CitizenSignupForm,
    meta: { requiresGuest: true }
  },
  {
    path: "/auth/signup/investor",
    name: "InvestorSignup",
    component: InvestorSignupForm,
    meta: { requiresGuest: true }
  },
  {
    path: "/auth/login/citizen",
    name: "CitizenLogin",
    component: CitizenLogin,
    meta: { requiresGuest: true }
  },
  {
    path: "/auth/login/investor",
    name: "InvestorLogin",
    component: InvestorLogin,
    meta: { requiresGuest: true }
  },
  {
    path: "/citizen/dashboard",
    name: "CitizenDashboard",
    component: CitizenDashboard,
    beforeEnter: authGuard,
  },
  {
    path: "/investor/dashboard",
    name: "InvestorDashboard",
    component: InvestorDashboard,
    beforeEnter: authGuard,
  },
  {
    path: "/citizen/visualization",
    name: "CitizenVisualization",
    component: CitizenVisualization,
    beforeEnter: authGuard,
  },
  {
    path: "/investor/visualization",
    name: "InvestorVisualization",
    component: InvestorVisualization,
    beforeEnter: authGuard,
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresGuest) && isUserLoggedIn()) {
    next({ name: 'Home' });
  } else {
    next(); // Continue to the route
  }
});

export default router;
