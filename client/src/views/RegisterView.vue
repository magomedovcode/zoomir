<template>
  <div class="min-h-screen flex flex-col bg-white">
    <AppHeader />

    <div class="flex-grow container max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 mt-4">
      <div class="text-center animate-fade-in-up">
        <h2 class="text-4xl font-bold bg-gradient-to-r from-yellow-500 to-amber-500 bg-clip-text text-transparent mb-3">
          Регистрация
        </h2>
        <p class="text-stone-600 text-lg">Создайте новый аккаунт</p>
      </div>
    </div>

    <div class="relative mt-8 sm:mx-auto sm:w-full sm:max-w-md animate-fade-in-up animation-delay-300 mb-16">
      <div class="bg-gradient-to-r from-stone-800 to-stone-700 backdrop-blur-sm rounded-2xl shadow-2xl py-8 px-6 sm:px-10 transform transition-all duration-500 hover:shadow-3xl">
        <form class="space-y-6" @submit.prevent="register">
          <div class="group">
            <label for="username" class="block text-base font-medium text-white mb-2">
              Имя пользователя
            </label>
            <div class="relative">
              <input
                  id="username"
                  v-model="userData.username"
                  type="text"
                  required
                  class="block w-full pl-6 pr-3 py-3 rounded-xl placeholder-stone-400 focus:outline-none focus:ring-2 focus:ring-yellow-500 focus:border-yellow-500 transition-all duration-300 bg-stone-700 backdrop-blur-sm group-hover:border-yellow-300"
                  placeholder="Введите имя пользователя"
              >
            </div>
          </div>

          <div class="group">
            <label for="password" class="block text-base font-medium text-white mb-2">
              Пароль
            </label>
            <div class="relative">
              <input
                  id="password"
                  v-model="userData.password"
                  type="password"
                  required
                  class="block w-full pl-6 pr-3 py-3 rounded-xl placeholder-stone-400 focus:outline-none focus:ring-2 focus:ring-yellow-500 focus:border-yellow-500 transition-all duration-300 bg-stone-700 backdrop-blur-sm group-hover:border-yellow-300"
                  placeholder="Введите пароль"
              >
            </div>
          </div>

          <div
              v-if="authStore.error"
              class="bg-red-50 border border-red-200 rounded-xl p-4 transform transition-all duration-300 animate-shake"
          >
            <div class="flex items-center">
              <svg class="h-5 w-5 text-red-400 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
              <p class="text-red-600 text-sm font-medium">{{ authStore.error }}</p>
            </div>
          </div>

          <div>
            <button
                type="submit"
                :disabled="authStore.isLoading"
                class="group relative w-full flex justify-center py-4 px-4 border border-transparent rounded-xl shadow-lg text-lg font-bold text-stone-800 bg-gradient-to-r from-yellow-500 to-amber-500 hover:from-yellow-600 hover:to-amber-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-yellow-500 disabled:opacity-50 transition-all duration-500 transform hover:-translate-y-1 hover:shadow-2xl disabled:hover:transform-none"
            >
              <svg
                  v-if="authStore.isLoading"
                  class="animate-spin -ml-1 mr-3 h-5 w-5 text-white"
                  fill="none"
                  viewBox="0 0 24 24"
              >
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
              </svg>

              <span class="relative z-10 flex items-center">
                {{ authStore.isLoading ? 'Вход...' : 'Создать аккаунт' }}
              </span>
            </button>
          </div>

          <div class="text-center pt-4 border-t border-stone-600">
            <router-link
                to="/login"
                class="group inline-flex items-center text-yellow-500 hover:text-yellow-600 font-medium transition-all duration-300 transform hover:-translate-y-0.5"
            >
              <span>Есть аккаунт? Авторизуйтесь</span>
              <svg class="w-4 h-4 ml-2 transform group-hover:translate-x-1 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
              </svg>
            </router-link>
          </div>
        </form>
      </div>
    </div>

    <AppFooter />
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/authStore'
import type { User } from '@/types'
import AppHeader from "@/components/AppHeader.vue";
import AppFooter from "@/components/AppFooter.vue";

const router = useRouter()
const authStore = useAuthStore()

const userData = ref<User>({
  username: '',
  password: ''
})

const register = async () => {
  await authStore.register(userData.value)
  if (authStore.isAuthenticated) {
    await router.push('/')
  }
}
</script>
