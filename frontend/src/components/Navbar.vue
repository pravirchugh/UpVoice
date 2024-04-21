<template>
  <nav class="navbar">
    <div class="navbar-brand">
      <a href="/" class="navbar-item">UpVoice</a>
    </div>
    <div class="navbar-menu">
      <div class="navbar-end">
        <!-- Signup and Login Links -->
        <router-link v-if="!isLoggedIn()" to="/auth/signup" class="navbar-item" style="font-weight: 500; font-size: 20px; padding: 10px">Signup</router-link>
        <router-link v-if="!isLoggedIn()" to="/auth/login" class="navbar-item" style="font-weight: 500; font-size: 20px; padding: 10px">Login</router-link>
        <router-link v-if="isLoggedIn() && $route.name !== 'CitizenDashboard'" to="/citizen/dashboard"
          class="navbar-item" style="font-weight: 500;">Citizen dashboard</router-link>
         <router-link v-if="isLoggedIn() && $route.name !== 'InvestorDashboard'" to="/investor/dashboard"
          class="navbar-item" style="font-weight: 500;">Investor dashboard</router-link>  
      
        <!-- Reputation metric for citizen -->
        <div v-if="isLoggedIn() && userType === 'citizen'" class="navbar-item" style="font-weight: 500;">
          <img src="/path/to/reputation-icon.png" alt="Reputation Icon" style="width: 20px; height: 20px; margin-right: 5px;">
          {{ reputation.toFixed(2) }} dB
        </div>


        
        <router-link v-if="isLoggedIn()">
          <button @click="logoutUser" role="link" style="margin: 0px 15px; font-weight: 500; background-color: #551a8b; padding: 10px; color:white; border-radius: 5px; width: auto">
            Logout
          </button>
        </router-link>
      </div>
    </div>
  </nav>
</template>

<script>
import authService from '../services/AuthService';
import { isUserLoggedIn } from '../utils';

export default {
  name: 'Navbar',
  data() {
    return {
      reputation: 0, // Set initial reputation to 0
      userType: '', // Store user type (citizen or investor)
    };
  },
  created() {
    if (this.isLoggedIn()) {
      // this.userType = getUserType(); // Get user type
      if (this.userType === 'citizen') {
        // Fetch reputation for citizen user
        this.fetchReputation();
      }
    }
  },
  methods: {
    isLoggedIn() {
      return isUserLoggedIn();
    },

    logoutUser() {
      authService.logoutUser();
    },
    fetchReputation() {
      // Here, you can fetch the reputation from your API or calculate it based on user data
      // For demonstration purposes, let's assume a random reputation value between 0 and 100
      this.reputation = Math.random() * 100;
    },
  }
};
</script>

<style scoped>
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
  border-bottom: 0.5px solid black;
  margin-bottom: 10px;
}

.navbar-brand {
  font-weight: bold;
  font-size: 40px;
  margin-left: 15px;
}

.navbar-menu {
  display: flex;
}

.navbar-end {
  margin-left: auto;
}

.navbar-item {
  margin-left: 1rem;
  text-decoration: none;
}
</style>