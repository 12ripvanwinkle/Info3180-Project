<template>
  <form @submit.prevent="searchProfiles">
    <input v-model="name" placeholder="Name" />
    <input v-model="birth_year" placeholder="Birth Year" />
    <input v-model="sex" placeholder="Sex" />
    <input v-model="race" placeholder="Race" />
    <button type="submit">Search</button>
  </form>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';

const emit = defineEmits(['search-results']);

const name = ref('');
const birth_year = ref('');
const sex = ref('');
const race = ref('');

const searchProfiles = async () => {
  const token = localStorage.getItem('token');
  const params = { name: name.value, birth_year: birth_year.value, sex: sex.value, race: race.value };
  const res = await axios.get('/search', {
    params,
    headers: { Authorization: `Bearer ${token}` }
  });
  emit('search-results', res.data);
};
</script>
