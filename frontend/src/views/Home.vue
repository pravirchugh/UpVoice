<template>
  <div class="container">
    <div class="home">
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
</template>

<script>
export default {
  name: 'UpVoice',
  data() {
    return {
      env: process.env.NODE_ENV
    }
  }
}
</script>

<style>
.home {
  background-image: url("../assets/home/plane_two.jpg");
  background-size: cover;
  /* Adjusts the background image size to contain within the container */
  background-position: top center;
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
</style>

<script>

</script>

