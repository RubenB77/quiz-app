<template>
  <div class="quiz-result-page">
    <h1>Résultat du quiz</h1>
    <div v-if="finalScore !== null">
      <p>Votre score: {{ finalScore }}</p>
      <router-link to="/" class="home-link">Retour à la page d'accueil</router-link>
      <div class="score-container">
        <h2 class="score-heading">Classement des scores :</h2>
        <ul class="score-list">
          <li v-for="score in registeredScores" :key="score.id" :class="['score-item', { 'current-player': score.playerName === currentPlayerName }]">
            <span class="player-name">{{ score.playerName }} -</span> <span class="player-score">{{ score.score }}</span>
          </li>
        </ul>
      </div>
    </div>
    <div v-else>
      <p>Aucun résultat disponible.</p>
    </div>
  </div>
</template>

<script>
import ParticipationStorageService from "@/services/ParticipationStorageService";
import QuizApiService from "@/services/QuizApiService";

export default {
  data() {
    return {
      finalScore: null,
      registeredScores: [],
      currentPlayerName: ParticipationStorageService.getPlayerName(),
    };
  },
  created() {
    this.finalScore = ParticipationStorageService.getParticipationScore();
    ParticipationStorageService.clear();

    this.loadRegisteredScores();
  },
  methods: {
    async loadRegisteredScores() {
      try {
        const response = await QuizApiService.getScores();
        this.registeredScores = response.data;
      } catch (error) {
        console.error("Erreur lors de la récupération des scores:", error);
      }
    },
  },
};
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

.score-container {
  margin-top: 20px;
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
  font-weight: bold;
}

.player-score {
  font-weight: bold;
}

.current-player {
  background-color: #ffd700;
}
</style>
