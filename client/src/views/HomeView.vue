<template>
  <div class="flex flex-col min-h-screen bg-white">
    <AppHeader />

    <section class="relative overflow-hidden bg-gradient-to-b from-amber-400 via-yellow-200 to-white text-white">
      <div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-32 lg:py-40">
        <div class="text-center">
          <h1 class="text-5xl md:text-7xl lg:text-8xl font-bold mb-6 tracking-tight">
            <span class="bg-gradient-to-b from-stone-700 to-stone-800 bg-clip-text text-transparent animate-fade-in-up">
              ZOOМИР
            </span>
          </h1>

          <p class="text-xl md:text-2xl lg:text-3xl mb-10 max-w-3xl text-stone-800 mx-auto opacity-90 animate-fade-in-up animation-delay-300">
            Всё для счастья ваших любимых питомцев
          </p>

          <div class="animate-fade-in-up animation-delay-500">
            <router-link
                to="/chapters"
                class="group relative inline-flex items-center justify-center px-8 py-4 text-lg font-bold text-yellow-500 bg-white rounded-2xl shadow-2xl hover:shadow-3xl transition-all duration-500 transform hover:-translate-y-2 hover:scale-105 overflow-hidden"
            >
              <span class="relative z-10 flex items-center">
                <svg class="w-5 h-5 mr-3 group-hover:rotate-12 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"/>
                </svg>
                В магазин
              </span>
            </router-link>
          </div>
        </div>
      </div>
    </section>

    <section class="py-20 relative">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16 animate-fade-in-up">
          <h2 class="text-4xl md:text-5xl font-bold bg-gradient-to-r from-yellow-500 to-amber-600 bg-clip-text text-transparent mb-4">
            Категории товаров
          </h2>
          <p class="text-xl text-stone-600 max-w-2xl mx-auto">
            Всё необходимое для комфорта и здоровья ваших питомцев
          </p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          <div
              v-for="(chapter, index) in filtersStore.productChapters"
              :key="chapter.id"
              class="group relative bg-white rounded-2xl shadow-xl border border-stone-300 p-8 hover:shadow-2xl transition-all duration-500 cursor-pointer overflow-hidden transform hover:-translate-y-2 animate-fade-in-up"
              :style="`animation-delay: ${index * 100}ms`"
              @click="$router.push(`/shop/${chapter.id}`)"
          >
            <div class="absolute top-0 right-0 w-20 h-20 -mr-6 -mt-6 rounded-full bg-gradient-to-r from-yellow-500 to-amber-600 opacity-10 group-hover:opacity-20 transition-opacity duration-500"></div>

            <div class="relative z-10 text-center">
              <h3 class="text-xl font-bold text-stone-800 transition-colors duration-300 mb-3">
                {{ chapter.name }}
              </h3>

              <div class="flex items-center justify-center space-x-2 text-yellow-500 group-hover:text-yellow-600 font-medium transition-colors duration-300">
                <span>Смотреть товары</span>
                <svg class="w-4 h-4 transform group-hover:translate-x-1 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
                </svg>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="py-20 bg-gradient-to-br from-white to-stone-50/50">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16">
          <h2 class="text-4xl md:text-5xl font-bold bg-gradient-to-r from-yellow-500 to-amber-600 bg-clip-text text-transparent mb-4">
            Популярные товары
          </h2>
          <p class="text-xl text-stone-600 max-w-2xl mx-auto">
            Самые востребованные товары для ваших питомцев
          </p>
        </div>

        <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-5 gap-6 mb-12" v-if="!productStore.isLoading">
          <ProductCard
              v-for="(product, index) in productStore.products.slice(0, 10)"
              :key="product.id"
              :product="product"
              class="transform transition-all duration-500 hover:scale-105 animate-fade-in-up"
              :style="`animation-delay: ${index * 100}ms`"
          />
        </div>

        <div v-else class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 mb-12">
          <div
              v-for="i in 8"
              :key="i"
              class="bg-gradient-to-br from-stone-200 to-stone-300 rounded-2xl h-80 animate-pulse shadow-sm"
          ></div>
        </div>

        <div class="text-center animate-fade-in-up animation-delay-800">
          <router-link
              to="/chapters"
              class="group relative inline-flex items-center justify-center px-8 py-4 text-lg font-bold text-white bg-gradient-to-r from-yellow-500 to-amber-600 rounded-2xl shadow-xl hover:shadow-2xl transition-all duration-500 transform hover:-translate-y-1 hover:scale-105 overflow-hidden"
          >
            <span class="relative z-10 flex items-center">
              <svg class="w-5 h-5 mr-3 group-hover:rotate-12 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
              </svg>
              Смотреть все товары
            </span>

            <div class="absolute inset-0 overflow-hidden">
              <div class="absolute -inset-y-full -left-20 group-hover:left-full w-20 bg-white/30 skew-x-12 transition-all duration-1000 group-hover:duration-500"></div>
            </div>
          </router-link>
        </div>
      </div>
    </section>

    <AppFooter />
  </div>
</template>

<script setup lang="ts">
import { onMounted } from 'vue'
import AppHeader from '@/components/AppHeader.vue'
import ProductCard from '@/components/ProductCard.vue'
import { useProductStore } from '@/stores/productStore'
import { useProductFiltersStore } from '@/stores/productFiltersStore'
import AppFooter from "@/components/AppFooter.vue";

const productStore = useProductStore()
const filtersStore = useProductFiltersStore()

onMounted(async () => {
  await productStore.fetchProducts({})
  await filtersStore.fetchProductChapters()
})
</script>
