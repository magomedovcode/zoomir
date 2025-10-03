<template>
  <div class="min-h-screen flex flex-col bg-white">
    <AppHeader />

    <div class="flex-grow container max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 mt-4">
      <div class="text-center mb-12">
        <h1 class="text-4xl font-bold bg-gradient-to-r from-yellow-500 to-amber-500 bg-clip-text text-transparent mb-4">
          Мои заказы
        </h1>
        <p class="text-stone-600 max-w-2xl mx-auto text-lg">История ваших покупок и текущие заказы</p>
      </div>

      <div v-if="orderStore.orders.length" class="space-y-4 md:space-y-6">
        <div
            v-for="order in orderStore.orders"
            :key="order.id"
            class="bg-white rounded-xl md:rounded-2xl shadow-lg border border-stone-300 overflow-hidden hover:shadow-xl transition-all duration-500"
        >
          <!-- Заголовок заказа -->
          <div class="bg-white p-4 md:p-6 border-b border-stone-300">
            <div class="flex flex-col gap-3 md:gap-4">
              <div class="flex items-start justify-between">
                <div class="flex items-center space-x-3">
                  <div class="w-10 h-10 md:w-12 md:h-12 bg-white rounded-lg md:rounded-xl shadow-sm border border-stone-300 flex items-center justify-center flex-shrink-0">
                    <svg class="w-5 h-5 md:w-6 md:h-6 text-yellow-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z"/>
                    </svg>
                  </div>
                  <div class="min-w-0">
                    <h3 class="text-lg md:text-xl font-bold text-stone-800 truncate">Заказ #{{ order.id }}</h3>
                    <p class="text-sm md:text-base text-stone-600 flex items-center space-x-1 mt-1">
                      <svg class="w-3 h-3 md:w-4 md:h-4 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/>
                      </svg>
                      <span class="truncate">{{ formatDate(order.date) }}</span>
                    </p>
                  </div>
                </div>
              </div>

              <!-- Статус заказа -->
              <div class="flex justify-start">
                <span class="inline-flex items-center px-3 py-1.5 md:px-4 md:py-2 rounded-full text-xs md:text-sm font-medium shadow-sm w-fit" :class="statusClasses[order.status]">
                  <span class="w-1.5 h-1.5 md:w-2 md:h-2 rounded-full mr-1.5 md:mr-2" :class="statusDotClasses[order.status]"></span>
                  {{ statusLabels[order.status] }}
                </span>
              </div>
            </div>
          </div>

          <!-- Состав заказа -->
          <div class="p-4 md:p-6">
            <h4 class="text-base md:text-lg font-semibold text-stone-800 mb-3 md:mb-4 flex items-center">
              <svg class="w-4 h-4 md:w-5 md:h-5 text-yellow-500 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4"/>
              </svg>
              Состав заказа
            </h4>

            <div class="space-y-3 md:space-y-4">
              <div
                  v-for="item in order.products_in_order"
                  :key="item.id"
                  class="flex items-center space-x-3 md:space-x-4 p-3 md:p-4 bg-white rounded-lg md:rounded-xl hover:bg-white transition-all duration-300 group"
              >
                <router-link
                    :to="getProductLink(item)"
                    class="relative flex-shrink-0">
                  <img
                      :src="MEDIA_URL + item.product_variant.first_image"
                      :alt="item.product_variant.product_title"
                      class="h-16 w-16 md:h-20 md:w-20 rounded-lg md:rounded-xl object-cover shadow-sm group-hover:shadow-md transition-all duration-300"
                  >
                  <div class="absolute -top-1 -right-1 md:-top-2 md:-right-2 bg-yellow-500 text-white text-xs font-bold px-1.5 py-0.5 md:px-2 md:py-1 rounded-full shadow-sm text-[10px] md:text-xs">
                    ×{{ item.quantity }}
                  </div>
                </router-link>

                <div class="flex-1 min-w-0">
                  <router-link
                      :to="getProductLink(item)"
                      class="font-medium text-stone-800 group-hover:text-yellow-500 transition-colors duration-300 text-sm md:text-base truncate">
                    {{ item.product_variant.product_title }}
                  </router-link>
                  <p class="text-xs md:text-sm text-stone-600 mt-1 truncate">Вариант: {{ item.product_variant.name }}</p>
                  <p class="text-xs md:text-sm text-stone-500 mt-1">
                    {{ Intl.NumberFormat('ru-RU', { style: 'currency', currency: 'RUB' }).format(+item.price) }} × {{ item.quantity }}
                  </p>
                </div>

                <div class="text-right flex-shrink-0">
                  <p class="text-base md:text-lg font-bold text-stone-800">
                    {{ Intl.NumberFormat('ru-RU', { style: 'currency', currency: 'RUB' }).format(+item.price * item.quantity) }}
                  </p>
                </div>
              </div>
            </div>
          </div>

          <!-- Футер заказа -->
          <div class="p-6 bg-gradient-to-r from-stone-800 to-stone-700">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div>
                <h5 class="font-semibold text-white mb-3 flex items-center">
                  <svg class="w-5 h-5 text-yellow-500 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/>
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/>
                  </svg>
                  Информация о доставке
                </h5>
                <div class="space-y-2 text-sm text-stone-300">
                  <p class="flex items-center space-x-2">
                    <span class="font-medium">Адрес:</span>
                    <span class="text-white">{{ order.address }}</span>
                  </p>
                  <p class="flex items-center space-x-2">
                    <span class="font-medium">Телефон:</span>
                    <span class="text-white">{{ order.phone }}</span>
                  </p>
                  <p class="flex items-center space-x-2">
                    <span class="font-medium">Дата доставки:</span>
                    <span class="text-white">{{ formatDate(order.delivery_date) }}</span>
                  </p>
                </div>
              </div>

              <div class="flex flex-col justify-end items-end">
                <div class="text-right">
                  <p class="text-sm text-stone-300 mb-2">Общая стоимость заказа</p>
                  <p class="text-3xl font-bold bg-gradient-to-r from-yellow-500 to-amber-600 bg-clip-text text-transparent">
                    {{ Intl.NumberFormat('ru-RU', { style: 'currency', currency: 'RUB' }).format(order.total_price) }}
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div v-else class="text-center py-16 max-w-2xl mx-auto">
        <div class="bg-white rounded-2xl shadow-lg border border-stone-300 p-12">
          <div class="w-32 h-32 mx-auto mb-8 bg-gradient-to-br from-yellow-100 to-amber-100 rounded-full flex items-center justify-center">
            <svg class="w-16 h-16 text-yellow-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z"/>
            </svg>
          </div>
          <h3 class="text-2xl font-bold text-stone-800 mb-4">Заказов пока нет</h3>
          <p class="text-stone-600 mb-8">Сделайте свой первый заказ и порадуйте вашего питомца!</p>
          <div class="space-y-4 sm:space-y-0 sm:space-x-4 sm:flex sm:justify-center">
            <router-link
                to="/chapters"
                class="inline-flex items-center px-6 py-3 bg-gradient-to-r from-yellow-500 to-amber-500 text-white font-semibold rounded-xl shadow-lg hover:shadow-xl transition-all duration-300 transform hover:-translate-y-0.5"
            >
              <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"/>
              </svg>
              Перейти в магазин
            </router-link>
            <router-link
                to="/"
                class="inline-flex items-center px-6 py-3 border-2 border-stone-300 text-stone-700 font-medium rounded-xl hover:border-yellow-400 hover:bg-yellow-50 transition-all duration-300"
            >
              На главную
            </router-link>
          </div>
        </div>
      </div>

      <div class="flex justify-center mt-12" v-if="orderStore.totalCount > orderStore.pageSize">
        <div class="flex items-center space-x-2 bg-white rounded-2xl shadow-lg border border-stone-300 p-2">
          <button
              @click="loadPage(orderStore.currentPage - 1)"
              :disabled="orderStore.currentPage === 1"
              class="flex items-center space-x-2 px-4 py-3 rounded-xl text-stone-600 hover:text-yellow-500 hover:bg-yellow-50 transition-all duration-300 disabled:opacity-40 disabled:cursor-not-allowed disabled:hover:bg-transparent"
          >
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/>
            </svg>
            <span class="font-medium">Назад</span>
          </button>

          <div class="flex items-center space-x-1 mx-4">
            <span class="px-4 py-2 bg-gradient-to-r from-yellow-500 to-amber-500 text-white font-semibold rounded-lg">
              {{ orderStore.currentPage }}
            </span>
            <span class="text-stone-500 mx-2">из</span>
            <span class="text-stone-700 font-medium">
              {{ Math.ceil(orderStore.totalCount / orderStore.pageSize) }}
            </span>
          </div>

          <button
              @click="loadPage(orderStore.currentPage + 1)"
              :disabled="orderStore.currentPage * orderStore.pageSize >= orderStore.totalCount"
              class="flex items-center space-x-2 px-4 py-3 rounded-xl text-stone-600 hover:text-yellow-500 hover:bg-yellow-50 transition-all duration-300 disabled:opacity-40 disabled:cursor-not-allowed disabled:hover:bg-transparent"
          >
            <span class="font-medium">Вперед</span>
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
            </svg>
          </button>
        </div>
      </div>
    </div>

    <AppFooter />
  </div>
</template>

<script setup lang="ts">
import {computed, onMounted} from 'vue'
import AppHeader from '@/components/AppHeader.vue'
import { useOrderStore } from '@/stores/orderStore'
import {type ProductInCart, Status} from '@/types'
import { MEDIA_URL } from '@/services/baseURL'
import AppFooter from "@/components/AppFooter.vue";

const orderStore = useOrderStore()

const getProductLink = (item: ProductInCart) => {
  return {
    path: `/details/${item.product_variant.product_id}`,
    query: {
      variant: item.product_variant.id.toString()
    }
  }
}

const statusLabels = {
  [Status.PENDING]: 'В обработке',
  [Status.CONFIRMED]: 'Подтвержден',
  [Status.SHIPPED]: 'Отправлен',
  [Status.DELIVERED]: 'Доставлен',
  [Status.CANCELLED]: 'Отменен'
}

const statusClasses = {
  [Status.PENDING]: 'bg-yellow-50 text-yellow-800 border border-yellow-200',
  [Status.CONFIRMED]: 'bg-blue-50 text-blue-800 border border-blue-200',
  [Status.SHIPPED]: 'bg-indigo-50 text-indigo-800 border border-indigo-200',
  [Status.DELIVERED]: 'bg-green-50 text-green-800 border border-green-200',
  [Status.CANCELLED]: 'bg-red-50 text-red-800 border border-red-200'
}

const statusDotClasses = {
  [Status.PENDING]: 'bg-yellow-500',
  [Status.CONFIRMED]: 'bg-blue-500',
  [Status.SHIPPED]: 'bg-indigo-500',
  [Status.DELIVERED]: 'bg-green-500',
  [Status.CANCELLED]: 'bg-red-500'
}

onMounted(async () => {
  await orderStore.fetchOrders()
})

const loadPage = (page: number) => {
  orderStore.currentPage = page;
  orderStore.fetchOrders();
}

const formatDate = (dateString: string) => {
  return new Date(dateString).toLocaleDateString('ru-RU', {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  })
}
</script>
