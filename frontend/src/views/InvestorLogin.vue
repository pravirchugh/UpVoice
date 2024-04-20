<template>
  <form class="login-form" style="padding: 20px;">
    <h2>Stakeholder Login</h2>
    <div class="flex flex-column gap-2" style="width: 100%;margin: 10px 0px;">
      <label for="email">Email</label>
      <InputText id="email" v-model="email" aria-describedby="username-help"  style="width: 100%;" />
    </div>
    <div class="flex flex-column gap-2" style="width: 100%; margin: 10px 0px;">
      <label for="password">Password</label>
      <InputText id="password" v-model="password" type="password" aria-describedby="password-help"  style="width: 100%;" />
    </div>
    <Button
      @click="loginStakeholder"
      style="padding: 15px; width: 60%; font-size: 18px; border-radius: 6px; text-transform: uppercase;">
      <span style="text-align: center; width: 100%;">
        Login
      </span>
    </Button>
  </form>
</template>

<script>
import authService from '../services/AuthService'

export default {
  data(){
    return {
      email: '',
      password: ''
    }
  },
  methods: {
    loginStakeholder() {
      return authService.loginStakeholder()
    }
  }

}
</script>

<style>
.login-form {
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
}

input[type="email"],
input[type="password"] {
  width: 100%;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 3px;
  margin-bottom: 10px;
}

button[type="submit"] {
  background-color: #551a8b;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 3px;
  cursor: pointer;
}</style>