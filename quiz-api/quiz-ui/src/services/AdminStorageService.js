export default {
  clearToken() {
    window.localStorage.clear();
  },
  saveAdminToken(token) {
    window.localStorage.setItem("token", token);
  },
  getAdminToken() {
    return window.localStorage.getItem("token");
  },
};
