<template>
  <div class="login-page">
    <h1>Login</h1>
    <form @submit.prevent="login">
      <div class="form-group">
        <label for="password">Password:</label>
        <input type="password" id="password" v-model="password" required>
      </div>
      <div>
        <button type="submit">Login</button>
      </div>
    </form>
    <div v-if="loggedIn">
      <h2>Login successful</h2>
      <!-- Add your admin content here -->
      <AdminPage />
    </div>
    <div v-if="errorMessage" class="error-message">
      {{ errorMessage }}
    </div>
  </div>
</template>

<script>
import QuizApiService from "@/services/QuizApiService";
import AdminPage from "./AdminPage.vue";
import AdminStorageService from "@/services/AdminStorageService";

export default {
  data() {
    return {
      password: "",
      loggedIn: false,
      errorMessage: "",
    };
  },
  methods: {
    async login() {
      try {
        const response = await QuizApiService.adminLogin(this.password);

        // Perform additional checks if necessary
        if (response.status === 200) {
          const token = response.data.token;
          AdminStorageService.saveAdminToken(token); // Store the token

          this.loggedIn = true;
          this.$router.push({ name: "AdminPage" }); // Redirect to the AdminPage
        } else {
          this.errorMessage = "Invalid password";
        }
      } catch (error) {
        console.error("Error logging in:", error);
        this.errorMessage = "Wrong Password";
      }
    },
  },
  components: {
    AdminPage,
  },
  created() {
    const token = AdminStorageService.getAdminToken(); // Get the stored token
    if (token) {
      // Perform token validation if necessary
      this.loggedIn = true;
      this.$router.push({ name: "AdminPage" }); // Redirect to the AdminPage
    }
  },
};
</script>

<style scoped>
.login-page {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 20px;
}

form {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 20px;
}

.form-group {
  margin-bottom: 30px;
}

label {
  font-weight: bold;
  margin-right: 20px;
}

input[type="password"] {
  padding: 5px;
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

.error-message {
  color: red;
  margin-top: 10px;
}
</style>
