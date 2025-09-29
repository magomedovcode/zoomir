<template>
  <footer class="bg-gradient-to-b from-gray-50 to-white shadow-lg border-t border-gray-200">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
      <!-- Основное содержимое футера -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 lg:gap-12">
        <!-- О компании -->
        <div class="lg:col-span-1">
          <div class="flex items-center space-x-2 mb-4">
            <div class="w-10 h-10 bg-gradient-to-r from-indigo-500 to-purple-600 rounded-xl flex items-center justify-center shadow-md">
              <span class="text-white font-bold text-lg">Z</span>
            </div>
            <span class="text-2xl font-bold bg-gradient-to-r from-indigo-600 to-purple-700 bg-clip-text text-transparent">
              Zoomir
            </span>
          </div>
          <p class="text-gray-600 leading-relaxed mb-6">
            Всё для комфортной жизни ваших любимых питомцев. Качественные товары с доставкой по всей России.
          </p>
        </div>

        <!-- Контакты -->
        <div>
          <h3 class="text-lg font-bold mb-6 bg-gradient-to-r from-indigo-600 to-purple-700 bg-clip-text text-transparent">
            Контакты
          </h3>
          <ul class="space-y-4">
            <li class="flex items-start space-x-3">
              <div class="w-6 h-6 bg-indigo-100 rounded-full flex items-center justify-center flex-shrink-0 mt-0.5">
                <svg class="w-4 h-4 text-indigo-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/>
                </svg>
              </div>
              <span class="text-gray-600">zoomir@gmail.com</span>
            </li>
            <li class="flex items-start space-x-3">
              <div class="w-6 h-6 bg-indigo-100 rounded-full flex items-center justify-center flex-shrink-0 mt-0.5">
                <svg class="w-4 h-4 text-indigo-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/>
                </svg>
              </div>
              <span class="text-gray-600">+1 (999) 999-99-99</span>
            </li>
            <li class="flex items-start space-x-3">
              <div class="w-6 h-6 bg-indigo-100 rounded-full flex items-center justify-center flex-shrink-0 mt-0.5">
                <svg class="w-4 h-4 text-indigo-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/>
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/>
                </svg>
              </div>
              <span class="text-gray-600">Россия, г. Ставрополь, ул. Зоомирная 14, магазин 88</span>
            </li>
          </ul>
        </div>

        <!-- Быстрые ссылки -->
        <div>
          <h3 class="text-lg font-bold mb-6 bg-gradient-to-r from-indigo-600 to-purple-700 bg-clip-text text-transparent">
            Навигация
          </h3>
          <ul class="space-y-3">
            <li v-for="link in navigationLinks" :key="link.to">
              <router-link
                  :to="link.to"
                  class="flex items-center space-x-2 text-gray-600 hover:text-indigo-600 transition-all duration-300 group py-1"
                  :class="{ 'text-indigo-600 font-medium': $route.path === link.to }"
              >
                <div class="w-1.5 h-1.5 bg-indigo-500 rounded-full opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
                <span class="group-hover:translate-x-1 transition-transform duration-300">{{ link.name }}</span>
              </router-link>
            </li>
          </ul>
        </div>
      </div>

      <!-- Нижняя часть футера -->
      <div class="border-t border-gray-200 mt-12 pt-8 flex flex-col md:flex-row justify-between items-center space-y-4 md:space-y-0">
        <p class="text-gray-500 text-sm text-center md:text-left">
          &copy; {{ new Date().getFullYear() }} Zoomir. Все права защищены.
        </p>
        <div class="flex space-x-6 text-sm text-gray-500">
          <a href="#" class="hover:text-indigo-600 transition-colors duration-300">Политика конфиденциальности</a>
          <a href="#" class="hover:text-indigo-600 transition-colors duration-300">Условия использования</a>
          <a href="#" class="hover:text-indigo-600 transition-colors duration-300">Обратная связь</a>
        </div>
      </div>
    </div>
  </footer>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const navigationLinks = ref([
  { to: '/', name: 'Главная' },
  { to: '/cart', name: 'Корзина' },
  { to: '/favorites', name: 'Избранное' },
  { to: '/orders', name: 'Заказы' },
  { to: '/chapters', name: 'Категории' }
])
</script>
