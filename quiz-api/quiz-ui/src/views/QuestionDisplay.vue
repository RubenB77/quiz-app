<template>
  <div>
    <h2>{{ question.title }}</h2>
    <img v-if="question.image" :src="question.image" />
    <p v-html="question.text"></p>
    <div v-for="(answer, index) in question.possibleAnswers" :key="index">
      <button @click="$emit('answer-selected', index)">{{ answer.text }}</button>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    question: {
      type: Object,
      required: true
    }
  }
};
</script>

<style scoped>
/* Ajoutez ici le style de votre composant */
</style>
