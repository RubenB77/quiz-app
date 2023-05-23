export default {
  clearToken() {
    window.localStorage.clear();
  },
  saveAdminToken(token) {
    window.localStorage.setItem("token", token);
    // Supprimer le token après une heure
    setTimeout(() => {
      this.clearToken();
    }, 60 * 60 * 1000); // 1 heure en millisecondes
  },
  getAdminToken() {
    return window.localStorage.getItem("token");
  },
};
