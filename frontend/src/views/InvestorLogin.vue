<template>
  <form class="login-form">
    <h2>Investor Login</h2>
    <label for="email">Email:</label>
    <input type="email" id="email" placeholder="Enter your email">
    <label for="password">Password:</label>
    <input type="password" id="password" placeholder="Enter your password">
    <button type="submit">Login</button>
  </form>
</template>

<style>
.login-form { 
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  width: 400px; 
  margin: 0 auto;
  border: 1px solid #ccc;
  border-radius: 5px;
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
input[type="email"],
input[type="password"] {
  width: 100%;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 3px;
  margin-bottom: 10px; 
}
button[type="submit"] {
  background-color: #551a8b;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 3px;
  cursor: pointer;
}
</style>