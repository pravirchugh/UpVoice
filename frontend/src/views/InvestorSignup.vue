<template>
  <form class="investor-signup-form" @submit.prevent="handleSubmit">
    <h2>Investor Sign Up</h2>

    <div class="flex flex-column gap-2" style="width: 100%;margin: 10px 0px;">
      <label for="name">Name</label>
      <InputText id="name" v-model="name" style="width: 100%;" />
    </div>

    <div class="flex flex-column gap-2" style="width: 100%;margin: 10px 0px;">
      <label for="companyName">Name</label>
      <InputText id="companyName" v-model="companyName" style="width: 100%;" />
    </div>

    <div class="flex flex-column gap-2" style="width: 100%;margin: 10px 0px;">
      <label for="email">Email</label>
      <InputText id="email" v-model="email" style="width: 100%;" />
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
      @click="handleSubmit"
      style="padding: 15px; width: 60%; font-size: 18px; border-radius: 6px; text-transform: uppercase;">
      <span style="text-align: center; width: 100%;">
        SignUp
      </span>
    </Button>
    <!-- <button type="submit">Sign Up</button> -->
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
  background-color: #551a8b;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 3px;
  cursor: pointer;
}
</style>