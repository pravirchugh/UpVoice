<template>
  <nav class="navbar">
    <div class="navbar-brand">
      <a href="/" class="navbar-item">UpVoice</a>
    </div>
    <div class="navbar-menu">
      <div class="navbar-end">
        <!-- Signup and Login Links -->
        <router-link to="/signup" class="navbar-item">Signup</router-link>
        <router-link to="/login" class="navbar-item">Login</router-link>
        <router-link to="/dashboard/citizen" class="navbar-item">Citizen dashboard</router-link>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'Navbar'
}
</script>

<style scoped>

.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
}

.navbar-brand {
  font-weight: bold;
  font-size: 40px;
  margin-left: 15px ;
}

.navbar-menu {
  display: flex;
}

.navbar-end {
  margin-left: auto;
}

.navbar-item {
  margin-left: 1rem;
  text-decoration: none;
}
</style>