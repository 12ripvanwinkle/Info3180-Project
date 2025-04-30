<template>
    <div class="form-container">
      <nav class="nav">
        <h1 class="logo">Jam-Date</h1>
        <router-link to="/" class="nav-link">Home</router-link>
        <router-link to="/login" class="nav-link">Login</router-link>
        <router-link to="/register" class="nav-link">Register</router-link>
      </nav>
      <div class="form-box">
        <h2>Jam-Date</h2>
        <form @submit.prevent="login">
          <input v-model="username" type="text" placeholder="Email" required />
          <input v-model="password" type="password" placeholder="Password" required />
          <button type="submit">Login</button>
        </form>
      </div>
    </div>
</template>
  
<script setup>
  import { ref } from 'vue';
  import axios from 'axios';
  import { useRouter } from 'vue-router';
  
  const username = ref('');
  const password = ref('');
  const router = useRouter();
  
  const login = async () => {
    try {
      const res = await axios.post('/api/auth/login', { username: username.value, password: password.value });
      localStorage.setItem('token', res.data.token);
      router.push('/home');
    } catch {
      alert('Login failed.');
    }
  };
</script>
  
<style scoped lang="css">
  .form-container {
    display: flex;
    align-items: center;
    justify-content: center;
    min-height: 100vh;
    background-color: #f4f4f4;
  }
  .nav {
  display: flex;
  justify-content: flex-end;
  padding: 1rem 2rem;
  gap: 1.5rem;
  background-color: rgba(0, 0, 0, 0.6); 
  position: absolute;
  width: 100%;
  top: 0;
  z-index: 10;
}

.nav-link {
  color: white;
  text-decoration: none;
  font-weight: bold;
}

.nav-link:hover {
  text-decoration: underline;
}
  
  .form-box {
    background: white;
    padding: 2rem;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    width: 100%;
    max-width: 400px;
  }
  
  h2 {
    margin-bottom: 1.5rem;
    text-align: center;
  }
  
  input {
    display: block;
    width: 100%;
    padding: 0.75rem;
    margin-bottom: 1rem;
    border-radius: 4px;
    border: 1px solid #ccc;
  }
  
  button {
    width: 100%;
    padding: 0.75rem;
    background-color: #4f46e5;
    color: white;
    border: none;
    border-radius: 4px;
    font-weight: bold;
    cursor: pointer;
  }
</style>