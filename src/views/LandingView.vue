<template>
  <div class="flex flex-col h-screen font-sans">
    <!-- Hero Section -->
    <div class="h-1/2 bg-cover bg-center relative text-white" style="background-image: url('@/assets/hero-group.jpg')">
       <!-- Navbar  -->
      <nav class="flex justify-end items-center gap-6 p-4 bg-black/60 absolute w-full top-0 z-10">
        <h1 class="text-xl font-bold mr-auto">Jam-Date</h1>
        <router-link to="/" class="text-white font-semibold hover:underline">Home</router-link>
        <router-link to="/login" class="text-white font-semibold hover:underline">Login</router-link>
        <router-link to="/register" class="text-white font-semibold hover:underline">Register</router-link>
      </nav>

      <!-- Hero Overlay -->
      <div class="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 bg-black/65 p-8 rounded-lg text-center">
        <h1 class="text-4xl sm:text-3xl font-bold mb-2">Find Your Match on Jam-Date</h1>
        <p class="text-lg text-gray-200">Connect with people who vibe with you.</p>
      </div>
    </div>

    <!-- Image carousel Section -->
     <div class = "flex flex-row justify-center items-center">
      <div to = '/register' class = "btn-4 bg-gray-100 flex items-center justify-center">Register</div>
     </div>
     
    <div class="overflow-hidden w-full bg-white py-6">
    <div
      ref="track"
      class="flex gap-4 animate-scroll whitespace-nowrap"
    >
      <div
        v-for="(image, index) in images"
        :key="index"
        class="w-40 h-40 rounded-xl overflow-hidden shadow-md flex-shrink-0"
      >
        <img :src="image" class="object-cover w-full h-full" />
      </div>
      <!-- Duplicate images for seamless scroll -->
      <div
        v-for="(image, index) in images"
        :key="'repeat-' + index"
        class="w-40 h-40 rounded-xl overflow-hidden shadow-md flex-shrink-0"
      >
        <img :src="image" class="object-cover w-full h-full" />
      </div>
    </div>
  </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';

const imageModules = import.meta.glob('@/assets/Sample/*.{jpg,png,webp}', { eager: true });
const images = Object.values(imageModules).map((mod) => mod.default);

const currentImage = ref(0);
let interval;

onMounted(() => {
  interval = setInterval(() => {
    currentImage.value = (currentImage.value + 1) % images.length;
  }, 3000);
});
onUnmounted(() => {
  clearInterval(interval);
});
</script>

<style scoped>
@keyframes scroll {
  0% {
    transform: translateX(0%);
  }
  100% {
    transform: translateX(-50%);
  }
}

.animate-scroll {
  animation: scroll 20s linear infinite;
}

</style>
