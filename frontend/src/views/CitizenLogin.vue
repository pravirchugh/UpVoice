<template>
  <form class="login-form" @submit.prevent>
    <h2>Citizen Login</h2>
    <div class="flex flex-column gap-2" style="width: 100%;margin: 10px 0px;">
      <label for="username">Username</label>
      <InputText id="username" v-model="username" style="width: 100%;" />
    </div>
    <div class="flex flex-column gap-2" style="width: 100%;margin: 10px 0px;">
      <label for="password">Password</label>
      <InputText id="password" type="password" v-model="password" style="width: 100%;" />
    </div>
    <button type="submit" @click="loginUser"
      style="padding: 15px; width: 60%; font-size: 18px; border-radius: 6px; text-transform: uppercase;">Login</button>
  </form>
</template>

<script>
import router from '../router';
import authService from '../services/AuthService'
export default {
  data() {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    async loginUser() {
      try {
        const payload = {
          username: this.username,
          password: this.password
        }
        await authService.loginUser(payload); 
        router.push({name: 'CitizenDashboard'})
      } catch (error) {
        console.log(error);
      }
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