<template>
  <header class="bg-white shadow-lg border-b border-gray-100 sticky top-0 z-50 transition-all duration-300">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between items-center h-16 md:h-20">
        <!-- Логотип -->
        <router-link
            to="/"
            class="flex items-center space-x-2 group transition-all duration-300 hover:scale-105"
        >
          <div class="relative">
            <div class="w-10 h-10 bg-gradient-to-r from-indigo-500 to-purple-600 rounded-xl flex items-center justify-center shadow-md">
              <span class="text-white font-bold text-lg">Z</span>
            </div>
          </div>
          <span class="text-2xl font-bold bg-gradient-to-r from-indigo-600 to-purple-700 bg-clip-text text-transparent">
            Zoomir
          </span>
        </router-link>

        <!-- Навигация -->
        <nav class="hidden md:flex space-x-8">
          <router-link
              to="/"
              class="relative py-2 text-gray-700 hover:text-indigo-600 transition-all duration-300 font-medium group"
              :class="{ 'text-indigo-600': $route.path === '/' }"
          >
            Главная
            <span
                v-if="$route.path === '/'"
                class="absolute bottom-0 left-0 w-full h-0.5 bg-gradient-to-r from-indigo-500 to-purple-600 rounded-full"
            ></span>
            <span
                v-else
                class="absolute bottom-0 left-0 w-0 h-0.5 bg-gradient-to-r from-indigo-500 to-purple-600 rounded-full transition-all duration-300 group-hover:w-full"
            ></span>
          </router-link>
          <router-link
              to="/chapters"
              class="relative py-2 text-gray-700 hover:text-indigo-600 transition-all duration-300 font-medium group"
              :class="{ 'text-indigo-600': $route.path === '/chapters' }"
          >
            Категории
            <span
                v-if="$route.path === '/chapters'"
                class="absolute bottom-0 left-0 w-full h-0.5 bg-gradient-to-r from-indigo-500 to-purple-600 rounded-full"
            ></span>
            <span
                v-else
                class="absolute bottom-0 left-0 w-0 h-0.5 bg-gradient-to-r from-indigo-500 to-purple-600 rounded-full transition-all duration-300 group-hover:w-full"
            ></span>
          </router-link>
          <router-link
              to="/orders"
              class="relative py-2 text-gray-700 hover:text-indigo-600 transition-all duration-300 font-medium group"
              :class="{ 'text-indigo-600': $route.path === '/orders' }"
          >
            Заказы
            <span
                v-if="$route.path === '/orders'"
                class="absolute bottom-0 left-0 w-full h-0.5 bg-gradient-to-r from-indigo-500 to-purple-600 rounded-full"
            ></span>
            <span
                v-else
                class="absolute bottom-0 left-0 w-0 h-0.5 bg-gradient-to-r from-indigo-500 to-purple-600 rounded-full transition-all duration-300 group-hover:w-full"
            ></span>
          </router-link>
        </nav>

        <!-- Действия пользователя -->
        <div class="flex items-center space-x-3 md:space-x-4">
          <!-- Избранное -->
          <router-link
              to="/favorites"
              class="relative p-2.5 rounded-xl text-gray-600 hover:text-indigo-600 transition-all duration-300 hover:bg-indigo-50 group"
          >
            <svg class="w-6 h-6 transition-transform duration-300 group-hover:scale-110" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/>
            </svg>
            <span
                v-if="favoritesStore.totalCount > 0"
                class="absolute -top-1 -right-1 bg-gradient-to-r from-red-500 to-pink-600 text-white text-xs rounded-full w-5 h-5 flex items-center justify-center shadow-sm"
            >
              {{ favoritesStore.totalCount }}
            </span>
          </router-link>

          <!-- Корзина -->
          <router-link
              to="/cart"
              class="relative p-2.5 rounded-xl text-gray-600 hover:text-indigo-600 transition-all duration-300 hover:bg-indigo-50 group"
          >
            <svg class="w-6 h-6 transition-transform duration-300 group-hover:scale-110" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"/>
            </svg>
            <span
                v-if="cartStore.cart?.total_items"
                class="absolute -top-1 -right-1 bg-gradient-to-r from-indigo-500 to-purple-600 text-white text-xs rounded-full w-5 h-5 flex items-center justify-center shadow-sm"
            >
              {{ cartStore.cart.total_items }}
            </span>
          </router-link>

          <!-- Профиль пользователя -->
          <div class="relative" v-if="authStore.isAuthenticated">
            <div class="flex items-center space-x-3">
              <div class="flex items-center space-x-2">
                <div class="w-8 h-8 rounded-full bg-gradient-to-r from-indigo-500 to-purple-600 flex items-center justify-center text-white font-medium text-sm shadow-sm">
                  {{ authStore.user?.username?.charAt(0).toUpperCase() }}
                </div>
                <span class="hidden md:inline text-gray-700 font-medium">{{ authStore.user?.username }}</span>
              </div>
              <button
                  @click="logout"
                  class="px-4 py-2 bg-gradient-to-r from-indigo-600 to-purple-700 text-white rounded-xl hover:shadow-lg transition-all duration-300 font-medium hover:from-indigo-700 hover:to-purple-800"
              >
                Выйти
              </button>
            </div>
          </div>

          <!-- Кнопки входа/регистрации -->
          <div v-else class="flex items-center space-x-3">
            <router-link
                to="/login"
                class="px-4 py-2 text-gray-700 hover:text-indigo-600 transition-colors duration-300 font-medium hidden md:block"
            >
              Войти
            </router-link>
            <router-link
                to="/register"
                class="px-4 py-2 bg-gradient-to-r from-indigo-600 to-purple-700 text-white rounded-xl hover:shadow-lg transition-all duration-300 font-medium hover:from-indigo-700 hover:to-purple-800"
            >
              Регистрация
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </header>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useAuthStore } from '@/stores/authStore'
import { useCartStore } from '@/stores/cartStore'
import { useFavoriteProductStore } from '@/stores/favoriteProductStore'

const authStore = useAuthStore()
const cartStore = useCartStore()
const favoritesStore = useFavoriteProductStore()
const showUserMenu = ref(false)

const logout = async () => {
  await authStore.logout()
  showUserMenu.value = false
}
</script>