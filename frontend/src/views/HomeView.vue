<template>
  <div class="home">
    <div class="hero">
      <h1 class="text-h2 mb-4">🎯 mkpStats</h1>
      <p class="text-h5 mb-8">Юнит-экономика маркетплейсов</p>
      
      <v-btn 
        size="large" 
        color="primary" 
        to="/products"
        class="mr-4"
      >
        📦 К товарам
      </v-btn>
      
      <v-btn 
        size="large" 
        color="secondary" 
        href="http://localhost:8000/docs"
        target="_blank"
      >
        🔧 API Docs
      </v-btn>
    </div>

    <div class="stats-grid">
      <v-card class="stat-card" elevation="4">
        <v-card-title>Backend</v-card-title>
        <v-card-subtitle>FastAPI + PostgreSQL</v-card-subtitle>
        <v-card-text>
          <strong>localhost:8000</strong><br>
          <a href="http://localhost:8000/docs" target="_blank">Swagger UI</a>
        </v-card-text>
      </v-card>

      <v-card class="stat-card" elevation="4">
        <v-card-title>Frontend</v-card-title>
        <v-card-subtitle>Vue 3 + Vite</v-card-subtitle>
        <v-card-text>
          <strong>localhost:3000</strong><br>
          Таблицы + графики
        </v-card-text>
      </v-card>
    </div>
  </div>
</template>

<script setup lang="ts">
// Главная страница Dashboard
</script>

<style scoped>
.home {
  min-height: 100vh;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  text-align: center;
  padding: 2rem;
}

.hero {
  max-width: 800px;
  margin: 0 auto;
  padding: 4rem 1rem;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  max-width: 1200px;
  margin: 4rem auto;
  padding: 0 1rem;
}

.stat-card {
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255,255,255,0.2);
}
</style>
