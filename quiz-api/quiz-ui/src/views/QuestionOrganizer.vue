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
          <button @click="editQuestion(question.id)" class="edit-button">Modifier</button>
          <button @click="deleteQuestion(question.id)">Supprimer</button>
        </div>
      </div>
    </div>
    <div class="button-container">
      <button @click="addQuestion">Ajouter une question</button>
      <button v-if="questions.length > 0" @click="deleteAllQuestions">Supprimer toutes les questions</button>
      <button class="logout-button" @click="logout">Déconnexion</button>
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
    async fetchQuestions() {
      try {
        const token = AdminStorageService.getAdminToken();
        const response = await QuizApiService.getAllQuestions(token);
        if (Array.isArray(response.data)) {
          this.questions = response.data.map((question) => ({
            id: question[0],
            position: question[1],
            title: question[2],
          }));
        } else {
          this.questions = [];
        }
      } catch (error) {
        console.error("Error fetching questions:", error);
      }
    },
    editQuestion(questionId) {
      console.log("aaaa"+questionId);
  this.$router.push({ name: 'ModifyQuestion', params: { questionId: questionId } });
},

    deleteQuestion(questionId) {
      const token = AdminStorageService.getAdminToken();
      QuizApiService.deleteQuestion(questionId, token)
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
       this.$router.push({ name: "AddQuestionPage" });
    },
    logout() {
      AdminStorageService.clearToken();
      this.$router.push({ name: "LoginPage" });
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
  display: flex;
  justify-content: center;
  gap: 10px;
}

button {
  padding: 10px 20px;
  background-color: #f5f5f5;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #e0e0e0;
}

.logout-button {
  background-color: red;
  color: white;
}

.edit-button {
  margin-right: 5px;
}
</style>
