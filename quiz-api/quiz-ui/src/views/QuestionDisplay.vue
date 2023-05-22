<template>
  <div>
    <h2>{{ question.title }}</h2>
    <div class="question-image-wrapper">
      <img v-if="question.image" :src="question.image" class="question-image" />
    </div>
    <p class="question-text" v-html="question.text"></p>
    <div class="answer-buttons">
      <button
        v-for="(answer, index) in question.possibleAnswers"
        :key="index"
        @click="$emit('answer-selected', index)"
        class="answer-button"
      >
        {{ answer.text }}
      </button>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    question: {
      type: Object,
      required: true,
    },
  },
};
</script>

<style scoped>
.question-image-wrapper {
  display: flex;
  justify-content: center;
  margin-bottom: 10px;
}

.question-image {
  max-width: 220px; 
}

.question-text {
  font-size: 20px; 
  line-height: 1.5;
  margin-bottom: 10px;
}

.answer-buttons {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 20px;
}

.answer-button {
  padding: 10px 20px;
  margin-bottom: 10px;
  background-color: #f5f5f5;
  border: none;
  border-radius: 5px;
  color: #333;
  font-size: 16px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.answer-button:hover {
  background-color: #e0e0e0;
}
</style>
