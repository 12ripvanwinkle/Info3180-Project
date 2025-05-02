<template>
  <NavigateBar/>
  <div class="min-h-screen bg-gradient-to-br from-green-200 to-green-100 py-10 px-4">
    <div class="max-w-6xl mx-auto text-center mb-10">
      <h1 class="text-4xl font-bold text-green-700" style="font-family: 'Pacifico', cursive;">Match Results</h1>
      <p class="text-gray-600 text-base mt-2">Profiles that best match based on your selected profile</p>
    </div>

    <div v-if="matches.length" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 max-w-6xl mx-auto">
      <div
        v-for="match in matches"
        :key="match.id"
        class="bg-white rounded-2xl shadow-md p-5 hover:shadow-lg transition-shadow duration-300"
      >
        <h3 class="text-xl font-semibold text-green-800 mb-1" style="font-family: 'Pacifico', cursive;">
          {{ match.name || 'Match' }}
        </h3>
        <p class="text-sm text-gray-600 italic mb-2">
          {{ match.biography?.slice(0, 100) }}...
        </p>
        <ul class="text-sm text-gray-700 space-y-1 mb-4">
          <li><span class="font-semibold">Age:</span> {{ match.birth_year }}</li>
          <li><span class="font-semibold">Sex:</span> {{ match.sex }}</li>
          <li><span class="font-semibold">Height:</span> {{ match.height }} in</li>
          <li><span class="font-semibold">Fav Cuisine:</span> {{ match.fav_cuisine }}</li>
        </ul>
        <router-link
          :to="`/profiles/${match.id}`"
          class="text-rose-600 hover:text-rose-800 hover:underline font-medium text-sm"
        >
          View More
        </router-link>
      </div>
    </div>

    <div v-else class="text-center mt-20 text-gray-500">
      <p class="text-lg font-medium">No matches found for this profile.</p>
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
      const res = await axios.get(`/api/profiles/matches/${profile_id}`, {
        headers: { Authorization: `Bearer ${getToken()}` }
      });
      matches.value = res.data;
    } catch (err) {
      console.error('Failed to load matches:', err);
    }
  });
</script>
  