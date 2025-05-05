<template>
    <div class="min-h-screen bg-[#E8C2CA]">
        <!-- Navigation Bar -->
        <NavigateBar />

        <!-- Profile Display Section -->
        <div class="max-w-4xl mx-auto bg-white shadow-md rounded-lg p-6 mt-12 mb-8">
            <div class="text-center">
                <img :src="`/uploads/${profile.user_photo}`" alt="Profile Photo"
                    class="w-36 h-36 mx-auto rounded-full mb-4 border-4 border-rose-400"/>
                <h1 class="text-3xl text-rose-600 font-pacifico font-semibold">{{ profile.user_name || 'User-NotFound' }}</h1>
                <p class="text-gray-500 text-sm mt-2 font-pacifico">Profile Details</p>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mt-8 font-light font-pacifico text-gray-700 text-sm">
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
                    <li><strong>Favourite Cuisine:</strong> {{ profile.fav_cuisine }}</li>
                    <li><strong>Favourite Colour:</strong> {{ profile.fav_colour }}</li>
                    <li><strong>Fav Subject:</strong> {{ profile.fav_school_subject }}</li>
                    <li><strong>Political:</strong> {{ profile.political ? 'Yes' : 'No' }}</li>
                    <li><strong>Religious:</strong> {{ profile.religious ? 'Yes' : 'No' }}</li>
                    <li><strong>Family-Oriented:</strong> {{ profile.family_oriented ? 'Yes' : 'No' }}</li>
                </ul>
            </div>

            <div class="flex justify-center gap-6 mt-10">
                <button
                    class="bg-rose-500 hover:bg-rose-600 text-white px-6 py-2 rounded-lg shadow font-pacifico transition duration-300 ease-in-out">
                    Email User
                </button>
                <button @click="addToFavourites"
                    class=" text-2xl bg-rose-500 hover:bg-rose-600 text-white px-6 py-2 rounded-lg shadow font-pacifico transition duration-300 ease-in-out">
                    ❤︎
                </button>
            </div>
        </div>
    </div>
</template>

<script setup>
    import { ref, onMounted } from 'vue';
    import { useRoute } from 'vue-router';
    import axios from 'axios';
    import { getToken } from '../utils/auth';
    import NavigateBar from '../components/NavigateBar.vue';
    import defaultProfileImage from '@/assets/Default/noProfile.png';

    const route = useRoute();
    const profile = ref({});

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