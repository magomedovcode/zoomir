<template>
  <div class="min-h-screen flex flex-col bg-white">
    <AppHeader />

    <div class="flex-grow container max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <div class="text-center mb-12">
        <div class="flex flex-row justify-center items-center gap-3">
          <div class="flex justify-center items-center mb-4">
            <div class="w-10 h-10 bg-gradient-to-r from-pink-500 to-rose-600 rounded-xl flex items-center justify-center shadow-lg">
              <svg class="w-5 h-5 text-white" fill="currentColor" viewBox="0 0 24 24">
                <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/>
              </svg>
            </div>
          </div>
          <h1 class="text-4xl font-bold bg-gradient-to-r from-pink-600 to-rose-700 bg-clip-text text-transparent mb-4">
            Избранное
          </h1>
        </div>
        <p class="text-gray-600 max-w-2xl mx-auto">Товары, которые вам особенно понравились</p>
      </div>

      <div v-if="favoritesStore.favoriteProducts.length" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6 mb-12">
        <FavoriteCard
            v-for="favorite in favoritesStore.favoriteProducts"
            :key="favorite.id"
            :product="favorite.product"
        />
      </div>

      <div v-else class="text-center py-16 max-w-2xl mx-auto">
        <div class="bg-white rounded-2xl shadow-lg border border-gray-100 p-12">
          <div class="w-32 h-32 mx-auto mb-8 bg-gradient-to-br from-pink-100 to-rose-100 rounded-full flex items-center justify-center">
            <svg class="w-16 h-16 text-pink-400" fill="currentColor" viewBox="0 0 24 24">
              <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/>
            </svg>
          </div>
          <h3 class="text-2xl font-bold text-gray-800 mb-4">В избранном пока пусто</h3>
          <p class="text-gray-600 mb-8">Добавляйте товары в избранное, чтобы не потерять и легко найти их позже</p>
          <div class="space-y-4 sm:space-y-0 sm:space-x-4 sm:flex sm:justify-center">
            <router-link
                to="/chapters"
                class="inline-flex items-center px-6 py-3 bg-gradient-to-r from-indigo-600 to-purple-700 text-white font-semibold rounded-xl shadow-lg hover:shadow-xl transition-all duration-300 transform hover:-translate-y-0.5"
            >
              <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"/>
              </svg>
              Перейти в магазин
            </router-link>
            <router-link
                to="/"
                class="inline-flex items-center px-6 py-3 border-2 border-gray-300 text-gray-700 font-medium rounded-xl hover:border-indigo-300 hover:bg-indigo-50 transition-all duration-300"
            >
              На главную
            </router-link>
          </div>
        </div>
      </div>

      <div class="flex flex-col sm:flex-row justify-between items-center p-8 bg-gradient-to-r from-stone-800 to-stone-700 rounded-2xl shadow-sm">
        <div class="flex items-center space-x-3 mb-4 sm:mb-0">
          <div class="w-12 h-12 bg-pink-600 rounded-xl flex items-center justify-center">
            <svg class="w-6 h-6 text-stone-800" fill="currentColor" viewBox="0 0 24 24">
              <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/>
            </svg>
          </div>
          <div>
            <h2 class="text-lg font-semibold text-white">
              {{ favoritesStore.favoriteProducts.length }} товаров в избранном
            </h2>
            <p class="text-white">Сохраняйте понравившиеся товары для быстрого доступа</p>
          </div>
        </div>

        <button
            v-if="favoritesStore.favoriteProducts.length"
            @click="clearFavorites"
            class="flex items-center space-x-2 px-6 py-3 bg-gradient-to-r from-rose-500 to-pink-600 hover:from-rose-600 hover:to-pink-700 text-stone-800 font-medium rounded-xl shadow-lg hover:shadow-xl transition-all duration-300 transform hover:-translate-y-0.5"
        >
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"/>
          </svg>
          <span>Очистить избранное</span>
        </button>
      </div>
    </div>

    <AppFooter />
  </div>
</template>

<script setup lang="ts">
import { onMounted } from 'vue'
import AppHeader from '@/components/AppHeader.vue'
import { useFavoriteProductStore } from '@/stores/favoriteProductStore'
import AppFooter from "@/components/AppFooter.vue";
import FavoriteCard from "@/components/FavoriteCard.vue";

const favoritesStore = useFavoriteProductStore();

onMounted(async () => {
  await favoritesStore.fetchFavoriteProducts();
})

const clearFavorites = async () => {
  await favoritesStore.clearFavorite();
  await favoritesStore.fetchFavoriteProducts();
}
</script>