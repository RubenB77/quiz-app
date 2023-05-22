<template>
  <div class="new-quiz-page">
    <h1>Commencer le quizz</h1>
    
    <form @submit.prevent="launchNewQuiz">
      <div class="mb-3">
        <label for="playerName" class="form-label">Entrez votre nom :</label>
        <input type="text" class="form-control" id="playerName" v-model="username">
      </div>
      <button type="submit" class="btn btn-primary">Commencer le quiz</button>
    </form>
  </div>
</template>

<script>
import ParticipationStorageService from "@/services/ParticipationStorageService";

export default {
  data() {
    return {
      username: ''
    };
  },
  methods: {
    async launchNewQuiz() {
      if (!this.username) {
        console.error('Username is not defined');
        return;
      }
      console.log("Launch new quiz with", this.username);
      ParticipationStorageService.savePlayerName(this.username);
      console.log('Router:', this.$router);
      this.$router.push('/questions');
    },
  },
};
</script>


<style>
@media (min-width: 1024px) {
  .new-quiz-page {
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center; 
    flex-direction: column;
  }
  
  form {
    width: 300px;
    margin-top: 20px;
  }
  
  .form-label {
    margin-bottom: 10px;
  }
}
</style>

