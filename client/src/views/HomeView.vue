<template>
  <div class="min-h-screen bg-gray-50">
    <AppHeader />

    <!-- Hero Section -->
    <section class="bg-indigo-700 text-white">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20">
        <div class="text-center">
          <h1 class="text-4xl md:text-6xl font-bold mb-6">Zoomir</h1>
          <p class="text-xl md:text-2xl mb-8">Всё для ваших любимых питомцев</p>
          <router-link
              to="/shop"
              class="inline-block bg-white text-indigo-700 px-8 py-3 rounded-lg font-medium hover:bg-gray-100 transition-colors"
          >
            В магазин
          </router-link>
        </div>
      </div>
    </section>

    <!-- Категории -->
    <section class="py-16">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h2 class="text-3xl font-bold text-center mb-12">Категории товаров</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          <div
              v-for="chapter in filtersStore.productChapters"
              :key="chapter.id"
              class="bg-white rounded-lg shadow-sm border p-6 hover:shadow-md transition-shadow cursor-pointer"
              @click="$router.push(`/shop/${chapter.id}`)"
          >
            <h3 class="text-xl font-semibold mb-4">{{ chapter.name }}</h3>
            <p class="text-gray-600">Широкий ассортимент товаров для ваших питомцев</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Популярные товары -->
    <section class="py-16 bg-white">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h2 class="text-3xl font-bold text-center mb-12">Популярные товары</h2>
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6" v-if="!productStore.isLoading">
          <ProductCard
              v-for="product in productStore.products.slice(0, 8)"
              :key="product.id"
              :product="product"
          />
        </div>
        <div v-else class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
          <div v-for="i in 8" :key="i" class="bg-gray-200 rounded-lg h-80 animate-pulse"></div>
        </div>

        <div class="text-center mt-12">
          <router-link
              to="/shop"
              class="inline-block bg-indigo-600 text-white px-8 py-3 rounded-lg font-medium hover:bg-indigo-700 transition-colors"
          >
            Смотреть все товары
          </router-link>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
import { onMounted } from 'vue'
import AppHeader from '@/components/AppHeader.vue'
import ProductCard from '@/components/ProductCard.vue'
import { useProductStore } from '@/stores/productStore'
import { useProductFiltersStore } from '@/stores/productFiltersStore'

const productStore = useProductStore()
const filtersStore = useProductFiltersStore()

onMounted(async () => {
  await productStore.fetchProducts({})
})
</script>
