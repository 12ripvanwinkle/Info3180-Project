<template>
    <div class="min-h-screen bg-[#E8C2CA]">
        <!-- Navigation Bar -->
        <NavigateBar />

    
        <!-- Welcome Heading -->
        
        <h1 class="text-3xl font-build text-center text-rose-600 my-12 mb-6 font-pacifico font-semibold">Welcome to Jam-Date</h1>

        <div class="flex justify-center mb-6">
        <router-link to="/profiles/favourites">
            <button
            type="button"
            class="bg-rose-500 text-white font-pacifico px-6 py-2 rounded-lg shadow hover:bg-rose-700 transition duration-300 ease-in-out"
            >
            View Favorites   ➤
            </button>
        </router-link>
        </div>
        <!-- Search Profiles Section -->
         
        <div class="max-w-3xl mx-auto bg-white shadow-md rounded-lg p-6 mb-8">
            <h2 class="text-xl font-regular mb-4 text-gray-700 font-pacifico">Search for your Match</h2>
            <form method="GET" @submit.prevent="searchProfiles" class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <input v-model="search.name" type="text" placeholder="Name" class="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 font-pacifico focus:ring-rose-600"/>
                <input v-model="search.birth_year" type="text" placeholder="Birth Year" class="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 font-pacifico focus:ring-rose-600"/>
                <input v-model="search.sex" type="text" placeholder="Sex" class="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 font-pacifico focus:ring-rose-600"/>
                <input v-model="search.race" type="text" placeholder="Race" class="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 font-pacifico focus:ring-rose-600"/>
                <button type="submit" class="col-span-full bg-rose-500 hover:bg-rose-600 text-white  py-2 rounded-md focus:outline-none focus:ring-2 font-pacifico focus:ring-rose-700">
                    Search
                </button>
            </form>
        </div>

        <hr class="border-t-2 border-dashed border-red-700 max-w-5xl mx-auto mb-10" />

        <!-- Recently Added Profiles Section -->
        <div class="max-w-5xl mx-auto">
            <h2 class="text-3xl my-5  font-pacifico text-rose-600 mb-4">Recently Added Profiles</h2>
            <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-6">
                <div v-for="profile in profiles" :key="profile.id" class="card-animate bg-white p-4 rounded-lg shadow hover:shadow-lg transition-transform duration-300 ease-in-out">
                    <img :src="getPhotoUrl(profile.photo)" alt="Profile Photo" class="w-full h-48 object-cover rounded mb-3" />
                    <h3 class="text-lg font-bold font-ubuntu">{{ profile.name }}</h3>
                    <router-link :to="`/profile/${profile.id}`" class="text-red-600 hover:underline mt-2 inline-block">View More Details</router-link>
                </div>
            </div>
        </div>

        <!-- Search Results Section -->
        <div v-if="searchResults.length" class="max-w-5xl mx-auto mt-10">
            <h2 class="text-xl font-semibold text-gray-700 mb-4">Search Results</h2>
            <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
                <div v-for="profile in searchResults" :key="profile.id" class="card-animate bg-white p-4 rounded-lg shadow hover:shadow-lg transition-transform duration-300 ease-in-out">
                    <img :src="getPhotoUrl(profile.photo)" alt="Profile Photo" class="w-full h-48 object-cover rounded mb-3"/>
                    <h3 class="text-lg font-bold font-ubuntu">{{ profile.name }}</h3>
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
  import NavigateBar from '../components/NavigateBar.vue';
  
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