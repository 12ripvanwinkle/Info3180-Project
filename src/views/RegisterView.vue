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

    <!-- Register Form Section -->
    <div class="w-1/2 bg-[#E8C2CA] flex flex-col items-center justify-center px-6">
      <div class="bg-white rounded-lg shadow-md w-full max-w-md p-6">
        <h2 class="text-center text-3xl font-bold mb-6 font-pacifico">Jam-Date</h2>
        <form method="POST" enctype="multipart/form-data" @submit.prevent="register" class="space-y-4" id="registrationForm">
          <input
            v-model="formData.username"
            type="text"
            placeholder="Username"
            required
            class="w-full px-4 py-2 border border-gray-300 rounded-md"
          />
          <input
            v-model="formData.email"
            type="email"
            placeholder="Email"
            required
            class="w-full px-4 py-2 border border-gray-300 rounded-md"
          />
          <input
            v-model="formData.name"
            type="text"
            placeholder="Name"
            required
            class="w-full px-4 py-2 border border-gray-300 rounded-md"
          />
          <input
            v-model="formData.password"
            type="password"
            placeholder="Password"
            required
            class="w-full px-4 py-2 border border-gray-300 rounded-md"
          />
          <div class="mb-4">
            <label for="fileInput" class="flex items-center gap-4 p-3 border-2 border-rose-400 bg-white rounded-lg cursor-pointer hover:bg-rose-50 transition">
              <span class="text-rose-500 px-2 py-1 rounded-md font-semibold border border-rose-400 bg-white font-size-3020">Choose Profile Picture</span>
              <span class="text-sm text-gray-600 truncate max-w-[200px]">
                {{ formData.profilePic ? formData.profilePic.name : 'No file chosen' }}
              </span>
              <input
                id="fileInput"
                type="file"
                @change="handleFileChange"
                accept="image/*"
                class="hidden"
              />
            </label>
          </div>

          <div class="flex flex-col items-center gap-2">
            <p class="text-sm text-rose-500">
              Already have an account?
              <a href="/login" class="underline font-medium text-pink-600 hover:text-pink-200">Sign in</a>
            </p>
            <button
              type="submit"
              class="w-full bg-rose-600 text-white font-bold py-2 rounded-md hover:bg-rose-800 transition"
            >
              Register
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
import { useRouter } from 'vue-router';
import Carousel from '@/components/Carousel.vue';

const formData = ref({
  username: '',
  email: '',
  name: '',
  password: '',
  profilePic: null
});

const router = useRouter();

function handleFileChange(event) {
  formData.value.profilePic = event.target.files[0];
}

function register() {
  let registrationForm = document.getElementById('registrationForm');
  const form_data = new FormData(registrationForm);

  form_data.append('username', formData.value.username);
  form_data.append('email', formData.value.email);
  form_data.append('name', formData.value.name);
  form_data.append('password', formData.value.password);
  form_data.append('photo', formData.value.profilePic);

  fetch('/api/register', {
    method: 'POST',
    body: form_data
  })
    .then((response) => {
      if (!response.ok) throw new Error('Could not register');
      return response.json();
    })
    .then((data) => {
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
    .catch((error) => {
      console.error('Error:', error);
    });
}
</script>
