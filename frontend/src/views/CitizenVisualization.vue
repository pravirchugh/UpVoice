<template>
    <div class="dashboard-link">
      <router-link to="/citizen/dashboard" :class="{ active: activeLink === 'Requests raised' }" @click="setActiveLink('citizens/dashboard')">Requests received</router-link>
      <router-link to="/citizen/visualization" :class="{ active: activeLink === 'Visualizations' }" @click="setActiveLink('Visualizations')">Visualizations</router-link>
    </div>
    <!-- <h1>Visualization</h1> -->
      <div class="chart-container">
      <canvas ref="myChart"></canvas>
    </div>
</template>

<script>
import Chart from 'chart.js/auto';
export default {
  data() {
    return {
      activeLink: 'Requests raised',
      chartData: {
        labels: ['Request 1', 'Request 2', 'Request 3', 'Request 4', 'Request 5'],
        datasets: [
          {
            label: 'Raised Date',
            backgroundColor: 'rgba(255, 99, 132, 0.2)',
            borderColor: 'rgba(255, 99, 132, 1)',
            borderWidth: 1,
            data: [10, 20, 15, 25, 18] // Sample data for raised date
          },
          {
            label: 'Completed Date',
            backgroundColor: 'rgba(54, 162, 235, 0.2)',
            borderColor: 'rgba(54, 162, 235, 1)',
            borderWidth: 1,
            data: [5, 15, 10, 20, 12] // Sample data for completed date
          }
        ]
      },
      chartOptions: {
        scales: {
          y: {
            beginAtZero: true
          }
        }
      },
      myChart: null
    };
  },
  mounted() {
    this.renderChart();
  },
  methods: {
    setActiveLink(link) {
      this.activeLink = link;
    },
    renderChart() {
      this.myChart = new Chart(this.$refs.myChart, {
        type: 'bar',
        data: this.chartData,
        options: this.chartOptions
      });
    }
  }
};
</script>


<style scoped>

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

.chart-container {
  width: 80%;
  margin: 0 auto;
}

</style>