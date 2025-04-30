<template>
  <div class="flex flex-col h-screen font-sans">
    <!-- Hero Section -->
    <div class="h-1/2 bg-[#e2143c] bg-cover bg-center relative text-white" >
        
        <!-- Welcome Logo -->
        <div class="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 text-center">
          <h1 class="text-7xl text-white-600 font-pacifico py-4">
                          Jam-Date
          </h1>
          <p class="text-lg text-white-200 font-spacegrotesk">Connect with people who vibe with you.</p>
        </div>
      </div>

      


      <!-- bottom half -->
      <div class="h-1/2 bg-[#E8C2CA] p-8">

        <!-- Login and Registration Button Section -->
        <div class = "flex flex-row justify-center items-center my-auto">
          <router-link to="/login">
              <button type="button" class="bg-rose-500 font-ubuntu-regular text-white text-medium leading-6 font-bold py-2 px-12 rounded-lg">Login</button>
          </router-link>
          <router-link to="/register">
              <button type= "button" class="bg-rose-500 font-ubuntu-regular text-white text-medium leading-6 font-bold py-2 px-12 rounded-lg ml-4">Register</button>
          </router-link>
        </div>

        <!-- Image carousel Section -->
        <div class="overflow-hidden w-full  py-6">
        <div ref="track" class="flex gap-4 animate-scroll whitespace-nowrap">
          <div
            v-for="(image, index) in images"
            :key="index"
            class="w-40 h-40 rounded-xl overflow-hidden shadow-md flex-shrink-0"
          >
            <img :src="image" class="object-cover w-full h-full" />
          </div>
      
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
