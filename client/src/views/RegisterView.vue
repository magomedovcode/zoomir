<template>
  <div class="min-h-screen bg-gray-50 flex flex-col justify-center py-12 sm:px-6 lg:px-8">
    <div class="sm:mx-auto sm:w-full sm:max-w-md">
      <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900">
        Регистрация
      </h2>
    </div>

    <div class="mt-8 sm:mx-auto sm:w-full sm:max-w-md">
      <div class="bg-white py-8 px-4 shadow sm:rounded-lg sm:px-10">
        <form class="space-y-6" @submit.prevent="register">
          <div>
            <label for="username" class="block text-sm font-medium text-gray-700">
              Имя пользователя
            </label>
            <div class="mt-1">
              <input
                  id="username"
                  v-model="userData.username"
                  type="text"
                  required
                  class="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500"
              >
            </div>
          </div>

          <div>
            <label for="password" class="block text-sm font-medium text-gray-700">
              Пароль
            </label>
            <div class="mt-1">
              <input
                  id="password"
                  v-model="userData.password"
                  type="password"
                  required
                  class="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500"
              >
            </div>
          </div>

          <div v-if="authStore.error" class="bg-red-50 border border-red-200 rounded-md p-4">
            <p class="text-red-600 text-sm">{{ authStore.error }}</p>
          </div>

          <div>
            <button
                type="submit"
                :disabled="authStore.isLoading"
                class="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 disabled:opacity-50"
            >
              {{ authStore.isLoading ? 'Вход...' : 'Войти' }}
            </button>
          </div>

          <div class="text-center">
            <router-link to="/login" class="text-indigo-600 hover:text-indigo-500">
              Уже есть аккаунт? Авторизуйтесь!
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

const register = async () => {
  await authStore.register(userData.value)
  if (authStore.isAuthenticated) {
    await router.push('/')
  }
}
</script>
