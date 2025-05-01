<template>
    <NavigateBar/>

    <div class="min-h-screen max-h-screen overflow-y-auto bg-gray-50 py-12 px-4">
      <div class="max-w-2xl mx-auto bg-white rounded-lg shadow-lg p-6">
        <h1 class="text-2xl font-bold text-center mb-6 text-red-600">Create New Profile</h1>
        <form @submit.prevent="createProfile" class="grid grid-cols-1 gap-4">
          <input v-model="form.description" placeholder="Description" required class="input" />
          <input v-model="form.parish" placeholder="Parish" required class="input" />
          <textarea v-model="form.biography" placeholder="Biography" required class="input"></textarea>
          <input v-model="form.sex" placeholder="Sex" required class="input" />
          <input v-model="form.race" placeholder="Race" required class="input" />
          <input v-model="form.birth_year" type="number" placeholder="Birth Year" required class="input" />
          <input v-model="form.height" type="number" placeholder="Height (inches)" required class="input" />
          <input v-model="form.fav_cuisine" placeholder="Favourite Cuisine" required class="input" />
          <input v-model="form.fav_colour" placeholder="Favourite Colour" required class="input" />
          <input v-model="form.fav_school_subject" placeholder="Fav School Subject" required class="input" />
          <label class="flex items-center gap-2">
            <input type="checkbox" v-model="form.political" /> Political
          </label>
          <label class="flex items-center gap-2">
            <input type="checkbox" v-model="form.religious" /> Religious
          </label>
          <label class="flex items-center gap-2">
            <input type="checkbox" v-model="form.family_oriented" /> Family Oriented
          </label>
  
          <button type="submit" class="mt-4 bg-red-600 hover:bg-red-700 text-white py-2 px-4 rounded">
            Create Profile
          </button>
        </form>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import axios from 'axios';
  import { useRouter } from 'vue-router';
  import { getToken } from '../utils/auth';
  import NavigateBar from '../components/NavigateBar.vue';
  
  const router = useRouter();
  
  const form = ref({
    description: '',
    parish: '',
    biography: '',
    sex: '',
    race: '',
    birth_year: '',
    height: '',
    fav_cuisine: '',
    fav_colour: '',
    fav_school_subject: '',
    political: false,
    religious: false,
    family_oriented: false
  });
  
  const createProfile = async () => {
    try {
      const res = await axios.post('/api/profiles', form.value, {
        headers: { Authorization: `Bearer ${getToken()}` }
      });
      alert('Profile created successfully!');
      router.push('/users/:user_id');
    } catch (err) {
      console.error('Error creating profile:', err);
      alert('Error: ' + (err.response?.data?.error || 'Something went wrong.'));
    }
  };
  </script>
  
  <style scoped>
  .input {
    padding: 0.75rem;
    border: 1px solid #ddd;
    border-radius: 0.375rem;
    width: 100%;
  }
  </style>
  