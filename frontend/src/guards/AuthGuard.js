import { isEmpty } from "../utils";
import authService from "../services/AuthService";
import router from "../router";



function authGuard(to, from, next) {
  const token = authService.getToken()

  if (!isEmpty(token)) {
    next();
  } else {
    localStorage.removeItem("user");
    next("/");
  }
}

export default authGuard;
