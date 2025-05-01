<template>
  <div class="flex h-screen">
    <!-- Carousel Section -->
    <div class="w-1/2 bg-[#e2143c] flex items-center justify-center">
      <div class="flex flex-col items-center justify-center h-full w-full">
        <h1 class="text-5xl text-[#E8C2CA] font-pacifico py-4">Find Love Today</h1>

        <div class="w-[500px] h-[600px] rounded-2xl shadow-xl overflow-hidden mb-4">
          <Carousel />
        </div>

       
      </div>
    </div>

    <!-- Login Form Section -->
    <div class="w-1/2 bg-[#E8C2CA] flex flex-col items-center justify-center px-6">
      <div class="bg-white rounded-lg shadow-md w-full max-w-md p-6">
        <h2 class="text-center text-3xl font-bold mb-6 font-pacifico">Jam-Date</h2>
        <form @submit.prevent="login" class="space-y-4">
          <input
            v-model="username"
            type="text"
            placeholder="Username"
            required
            class="w-full px-4 py-2 border border-gray-300 rounded-md"
          />
          <input
            v-model="password"
            type="password"
            placeholder="Password"
            required
            class="w-full px-4 py-2 border border-gray-300 rounded-md"
          />
           <!-- Back Button and Sign In Link -->
        <div class="flex flex-col items-center gap-2">
          
          <p class="text-sm text-rose-500">
            Dont have an account?
            <a href="/register" class="underline font-medium text-pink-600 hover:text-pink-200">Sign up</a>
          </p>
          <button
            type="submit"
            class="w-full bg-rose-600 text-white font-bold py-2 rounded-md hover:bg-rose-800 transition"
          >
            Login
          </button>
          <button
            class="w-full py-2 bg-white text-[#e2143c] rounded-full font-semibold hover:bg-rose-300 transition"
            @click="$router.back?.() || window.history.back()"
          >
            Back
          </button>
        </div>
          
          
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';
import Carousel from '@/components/Carousel.vue';

const username = ref('');
const password = ref('');
const router = useRouter();

const login = async () => {
  try { 
    const res = await axios.post('/api/auth/login', {
      username: username.value,
      password: password.value,
    });
    localStorage.setItem('token', res.data.token);
    localStorage.setItem('user_id', res.data.user.id);
    localStorage.setItem('name', res.data.user.name);
    localStorage.setItem('photo', res.data.user.photo);
    router.push('/home');
  } catch {
    alert('Login failed.');
  }
};
</script>
