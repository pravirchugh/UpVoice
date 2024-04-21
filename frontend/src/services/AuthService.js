import ApiService from "./ApiService";

const ENDPOINTS = {
  LOGIN_USER: "auth/login-user",
  LOGIN_STAKEHOLDER: "auth/login-stakeholder",
  SIGN_UP_USER: "auth/add-user",
  SIGN_UP_STAKEHOLDER: "/auth/add-stakeholder",
  LOGOUT_USER: "/auth/logout-user",
  LOGOUT_STAKEHOLDER: "/auth/logout-stakeholder",
};

class AuthService extends ApiService {
  constructor() {
    super();
    this.init();
  }

  init = async () => {
    const token = this.getToken();
    const user = this.getUser();

    if (token && user) {
      await this.setAuthorizationHeader();
      this.api.setUnauthorizedCallback(this.destroySession.bind(this));
    }
  };

  setAuthorizationHeader = () => {
    const token = this.getToken();
    if (token) {
      this.api.attachHeaders({
        Authorization: `Bearer ${token}`,
      });
    }
  };

  createSession = (user) => {
    localStorage.setItem("user", JSON.stringify(user));
    this.setAuthorizationHeader();
  };

  destroySession = () => {
    localStorage.clear();
    this.api.removeHeaders(["Authorization"]);
  };

  loginUser = async (loginData) => {
    const { data } = await this.apiClient.post(ENDPOINTS.LOGIN_USER, loginData);
    this.createSession(data);
    return loginData;
  };

  loginStakeholder = async (loginData) => {
    const { data } = await this.apiClient.post(
      ENDPOINTS.LOGIN_STAKEHOLDER,
      loginData
    );
    this.createSession(data);
    return loginData;
  };

  logoutUser = async () => {
    const { data } = await this.apiClient.post(ENDPOINTS.LOGOUT_USER);
    this.destroySession();
    return {
      ok: true,
      data,
    };
  };

  logoutStakeholder = async () => {
    const { data } = await this.apiClient.post(ENDPOINTS.LOGOUT_STAKEHOLDER);
    this.destroySession();
    return {
      ok: true,
      data,
    };
  };

  signupUser = async (signupData) => {
    await this.apiClient.post(ENDPOINTS.SIGN_UP_USER, signupData);
    const { username, password } = signupData;
    return this.login({
      username,
      password,
    });
  };

  signupStakeholder = async (signupData) => {
    await this.apiClient.post(ENDPOINTS.SIGN_UP_USER, signupData);
    const { username, email, password } = signupData;
    return this.login({
      username,
      email,
      password,
    });
  };

  getToken = () => {
    let user = localStorage.getItem("user");
    user = user ? JSON.parse(user)?.access_token : undefined;
    return user;
  };

  getUser = () => {
    const user = localStorage.getItem("user");
    return JSON.parse(user);
  };

  updateUserInStorage = (property) => {
    const user = localStorage.getItem("user");
    let jsonUser = JSON.parse(user);
    jsonUser = {
      ...jsonUser,
      ...property,
    };
    localStorage.setItem("user", JSON.stringify(jsonUser));
  };
}

const authService = new AuthService();

export default authService;
