<template>
  <header class="bg-white shadow-sm border-b">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between items-center h-16">
        <router-link to="/" class="flex items-center space-x-2">
          <span class="text-2xl font-bold text-indigo-600">Zoomir</span>
        </router-link>

        <nav class="hidden md:flex space-x-8">
          <router-link
              to="/"
              class="text-gray-700 hover:text-indigo-600 transition-colors"
              :class="{ 'text-indigo-600 font-medium': $route.path === '/' }"
          >
            Главная
          </router-link>
          <router-link
              to="/chapters"
              class="text-gray-700 hover:text-indigo-600 transition-colors"
              :class="{ 'text-indigo-600 font-medium': $route.path === '/chapters' }"
          >
            Категории
          </router-link>
          <router-link
              to="/shop"
              class="text-gray-700 hover:text-indigo-600 transition-colors"
              :class="{ 'text-indigo-600 font-medium': $route.path.includes('/shop') }"
          >
            Все товары
          </router-link>
        </nav>

        <div class="flex items-center space-x-4">
          <router-link to="/favorites" class="relative p-2 text-gray-600 hover:text-indigo-600">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/>
            </svg>
            <span v-if="favoritesStore.totalCount > 0" class="absolute -top-1 -right-1 bg-red-500 text-white text-xs rounded-full w-5 h-5 flex items-center justify-center">
              {{ favoritesStore.totalCount }}
            </span>
          </router-link>

          <router-link to="/cart" class="relative p-2 text-gray-600 hover:text-indigo-600">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"/>
            </svg>
            <span v-if="cartStore.cart?.total_items" class="absolute -top-1 -right-1 bg-indigo-600 text-white text-xs rounded-full w-5 h-5 flex items-center justify-center">
              {{ cartStore.cart.total_items }}
            </span>
          </router-link>

          <div class="relative" v-if="authStore.isAuthenticated">
            <button @click="showUserMenu = !showUserMenu" class="flex items-center space-x-2 p-2 rounded-lg hover:bg-gray-100">
              <span class="text-gray-700">{{ authStore.user?.username }}</span>
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
              </svg>
            </button>

            <div v-if="showUserMenu" class="absolute right-0 mt-2 w-48 bg-white rounded-lg shadow-lg border py-1 z-50">
              <router-link to="/orders" class="block px-4 py-2 text-gray-700 hover:bg-gray-100">Мои заказы</router-link>
              <button @click="logout" class="block w-full text-left px-4 py-2 text-gray-700 hover:bg-gray-100">Выйти</button>
            </div>
          </div>

          <div v-else class="flex space-x-2">
            <router-link to="/login" class="px-4 py-2 text-gray-700 hover:text-indigo-600">Войти</router-link>
            <router-link to="/register" class="px-4 py-2 bg-indigo-600 text-white rounded-lg hover:bg-indigo-700">Регистрация</router-link>
          </div>
        </div>
      </div>
    </div>
  </header>
</template>

<script setup lang="ts">
import {onMounted, ref} from 'vue'
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
