<template>
  <div class="page-wrapper">
    <h1 class="question-indicator">Question {{ currentQuestionPosition }} / {{ totalNumberOfQuestions }}</h1>
    <div class="content-wrapper">
      <QuestionDisplay
        v-if="currentQuestion"
        :question="currentQuestion"
        @answer-selected="answerClickedHandler"
      />
    </div>
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
    }
  },
  methods: {
    async loadQuestionByPosition(position) {
      try {
        const { data } = await QuizApiService.getQuestion(position);
        this.currentQuestion = data;
      } catch (error) {
        console.error(error);
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
      }
    },
  },
};
</script>

<style scoped>
.page-wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
}

.question-indicator {
  position: absolute;
  top: 10px;
  left: 10px;
}

.content-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-grow: 1;
}

.content-wrapper img {
  max-width: 100%;
  max-height: 400px;
}

/* Ajoutez ici le style supplémentaire pour votre composant */
</style>
