<template>
  <div class="min-h-screen flex flex-col bg-gray-50">
    <AppHeader />

    <div class="flex-grow container max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <h1 class="text-3xl font-bold mb-8">Корзина</h1>

      <div v-if="cartStore.cart?.products_in_cart?.length" class="lg:grid lg:grid-cols-12 lg:gap-x-12">
        <!-- Список товаров -->
        <div class="lg:col-span-7">
          <ul class="border-b border-gray-200 divide-y divide-gray-200">
            <li v-for="item in cartStore.cart.products_in_cart" :key="item.id" class="flex py-6">
              <div class="flex-shrink-0">
                <img
                    :src="MEDIA_URL + item.product_variant.first_image"
                    :alt="item.product_variant.product_title"
                    class="w-24 h-24 rounded-md object-cover object-center sm:w-32 sm:h-32"
                >
              </div>

              <div class="ml-4 flex-1 flex flex-col sm:ml-6">
                <div>
                  <div class="flex justify-between">
                    <h4 class="text-sm font-medium text-gray-700">
                      {{ item.product_variant.product_title }}
                    </h4>
                    <p class="ml-4 text-sm font-medium text-gray-900">{{ Intl.NumberFormat('ru-RU', { style: 'currency', currency: 'RUB' }).format(+item.product_variant.price * item.quantity) }}</p>
                  </div>
                  <p class="mt-1 text-sm text-gray-500">Вариант: {{ item.product_variant.name }}</p>
                  <p class="mt-1 text-sm text-gray-500">Цена за штуку: {{ Intl.NumberFormat('ru-RU', { style: 'currency', currency: 'RUB' }).format(+item.product_variant.price) }}</p>
                </div>

                <div class="mt-4 flex-1 flex items-end justify-between">
                  <div class="flex items-center space-x-3">
                    <button
                        @click="updateQuantity(item.product_variant.id, item.quantity - 1)"
                        class="w-8 h-8 rounded-full border border-gray-300 flex items-center justify-center text-gray-400 hover:text-gray-600 hover:border-gray-400 disabled:opacity-50 disabled:cursor-not-allowed"
                        :disabled="item.quantity <= 1 || cartStore.isLoading"
                    >
                      <span class="sr-only">Уменьшить</span>
                      <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 12H4"/>
                      </svg>
                    </button>

                    <span class="text-gray-700 font-medium min-w-[2rem] text-center">{{ item.quantity }}</span>

                    <button
                        @click="updateQuantity(item.product_variant.id, item.quantity + 1)"
                        class="w-8 h-8 rounded-full border border-gray-300 flex items-center justify-center text-gray-400 hover:text-gray-600 hover:border-gray-400 disabled:opacity-50 disabled:cursor-not-allowed"
                        :disabled="cartStore.isLoading"
                    >
                      <span class="sr-only">Увеличить</span>
                      <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/>
                      </svg>
                    </button>
                  </div>

                  <button
                      @click="removeFromCart(item.product_variant.id)"
                      type="button"
                      class="ml-4 text-sm font-medium text-indigo-600 hover:text-indigo-500"
                  >
                    Удалить
                  </button>
                </div>
              </div>
            </li>
          </ul>
        </div>

        <!-- Итоги заказа -->
        <div class="mt-16 lg:mt-0 lg:col-span-5">
          <div class="bg-white rounded-lg shadow-sm border p-6">
            <h2 class="text-lg font-medium text-gray-900">Итого</h2>

            <dl class="mt-6 space-y-4">
              <div class="flex items-center justify-between">
                <dt class="text-sm text-gray-600">Количество товаров</dt>
                <dd class="text-sm font-medium text-gray-900">{{ cartStore.cart.total_items }}</dd>
              </div>
              <div class="flex items-center justify-between border-t border-gray-200 pt-4">
                <dt class="text-base font-medium text-gray-900">Общая стоимость</dt>
                <dd class="text-base font-medium text-gray-900">{{ Intl.NumberFormat('ru-RU', { style: 'currency', currency: 'RUB' }).format(+cartStore.cart.total_price) }}</dd>
              </div>
            </dl>

            <div class="mt-6">
              <button
                  @click="checkout"
                  class="w-full bg-indigo-600 border border-transparent rounded-md shadow-sm py-3 px-4 text-base font-medium text-white hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
              >
                Оформить заказ
              </button>
            </div>
          </div>
        </div>
      </div>

      <div v-else class="text-center py-12">
        <svg class="mx-auto h-24 w-24 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"/>
        </svg>
        <h3 class="mt-4 text-lg font-medium text-gray-900">Корзина пуста</h3>
        <p class="mt-2 text-gray-500">Добавьте товары в корзину, чтобы сделать заказ.</p>
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
import {onMounted} from 'vue'
import { useRouter } from 'vue-router'
import AppHeader from '@/components/AppHeader.vue'
import { useCartStore } from '@/stores/cartStore'
import { MEDIA_URL } from '@/services/baseURL'
import AppFooter from "@/components/AppFooter.vue";

const router = useRouter()
const cartStore = useCartStore()

onMounted(async () => {
  await cartStore.fetchCart();
})

const updateQuantity = async (productId: number, newQuantity: number) => {
  if (newQuantity < 1) return
  await cartStore.updateQuantity(productId, newQuantity)
}

const removeFromCart = async (itemId: number) => {
  await cartStore.removeFromCart(itemId)
  await cartStore.fetchCart()
}

const checkout = () => {
  router.push('/checkout')
}
</script>
