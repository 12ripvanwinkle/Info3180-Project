<template>
  <div class="home-container">
    <div class="hero-section">
      <nav class="nav">
        <h1 class="logo">Jam-Date</h1>
        <router-link to="/" class="nav-link">Home</router-link>
        <router-link to="/login" class="nav-link">Login</router-link>
        <router-link to="/register" class="nav-link">Register</router-link>
      </nav>
      <div class="hero-overlay">
        <h1 class="hero-title">Find Your Match on Jam-Date</h1>
        <p class="hero-subtitle">Connect with people who vibe with you.</p>
      </div>
    </div>
    <section class="grid-section">
      <div class="grid">
        <img :src="thumb1" class="grid-img" />
        <img :src="thumb2" class="grid-img" />
        <img :src="thumb3" class="grid-img" />
      </div>
    </section>
  </div>
</template>

<script setup>
  import thumb1 from '@/assets/thumb-1.jpg';
  import thumb2 from '@/assets/thumb-2.jpg';
  import thumb3 from '@/assets/thumb-3.jpg';
</script>

<style>
.home-container {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
  width: 100%;
}

/* Hero section with shared background */
.hero-section {
  background-image: url('@/assets/hero-group.jpg');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  height: 75vh; 
  color: white;
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
}
.logo {
  font-size: 1.5rem;
  font-weight: bold;
  justify-content: left;
}
/* Nav */
.nav {
  display: flex;
  justify-content: flex-end;
  padding: 1rem 2rem;
  gap: 1.5rem;
  background-color: rgba(0, 0, 0, 0.6); 
  position: absolute;
  width: 100%;
  top: 0;
  z-index: 10;
}

.nav-link {
  color: white;
  text-decoration: none;
  font-weight: bold;
}

.nav-link:hover {
  text-decoration: underline;
}

/* Hero content */
.hero-overlay {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: rgba(0, 0, 0, 0.5);
  padding: 2rem;
  border-radius: 10px;
  text-align: center;
  background-color: rgba(0, 0, 0, 0.65);
}

.hero-title {
  font-size: 2.8rem;
  margin-bottom: 0.5rem;
}

.hero-subtitle {
  font-size: 1.2rem;
  color: #f0f0f0;
}

/* Grid section */
.grid-section {
  background-color: burlywood;
  padding: 1rem 0;
  margin: 0;
  text-align: center;
}
.grid {
  display: flex;
  justify-content: center;
  gap: 1.5rem;
  flex-wrap: wrap;
  margin-bottom: 0;
}

.grid-img {
  width: 200px;
  height: 200px;
  object-fit: cover;
  border-radius: 12px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
}
.grid-img:hover {
  transform: scale(1.05);
  transition: transform 0.3s ease;
}
@media (max-width: 768px) {
  .hero-title {
    font-size: 2rem;
  }

  .hero-subtitle {
    font-size: 1rem;
  }

  .grid-img {
    width: 150px;
    height: 150px;
  }
}
</style>
