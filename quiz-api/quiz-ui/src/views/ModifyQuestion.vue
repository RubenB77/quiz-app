<template>
  <div class="modify-question">
    <h1>Modifier une question</h1>
    <div class="question-box">
      <div class="form-group">
        <label for="position">Position:</label>
        <input type="number" id="position" v-model="newPosition">
      </div>
      <div class="form-group">
        <label for="title">Titre:</label>
        <input type="text" id="title" v-model="newTitle">
      </div>
      <div class="form-group">
        <label for="text">Texte:</label>
        <textarea id="text" rows="4" v-model="newText"></textarea>
      </div>
      <div class="form-group">
        <label for="image">Image:</label>
        <div class="image-container">
          <input type="text" id="image" v-model="newImage">
        </div>
        <div class="image-preview" v-if="newImage">
          <img :src="newImage" alt="Question Image">
        </div>
      </div>
      <div class="form-group" v-for="(answer, index) in newAnswers" :key="index">
        <label :for="`answer-${index}`" class="answer-label">Réponse {{ index + 1 }}:</label>
        <div class="answer-inputs">
          <input :id="`answer-${index}`" type="text" v-model="answer.text">
        </div>
        <div class="answer-checkbox">
          <input :id="`correct-${index}`" type="checkbox" v-model="answer.isCorrect">
        </div>
      </div>
      <button @click="updateQuestion" class="update-button">Valider</button>
      <button @click="annuler" class="cancel-button">Annuler</button>
    </div>
  </div>
</template>

<script>
import QuizApiService from "@/services/QuizApiService";
import AdminStorageService from "@/services/AdminStorageService";

export default {
  props: {
    questionId: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      newPosition: "",
      newTitle: "",
      newText: "",
      newImage: "",
      newAnswers: [],
    };
  },
  methods: {
    async updateQuestion() {
      const id = this.questionId;
      const token = AdminStorageService.getAdminToken();
      const data = {
        position: this.newPosition,
        title: this.newTitle,
        text: this.newText,
        image: this.newImage,
        possibleAnswers: this.newAnswers,
      };
      try {
        await QuizApiService.updtquestion(id, token, data);
        console.log("Question updated successfully!");
        this.$router.push({ name: "OrgaPage" });
      } catch (error) {
        console.error("Error updating question:", error);
      }
    },
    async annuler(){this.$router.push({ name: "OrgaPage" });},
    async fetchQuestion() {
      try {
        const token = AdminStorageService.getAdminToken();
        console.log(this.questionId);
        const response = await QuizApiService.getQuestionByid(this.questionId);
        console.log(response.data);
        this.newPosition = response.data.position;
        this.newTitle = response.data.title;
        this.newText = response.data.text;
        this.newImage = response.data.image;
        this.newAnswers = response.data.possibleAnswers.map((answer) => ({
          text: answer.text,
          isCorrect: answer.isCorrect,
        }));
      } catch (error) {
        console.error("Error fetching question:", error);
      }
    },
  },
  created() {
    this.fetchQuestion();
  },
};
</script>

<style scoped>
.modify-question {
  text-align: center;
  padding: 20px;
}

.question-box {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 20px;
  margin-left: 10px;
}

.form-group {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
}

.label {
  font-weight: bold;
  margin-right: 20px;
}

input[type="number"],
input[type="text"],
textarea {
  width: 300px;
  padding: 5px;
  margin-left: 10px;
}

.image-container {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
}

.image-container input {
  flex-grow: 1;
}

.image-preview {
  margin-left: 10px;
}

.image-preview img {
  width: 50px;
  height: 50px;
  object-fit: cover;
  border-radius: 50%;
}

.answer-label {
  margin-right: 10px;
  margin-left: 10px;
}

.answer-inputs {
  display: flex;
  align-items: center;
  margin-left: 20px;
}

.answer-checkbox {
  margin-left: 10px;
}

button {
  padding: 10px 20px;
  background-color: #f5f5f5;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  margin-top: 20px;
}

button:hover {
  background-color: #e0e0e0;
}

.update-button {
  background-color: green;
  color: white;
}
.cancel-button {
  background-color: red;
  color: white;
}
.update-button:hover {
  background-color: #007f00;
}
</style>
