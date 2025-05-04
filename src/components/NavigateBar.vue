<template>
  <nav class="bg-[#e2143c] shadow p-4 flex justify-between items-center sticky top-0 z-50">
    <router-link to="/home" class="text-2xl font-bold text-white font-pacifico">Jam-Date</router-link>

    <div class="flex gap-4 items-center relative">

  
      



      <!--Profile Section-->
      <div class="relative" @click="toggleDropdown">
        <div class="flex items-center cursor-pointer">
          <img
            :src="getPhotoUrl(user.photo)" alt="Profile" class="w-10 h-10 rounded-full object-cover "/>
          <span class="ml-2 text-white font-[500]">{{ user.name || 'testuser' }}</span>
        </div>
        <div
          v-if="showDropdown"
          class="absolute right-0 mt-2 w-40 bg-white rounded shadow-md z-50"
        >
          <router-link :to="`/users/${userId}`"class="block px-4 py-2 font-semibold hover:bg-gray-100 text-gray-700 font-ubuntu" active-class="font-bold underline">My Profile</router-link>
          <router-link to="/profiles/new" class="block px-4 py-2 font-semibold hover:bg-gray-100 text-gray-700 font-ubuntu" active-class="font-bold underline" >Add Profile</router-link>
          <router-link to="/logout" class="block px-4 py-2 font-semibold hover:bg-gray-100 text-gray-700 font-ubuntu" active-class="font-bold underline">Logout</router-link>
        </div>
      </div>
    </div>
  </nav>
</template>

<script setup>
 import { ref, onMounted } from 'vue';
 const userId = localStorage.getItem('user_id');
 const showDropdown = ref(false);
 import defaultProfileImage from '@/assets/Default/noProfile.png'; 

 const user = ref({
    name: '',
    photo: null,
  });

  onMounted(() => {
    const storedName = localStorage.getItem('name');
    const storedPhoto = localStorage.getItem('photo');

    user.value.name = storedName || 'Anonymous';
    user.value.photo = storedPhoto || '';
  });

  function toggleDropdown() {
    showDropdown.value = !showDropdown.value;
  }

  function getPhotoUrl(filename) {
        return `/uploads/${filename}`;
    }
</script>

<style scoped>
  .nav-link {
    transition: all 0.2s ease-in-out;
  }
  .nav-link:hover {
    color: #dc2626;
  }
</style>
