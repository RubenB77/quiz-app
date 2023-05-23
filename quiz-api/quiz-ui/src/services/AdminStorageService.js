export default {
  clearToken() {
    window.localStorage.clear();
  },
  saveAdminToken(token) {
    window.localStorage.setItem("token", token);
    setTimeout(() => {
      this.clearToken();
    }, 60 * 60 * 1000); 
  },
  getAdminToken() {
    return window.localStorage.getItem("token");
  },
};
