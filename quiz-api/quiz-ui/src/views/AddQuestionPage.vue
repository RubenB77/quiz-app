<template>
  <div class="add-question">
    <h1>Ajouter une question</h1>
    <div class="question-box">
      <div class="form-group">
        <label for="position">Position:</label>
        <input type="number" id="position" v-model="position">
      </div>
      <div class="form-group">
        <label for="title">Titre:</label>
        <input type="text" id="title" v-model="title">
      </div>
      <div class="form-group">
        <label for="text">Texte:</label>
        <textarea id="text" rows="4" v-model="text"></textarea>
      </div>
      <div class="form-group">
        <label for="image">Image:</label>
        <input type="text" id="image" v-model="image">
      </div>
      <div class="form-group" v-for="(answer, index) in possibleAnswers" :key="index">
        <label :for="`answer-${index}`">Réponse {{ index + 1 }}:</label>
        <div class="answer-inputs">
          <input :id="`answer-${index}`" type="text" v-model="answer.text">
        </div>
        <div class="answer-checkbox">
          <input :id="`correct-${index}`" type="checkbox" v-model="answer.isCorrect">
        </div>
      </div>
      <div class="button-container">
        <button @click="addQuestion" class="add-button">Ajouter</button>
        <button @click="cancel" class="cancel-button">Annuler</button>
      </div>
    </div>
  </div>
</template>

<script>
import QuizApiService from "@/services/QuizApiService";
import AdminStorageService from "@/services/AdminStorageService";

export default {
  data() {
    return {
      position: null,
      title: "",
      text: "",
      image: "",
      possibleAnswers: [
        { text: "", isCorrect: false },
        { text: "", isCorrect: false },
        { text: "", isCorrect: false },
        { text: "", isCorrect: false },
      ],
    };
  },
  methods: {
    async addQuestion() {
      const data = {
        position: this.position,
        title: this.title,
        text: this.text,
        image: this.image,
        possibleAnswers: this.possibleAnswers,
      };
      const token = AdminStorageService.getAdminToken();
      try {
        await QuizApiService.addQuestion(data, token);
        console.log("Question added successfully!");
        this.$router.push({ name: "OrgaPage" });
      } catch (error) {
        console.error("Error adding question:", error);
      }
    },
    cancel() {
      this.$router.push({ name: "OrgaPage" });
    },
  },
};
</script>

<style scoped>
.add-question {
  text-align: center;
  padding: 20px;
}

.question-box {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 20px;
}

.form-group {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
}

label {
  font-weight: bold;
  margin-right: 20px;
}

input[type="number"],
input[type="text"],
textarea {
  width: 300px;
  padding: 5px;
}

.answer-inputs {
  display: flex;
  align-items: center;
  margin-left: 10px;
}

.answer-checkbox {
  margin-left: 10px;
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

.add-button {
  background-color: green;
  color: white;
}

.add-button:hover {
  background-color: #007f00;
}

.cancel-button {
  background-color: red;
  color: white;
}

.cancel-button:hover {
  background-color: #7f0000;
}
</style>
