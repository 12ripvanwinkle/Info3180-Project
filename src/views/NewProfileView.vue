<template>
  <div class="min-h-screen bg-[#E8C2CA]">
    <!-- Navigation Bar -->
    <NavigateBar />

    <div class="max-w-4xl mx-auto bg-white shadow-md rounded-lg p-6 mt-12 mb-8">
      <div class="text-center">
        <h1 class="text-3xl text-rose-600 font-pacifico font-semibold mb-2">Create New Profile</h1>
        <p class="text-rose-400 text-m font-pacifico">Tell us about yourself</p>
      </div>

      <form @submit.prevent="createProfile" class="grid grid-cols-1 md:grid-cols-2 gap-6 mt-8 font-light font-pacifico text-slate-900 text-sm">
        <!-- Left Side -->
        <div class="space-y-3">
          <input v-model="form.description" placeholder="Description" required class="input" />
          <input v-model="form.parish" placeholder="Parish" required class="input" />
          <textarea v-model="form.biography" placeholder="Biography" required class="input h-24"></textarea>
          <input v-model="form.sex" placeholder="Sex" required class="input" />
          <input v-model="form.race" placeholder="Race" required class="input" />
          <input v-model="form.birth_year" type="number" placeholder="Birth Year" required class="input" />
          <input v-model="form.height" type="number" placeholder="Height (inches)" required class="input" />
        </div>

        <!-- Right Side -->
        <div class="space-y-3">
          <input v-model="form.fav_cuisine" placeholder="Favourite Cuisine" required class="input" />
          <input v-model="form.fav_colour" placeholder="Favourite Colour" required class="input" />
          <input v-model="form.fav_school_subject" placeholder="Favourite School Subject" required class="input" />

          <label class="flex items-center gap-3">
            <input type="checkbox" v-model="form.political" />
            <span>Political</span>
          </label>
          <label class="flex items-center gap-3">
            <input type="checkbox" v-model="form.religious" />
            <span>Religious</span>
          </label>
          <label class="flex items-center gap-3">
            <input type="checkbox" v-model="form.family_oriented" />
            <span>Family Oriented</span>
          </label>
        </div>
      </form>

 
      <div class="flex justify-center mt-10">
        <button
          @click="createProfile"
          class="bg-rose-500 hover:bg-rose-600 text-white px-6 py-2 rounded-lg shadow font-pacifico transition duration-300 ease-in-out">
          Create Profile
        </button>
      </div>
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
    @apply w-full px-4 py-2 border border-rose-300 rounded-lg shadow-sm text-sm focus:outline-none focus:ring-2 focus:ring-rose-400;
    font-family: 'Pacifico', cursive;
  }
  </style>
  