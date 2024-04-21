<template>
  <nav class="navbar">
    <div class="navbar-brand">
      <a href="/" class="navbar-item">UpVoice</a>
    </div>
    <div class="navbar-menu">
      <div class="navbar-end">
        <!-- Signup and Login Links -->
        <router-link v-if="!isLoggedIn()" to="/auth/signup" class="navbar-item"
          style="font-weight: 500; font-size: 20px; padding: 10px">Signup</router-link>
        <router-link v-if="!isLoggedIn()" to="/auth/login" class="navbar-item"
          style="font-weight: 500; font-size: 20px; padding: 10px">Login</router-link>
        <router-link v-if="isLoggedIn() && userType == 'citizen'" to="/citizen/dashboard" class="navbar-item"
          style="font-weight: 500;">Citizen dashboard</router-link>
        <router-link v-if="isLoggedIn() && userType == 'stakeholder'" to="/investor/dashboard" class="navbar-item"
          style="font-weight: 500;">Investor dashboard</router-link>
        <!-- Reputation metric for citizen -->
        <!-- <div v-if="isLoggedIn() && userType === 'citizen'" class="navbar-item" style="font-weight: 500;">
          <img src="/path/to/reputation-icon.png" alt="Reputation Icon" style="width: 20px; height: 20px; margin-right: 5px;">
          {{ reputation.toFixed(2) }} dB
        </div> -->
        <div v-if="userType === 'citizen'" class="game_citizen">
          <img src="../assets/home/megaphone score.png" alt="reputation" style="width: 50px; margin: 5px;">
          <p>54 dB</p>
        </div>
        <div v-if="userType === 'stakeholder'" class="game_investor_money">
          <img src="../assets/home/dollar.png" alt="reputation" style="width: 40px; height: 40px; margin: 5px;">
          <p>5000</p>
        </div>
        <div v-if="userType === 'stakeholder'" class="game_investor_health">
          <img src="../assets/home/sign.png" alt="reputation" style="width: 40px; height: 40px; margin: 5px;">
          <p>300</p>
        </div>
        <Button @click="logoutUser" v-if="isLoggedIn()"
          style="margin: 0px 15px; font-weight: 500; background-color: #551A8B; padding: 10px; color:white; border-radius: 5px; width: auto">
          Logout
        </Button>
      </div>
    </div>
  </nav>
</template>
<script>
import router from '../router';
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
    // const currentUser = authService.decodeToken()
    // console.log('user',currentUser);

    if (this.isLoggedIn()) {
      this.updateUserType(); // Update user type
      if (this.userType === 'citizen') {
        this.fetchReputation(); // Fetch reputation for citizen user
      }
    }
  },
  watch: {
    '$route'() {
      // When route changes, check if user is logged in and update user type and reputation if necessary
      if (this.isLoggedIn()) {
        this.updateUserType();
        if (this.userType === 'citizen') {
          this.fetchReputation();
        }
      }
    }
  },
  methods: {
    isLoggedIn() {
      return isUserLoggedIn();
    },
    reloadPage() {
      window.location.reload();
    },
    async logoutUser() {
      if(this.userType === 'citizen') {
        await authService.logoutUser();
      } else {
        await authService.logoutStakeholder();
      }
      
      this.reloadPage()
    },
    fetchReputation() {
      // Here, you can fetch the reputation from your API or calculate it based on user data
      // For demonstration purposes, let's assume a random reputation value between 0 and 100
      this.reputation = Math.random() * 100;
    },
    updateUserType() {
      // Update user type based on user data
      // const currentUser = authService.decodeToken()
      // console.log(currentUser);
      const user = authService.getUser()
      this.userType = user.user_type  // Assuming you have a function to get the user type
    }
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
  display: flex;
  align-items: center;
}

.navbar-item {
  margin-left: 1rem;
  text-decoration: none;
  padding: 20px;
}

.game_citizen {
  display: flex;
}

.game_investor_money {
  display: flex;
  align-items: center;
}

.game_investor_health {
  display: flex;
  align-items: center;
}</style>