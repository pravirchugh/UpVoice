import authService from "../services/AuthService";

export function isEmpty(value) {
  if (value === null || value === undefined) {
    return true;
  }
  if (typeof value === "number" || typeof value === "boolean") {
    return false;
  }
  if (typeof value === "string" || Array.isArray(value)) {
    return value.length === 0;
  }
  if (typeof value === "object") {
    return Object.keys(value).length === 0;
  }
  return false;
}

export function isUserLoggedIn() {
  let isLoggedIn = false;
  const token = authService.getToken();

  if (!isEmpty(token)) {
    isUserLoggedIn = true;
  }

  return isLoggedIn;
}
