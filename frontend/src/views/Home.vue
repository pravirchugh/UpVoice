<template>
  <div class="container">
    <!-- Separate div for background image -->
    <div class="background" ref="background"></div>
    <div class="home" ref="home">
      <div class="title">
        <h1>Raise your voices</h1>
      </div>
      <div class="content">
        <p>Giving Citizens a new voice! The right to inform stakeholders on
          if the business practices of a company are being followed or not - can view this through an environmental lens
          as well.
        </p>
      </div>
    </div>
  </div>
  <div class="info">
    <img src="../assets/home/megaphone.jpg" alt="megaphone image" class="mega">
    <div class="info-body">
      <h1>What we do</h1>
       <p>If you are a citizen - Raise issues which have been ignored by  </p>
       <p>If you are a investor - See where your organization is lacking, optemize profits!</p>
    </div>
  </div>
  <div class="footer">
    <p>&copy; 2024 UpVoice. LAHacks 24'.</p>
  </div>
</template>

<script>
export default {
  name: 'home',
  mounted() {
    // Apply animation when component is mounted
    this.animateBackground();
  },
  methods: {
    animateBackground() {
      console.log(this.$refs.background);
      // Apply CSS animation to background image
      this.$refs.background.style.animation = 'slideFromBottom 2s forwards';
    }
  }
}
</script>

<style>
.container {
  position: relative;
}

.info{
  display: flex;
}

.mega{
  width: 800px;
}

.background {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: url("../assets/home/plane_two.jpg");
  background-size: contain;
  background-repeat: no-repeat;
  background-position: top center;
  animation: slideFromBottom 2s forwards;
  z-index: -1; /* Set z-index to -1 to position the background behind other content */
}

.home {
  min-height: 100vh;
  color: #2c3e50;
  margin-top: 100px;
}

.content {
  width: 500px;
  margin-left: 50px;
}

.content p {
  font-size: 20px;
  text-align: justify;
}

h1 {
  margin-left: 50px;
}

.footer {
  border-top: 0.5px solid black;
  text-align: center;
  padding: 20px 0;
  background-color: #f8f9fa;
  color: #6c757d;
}

@keyframes slideFromBottom {
  from {
    transform: translateY(100%);
  }
  to {
    transform: translateY(0);
  }
}
</style>
