<template>
  <div class="min-h-screen bg-gray-50">
    <AppHeader />

    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <div class="flex justify-between items-center mb-8">
        <h1 class="text-3xl font-bold">Избранное</h1>
        <button
            v-if="favoritesStore.favoriteProducts.length"
            @click="clearFavorites"
            class="text-red-600 hover:text-red-700"
        >
          Очистить избранное
        </button>
      </div>

      <div v-if="favoritesStore.favoriteProducts.length" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
        <ProductCard
            v-for="favorite in favoritesStore.favoriteProducts"
            :key="favorite.id"
            :product="favorite.product"
        />
      </div>

      <div v-else class="text-center py-12">
        <svg class="mx-auto h-24 w-24 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/>
        </svg>
        <h3 class="mt-4 text-lg font-medium text-gray-900">Нет избранных товаров</h3>
        <p class="mt-2 text-gray-500">Добавляйте товары в избранное, чтобы не потерять.</p>
        <div class="mt-6">
          <router-link to="/shop" class="inline-flex items-center px-4 py-2 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700">
            В магазин
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { onMounted } from 'vue'
import AppHeader from '@/components/AppHeader.vue'
import ProductCard from '@/components/ProductCard.vue'
import { useFavoriteProductStore } from '@/stores/favoriteProductStore'

const favoritesStore = useFavoriteProductStore()

onMounted(async () => {
  await favoritesStore.fetchFavoriteProducts()
})

const clearFavorites = async () => {
  await favoritesStore.clearFavorite()
  await favoritesStore.fetchFavoriteProducts()
}
</script>