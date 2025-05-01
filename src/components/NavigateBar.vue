<template>
    <nav class="bg-white shadow p-4 flex justify-between items-center sticky top-0 z-50">
      <router-link to="/" class="text-2xl font-bold text-red-600">Jam-Date</router-link>
      
      <div class="flex gap-4 items-center">
        <router-link
          v-if="isLoggedIn"
          :to="`/users/${userId}`"
          class="nav-link text-gray-700 font-medium"
          active-class="font-bold underline"
        >My Profile</router-link>
  
        <router-link
          v-if="isLoggedIn "
          to="/profiles/new"
          class="nav-link text-gray-700 font-medium"
          active-class="font-bold underline"
        >Add Profile</router-link>
  
        <router-link
          v-if="isLoggedIn"
          to="/profiles/favourites"
          class="nav-link text-gray-700 font-medium"
          active-class="font-bold underline"
        >Reports</router-link>
  
        <router-link
          v-if="isLoggedIn"
          to="/logout"
          class="nav-link text-gray-700 font-medium"
          active-class="font-bold underline"
        >Logout</router-link>
      </div>
    </nav>
</template>
  
<script setup>
  import { computed } from 'vue';
  
  const userId = localStorage.getItem('user_id');
  const isLoggedIn = computed(() => !!localStorage.getItem('token'));
</script>
  
<style scoped>
  .nav-link {
    transition: all 0.2s ease-in-out;
  }
  .nav-link:hover {
    color: #dc2626;
  }
</style>
  