<template>
    <div>
      <h1>Welcome to Jam-Date</h1>
      <div v-if="profiles.length">
        <h2>Recent Profiles</h2>
        <ul>
          <li v-for="profile in profiles" :key="profile.id">
            {{ profile.name }} - <router-link :to="`/profiles/${profile.id}`">View More</router-link>
          </li>
        </ul>
      </div>
      <form @submit.prevent="searchProfiles">
        <input v-model="search.name" placeholder="Name" />
        <input v-model="search.birth_year" placeholder="Birth Year" />
        <input v-model="search.sex" placeholder="Sex" />
        <input v-model="search.race" placeholder="Race" />
        <button type="submit">Search</button>
      </form>
      <ul>
        <li v-for="profile in searchResults" :key="profile.id">
          {{ profile.name }} - <router-link :to="`/profiles/${profile.id}`">View More</router-link>
        </li>
      </ul>
    </div>
</template>
  
<script>
    import axios from 'axios';
    import { getToken } from '../utils/auth';

    export default {
    data() {
        return {
        profiles: [],
        search: { name: '', birth_year: '', sex: '', race: '' },
        searchResults: []
        };
    },
    created() {
        axios.get('/api/profiles', {
        headers: getToken() ? { Authorization: `Bearer ${getToken()}` } : {}
        }).then(res => {
        this.profiles = res.data.slice(-4).reverse();
        });
    },
    methods: {
        searchProfiles() {
        axios.get('/api/search', {
            headers: getToken() ? { Authorization: `Bearer ${getToken()}` } : {},
            params: this.search
        }).then(res => {
            this.searchResults = res.data;
        });
        }
    }
    };
</script>