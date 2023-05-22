import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '@/views/HomePage.vue'
import NewQuizPage from '@/views/NewQuizPage.vue'
import QuestionManager from '@/views/QuestionManager.vue'
import QuizResultPage from '@/views/QuizResultPage.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: "/",
      name: "HomePage",
      component: HomePage,
    },
    {
      path: "/start-new-quiz-page",
      name: "NewQuizPage",
      component: NewQuizPage,
    },
    {
      path: "/questions",
      name: "QuestionManager",
      component: QuestionManager,
    },
    {
      path: '/end-quiz',
      name: 'EndQuiz',
      component: QuizResultPage, // Remplacez "EndQuizComponent" par le composant réel utilisé pour la fin du quiz
    },
  ]
})

export default router
