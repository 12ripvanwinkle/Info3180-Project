<template>
     <!-- Navbar -->
    <NavigateBar />

    

    <!-- User Profile Header -->
    <div class="min-h-screen  py-10 px-4 text-gray-800">
      <!--New Profile Button-->
          <router-link to="/profiles/new"class="absolute top-4 right-4 bg-rose-500 hover:bg-rose-600 text-white font-bold py-2 px-4 rounded shadow">
            Create Profile
          </router-link>
      <div class = "bg-white shadow-md rounded-lg p-6 mb-8">
        
      <div class="max-w-4xl mx-auto text-center mb-10">
        <img :src="getPhotoUrl(user.photo)" alt="Profile" class="w-32 h-32 rounded-full mx-auto mb-4 shadow-lg border-4 border-white" />
        <h1 class="text-5xl text-center text-rose-600 font-pacifico mb-4">{{ user.name}}</h1>
        <p class="text-center text-gray-600 font-ubuntu my-4 font-semibold">{{ user.username }}</p>
      </div>



    <!-- Profiles Section -->
      <section class="max-w-6xl mx-auto mb-10"> 
        <h2 class="text-4xl text-rose-500 font-pacifico mb-4">My Profiles</h2>
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
          <div v-for="profile in myProfiles" :key="profile.id" class="bg-white p-4 rounded shadow">
            <img :src="getPhotoUrl(profile.user_photo)" alt="Profile Photo" class="w-full h-48 object-cover rounded mb-3" />
            <h3 class="font-bold text-lg mb-1">{{ user.name }}</h3>
            <p class="text-sm text-gray-600 font-ubuntu mb-2">{{ profile.biography.slice(0, 100) }}...</p>
            <div class="flex justify-between items-center">
              <router-link :to="`/profiles/${profile.id}`" class="text-sm text-blue-600 font-spacegrotesk hover:underline">Show More Details </router-link>
              <router-link :to="`/profiles/${profile.id}/matches`" class="bg-rose-400 hover:bg-rose-500 text-white px-3 py-1 font-spacegrotesk rounded text-sm"> Match Me  </router-link>
            </div>
          </div>
        </div>
      </section>
      <section class="max-w-6xl mx-auto">
        <h2 class="text-4xl text-rose-500 font-pacifico mb-4">Users I Favorited</h2>
        <div v-if="favourites.length" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
          <div v-for="fav in favourites" :key="fav.id" class="bg-white p-4 rounded shadow text-center">
            <img :src="getPhotoUrl(fav.photo)" alt="Fav User" class="w-24 h-24 rounded-full mx-auto mb-2 border" />
            <h3 class="text-lg font-bold">{{ fav.name }}</h3>
            <p class="text-sm text-gray-500">{{ fav.email }}</p>
          </div>
        </div>
        <p v-else class="text-sm text-gray-500">You haven't favorited any users yet.</p>
      </section>
    </div>
    </div>
  </template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import axios from 'axios';
import { getToken } from '../utils/auth';
import NavigateBar from '../components/NavigateBar.vue';
import defaultProfileImage from '@/assets/Default/noProfile.png';

const route = useRoute();
const user = ref({});
const myProfiles = ref([]);
const favourites = ref([]);

function getPhotoUrl(filename) {
        if (!filename || filename === 'undefined') {
             return defaultProfileImage;
        }
        if (filename.startsWith('http://') || filename.startsWith('https://')) {
            return filename;
        }
        return `/static/uploads/${filename}`;
}
onMounted(async () => {
    try{
        const userId = parseInt(localStorage.getItem('user_id'));
        const userRes = await axios.get(`/api/users/${userId}`);
        user.value = userRes.data;

        const profileRes = await axios.get(`/api/profiles`, {
            headers: {Authorization: `Bearer ${getToken()}` }
        });
        myProfiles.value = profileRes.data.profiles.filter(p => p.user_id === parseInt(userId));
        const favRes = await axios.get(`/api/users/${userId}/favourites`)
        favourites.value = favRes.data;
    }
    catch (error) {
        console.error('Error:', error);
    }
});
</script>

<style scoped>
</style>