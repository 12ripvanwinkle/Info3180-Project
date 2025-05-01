<script setup>
import { RouterLink, RouterView } from 'vue-router';
import NavigateBar from './components/NavigateBar.vue';
import '@/assets/Main.css';
</script>



<template>
  <main>
      <RouterView />
  </main>
</template>

<style>

  .fade-enter-active, .fade-leave-active {
    transition: opacity .5s ease;
  }
  .fade-enter-from, .fade-leave-to {
    opacity: 0;
  }
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}


</style>