<template>
  <div class="admin-page">
    <h1>Admin Page</h1>
    <div class="button-container">
      <router-link to="/question-organizer" class="manage-questions-link">Gestion des questions</router-link>
      <div class="button-space"></div>
      <button @click="deleteParticipations">Supprimer les participations</button>
    </div>
    <button @click="logout" class="logout-button">Déconnexion</button>
  </div>
</template>

<script>
import AdminStorageService from "@/services/AdminStorageService";
import QuizApiService from "@/services/QuizApiService";

export default {
  methods: {
    logout() {
      AdminStorageService.clearToken(); // Supprime le token d'authentification
      this.$router.push("/"); // Redirige l'utilisateur vers la page d'accueil
    },
    deleteParticipations() {
      QuizApiService.DeleteParticipations(AdminStorageService.getAdminToken());
      console.log("Suppression des participations effectuée !");
    },
  },
};
</script>

<style scoped>
.admin-page {
  text-align: center;
  padding: 20px;
}

.button-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 20px;
}

.button-space {
  height: 10px;
}

button {
  padding: 10px 20px;
  background-color: #f5f5f5;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  margin: 0 auto;
  margin-top: 20px;
}

button:hover {
  background-color: #e0e0e0;
}

.logout-button {
  padding: 10px 20px;
  background-color: red;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  color: white;
  margin-top: 20px;
  margin: 0 auto;
}

.logout-button:hover {
  background-color: #c50000;
}

.manage-questions-link {
  display: inline-block;
  background-color: #f5f5f5;
  padding: 10px 20px;
  text-align: center;
  text-decoration: none;
  color: black;
  border-radius: 5px;
  transition: background-color 0.3s;
  margin-top: 10px;
}

.manage-questions-link:hover {
  background-color: #e0e0e0;
}
</style>
