import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '@/views/HomePage.vue'
import NewQuizPage from '@/views/NewQuizPage.vue'
import QuestionManager from '@/views/QuestionManager.vue'
import QuizResultPage from '@/views/QuizResultPage.vue'
import LoginPage from '@/views/LoginPage.vue'
import OrgaPage from '@/views/QuestionOrganizer.vue'
import AdminPage from '@/views/AdminPage.vue'
import ModifyQuestion from '@/views/ModifyQuestion.vue';
import AddQuestion from '@/views/AddQuestionPage.vue';
const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: "/",
      name: "HomePage",
      component: HomePage,
    },
    {
      path: "/add-question",
      name: "AddQuestionPage",
      component: AddQuestion,
    },
    {
      path: '/modify-question/:questionId',
      name: 'ModifyQuestion',
      component: ModifyQuestion,
      props: route => ({
        questionId: route.params.questionId,
      }),},
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
      component: QuizResultPage, 
    },
    {
    path: "/login-page",
      name: "LoginPage",
      component: LoginPage,
    },
    {
      path: "/admin",
      name: "AdminPage",
      component: AdminPage,
    },
    {
      path: "/question-organizer",
      name: "OrgaPage",
      component: OrgaPage,
    },
  ]
})

export default router
