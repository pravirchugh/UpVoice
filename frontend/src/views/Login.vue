<template>
  <div class="login-container">
    <h2>Login</h2>
    <!-- User Type Selection -->
    <div>
      <label>
        <input type="radio" value="citizen" v-model="selectedUserType"> Citizen
      </label>
      <label>
        <input type="radio" value="investor" v-model="selectedUserType"> Investor
      </label>
    </div>
    <!-- Submit Button -->
    <button @click="handleLogin">Login</button>
  </div>
</template>

<script>
import router from '../router'; // Adjust path if needed

export default {
  data() {
    return {
      selectedUserType: 'citizen' // Default selection
    };
  },
  methods: {
    handleLogin() {
      if (this.selectedUserType === 'citizen') {
        router.push('/login/citizen');
      } else {
        router.push('/login/investor');
      }
    }
  }
};
</script>

<style>
.login-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  width: 400px; /* Adjust width as needed */
  margin: 0 auto; /* Center the container */
  border: 1px solid #ccc;
  border-radius: 5px;
}

h2 {
  margin-bottom: 20px;
  text-align: center;
}

label {
  display: block;
  margin-bottom: 10px;
}

input[type="radio"] {
  margin-right: 5px;
}

button {
  background-color: #4CAF50; /* Green */
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 3px;
  cursor: pointer;
  margin-top: 20px;
}
</style>