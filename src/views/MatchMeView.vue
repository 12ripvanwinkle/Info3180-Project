<template>
    <NavigateBar/>
    <div class="min-h-screen bg-gradient-to-br from-green-200 to-green-100 py-10 px-4">
      <div class="max-w-6xl mx-auto text-center mb-8">
        <h1 class="text-3xl font-bold text-green-700">Match Results</h1>
        <p class="text-gray-600 mt-2">Profiles that best match based on your selected profile</p>
      </div>
  
      <div v-if="matches.length" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 max-w-6xl mx-auto">
        <div v-for="match in matches" :key="match.id" class="bg-white rounded-lg shadow p-4 text-left">
          <h3 class="text-lg font-bold mb-1">{{ match.name || 'Match' }}</h3>
          <p class="text-sm text-gray-500 mb-2">{{ match.biography?.slice(0, 100) }}...</p>
          <ul class="text-xs text-gray-600 mb-2">
            <li><strong>Age:</strong> {{ match.birth_year }}</li>
            <li><strong>Sex:</strong> {{ match.sex }}</li>
            <li><strong>Height:</strong> {{ match.height }} in</li>
            <li><strong>Fav Cuisine:</strong> {{ match.fav_cuisine }}</li>
          </ul>
          <router-link :to="`/profiles/${match.id}`" class="text-red-600 hover:underline font-semibold text-sm">
            View More
          </router-link>
        </div>
      </div>
  
      <div v-else class="text-center mt-10 text-gray-500">
        <p>No matches found for this profile.</p>
      </div>
    </div>
</template>
  
<script setup>
  import { ref, onMounted } from 'vue';
  import { useRoute } from 'vue-router';
  import axios from 'axios';
  import { getToken } from '../utils/auth';
import NavigateBar from '../components/NavigateBar.vue';
  
  const route = useRoute();
  const matches = ref([]);
  
  onMounted(async () => {
    const profile_id = route.params.profile_id;
    try {
      const res = await axios.get(`http://localhost:5000/api/profiles/matches/${profile_id}`, {
        headers: { Authorization: `Bearer ${getToken()}` }
      });
      matches.value = res.data;
    } catch (err) {
      console.error('Failed to load matches:', err);
    }
  });
</script>
  