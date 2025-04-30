<template>
    <div class="card">
        <h3>{{ profile.name }}</h3>
        <p>{{ profile.sex }}, {{ profile.race }}</p>
        <router-link :to="`/profiles/${profile.id}`">View More Details</router-link>
        <button @click="favourite">❤️ Favourite</button>
    </div>
</template>
  
<script setup>
  import axios from 'axios';
  const props = defineProps(['profile']);
  
  const favourite = async () => {
    const token = localStorage.getItem('token');
    await axios.post(`/profiles/${props.profile.user_id}/favourite`, {}, {
      headers: { Authorization: `Bearer ${token}` }
    });
    alert("Added to favourites!");
  };
</script>

<style scoped>
</style>
  