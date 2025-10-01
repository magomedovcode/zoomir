<template>
  <header class="bg-stone-800 shadow-lg sticky top-0 z-50 transition-all duration-300">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between items-center h-16 md:h-20">
        <router-link
            to="/"
            class="flex items-center space-x-2 group transition-all duration-300 hover:scale-105"
        >
          <img
              src="/logo.png"
              alt="ZOOМИР"
              class="h-11 w-auto object-contain transition-transform duration-300 group-hover:scale-105"
          >
        </router-link>

        <nav class="hidden md:flex space-x-8">
          <router-link
              to="/"
              class="relative py-2 text-white text-lg hover:text-yellow-400 transition-all duration-300 font-medium group"
              :class="{ 'text-yellow-400': $route.path === '/' }"
          >
            Главная
            <span
                v-if="$route.path === '/'"
                class="absolute bottom-0 left-0 w-full h-0.5 bg-gradient-to-r from-yellow-400 to-amber-400 rounded-full"
            ></span>
            <span
                v-else
                class="absolute bottom-0 left-0 w-0 h-0.5 bg-gradient-to-r from-yellow-400 to-amber-400 rounded-full transition-all duration-300 group-hover:w-full"
            ></span>
          </router-link>
          <router-link
              to="/chapters"
              class="relative py-2 text-white text-lg hover:text-yellow-400 transition-all duration-300 font-medium group"
              :class="{ 'text-yellow-400': $route.path === '/chapters' }"
          >
            Категории
            <span
                v-if="$route.path === '/chapters'"
                class="absolute bottom-0 left-0 w-full h-0.5 bg-gradient-to-r from-yellow-400 to-amber-400 rounded-full"
            ></span>
            <span
                v-else
                class="absolute bottom-0 left-0 w-0 h-0.5 bg-gradient-to-r from-yellow-400 to-amber-400 rounded-full transition-all duration-300 group-hover:w-full"
            ></span>
          </router-link>
          <router-link
              to="/orders"
              class="relative py-2 text-white text-lg hover:text-yellow-400 transition-all duration-300 font-medium group"
              :class="{ 'text-yellow-400': $route.path === '/orders' }"
          >
            Заказы
            <span
                v-if="$route.path === '/orders'"
                class="absolute bottom-0 left-0 w-full h-0.5 bg-gradient-to-r from-yellow-400 to-amber-400 rounded-full"
            ></span>
            <span
                v-else
                class="absolute bottom-0 left-0 w-0 h-0.5 bg-gradient-to-r from-yellow-400 to-amber-400 rounded-full transition-all duration-300 group-hover:w-full"
            ></span>
          </router-link>
        </nav>

        <div class="hidden md:flex items-center space-x-4">
          <router-link
              to="/favorites"
              class="relative p-2.5 rounded-xl text-white transition-all duration-300 group hover:text-yellow-400 hover:bg-stone-700"
              active-class="text-yellow-400"
          >
            <svg class="w-6 h-6 transition-transform duration-300 group-hover:scale-110" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/>
            </svg>
            <span
                v-if="favoritesStore.favoriteProducts.length > 0"
                class="absolute font-bold -top-1 -right-1 bg-gradient-to-r from-red-500 to-pink-600 text-stone-800 text-xs rounded-full w-5 h-5 flex items-center justify-center shadow-sm"
            >
              {{ favoritesStore.favoriteProducts.length }}
            </span>
          </router-link>

          <router-link
              to="/cart"
              class="relative p-2.5 rounded-xl text-white hover:text-yellow-400 transition-all duration-300 hover:bg-stone-700 group"
              active-class="text-yellow-500"
          >
            <svg class="w-6 h-6 transition-transform duration-300 group-hover:scale-110" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"/>
            </svg>
            <span
                v-if="cartStore.cart?.total_items"
                class="absolute font-bold -top-1 -right-1 bg-gradient-to-r from-yellow-500 to-amber-400 text-stone-800 text-xs rounded-full w-5 h-5 flex items-center justify-center shadow-sm"
            >
              {{ cartStore.cart.total_items }}
            </span>
          </router-link>

          <div class="relative" v-if="authStore.isAuthenticated">
            <div class="flex items-center space-x-3">
              <div class="flex items-center space-x-2">
                <div class="w-8 h-8 rounded-full bg-gradient-to-r from-yellow-400 to-amber-400 flex items-center justify-center text-white font-medium text-sm shadow-sm">
                  {{ authStore.user?.username?.charAt(0).toUpperCase() }}
                </div>
                <span class="text-white text-lg">{{ authStore.user?.username }}</span>
              </div>
              <button
                  @click="logout"
                  class="px-4 py-2 bg-gradient-to-r from-yellow-400 to-amber-400 text-stone-800 rounded-xl hover:shadow-lg transition-all duration-300 font-medium hover:from-yellow-500 hover:to-amber-500"
              >
                Выйти
              </button>
            </div>
          </div>

          <div v-else class="flex items-center space-x-3">
            <router-link
                to="/login"
                class="px-4 py-2 text-white hover:text-yellow-400 transition-colors duration-300 font-medium"
            >
              Войти
            </router-link>
            <router-link
                to="/register"
                class="px-4 py-2 bg-gradient-to-r from-yellow-400 to-amber-400 text-stone-800 rounded-xl hover:shadow-lg transition-all duration-300 font-medium hover:from-yellow-500 hover:to-amber-500"
            >
              Регистрация
            </router-link>
          </div>
        </div>

        <div class="flex md:hidden items-center space-x-2">
          <router-link
              to="/favorites"
              class="relative p-2 rounded-xl text-white hover:text-yellow-400 transition-all duration-300 hover:bg-stone-700"
              active-class="text-yellow-400 bg-stone-700"
          >
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/>
            </svg>
            <span
                v-if="favoritesStore.favoriteProducts.length > 0"
                class="absolute font-bold -top-1 -right-1 bg-gradient-to-r from-red-500 to-pink-600 text-stone-800 text-xs rounded-full w-4 h-4 flex items-center justify-center"
            >
              {{ favoritesStore.favoriteProducts.length }}
            </span>
          </router-link>

          <router-link
              to="/cart"
              class="relative p-2 rounded-xl text-white hover:text-yellow-400 transition-all duration-300 hover:bg-stone-700"
              active-class="text-yellow-400 bg-stone-700"
          >
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"/>
            </svg>
            <span
                v-if="cartStore.cart?.total_items"
                class="absolute font-bold -top-1 -right-1 bg-gradient-to-r from-yellow-400 to-amber-400 text-stone-800 text-xs rounded-full w-4 h-4 flex items-center justify-center"
            >
              {{ cartStore.cart.total_items }}
            </span>
          </router-link>

          <button
              @click="toggleMobileMenu"
              class="p-2 rounded-xl text-white hover:text-yellow-400 transition-all duration-300 hover:bg-stone-700 focus:outline-none"
              :class="{ 'text-yellow-400 bg-stone-700': isMobileMenuOpen }"
          >
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path
                  v-if="!isMobileMenuOpen"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M4 6h16M4 12h16M4 18h16"
              />
              <path
                  v-else
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M6 18L18 6M6 6l12 12"
              />
            </svg>
          </button>
        </div>
      </div>

      <div
          v-if="isMobileMenuOpen"
          class="fixed inset-0 z-50 md:hidden"
      >
        <div
            class="absolute inset-0 bg-white bg-opacity-40 backdrop-blur-sm transition-opacity duration-300"
            @click="closeMobileMenu"
        ></div>

        <div
            class="absolute inset-0 bg-stone-800 flex flex-col"
        >
          <div class="flex items-center justify-between px-6 py-4">
            <router-link
                to="/"
                class="flex items-center space-x-2 group transition-all duration-300 hover:scale-105"
            >
              <img
                  src="/logo.png"
                  alt="ZOOМИР"
                  class="h-11 w-auto object-contain transition-transform duration-300 group-hover:scale-110"
              >
            </router-link>
            <button
                @click="closeMobileMenu"
                class="p-2 rounded-xl text-white hover:text-yellow-400 transition-colors duration-300"
            >
              <svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
              </svg>
            </button>
          </div>

          <nav class="flex-1 flex flex-col justify-center items-center space-y-6">
            <router-link
                to="/"
                class="text-2xl font-semibold transition-colors duration-300 text-white"
                :class="{ 'text-yellow-400': $route.path === '/' }"
                @click="closeMobileMenu"
            >
              Главная
            </router-link>
            <router-link
                to="/chapters"
                class="text-2xl font-semibold transition-colors duration-300 text-white"
                :class="{ 'text-yellow-400': $route.path === '/chapters' }"
                @click="closeMobileMenu"
            >
              Категории
            </router-link>
            <router-link
                to="/orders"
                class="text-2xl font-semibold transition-colors duration-300 text-white"
                :class="{ 'text-yellow-400': $route.path === '/orders' }"
                @click="closeMobileMenu"
            >
              Заказы
            </router-link>
          </nav>

          <div class="px-6 py-6">
            <div
                v-if="authStore.isAuthenticated"
                class="flex items-center space-x-3 mb-4 cursor-pointer"
                @click="toggleLogout"
            >
              <div class="w-12 h-12 rounded-full bg-gradient-to-r from-yellow-400 to-amber-400 flex items-center justify-center text-white font-medium text-lg shadow-sm">
                {{ authStore.user?.username?.charAt(0).toUpperCase() }}
              </div>
              <p class="text-lg text-white">
                {{ authStore.user?.username }}
              </p>
              <svg
                  class="w-5 h-5 text-white transition-transform duration-300"
                  :class="{ 'rotate-180': showLogout }"
                  fill="none" stroke="currentColor" viewBox="0 0 24 24"
              >
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
              </svg>
            </div>

            <div v-if="showLogout" class="space-y-3">
              <button
                  @click="logout"
                  class="w-full py-3 text-lg bg-gradient-to-r from-yellow-400 to-amber-400 text-stone-800 rounded-xl hover:shadow-lg transition-all duration-300 font-medium"
              >
                Выйти
              </button>
            </div>

            <div v-else-if="!authStore.isAuthenticated" class="space-y-3">
              <router-link
                  to="/login"
                  class="block w-full py-3 text-center text-lg text-white rounded-xl hover:text-yellow-400 transition-all duration-300 font-medium"
                  @click="closeMobileMenu"
              >
                Войти
              </router-link>
              <router-link
                  to="/register"
                  class="block w-full py-3 text-center text-lg bg-gradient-to-r from-yellow-400 to-amber-400 text-stone-800 rounded-xl hover:shadow-lg transition-all duration-300 font-medium"
                  @click="closeMobileMenu"
              >
                Регистрация
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </div>
  </header>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'
import { useAuthStore } from '@/stores/authStore'
import { useCartStore } from '@/stores/cartStore'
import { useFavoriteProductStore } from '@/stores/favoriteProductStore'

const authStore = useAuthStore()
const cartStore = useCartStore()
const favoritesStore = useFavoriteProductStore()
const isMobileMenuOpen = ref(false)
const showLogout = ref(false)

const toggleMobileMenu = () => {
  isMobileMenuOpen.value = !isMobileMenuOpen.value
}

const closeMobileMenu = () => {
  isMobileMenuOpen.value = false
}

const logout = async () => {
  await authStore.logout()
  showLogout.value = false
  closeMobileMenu()
}

const handleClickOutside = (event: Event) => {
  const target = event.target as HTMLElement
  if (!target.closest('.max-w-7xl')) {
    closeMobileMenu()
  }
}

const handleResize = () => {
  if (window.innerWidth >= 768) {
    closeMobileMenu()
  }
}

const toggleLogout = () => {
  showLogout.value = !showLogout.value
}

onMounted(() => {
  document.addEventListener('click', handleClickOutside)
  window.addEventListener('resize', handleResize)
})

onUnmounted(() => {
  document.removeEventListener('click', handleClickOutside)
  window.removeEventListener('resize', handleResize)
})
</script>
