<template>
  <div class="home-page">
    <h1 class="page-title">Bienvenue sur Quizzo</h1>
    <div class="score-container">
      <h2 class="score-heading">Meilleurs scores :</h2>
      <ul class="score-list">
        <li v-for="score in registeredScores" :key="score.id" class="score-item">
          <span class="player-name">{{ score.playerName }} -</span> <span class="player-score">{{ score.score }}</span>
        </li>
      </ul>
    </div>
    <router-link to="/start-new-quiz-page" class="start-quiz-link">Démarrer le quiz !</router-link>
  </div>
</template>

<script>
import quizApiService from "@/services/QuizApiService";

export default {
  name: "HomePage",
  data() {
    return {
      registeredScores: []
    };
  },
  async created() {
    console.log("Composant Home page 'created'");
    try {
      const response = await quizApiService.getScores();
      this.registeredScores = response.data;
    } catch (error) {
      console.error("Erreur lors de la récupération des scores:", error);
    }
  }
}
</script>

<style>
.home-page {
  text-align: center;
  padding: 20px;
}

.page-title {
  color: blue;
  font-size: 24px;
  margin-bottom: 20px;
}

.score-container {
  margin-bottom: 30px;
}

.score-heading {
  font-size: 18px;
  margin-bottom: 10px;
}

.score-list {
  list-style-type: none;
  padding: 0;
}

.score-item {
  margin-bottom: 5px;
  background-color: #f5f5f5;
  padding: 10px;
  border-radius: 5px;
}

.player-name {
  color: gray;
  font-weight: bold;
}

.player-score {
  color: gray;
  font-weight: bold;
}

.start-quiz-link {
  display: inline-block;
  background-color: #f5f5f5;
  padding: 10px 20px;
  text-align: center;
  text-decoration: none;
  color: black;
  border-radius: 5px;
  transition: background-color 0.3s;
}

.start-quiz-link:hover {
  background-color: #e0e0e0;
}
</style>
