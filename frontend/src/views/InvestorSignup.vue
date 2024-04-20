<template>
  <form class="investor-signup-form" @submit.prevent="handleSubmit">
    <h2>Investor Sign Up</h2>

    <label for="name">Name:</label>
    <input type="text" id="name" placeholder="Enter your name">

    <label for="companyName">Company Name:</label>
    <input type="text" id="companyName" placeholder="Enter your company name">

    <label for="email">Email:</label>
    <input type="email" id="email" placeholder="Enter your email">

    <label for="password">Password:</label>
    <input type="password" id="password" placeholder="Enter your password">

    <label for="confirmPassword">Confirm Password:</label>
    <input type="password" id="confirmPassword" placeholder="Confirm your password">

    <button type="submit">Sign Up</button>
    <p v-if="errorMessage">{{ errorMessage }}</p>
  </form>
</template>


<script>
export default {
  data() {
    return {
      name: '',
      companyName: '',
      email: '',
      password: '',
      confirmPassword: '',
      errorMessage: '',
    };
  },
  methods: {
    async handleSubmit() {
      // Basic client-side validation (you should do more thorough validation)
      if (this.password !== this.confirmPassword) {
        this.errorMessage = 'Passwords do not match.';
        return;
      }

      try {
        const response = await axios.post('/add-stakeholder', { // Assuming '/add-stakeholder' is the correct route
          username: this.name, // Assuming 'name' is used as username in the backend
          company: this.companyName,
          email: this.email,
          password: this.password,
        });

        // Handle successful signup (e.g., redirect to a success page or login)
        console.log(response.data); // Log the response for now
        this.errorMessage = ''; // Clear any previous error message
        // ... your success logic here ...
      } catch (error) {
        // Handle signup errors
        console.error(error);
        this.errorMessage = 'Signup failed. Please try again.'; // Display a generic error message for now
      }
    },
  },
};
    
</script>


<style>
.investor-signup-form {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  width: 400px;
  margin: 0 auto;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.investor-signup-form h2 {
  margin-bottom: 20px;
  text-align: center;
}

.investor-signup-form label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

.investor-signup-form input[type="text"],
.investor-signup-form input[type="email"],
.investor-signup-form input[type="password"] {
  width: 100%;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 3px;
  margin-bottom: 10px;
}

.investor-signup-form button[type="submit"] {
  background-color: #2c3e50;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 3px;
  cursor: pointer;
}
</style>