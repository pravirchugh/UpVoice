 <template>
  <div class="dashboard-nav">
    <router-link to="/citizen/dashboard" :class="{ active: isActive('/citizenDashboard') }">Raise Request</router-link>
    <router-link to="/citizenVisualization" :class="{ active: isActive('/citizenVisualization') }">Visualization</router-link>
  </div>
</template>

<script>
export default {
  methods: {
    isActive(route) {
      return this.$route.path === route;
    }
  }
};
</script>

<style scoped>
.dashboard-nav {
  display: flex;
  align-items: center; /* Align links vertically in the center */
}

.dashboard-nav router-link {
  margin-right: 20px;
  color: #333;
  text-decoration: none;
  transition: color 0.3s ease;
  padding: 30px; /* Adjust padding as needed */
  border-radius: 5px;
}

.dashboard-nav router-link.active {
  color: #007bff; /* Change to your active color */
  background-color: bisque; /* Change to your active background color */
}
</style>