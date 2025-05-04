<template>
  <NavigateBar/>

    <div class="min-h-screen  bg-rose-500 py-10 px-4 text-gray-800">
      <div class="max-w-6xl mx-auto text-center mb-8">
        <h1 class="text-5xl  text-white font-pacifico mb-2">♥ Favourites ♥</h1>
        <p class="text-white font-ubuntu my-4 font-semibold">See who's most loved and your own favourites 🎔</p>
      </div>

      <div class="max-w-3xl mx-auto flex flex-wrap justify-center gap-4 mb-8">
        <label class="font-semibold font-ubuntu text-white">Sort by:</label>
        <select v-model="sortOption" class="border px-3 py-1 rounded shadow" @change="sortLists">
          <option value="name">Name</option>
          <option value="parish">Parish</option>
          <option value="age">Age</option>
        </select>
      </div>

      <section class="max-w-6xl mx-auto mb-12 my-16">
        <h2 class="text-3xl text-white font-pacifico mb-4 ">Top 20 Most Favorited Users</h2>
        <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-6">
          <div v-for="user in sortedTop" :key="user.id" class="bg-gray-100 p-4 rounded shadow text-center">
            <img :src="getPhotoUrl(user.photo)" alt="User" class="w-20 h-20 mx-auto rounded-full mb-2" />
            <h3 class="font-semibold font-ubuntu">{{ user.name }}</h3>
            <p class="text-sm font-ubuntu">{{ user.email }}</p>
          </div>
        </div>
      </section>
      
      <section class="max-w-6xl mx-auto">
        <h2 class="text-3xl text-white font-pacifico  mb-4">Users You Favorited</h2>
        <div v-if="sortedMine.length" class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-6">
          <div v-for="user in sortedMine" :key="user.id" class="bg-gray-100 p-4 rounded shadow text-center">
            <img :src="getPhotoUrl(user.photo)" alt="Fav" class="w-20 h-20 mx-auto rounded-full mb-2" />
            <h3 class="font-semibold font-ubuntu">{{ user.name }}</h3>
            <p class="text-sm font-ubuntu">{{ user.email }}</p>
          </div>
        </div>
        <p v-else class="text-m font-semibold font-ubuntu text-white text-center my-16">You haven’t added anyone to favourites yet.</p>
      </section>
    </div>
</template>
  
<script setup>
  import { ref, onMounted } from 'vue';
  import axios from 'axios';
  import { getToken } from '../utils/auth';
  import NavigateBar from '../components/NavigateBar.vue';
  import defaultProfileImage from '@/assets/Default/noProfile.png';
  
  const topFavorites = ref([]);
  const myFavorites = ref([]);
  const sortedTop = ref([]);
  const sortedMine = ref([]);
  const sortOption = ref('name');
  
  function getPhotoUrl(filename) {
    return `/uploads/${filename}`;
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
      const topRes = await axios.get('/api/users/favorites/20');
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
  