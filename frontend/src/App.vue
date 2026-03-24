<template>
  <v-app>
    <!-- Навигация -->
    <v-app-bar app color="primary" dark>
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
      
      <v-toolbar-title class="text-h6">
        🎯 mkpStats
      </v-toolbar-title>
      
      <v-spacer></v-spacer>
      
      <v-btn to="/" text>
        <v-icon left>mdi-home</v-icon>
        Главная
      </v-btn>
      
      <v-btn to="/products" text>
        <v-icon left>mdi-package-variant</v-icon>
        Товары
      </v-btn>
    </v-app-bar>

    <!-- Боковое меню -->
    <v-navigation-drawer v-model="drawer" app temporary>
      <v-list nav>
        <v-list-item 
          prepend-icon="mdi-home" 
          title="Главная" 
          to="/"
        />
        <v-list-item 
          prepend-icon="mdi-package-variant" 
          title="Товары" 
          to="/products"
        />
      </v-list>
    </v-navigation-drawer>

    <!-- Основной контент -->
    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const drawer = ref(false)
</script>
