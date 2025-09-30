<template>
  <div class="min-h-screen bg-gradient-to-br from-indigo-50 via-purple-50/30 to-pink-50/20 flex flex-col justify-center py-12 sm:px-6 lg:px-8 relative overflow-hidden">
    <div class="absolute inset-0 opacity-50">
      <div class="absolute top-1/4 left-1/4 w-72 h-72 bg-indigo-200 rounded-full mix-blend-multiply filter blur-3xl animate-pulse"></div>
      <div class="absolute top-1/3 right-1/4 w-96 h-96 bg-purple-200 rounded-full mix-blend-multiply filter blur-3xl animate-pulse animation-delay-2000"></div>
      <div class="absolute bottom-1/4 left-1/3 w-80 h-80 bg-pink-200 rounded-full mix-blend-multiply filter blur-3xl animate-pulse animation-delay-4000"></div>
    </div>

    <div class="relative sm:mx-auto sm:w-full sm:max-w-md">
      <div class="text-center animate-fade-in-up">
        <h2 class="text-4xl font-bold bg-gradient-to-r from-indigo-600 to-purple-700 bg-clip-text text-transparent mb-3">
          Вход в аккаунт
        </h2>
        <p class="text-gray-600">Войдите в свой аккаунт Zoomir</p>
      </div>
    </div>

    <div class="relative mt-8 sm:mx-auto sm:w-full sm:max-w-md animate-fade-in-up animation-delay-300">
      <div class="bg-white/80 backdrop-blur-sm rounded-2xl shadow-2xl border border-white/60 py-8 px-6 sm:px-10 transform transition-all duration-500 hover:shadow-3xl">
        <form class="space-y-6" @submit.prevent="login">
          <div class="group">
            <label for="username" class="block text-sm font-medium text-gray-700 mb-2">
              Имя пользователя
            </label>
            <div class="relative">
              <input
                  id="username"
                  v-model="userData.username"
                  type="text"
                  required
                  class="block w-full pl-6 pr-3 py-3 border border-gray-300 rounded-xl placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition-all duration-300 bg-white/50 backdrop-blur-sm group-hover:border-indigo-300"
                  placeholder="Введите имя пользователя"
              >
            </div>
          </div>

          <div class="group">
            <label for="password" class="block text-sm font-medium text-gray-700 mb-2">
              Пароль
            </label>
            <div class="relative">
              <input
                  id="password"
                  v-model="userData.password"
                  type="password"
                  required
                  class="block w-full pl-6 pr-3 py-3 border border-gray-300 rounded-xl placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition-all duration-300 bg-white/50 backdrop-blur-sm group-hover:border-indigo-300"
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
                class="group relative w-full flex justify-center py-4 px-4 border border-transparent rounded-xl shadow-lg text-lg font-bold text-white bg-gradient-to-r from-indigo-600 to-purple-700 hover:from-indigo-700 hover:to-purple-800 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 disabled:opacity-50 transition-all duration-500 transform hover:-translate-y-1 hover:shadow-2xl disabled:hover:transform-none"
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
                {{ authStore.isLoading ? 'Вход...' : 'Войти' }}
              </span>
            </button>
          </div>

          <div class="text-center pt-4 border-t border-gray-200/60">
            <router-link
                to="/register"
                class="group inline-flex items-center text-indigo-600 hover:text-indigo-700 font-medium transition-all duration-300 transform hover:-translate-y-0.5"
            >
              <span>Нет аккаунта? Зарегистрируйтесь</span>
              <svg class="w-4 h-4 ml-2 transform group-hover:translate-x-1 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
              </svg>
            </router-link>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/authStore'
import type { User } from '@/types'

const router = useRouter()
const authStore = useAuthStore()

const userData = ref<User>({
  username: '',
  password: ''
})

const login = async () => {
  await authStore.login(userData.value)
  if (authStore.isAuthenticated) {
    await router.push('/')
  }
}
</script>
