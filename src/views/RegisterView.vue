<template>
    <div class="form-container">
      <nav class="nav">
        <h1 class="logo">Jam-Date</h1>
        <router-link to="/" class="nav-link">Home</router-link>
        <router-link to="/login" class="nav-link">Login</router-link>
        <router-link to="/register" class="nav-link">Register</router-link>
      </nav>
      <div class="form-box">
        <h2>Register</h2>
        <form method = "POST" enctype="multipart/form-data" @submit.prevent="register" id="registrationForm">
          <input v-model="formData.username" type="text" placeholder="Username" required />
          <input v-model="formData.email" type="email" placeholder="Email" required />
          <input v-model="formData.name" type="text" placeholder="Name" required />
          <input v-model="formData.password" type="password" placeholder="Password" required />
          <input type="file" @change="handleFileChange"/>
          <button type="submit">Register</button>
        </form>
      </div>
    </div>
</template>
  
<script setup>
  import { ref, onMounted } from 'vue';
  import { useRouter } from 'vue-router';
  const formData = ref({
    username: '',
    email: '',
    name: '',
    password: '',
    profilePic: null
  });

  const router = useRouter();
  
  function register() {
    let registrationForm = document.getElementById('registrationForm');
    let form_data = new FormData(registrationForm);

    form_data.append('username', formData.username);
    form_data.append('email', formData.email);
    form_data.append('name', formData.name);
    form_data.append('password', formData.password);
    form_data.append('profilePic', formData.profilePic);

    fetch('/api/register', {
      method: 'POST',
      body: form_data
    })
    .then(function (response) {
      if (!response.ok){
        throw new Error("Could not register");
      }
      return response.json
    })
    .then(function (data) {
      console.log('Success:', data);
      formData.value = {
        username: '',
        email: '',
        name: '',
        password: '',
        profilePic: null
      };
      router.push('/login');
    })
    .catch(function (error) {
      console.error('Error:', error)
    });
  }; 
  function handleFileChange(event) {
        formData.profilePic = event.target.files[0];
}
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
    background-color: #dc2626;
    color: white;
    border: none;
    border-radius: 4px;
    font-weight: bold;
    cursor: pointer;
  }
</style>