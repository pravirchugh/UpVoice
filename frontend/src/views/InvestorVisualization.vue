<template>
<div class="dashboard-link">
      <router-link to="/investor/dashboard" :class="{ active: activeLink === 'Requests received' }" @click="setActiveLink('investor/dashboard')">Requests received</router-link>
    <router-link to="/investor/visualization" :class="{ active: activeLink === 'Visualizations' }" @click="setActiveLink('Visualizations')">Visualizations</router-link>
</div>
  <div class="visualization-container">
    <div id="plotly-graph"></div>
  </div>
</template>

<script>
export default {
  mounted() {
    this.loadPlotly();
  },
  methods: {
    loadPlotly() {
      const script = document.createElement('script');
      script.src = 'https://cdn.plot.ly/plotly-latest.min.js';
      script.async = true;
      script.onload = () => this.plotGraph();
      document.head.appendChild(script);
    },
    plotGraph() {
      const days = Array.from({ length: 30 }, (_, i) => i + 1); // 30 days
      const issues = this.generateRandomData(30); // Generate random data for issues

      const trace = {
        x: days,
        y: issues,
        type: 'scatter',
        mode: 'lines+markers',
        marker: {
          color: 'blue'
        },
        line: {
          color: 'blue'
        }
      };

      const layout = {
        title: 'Prediction of Issues vs Number of Days',
        xaxis: {
          title: 'Number of Days'
        },
        yaxis: {
          title: 'Number of Issues'
        },
        margin: {
          l: 50,
          r: 50,
          b: 50,
          t: 50,
          pad: 4
        },
        autosize: true,
        showlegend: false
      };

      Plotly.newPlot('plotly-graph', [trace], layout);
    },
    generateRandomData(numPoints) {
      return Array.from({ length: numPoints }, () => Math.floor(Math.random() * 10)); // Random number of issues
    }
  }
};
</script>

<style scoped>
.visualization-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 80vh; /* Adjust height as needed */
}

#plotly-graph {
  width: 80%; /* Adjust width as needed */
  height: 80%; /* Adjust height as needed */
}

.dashboard-link {
  display: flex;
  justify-content: center;
  margin-top: 50px; /* Adjust as needed */
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
