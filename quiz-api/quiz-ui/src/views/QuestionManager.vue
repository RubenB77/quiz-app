<template>
  <div>
    <h1>Question {{ currentQuestionPosition }} / {{ totalNumberOfQuestions }}</h1>
    <QuestionDisplay
      v-if="currentQuestion"
      :question="currentQuestion"
      @answer-selected="answerClickedHandler"
    />
  </div>
</template>

<script>
import axios from "axios";
import QuestionDisplay from "./QuestionDisplay.vue";

export default {
  components: {
    QuestionDisplay,
  },
  data() {
    return {
      totalNumberOfQuestions: 0,
      currentQuestion: null,
      currentQuestionPosition: 1,
      possibleAnswers: [],
    };
  },
  async created() {
    this.totalNumberOfQuestions = await this.getNumberOfQuestions();
    if (this.totalNumberOfQuestions > 0) {
      await this.loadQuestionByPosition(this.currentQuestionPosition);
    }
  },
  methods: {
    async loadQuestionByPosition(position) {
  try {
    const response = await axios.get(`http://localhost:5000/api/questions/${position}`);
    this.currentQuestion = response.data;
  } catch (error) {
    console.error(error);
    // Traitez l'erreur de récupération de la question
    // Par exemple, vous pouvez afficher un message d'erreur ou rediriger vers une page d'erreur
  }
},

    async answerClickedHandler(answerIndex) {
      this.possibleAnswers.push(answerIndex);

      if (this.currentQuestionPosition < this.totalNumberOfQuestions) {
        this.currentQuestionPosition++;
        await this.loadQuestionByPosition(this.currentQuestionPosition);
      } else {
        this.$router.push("/end-quiz"); // Redirige vers la page de fin du quiz
      }
    },
    async getNumberOfQuestions() {
  const response = await axios.get("http://localhost:5000/api/questions/count");
  return response.data.count;
},
  },
};
</script>

<style scoped>
/* Ajoutez ici le style de votre composant */
</style>
