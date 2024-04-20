<template>
  <div class="login-container">
    <h2>Login</h2>
    <!-- User Type Selection -->
    <div class="card-container">
      <!-- Citizen Card -->
      <div class="card" @click="handleLogin('citizen')">
        <img src="../assets/home/citizen.jpg" alt="Citizen">
        <p class="citizen">Citizen</p>
      </div>
      <!-- Investor Card -->
      <div class="card" @click="handleLogin('investor')">
        <img src="../assets/home/investor.jpg" alt="Investor">
        <p class="investor">Investor</p>
      </div>
    </div>
  </div>
</template>

<script>
import router from '../router'; // Adjust path if needed

export default {
  methods: {
    handleLogin(userType) {
      if (userType === 'citizen') {
        router.push('/auth/login/citizen');
      } else {
        router.push('/auth/login/investor');
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
  width: 100%; /* Adjust width as needed */
}

h2 {
  margin-bottom: 20px;
  text-align: center;
  font-size: 30px;
}

.card-container {
  display: flex;
  justify-content: space-around;
  width: 60%;
}

.card {
  width: 400px; 
  border: 1px solid #ccc;
  border-radius: 5px;
  padding: 10px;
  cursor: pointer;
  transition: transform 0.3s ease;
}

.card:hover {
  transform: translateY(-5px);
}

.card img {
  width: 100%;
  border-radius: 5px;
}

.card p {
  text-align: center;
  margin-top: 10px;
}
</style>


<!-- <template>
  <div class="login-container">
    <h2>Login</h2>
    <div>
      <label>
        <input type="radio" value="citizen" v-model="selectedUserType"> Citizen
      </label>
      <label>
        <input type="radio" value="investor" v-model="selectedUserType"> Investor
      </label>
    </div>
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
        router.push('/auth/login/citizen');
      } else {
        router.push('/auth/login/investor');
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
  width: 400px;
  /* Adjust width as needed */
  margin: 0 auto;
  /* Center the container */
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
  background-color: #4CAF50;
  /* Green */
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 3px;
  cursor: pointer;
  margin-top: 20px;
}
</style> -->
