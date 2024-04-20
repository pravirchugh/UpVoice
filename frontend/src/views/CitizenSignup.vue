<template>
  <form class="signup-form">
    <h2 style="text-transform: uppercase;">Sign Up</h2>

    <div class="flex flex-column gap-2" style="width: 100%; margin: 10px 0px;">
      <label for="username">Username</label>
      <InputText id="username" v-model="username"  style="width: 100%;" />
    </div>

    <div class="flex flex-column gap-2" style="width: 100%; margin: 10px 0px;">
      <label for="email">Email</label>
      <InputText id="email" v-model="email"  style="width: 100%;" />
    </div>

    <div class="flex flex-column gap-2" style="width: 100%; margin: 10px 0px;">
      <label for="password">Password</label>
      <InputText id="password" v-model="password" type="password" style="width: 100%;" />
    </div>

    <div class="flex flex-column gap-2" style="width: 100%; margin: 10px 0px;">
      <label for="confirmPassword">Confirm Password</label>
      <InputText id="confirmPassword" v-model="confirmPassword" type="password" style="width: 100%;" />
    </div> 

    <Button
      @click="this.performSignUp"
      style="padding: 15px; width: 60%; font-size: 18px; border-radius: 6px; text-transform: uppercase;">
      <span style="text-align: center; width: 100%;">
        Sign Up
      </span>
    </Button>

    <!-- <button type="submit" @click="this.performSignUp">Sign Up</button> -->
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
      const emailProvided = false
      if (this.email !== '') {
        emailProvided = true
      }

      if (this.password !== this.confirmPassword) {
        return;
      }

      const payload = {
        username: this.username,
        ...(emailProvided ? { email: this.email, "email_provided": emailProvided } : {}),
        password: this.password
      }
      return authService.signupUser(payload)
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