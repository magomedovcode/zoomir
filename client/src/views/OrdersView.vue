<template>
  <div class="min-h-screen flex flex-col bg-gray-50">
    <AppHeader />

    <div class="flex-grow container max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <h1 class="text-3xl font-bold mb-8">Мои заказы</h1>

      <div v-if="orderStore.orders.length" class="space-y-6">
        <div v-for="order in orderStore.orders" :key="order.id" class="bg-white rounded-lg shadow-sm border p-6">
          <div class="flex justify-between items-start mb-4">
            <div>
              <h3 class="text-lg font-medium">Заказ #{{ order.id }}</h3>
              <p class="text-sm text-gray-500">от {{ formatDate(order.date) }}</p>
            </div>
            <span class="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium" :class="statusClasses[order.status]">
              {{ statusLabels[order.status] }}
            </span>
          </div>

          <div class="border-t border-gray-200 pt-4">
            <h4 class="font-medium mb-2">Товары:</h4>
            <ul class="divide-y divide-gray-200">
              <li v-for="item in order.products_in_order" :key="item.id" class="py-3 flex justify-between">
                <div class="flex">
                  <img
                      :src="MEDIA_URL + item.product_variant.first_image"
                      :alt="item.product_variant.product_title"
                      class="h-16 w-16 rounded-md object-cover"
                  >
                  <div class="ml-4">
                    <p class="text-sm font-medium text-gray-900">{{ item.product_variant.product_title }}, {{ item.product_variant.name }}</p>
                    <p class="text-sm text-gray-500">Количество: {{ item.quantity }}</p>
                    <p class="text-sm text-gray-500">Цена за штуку: {{ Intl.NumberFormat('ru-RU', { style: 'currency', currency: 'RUB' }).format(+item.price) }}</p>
                  </div>
                </div>
                <p class="text-sm font-medium text-gray-900">{{ Intl.NumberFormat('ru-RU', { style: 'currency', currency: 'RUB' }).format(+item.price * item.quantity) }}</p>
              </li>
            </ul>
          </div>

          <div class="border-t border-gray-200 pt-4 flex justify-between items-center">
            <div>
              <p class="text-sm text-gray-600">Адрес доставки: {{ order.address }}</p>
              <p class="text-sm text-gray-600">Телефон: {{ order.phone }}</p>
              <p class="text-sm text-gray-600">Дата доставки: {{ formatDate(order.delivery_date) }}</p>
            </div>
            <p class="text-lg font-bold">Итого: {{ Intl.NumberFormat('ru-RU', { style: 'currency', currency: 'RUB' }).format(order.total_price) }}</p>
          </div>
        </div>
      </div>

      <div v-else class="text-center py-12">
        <svg class="mx-auto h-24 w-24 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z"/>
        </svg>
        <h3 class="mt-4 text-lg font-medium text-gray-900">Заказов пока нет</h3>
        <p class="mt-2 text-gray-500">Сделайте свой первый заказ!</p>
        <div class="mt-6">
          <router-link to="/shop" class="inline-flex items-center px-4 py-2 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700">
            В магазин
          </router-link>
        </div>
      </div>
    </div>

    <AppFooter />
  </div>
</template>

<script setup lang="ts">
import { onMounted } from 'vue'
import AppHeader from '@/components/AppHeader.vue'
import { useOrderStore } from '@/stores/orderStore'
import { Status } from '@/types'
import { MEDIA_URL } from '@/services/baseURL'
import AppFooter from "@/components/AppFooter.vue";

const orderStore = useOrderStore()

const statusLabels = {
  [Status.PENDING]: 'В обработке',
  [Status.CONFIRMED]: 'Подтвержден',
  [Status.SHIPPED]: 'Отправлен',
  [Status.DELIVERED]: 'Доставлен',
  [Status.CANCELED]: 'Отменен'
}

const statusClasses = {
  [Status.PENDING]: 'bg-yellow-100 text-yellow-800',
  [Status.CONFIRMED]: 'bg-blue-100 text-blue-800',
  [Status.SHIPPED]: 'bg-indigo-100 text-indigo-800',
  [Status.DELIVERED]: 'bg-green-100 text-green-800',
  [Status.CANCELED]: 'bg-red-100 text-red-800'
}

onMounted(async () => {
  await orderStore.fetchOrders()
})

const formatDate = (dateString: string) => {
  return new Date(dateString).toLocaleDateString('ru-RU')
}
</script>