<template>
  <form class="signup-form">
    <h2>Sign Up</h2>

    <label for="username">Username:</label>
    <input type="text" id="username" placeholder="Enter username" v-model="username">

    <label for="email">Email:</label>
    <input type="email" id="email" placeholder="Enter email" v-model="email">

    <label for="password">Password:</label>
    <input type="password" id="password" placeholder="Enter password" v-model="password">

    <label for="confirmPassword">Confirm Password:</label>
    <input type="password" id="confirmPassword" placeholder="Confirm password" v-model="confirmPassword">

    <button type="submit" @click="this.performSignUp">Sign Up</button>
  </form>
</template>

<script>
import authService from '../services/AuthService';

export default {
  components: {
  },
  data() {
    return {
      email: '',
      password: '',
      confirmPassword: '',
      error: ''
    }
  },
  methods: {
    performSignUp() {
      if(this.password !== this.confirmPassword) {
        return;
      }

      const payload = {
        username: this.username,
        email: this.email,
        password: this.password
      }
      return authService.signup(payload)
    }
  },
  mounted() {

  },
  setup() {

  },
  created() {

  }
}
</script>

<style>
.signup-form {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  width: 400px;
  margin: 0 auto;
  border: 1px solid #ccc;
  border-radius: 5px;
}

h2 {
  margin-bottom: 20px;
  text-align: center;
}

label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
  /* Added for emphasis */
}

input[type="text"],
input[type="email"],
input[type="password"] {
  width: 100%;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 3px;
  margin-bottom: 10px;
  /* Added for spacing */
}

button[type="submit"] {
  background-color: #551a8b;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 3px;
  cursor: pointer;
}
</style>