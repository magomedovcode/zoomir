<template>
  <div class="min-h-screen flex flex-col bg-gradient-to-br from-gray-50 to-indigo-50/30">
    <AppHeader />

    <div class="flex-grow container max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <!-- Заголовок страницы -->
      <div class="text-center mb-16">
        <div class="flex justify-center items-center mb-4">
          <div class="w-16 h-16 bg-gradient-to-r from-indigo-500 to-purple-600 rounded-2xl flex items-center justify-center shadow-lg">
            <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"/>
            </svg>
          </div>
        </div>
        <h1 class="text-4xl font-bold bg-gradient-to-r from-indigo-600 to-purple-700 bg-clip-text text-transparent mb-4">
          Категории товаров
        </h1>
        <p class="text-gray-600 max-w-2xl mx-auto text-lg">Всё необходимое для ваших питомцев в одном месте</p>
      </div>

      <!-- Сетка категорий -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 lg:gap-8">
        <div
            v-for="(chapter, index) in filtersStore.productChapters"
            :key="chapter.id"
            class="group relative bg-white rounded-2xl shadow-lg border border-gray-100 p-8 hover:shadow-2xl transition-all duration-500 cursor-pointer overflow-hidden"
            @click="$router.push(`/shop/${chapter.id}`)"
        >
          <!-- Градиентный фон при наведении -->
          <div class="absolute inset-0 bg-gradient-to-br from-indigo-50 to-purple-50 opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>

          <!-- Декоративный элемент -->
          <div class="absolute top-0 right-0 w-24 h-24 -mr-6 -mt-6 rounded-full bg-gradient-to-r from-indigo-500 to-purple-600 opacity-10 group-hover:opacity-20 transition-opacity duration-500"></div>

          <!-- Название категории -->
          <div class="relative z-10 text-center">
            <h3 class="text-xl font-bold text-gray-800 group-hover:text-indigo-700 transition-colors duration-300 mb-3">
              {{ chapter.name }}
            </h3>

            <!-- Кнопка перехода -->
            <div class="flex items-center justify-center space-x-2 text-indigo-600 group-hover:text-indigo-700 font-medium transition-colors duration-300">
              <span>Смотреть товары</span>
              <svg class="w-4 h-4 transform group-hover:translate-x-1 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
              </svg>
            </div>
          </div>
        </div>
      </div>

      <!-- Дополнительная информация -->
      <div class="mt-16 bg-gradient-to-r from-indigo-50 to-purple-50 rounded-2xl p-8 border border-indigo-100">
        <div class="flex flex-col md:flex-row items-center justify-between">
          <div class="flex items-center space-x-4 mb-6 md:mb-0">
            <div class="w-12 h-12 bg-indigo-100 rounded-xl flex items-center justify-center">
              <svg class="w-6 h-6 text-indigo-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/>
              </svg>
            </div>
            <div>
              <h3 class="text-lg font-semibold text-gray-800">Не нашли нужную категорию?</h3>
              <p class="text-gray-600">Свяжитесь с нами - мы поможем подобрать товары для вашего питомца</p>
            </div>
          </div>
          <button class="px-6 py-3 bg-gradient-to-r from-indigo-600 to-purple-700 text-white font-semibold rounded-xl hover:shadow-lg transition-all duration-300 transform hover:-translate-y-0.5">
            Связаться с нами
          </button>
        </div>
      </div>
    </div>

    <AppFooter />
  </div>
</template>

<script setup lang="ts">
import { onMounted } from 'vue'
import AppHeader from '@/components/AppHeader.vue'
import { useProductFiltersStore } from '@/stores/productFiltersStore'
import AppFooter from "@/components/AppFooter.vue";

const filtersStore = useProductFiltersStore()

onMounted(async () => {
  await filtersStore.fetchProductChapters()
})
</script>