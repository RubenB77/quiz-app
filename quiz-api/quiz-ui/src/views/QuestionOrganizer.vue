<template>
  <div class="question-organizer">
    <h1>Gestion des questions</h1>
    <div class="question-list">
      <div v-for="question in questions" :key="question.id" class="question-item">
        <div class="question-info">
          <div class="question-id-box">
            <h3 class="question-id">{{ question.position }}</h3>
          </div>
          <div class="question-content">
            <p class="question-title">{{ question.title }}</p>
          </div>
        </div>
        <div>
          <button @click="editQuestion(question.id)">Modifier</button>
          <button @click="deleteQuestion(question.id)">Supprimer</button>
        </div>
      </div>
    </div>
    <div class="button-container">
      <button @click="deleteAllQuestions">Supprimer toutes les questions</button>
      <button @click="addQuestion">Ajouter une question</button>
    </div>
  </div>
</template>

<script>
import AdminStorageService from "@/services/AdminStorageService";
import QuizApiService from "@/services/QuizApiService";

export default {
  data() {
    return {
      questions: [],
    };
  },
  methods: {
    fetchQuestions() {
      const token = AdminStorageService.getAdminToken();
      QuizApiService.getAllQuestions(token)
        .then(response => {
          if (response.data && Array.isArray(response.data)) {
            this.questions = response.data;
          } else {
            this.questions = [];
          }
        })
        .catch(error => {
          console.error("Error fetching questions:", error);
        });
    },
    editQuestion(questionId) {
      // Rediriger vers la page de modification de question en passant l'ID de la question en paramètre
      // this.$router.push({ name: "EditQuestion", params: { id: questionId } });
    },
    deleteQuestion(questionId) {
      const token = AdminStorageService.getAdminToken();
      QuizApiService.DeleteQuestion(questionId, token)
        .then(() => {
          this.fetchQuestions();
        })
        .catch((error) => {
          console.error("Error deleting question:", error);
        });
    },
    deleteAllQuestions() {
      const token = AdminStorageService.getAdminToken();
      QuizApiService.deleteAllQuestions(token)
        .then(() => {
          this.fetchQuestions();
        })
        .catch((error) => {
          console.error("Error deleting all questions:", error);
        });
    },
    addQuestion() {
      // Rediriger vers la page d'ajout de question
      // this.$router.push({ name: "AddQuestion" });
    },
  },
  created() {
    this.fetchQuestions();
  },
};
</script>

<style scoped>
.question-organizer {
  text-align: center;
  padding: 20px;
}

.question-list {
  margin-top: 20px;
}

.question-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}

.question-info {
  display: flex;
  align-items: center;
}

.question-id-box {
  background-color: #f5f5f5;
  padding: 10px;
  border-radius: 5px;
  margin-right: 10px;
}

.question-id {
  font-size: 18px;
  margin: 0;
}

.question-content {
  flex-grow: 1;
}

.question-title {
  margin: 0;
}

.button-container {
  margin-top: 20px;
}

button {
  padding: 10px 20px;
  background-color: #f5f5f5;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  margin: 0 10px;
}

button:hover {
  background-color: #e0e0e0;
}
</style>

