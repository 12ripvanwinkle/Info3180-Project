<template>
    <NavigateBar/>
    <div class="min-h-screen bg-gradient-to-br from-green-600 to-green-800 text-white py-10 px-4">
        <div class="max-w-4xl mx-auto bg-green-900 rounded-lg p-6 shadow-lg text-center">
            <img :src="getPhotoUrl(profile.photo)" alt="Profile Photo" class="w-36 h-36 mx-auto rounded-full mb-4 border-4 border-white"/>
            <h1 class="text-3xl font-bold">{{ profile.name || 'Jam-Date' }}</h1>
            <p class="text-gray-200 text-sm mt-2">Profile Details</p>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6 max-w-4xl mx-auto mt-10 text-sm">
            <ul class="space-y-1">
                <li><strong>Description:</strong> {{ profile.description }}</li>
                <li><strong>Parish:</strong> {{ profile.parish }}</li>
                <li><strong>Biography:</strong> {{ profile.biography }}</li>
                <li><strong>Sex:</strong> {{ profile.sex }}</li>
                <li><strong>Race:</strong> {{ profile.race }}</li>
                <li><strong>Birth Year:</strong> {{ profile.birth_year }}</li>
                <li><strong>Height:</strong> {{ profile.height }}</li>
            </ul>
            <ul class="space-y-1">
                <li><strong>Favourite Cuisine:</strong> {{ profile.fave_cuisine }}</li>
                <li><strong>Favourite Colour:</strong> {{ profile.fav_colour }}</li>
                <li><strong>Fav Subject:</strong> {{ profile.fav_school_subject }}</li>
                <li><strong>Political:</strong> {{ profile.political ? 'Yes' : 'No' }}</li>
                <li><strong>Religious:</strong> {{ profile.religious ? 'Yes' : 'No' }}</li>
                <li><strong>Family-Oriented:</strong> {{ profile.family_oriented ? 'Yes' : 'No' }}</li>
            </ul>
        </div>
        <div class="flex justify-center gap-6 mt-10">
            <button class="bg-red-500 hover:bg-red-600 text-white px-5 py-2 rounded font-semibold">Email User</button>
            <button @click="addToFavourites" class="bg-red-500 hover:bg-red-600 text-white px-5 py-2 rounded font-semibold">❤️</button>
        </div>
    </div>
</template>
<script setup>
    import { ref, onMounted } from 'vue';
    import { useRoute } from 'vue-router';
    import axios from 'axios';
    import { getToken } from '../utils/auth';
import NavigateBar from '../components/NavigateBar.vue';

    const route = useRoute();
    const profile = ref({});

    function getPhotoUrl(filename) {
        return filename ? `/uploads/${filename}` : '';
    }
    onMounted(async () => {
        const id = route.params.profile_id;
        try {
            const res = await axios.get(`/api/profiles/${id}`,{
                headers: { Authorization: `Bearer ${getToken()}` }
            });
            profile.value = res.data;
        }
        catch (error) {
            console.error('Error:', error);
        }
    });

    async function addToFavourites() {
        try {
            const res = await axios.post(`/api/profiles/${profile.value.user_id}/favourite`, {}, {
                headers: { Authorization: `Bearer ${getToken()}` }
            });
            alert('Added to favourites')
        }
        catch (error) {
            console.error('Error:', error);
            alert('Something went wrong');
        }
    }
</script>
<style scoped>
</style>