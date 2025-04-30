<template>
  <header>
    <nav>
      <router-link to="/">Home</router-link>
      <router-link v-if="!loggedIn" to="/login">Login</router-link>
      <router-link v-if="!loggedIn" to="/register">Register</router-link>
      <router-link v-if="loggedIn" :to="`/users/${user_id}`">My Profile</router-link>
      <router-link v-if="loggedIn" to="/profiles/favourites">Favourites</router-link>
      <router-link v-if="loggedIn" to="/logout">Logout</router-link>
    </nav>
  </header>
</template>

<script setup>
import { RouterLink } from "vue-router";
import { jwtDecode } from 'jwt-decode';

const token = localStorage.getItem('token');
const loggedIn = !!token;
let user_id = null;

if (token) {
  const decoded = jwtDecode(token);
  user_id = decoded.sub;
}
</script>

  
  <style>
  /* Add any component specific styles here */
  
  </style>