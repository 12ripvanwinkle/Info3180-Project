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
        <select v-model="form.sex" required class="input">
          <option disabled value="">Select Sex</option>
          <option value="Male">Male</option>
          <option value="Female">Female</option>
        </select>
        <select v-model="form.race" required class="input">
          <option disabled value="">Select Race</option>
          <option value="Asian">Asian</option>
          <option value="Black">Black</option>
          <option value="White">White</option>
          <option value="Hispanic">Hispanic</option>
        </select>
        <select v-model="form.birth_year" required class="input">
          <option disabled value="">Select Birth Year</option>
          <option v-for="year in birthYears" :key="year" :value="year">{{ year }}</option>
        </select>
          <select v-model="form.height" required class="input">
            <option disabled value="">Select Height</option>
            <option value="<4ft">Less than 4ft</option>
            <option value="4ft">4ft</option>
            <option value="4ft 1in">4ft 1in</option>
            <option value="4ft 2in">4ft 2in</option>
            <option value="4ft 3in">4ft 3in</option>
            <option value="4ft 4in">4ft 4in</option>
            <option value="4ft 5in">4ft 5in</option>
            <option value="4ft 6in">4ft 6in</option>
            <option value="4ft 7in">4ft 7in</option>
            <option value="4ft 8in">4ft 8in</option>
            <option value="4ft 9in">4ft 9in</option>
            <option value="4ft 10in">4ft 10in</option>
            <option value="4ft 11in">4ft 11in</option>
            <option value="5ft">5ft</option>
            <option value="5ft 1in">5ft 1in</option>
            <option value="5ft 2in">5ft 2in</option>
            <option value="5ft 3in">5ft 3in</option>
            <option value="5ft 4in">5ft 4in</option>
            <option value="5ft 5in">5ft 5in</option>
            <option value="5ft 6in">5ft 6in</option>
            <option value="5ft 7in">5ft 7in</option>
            <option value="5ft 8in">5ft 8in</option>
            <option value="5ft 9in">5ft 9in</option>
            <option value="5ft 10in">5ft 10in</option>
            <option value="5ft 11in">5ft 11in</option>
            <option value="6ft">6ft</option>
            <option value="6ft 1in">6ft 1in</option>
            <option value="6ft 2in">6ft 2in</option>
            <option value="6ft 3in">6ft 3in</option>
            <option value="6ft 4in">6ft 4in</option>
            <option value="6ft 5in">6ft 5in</option>
            <option value="6ft 6in">6ft 6in</option>
            <option value="6ft 7in">6ft 7in</option>
            <option value="6ft 8in">6ft 8in</option>
            <option value="6ft 9in">6ft 9in</option>
            <option value="6ft 10in">6ft 10in</option>
            <option value="6ft 11in">6ft 11in</option>
            <option value="7ft">7ft</option>
            <option value="7ft+">7ft+</option>
          </select>
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
  const birthYears = ref([]);
  
  const currentYear = new Date().getFullYear();
  const minYear = currentYear - 50; 
  const maxYear = currentYear - 18; 
  birthYears.value = Array.from({ length: maxYear - minYear + 1 }, (_, i) => minYear + i);

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
