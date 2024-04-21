<template>
  <!-- <div> -->
  <div class="dashboard-link">
      <router-link to="/citizen/dashboard" :class="{ active: activeLink === 'Requests raised' }" @click="setActiveLink('citizens/dashboard')">Requests received</router-link>
    <router-link to="/citizen/visualization" :class="{ active: activeLink === 'Visualizations' }" @click="setActiveLink('Visualizations')">Visualizations</router-link>
</div>
  <div class="form-container">
    <h2>Raise your voice</h2>
    <div class="form-row">
      <label for="category">Category:</label>
      <Dropdown :options="categoryOptions" v-model="selectedCategory" placeholder="Select a category"
        @change="onCategoryChange" />
    </div>
    <div class="form-row">
      <label for="company">Choose company:</label>
      <Dropdown :options="companyOptions" v-model="selectedCompany" placeholder="Select a company" />
    </div>
    <div class="form-row">
      <label for="issue">Issue:</label>
      <Textarea id="issue" style="width: 100%; border-radius: 6px; border-color: #cbd5e1; padding: 5px;" v-model="issue" rows="5" :autoResize="true" />
    </div>
    <!-- <div class="form-row">
      <label for="emailPrompt">Email prompt:</label>
      <Textarea id="emailPrompt" v-model="emailPrompt" disabled />
    </div> -->
    <div class="form-row">
      <Button label="Send" @click="submitForm" />
    </div>
  </div>
</template>

<script>

import DashboardNav from '../components/DashboardNav.vue'; 
import citizenDashboardService from '../services/CitizenDashboardService';

export default {
  components: {
    DashboardNav
  },
  methods: {
    async fetchCompanies() {
      try {
        const companies = await citizenDashboardService.fetchCompanies();
        console.log(companies);
      } catch (error) {
        console.log(error);
      }
    },
    async fetchCompanyCategories() {
      try {
        const categories = await citizenDashboardService.fetchCompanyCategories();
        console.log(categories);
      } catch (error) {
        console.log(error);
      }
    }
  },
  mounted() {
    this.fetchCompanies()
    this.fetchCompanyCategories()
  }
};
</script>

<style scoped>
.form-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  width: 400px;
  margin: 0 auto;
  border: 1px solid #ccc;
  border-radius: 5px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.form-row {
  width: 100%;
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

.p-dropdown {
  width: 100%;
  margin-bottom: 15px;
}

.p-textarea {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  margin-bottom: 15px;
}

.p-button {
  width: 100%;
  background-color: #551a8b;
  color: white;
  padding: 12px 24px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.p-button:hover {
  background-color: #470f71;
}


.dashboard-link {
  display: flex;
  justify-content: center;
  margin-top: 50px; /* Adjust as needed */
  margin-bottom: 20px;
}

.dashboard-link a {
  margin: 0 10px;
  padding: 10px 20px;
  text-decoration: none;
  border-radius: 5px;
  background-color: #551a8b; /* Change color as needed */
  color: #fff;
}

.dashboard-link a.active {
  background-color: #551a8b; /* Change color for active link */
}


</style>