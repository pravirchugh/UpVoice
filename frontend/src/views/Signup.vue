<template>
  <div class="signup-container">
    <h2>Sign Up</h2>
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
    <button @click="handleSubmit">Sign Up</button>
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
    handleSubmit() {
      if (this.selectedUserType === 'citizen') {
        router.push('/auth/signup/citizen');
      } else {
        router.push('/auth/signup/investor');
      }
    }
  }
};
</script>

<style>
.signup-container {
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
  background-color: #551a8b;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 3px;
  cursor: pointer;
  margin-top: 20px;
}
</style>