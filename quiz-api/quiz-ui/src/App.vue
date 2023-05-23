<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header class="header-container">
      <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/start-new-quiz-page">New Quiz</RouterLink>
        <RouterLink to="/login-page">Admin Page</RouterLink>
      </nav>
  </header>

  <RouterView />
</template>

<style scoped>
.header-container {
  position: fixed;
  top: 0;
  left: 0;
  width: 200px;
  height: 100vh;
  background-color: #f5f5f5;
  padding: 20px;
  box-sizing: border-box;
}

nav {
  font-size: 12px;
  text-align: left;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: block;
  padding: 10px 0;
  text-decoration: none;
  margin-bottom: 10px; 
  border-bottom: 1px solid #e0e0e0; 
  text-align: center; 
}

nav a:first-of-type {
  margin-top: 10px; 
  border-top: 1px solid #e0e0e0; 
}

@media (min-width: 1024px) {
  .header-container {
    width: 250px; 
    padding-right: 40px; 
  }

  nav {
    font-size: 14px; 
  }
}
</style>
