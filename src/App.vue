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
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html, body {
  width: 100%;
  height: 100%;
  overflow: hidden;
  font-family: Arial, sans-serif;
  background-color: #fff;
}
</style>