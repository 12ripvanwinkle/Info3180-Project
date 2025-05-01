<template>
    <div class="min-h-screen bg-white py-10 px-4 text-gray-800">
      <div class="max-w-6xl mx-auto text-center mb-8">
        <h1 class="text-3xl font-bold text-red-600 mb-2">Favourites Report</h1>
        <p class="text-gray-600">See who's most loved and your own favourites</p>
      </div>

      <div class="max-w-3xl mx-auto flex flex-wrap justify-center gap-4 mb-8">
        <label class="font-semibold">Sort by:</label>
        <select v-model="sortOption" class="border px-3 py-1 rounded shadow" @change="sortLists">
          <option value="name">Name</option>
          <option value="parish">Parish</option>
          <option value="age">Age</option>
        </select>
      </div>

      <section class="max-w-6xl mx-auto mb-12">
        <h2 class="text-xl font-bold mb-4">Top 20 Most Favorited Users</h2>
        <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-6">
          <div v-for="user in sortedTop" :key="user.id" class="bg-gray-100 p-4 rounded shadow text-center">
            <img :src="getPhotoUrl(user.photo)" alt="User" class="w-20 h-20 mx-auto rounded-full mb-2" />
            <h3 class="font-semibold">{{ user.name }}</h3>
            <p class="text-sm text-gray-600">{{ user.email }}</p>
          </div>
        </div>
      </section>
      
      <section class="max-w-6xl mx-auto">
        <h2 class="text-xl font-bold mb-4">Users You Favorited</h2>
        <div v-if="sortedMine.length" class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-6">
          <div v-for="user in sortedMine" :key="user.id" class="bg-gray-100 p-4 rounded shadow text-center">
            <img :src="getPhotoUrl(user.photo)" alt="Fav" class="w-20 h-20 mx-auto rounded-full mb-2" />
            <h3 class="font-semibold">{{ user.name }}</h3>
            <p class="text-sm text-gray-600">{{ user.email }}</p>
          </div>
        </div>
        <p v-else class="text-sm text-gray-500 text-center">You haven’t added anyone to favourites yet.</p>
      </section>
    </div>
</template>
  
<script setup>
  import { ref, onMounted } from 'vue';
  import axios from 'axios';
  import { getToken } from '../utils/auth';
  
  const topFavorites = ref([]);
  const myFavorites = ref([]);
  const sortedTop = ref([]);
  const sortedMine = ref([]);
  const sortOption = ref('name');
  
  function getPhotoUrl(photo) {
    return photo ? `/uploads/${photo}` : '';
  }
  
  function sortLists() {
    const sortKey = sortOption.value;
  
    const sortFn = (a, b) => {
      if (sortKey === 'age') return (a.birth_year || 0) - (b.birth_year || 0);
      return (a[sortKey] || '').toString().localeCompare((b[sortKey] || '').toString());
    };
  
    sortedTop.value = [...topFavorites.value].sort(sortFn);
    sortedMine.value = [...myFavorites.value].sort(sortFn);
  }
  
  onMounted(async () => {
    try {
      // Top N favorites
      const topRes = await axios.get('/api/users/favorities/20');
      topFavorites.value = topRes.data;
      sortedTop.value = topRes.data;
  
      // Current user ID
      const userRes = await axios.get('/api/auth/login', {
        headers: { Authorization: `Bearer ${getToken()}` }
      });
      const userId = userRes.data?.user?.id;
  
      if (userId) {
        const favRes = await axios.get(`/api/users/${userId}/favourites`);
        myFavorites.value = favRes.data;
        sortedMine.value = favRes.data;
      }
    } catch (err) {
      console.error('Failed to fetch reports:', err);
    }
  });
</script>
  