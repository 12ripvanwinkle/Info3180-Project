<template>
    <div class="min-h-screen bg-gray-100">
        <nav class="bg-gray-800 text-white px-6 py-3 flex justify-between items-center">
            <div class="text-xl font-bold">Jam<span class="text-yellow-400">+Date</span></div>
            <div class="space-x-4">
                <router-link to="/logout">
                    <button class="hover:underline">Logout</button>
                </router-link>
            </div>
        </nav>
        <div class="bg-yellow-400 px-6 py-2 text-sm font-medium">
             <router-link to="/users/user_id">
                <button class="mx-1">My Profile</button> 
             </router-link>
        </div>
        <h1 class="text-3xl font-build text-center text-red-600 mb-6">Welcome to Jam-Date</h1>
        <div class="max-w-3xl max-auto bg-white shadow-md rounded-lg p-6 mb-8">
            <h2 class="text-xl font-semibold mb-4 text-gray-700">Search Profiles</h2>
            <form method="GET" @submit.prevent="searchProfiles" class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <input v-model="search.name" type="text" placeholder="Name" class="input"/>
                <input v-model="search.birth_year" type="text" placeholder="Birth Year" class="input"/>
                <input v-model="search.sex" type="text" placeholder="Sex" class="input"/>
                <input v-model="search.race" type="text" placeholder="Race" class="input"/>
                <button type="submit" class="col-span-full bg-red-600 hover:bg-red-700 text-white font-bold py-2 rounded">Search</button>
            </form>
        </div>
        <div class="max-w-5xl mx-auto">
            <h2 class="text-xl font-semibold text-gray-700 mb-4">Recently Added Profiles</h2>
            <div class="grid gird-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-6">
                <div v-for="profile in profiles" :key="profile.id" class="bg-white p-4 rounded-lg shadow hover:shadow-lg">
                    <img :src="getPhotoUrl(profile.photo)" alt="Profile Photo" class="w-full h-48 object-cover rounded mb-3"/>
                    <h3 class="text-lg font-bold">{{ profile.name }}</h3>
                    <router-link :to="`/profile/${profile.id}`" class="text-red-600 hover:underline mt-2 inline-block">View More Details</router-link>
                </div>
            </div>
        </div>
        <div v-if="searchResults.length" class="max-w-5xl mx-auto mt-10">
            <h2 class="text-xl font-semibold text-grey-700 mb-4">Search Results</h2>
            <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
                <div v-for="profile in searchResults" :key="profile.id" class="bg-white p-4 rounded-lg shadow hover:shadow-lg">
                    <img :src="getPhotoUrl(profile.photo)" alt="Profile Photo" class="w-full h-48 object-cover rounded mb-3"/>
                    <h3 class="text-lg font-bold">{{ profile.name }}</h3>
                    <router-link :to="`/profile/${profile.id}`" class="text-red-600 hover:underline mt-2 inline-block">View More Details</router-link>
                </div>
            </div>
        </div>
    </div>
  </template>
  
  <script setup>
  import axios from 'axios';
  import { getToken } from '../utils/auth';
  import { ref, onMounted } from 'vue';
  
  const profiles = ref([]);
  const searchResults = ref([]);
  const search = ref({
    name: '',
    birth_year: '',
    sex: '',
    race: ''
  });

  function getPhotoUrl(filename) {
    return `/uploads/${filename}`;
  }

  onMounted(async () => {
    try {
        const res = await axios.get('/api/profiles', {
            headers: {Authorization: `Bearer ${getToken()}`}
        });
        console.log("Profile API response:", res.data);
        profiles.value = res.data.profiles.slice(-4).reverse();
    }
    catch (error){
        console.error('Error:', error);
    }
});

    async function searchProfiles() {
        try {
            const res = await axios.get('/api/search', {
            headers: { Authorization: `Bearer ${getToken()}`},
            params: search.value
        });
        searchResults.value = res.data;
        }
        catch (error) {
            console.error('Error:', error);
        }
    }
</script>

<style scoped>
.input {
    padding: 0.5rem;
    border: 1px solid #ccc;
    border-radius:0.375rem;
    width: 100%;
}
</style>