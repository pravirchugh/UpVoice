<template>
  <nav class="navbar">
    <div class="navbar-brand">
      <a href="/" class="navbar-item">UpVoice</a>
    </div>
    <div class="navbar-menu">
      <div class="navbar-end">
        <!-- Signup and Login Links -->
        <router-link v-if="!isLoggedIn()" to="/auth/signup" class="navbar-item" style="font-weight: 500;">Signup</router-link>
        <router-link v-if="!isLoggedIn()" to="/auth/login" class="navbar-item" style="font-weight: 500;">Login</router-link>
        <router-link v-if="isLoggedIn() && $route.name !== 'CitizenDashboard'" to="/citizen/dashboard"
          class="navbar-item" style="font-weight: 500;">Citizen dashboard</router-link>
        <router-link v-if="isLoggedIn()">
          <button @click="logoutUser" role="link" style="margin: 0px 15px; font-weight: 500">
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
  methods: {
    isLoggedIn() {
      return isUserLoggedIn();
    },

    logoutUser() {
      authService.logoutUser();
    }
  }
}
</script>

<style scoped>
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
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