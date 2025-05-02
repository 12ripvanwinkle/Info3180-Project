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
                <select v-model="search.birth_year" class="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 font-pacifico focus:ring-rose-600">
                    <option disabled value="">Select Birth Year</option>
                    <option v-for="year in birthYears" :key="year" :value="year">{{ year }}</option>
                </select>
                <select v-model="search.sex" class="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 font-pacifico focus:ring-rose-600">
                    <option disabled value="">Select Sex</option>
                    <option value="Male">Male</option>
                    <option value="Female">Female</option>
                </select>
                <select v-model="search.race" class="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 font-pacifico focus:ring-rose-600">
                    <option disabled value="">Select Race</option>
                    <option value="Asian">Asian</option>
                    <option value="Black">Black</option>
                    <option value="White">White</option>
                    <option value="Hispanic">Hispanic</option>
                </select> 
                <button type="submit" class="col-span-full bg-rose-500 hover:bg-rose-600 text-white  py-2 rounded-md focus:outline-none focus:ring-2 font-pacifico focus:ring-rose-700">
                    Search
                </button>
            </form>
        </div>

        <hr class="border-t-2 border-dashed border-red-700 max-w-5xl mx-auto mb-10" />

        <!-- Search Results Section -->
        <div v-if="searchResults" class="max-w-5xl mx-auto mt-10">
            <h2 class="text-xl font-semibold text-gray-700 mb-4">Search Results</h2>
            <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
                <div v-for="profile in searchResults" :key="profile.id" class="card-animate bg-white p-4 rounded-lg shadow hover:shadow-lg transition-transform duration-300 ease-in-out">
                    <img :src="getPhotoUrl(profile.user_photo)" alt="Profile Photo" class="w-full h-48 object-cover rounded mb-3"/>
                    <h3 class="text-lg font-bold font-ubuntu">{{ profile.user_name }}</h3>
                    <router-link :to="`/profiles/${profile.id}`" class="text-red-600 hover:underline mt-2 inline-block">View More Details</router-link>
                </div>
            </div>
        </div>

        <!-- Recently Added Profiles Section -->
        <div class="max-w-5xl mx-auto">
            <h2 class="text-3xl my-5  font-pacifico text-rose-600 mb-4">Recently Added Profiles</h2>
            <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-6">
                <div v-for="profile in profiles" :key="profile.id" class="card-animate bg-white p-4 rounded-lg shadow hover:shadow-lg transition-transform duration-300 ease-in-out">
                    <img :src="getPhotoUrl(profile.user_photo)" alt="Profile Photo" class="w-full h-48 object-cover rounded mb-3" />
                    <h3 class="text-lg font-bold font-ubuntu">{{ profile.user_name }}</h3>
                    <router-link :to="`/profiles/${profile.id}`" class="text-red-600 hover:underline mt-2 inline-block">View More Details</router-link>
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
  import { useRouter } from 'vue-router';
  
  const profiles = ref([]);
  const searchResults = ref([]);
  const search = ref({
    name: '',
    birth_year: '',
    sex: '',
    race: ''
  });

  const hasProfile = ref(false);
  const router = useRouter();

  function getPhotoUrl(filename) {
    return `/uploads/${filename}`;
  }

    const currentYear = new Date().getFullYear();
    const minYear = currentYear - 50; // Age 50
    const maxYear = currentYear - 18; // Age 18
    birthYears.value = Array.from({ length: maxYear - minYear + 1 }, (_, i) => minYear + i);


  onMounted(async () => {
    try {
        const res = await axios.get('/api/profiles', {
            headers: {Authorization: `Bearer ${getToken()}`}
        });
        console.log("Profile API response:", res.data);
        profiles.value = res.data.profiles.slice(-4).reverse();

        const userId = parseInt(localStorage.getItem('user_id')); 
        const userProfiles = res.data.profiles.filter(p => p.user_id === userId);

        if (userProfiles.length === 0) {
            alert("You must create a profile before viewing others.");
            router.push('/profiles/new'); 
            return;
        }
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
        console.log(res.data);
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