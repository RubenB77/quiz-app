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
import QuizApiService from "@/services/QuizApiService";
import QuestionDisplay from "./QuestionDisplay.vue";
import ParticipationStorageService from "@/services/ParticipationStorageService";

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
    try {
      const { data } = await QuizApiService.getQuizInfo();
      this.totalNumberOfQuestions = data.size;
      if (this.totalNumberOfQuestions > 0) {
        await this.loadQuestionByPosition(this.currentQuestionPosition);
      }
    } catch (error) {
      console.error(error);
      // Handle the error of fetching the quiz info
      // You can show an error message or redirect to an error page, for instance
    }
  },
  methods: {
    async loadQuestionByPosition(position) {
      try {
        const { data } = await QuizApiService.getQuestion(position);
        this.currentQuestion = data;
      } catch (error) {
        console.error(error);
        // Handle the error of fetching the question
        // You can show an error message or redirect to an error page, for instance
      }
    },
    answerClickedHandler(answerIndex) {
      this.possibleAnswers.push(answerIndex);

      if (this.currentQuestionPosition < this.totalNumberOfQuestions) {
        this.currentQuestionPosition++;
        this.loadQuestionByPosition(this.currentQuestionPosition);
      } else {
        this.calculateFinalScore();
      }
    },
    async calculateFinalScore() {
      try {
        const playerName = ParticipationStorageService.getPlayerName();
        const participationScore = this.possibleAnswers.map(answer => answer + 1);

        const { data } = await QuizApiService.submitParticipation(playerName, participationScore);

        const finalScore = data.score;
        ParticipationStorageService.saveParticipationScore(finalScore);

        this.$router.push("/end-quiz");
      } catch (error) {
        console.error(error);
        // Handle the error of submitting participation
        // You can show an error message or redirect to an error page, for instance
      }
    },
  },
};
</script>

<style scoped>
/* Add your component style here */
</style>
