<template>
  <div class="quiz-result-page">
    <h1>Résultat du quiz</h1>
    <div v-if="finalScore !== null">
      <p>Votre score: {{ finalScore }}</p>
      <router-link to="/" class="home-link">Retour à la page d'accueil</router-link>
    </div>
    <div v-else>
      <p>Aucun résultat disponible.</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      finalScore: null
    }
  },
  created() {
    this.finalScore = localStorage.getItem('participationScore')
    localStorage.removeItem('participationScore')
  }
}
</script>

<style scoped>
.quiz-result-page {
  text-align: center;
  padding: 20px;
}

.home-link {
  display: inline-block;
  background-color: #f5f5f5;
  padding: 10px 20px;
  text-align: center;
  text-decoration: none;
  color: black;
  border-radius: 5px;
  transition: background-color 0.3s;
}

.home-link:hover {
  background-color: #e0e0e0;
}
</style>
