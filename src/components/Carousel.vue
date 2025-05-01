<template>
    
    <Carousel v-bind="carouselConfig">
      <Slide v-for="(image, index) in images" :key="index">
        <div class="w-full h-full">
          <img :src="image" class="w-full h-full object-cover rounded-lg" />
        </div>
      </Slide>
    </Carousel>
</template>
  
  <script setup>
  import 'vue3-carousel/carousel.css';
  import { Carousel, Slide } from 'vue3-carousel';
  
  const carouselConfig = {
  itemsToShow: 1,
  autoplay: 2000,
  pauseAutoplayOnHover: true,
  mouseDrag: true,
  wrapAround: true,
  transition: 500, 
  easing: 'ease-in-out', 
};
  
  const imageModules = import.meta.glob('@/assets/Sample/*.{jpg,png,webp}', { eager: true });
  const images = Object.values(imageModules).map((mod) => mod.default);
  </script>
  