<template>
  <div class="min-h-screen flex flex-col bg-white">
    <AppHeader />

    <div class="flex-grow container max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <div class="text-center mb-8 sm:mb-12 mt-4">
        <h1 class="text-2xl sm:text-4xl font-bold bg-gradient-to-r from-yellow-500 to-amber-500 bg-clip-text text-transparent mb-2 sm:mb-4">
          Корзина покупок
        </h1>
        <p class="text-sm sm:text-base text-stone-600 max-w-2xl mx-auto">Проверьте выбранные товары перед оформлением заказа</p>
      </div>

      <div v-if="cartStore.cart?.products_in_cart?.length" class="lg:grid lg:grid-cols-12 lg:gap-8">
        <div class="lg:col-span-8">
          <div class="bg-white rounded-xl sm:rounded-2xl shadow-lg border border-gray-300 overflow-hidden">
            <div class="p-4 sm:p-6 border-b border-gray-300">
              <h2 class="text-lg sm:text-xl font-semibold text-stone-800 flex items-center justify-center sm:justify-start">
                <svg class="w-5 h-5 sm:w-6 sm:h-6 text-yellow-500 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z"/>
                </svg>
                Товары в корзине ({{ cartStore.cart.total_items }})
              </h2>
            </div>

            <ul class="divide-y divide-stone-300">
              <li v-for="item in cartStore.cart.products_in_cart" :key="item.id" class="p-4 sm:p-6 hover:bg-stone-50/50 transition-all duration-300">
                <div class="block sm:hidden">
                  <div class="flex justify-between items-start mb-3">
                    <router-link
                        :to="getProductLink(item)"
                        class="flex-shrink-0 relative"
                    >
                      <img
                          :src="MEDIA_URL + item.product_variant.first_image"
                          :alt="item.product_variant.product_title"
                          class="w-16 h-16 rounded-lg object-cover object-center shadow-md"
                      >
                      <div class="absolute -top-1 -right-1 bg-yellow-500 text-white text-xs font-medium px-1.5 py-0.5 rounded-full shadow-sm">
                        {{ item.quantity }} шт
                      </div>
                    </router-link>

                    <button
                        @click="removeFromCart(item.product_variant.id)"
                        type="button"
                        class="p-2 text-red-600 hover:text-red-700 hover:bg-red-50 rounded-lg transition-all duration-300"
                    >
                      <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"/>
                      </svg>
                    </button>
                  </div>

                  <div class="space-y-2">
                    <router-link
                        :to="getProductLink(item)"
                        class="text-base font-semibold text-stone-800 hover:text-yellow-500 transition-colors duration-300 line-clamp-2"
                    >
                      {{ item.product_variant.product_title }}
                    </router-link>

                    <p class="text-sm text-stone-600">Вариант: {{ item.product_variant.name }}</p>

                    <div class="flex justify-between items-center">
                      <p class="text-sm text-stone-500">
                        Цена:
                        <span class="font-medium text-yellow-500">
                          {{ Intl.NumberFormat('ru-RU', { style: 'currency', currency: 'RUB' }).format(+item.product_variant.price) }}
                        </span>
                      </p>
                      <p class="text-lg font-bold text-stone-900">
                        {{ Intl.NumberFormat('ru-RU', { style: 'currency', currency: 'RUB' }).format(+item.product_variant.price * item.quantity) }}
                      </p>
                    </div>

                    <div class="flex items-center justify-between pt-2">
                      <span class="text-sm font-medium text-stone-700">Кол-во:</span>
                      <div class="flex items-center space-x-2 bg-stone-100 rounded-lg p-1">
                        <button
                            @click="updateQuantity(item.product_variant.id, item.quantity - 1)"
                            class="w-8 h-8 rounded-lg bg-white shadow-sm flex items-center justify-center text-stone-600 hover:text-yellow-500 hover:bg-yellow-50 transition-all duration-300 disabled:opacity-40 disabled:cursor-not-allowed disabled:hover:bg-white disabled:hover:text-stone-600"
                            :disabled="item.quantity <= 1 || cartStore.isLoading"
                        >
                          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 12H4"/>
                          </svg>
                        </button>

                        <span class="text-stone-800 font-semibold min-w-[1.5rem] text-center">{{ item.quantity }}</span>

                        <button
                            @click="updateQuantity(item.product_variant.id, item.quantity + 1)"
                            class="w-8 h-8 rounded-lg bg-white shadow-sm flex items-center justify-center text-stone-600 hover:text-yellow-500 hover:bg-yellow-50 transition-all duration-300 disabled:opacity-40 disabled:cursor-not-allowed"
                            :disabled="cartStore.isLoading"
                        >
                          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/>
                          </svg>
                        </button>
                      </div>
                    </div>
                  </div>
                </div>

                <div class="hidden sm:flex space-x-6">
                  <router-link
                      :to="getProductLink(item)"
                      class="flex-shrink-0 relative"
                  >
                    <img
                        :src="MEDIA_URL + item.product_variant.first_image"
                        :alt="item.product_variant.product_title"
                        class="w-24 h-24 rounded-xl object-cover object-center sm:w-32 sm:h-32 shadow-md transition-transform duration-300 hover:scale-105"
                    >
                    <div class="absolute -top-2 -right-2 bg-yellow-500 text-white text-xs font-medium px-2 py-1 rounded-full shadow-sm">
                      {{ item.quantity }} шт
                    </div>
                  </router-link>

                  <div class="flex-1 min-w-0">
                    <div class="flex items-start justify-between">
                      <div class="flex-1">
                        <router-link
                            :to="getProductLink(item)"
                            class="text-lg font-semibold text-stone-800 hover:text-yellow-500 transition-colors duration-300"
                        >
                          {{ item.product_variant.product_title }}
                        </router-link>
                        <p class="mt-1 text-stone-600">Вариант: {{ item.product_variant.name }}</p>
                        <p class="mt-2 text-sm text-stone-500">
                          Цена за штуку:
                          <span class="font-medium text-yellow-500">
                            {{ Intl.NumberFormat('ru-RU', { style: 'currency', currency: 'RUB' }).format(+item.product_variant.price) }}
                          </span>
                        </p>
                      </div>

                      <div class="text-right ml-4">
                        <p class="text-xl font-bold text-stone-900">
                          {{ Intl.NumberFormat('ru-RU', { style: 'currency', currency: 'RUB' }).format(+item.product_variant.price * item.quantity) }}
                        </p>
                      </div>
                    </div>

                    <div class="mt-6 flex items-center justify-between">
                      <div class="flex items-center space-x-4">
                        <span class="text-sm font-medium text-stone-700">Количество:</span>
                        <div class="flex items-center space-x-3 bg-stone-100 rounded-xl p-1">
                          <button
                              @click="updateQuantity(item.product_variant.id, item.quantity - 1)"
                              class="w-10 h-10 rounded-lg bg-white shadow-sm flex items-center justify-center text-stone-600 hover:text-yellow-500 hover:bg-yellow-50 transition-all duration-300 disabled:opacity-40 disabled:cursor-not-allowed disabled:hover:bg-white disabled:hover:text-stone-600"
                              :disabled="item.quantity <= 1 || cartStore.isLoading"
                          >
                            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 12H4"/>
                            </svg>
                          </button>

                          <span class="text-stone-800 font-semibold min-w-[2rem] text-center text-lg">{{ item.quantity }}</span>

                          <button
                              @click="updateQuantity(item.product_variant.id, item.quantity + 1)"
                              class="w-10 h-10 rounded-lg bg-white shadow-sm flex items-center justify-center text-stone-600 hover:text-yellow-500 hover:bg-yellow-50 transition-all duration-300 disabled:opacity-40 disabled:cursor-not-allowed"
                              :disabled="cartStore.isLoading"
                          >
                            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/>
                            </svg>
                          </button>
                        </div>
                      </div>

                      <button
                          @click="removeFromCart(item.product_variant.id)"
                          type="button"
                          class="flex items-center space-x-2 px-4 py-2 text-red-600 hover:text-red-700 hover:bg-red-50 rounded-xl transition-all duration-300 font-medium"
                      >
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"/>
                        </svg>
                        <span>Удалить</span>
                      </button>
                    </div>
                  </div>
                </div>
              </li>
            </ul>
          </div>
        </div>

        <div class="mt-6 lg:mt-0 lg:col-span-4">
          <div class="bg-gradient-to-br from-white to-stone-50 rounded-xl sm:rounded-2xl shadow-lg border border-gray-300 p-4 sm:p-6 lg:sticky lg:top-24">
            <div class="flex items-center space-x-2 mb-4 sm:mb-6">
              <div class="w-8 h-8 sm:w-10 sm:h-10 bg-gradient-to-r from-yellow-400 to-amber-500 rounded-lg sm:rounded-xl flex items-center justify-center">
                <svg class="w-4 h-4 sm:w-6 sm:h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
                </svg>
              </div>
              <h2 class="text-lg sm:text-xl font-bold text-stone-800">Итог заказа</h2>
            </div>

            <dl class="space-y-3 sm:space-y-4">
              <div class="flex items-center justify-between py-2 sm:py-3">
                <dt class="text-sm sm:text-base text-stone-600">Товары ({{ cartStore.cart.total_items }})</dt>
                <dd class="font-medium text-stone-900">{{ Intl.NumberFormat('ru-RU', { style: 'currency', currency: 'RUB' }).format(+cartStore.cart.total_price) }}</dd>
              </div>

              <div class="flex items-center justify-between py-2 sm:py-3 border-t border-stone-300">
                <dt class="text-sm sm:text-base text-stone-600">Доставка</dt>
                <dd class="font-medium text-green-600">Бесплатно</dd>
              </div>

              <div class="flex items-center justify-between pt-3 sm:pt-4 border-t border-stone-300 mt-2">
                <dt class="text-base sm:text-lg font-bold text-stone-800">Общая стоимость</dt>
                <dd class="text-xl sm:text-2xl font-bold bg-gradient-to-r from-yellow-500 to-amber-500 bg-clip-text text-transparent">
                  {{ Intl.NumberFormat('ru-RU', { style: 'currency', currency: 'RUB' }).format(+cartStore.cart.total_price) }}
                </dd>
              </div>
            </dl>

            <div class="mt-6 space-y-3 sm:space-y-4">
              <button
                  @click="checkout"
                  class="w-full bg-gradient-to-r from-yellow-500 to-amber-500 hover:from-yellow-600 hover:to-amber-600 text-white font-semibold py-3 sm:py-4 px-6 rounded-lg sm:rounded-xl shadow-lg hover:shadow-xl transition-all duration-300 flex items-center justify-center space-x-2"
              >
                <svg class="w-4 h-4 sm:w-5 sm:h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
                </svg>
                <span class="text-sm sm:text-base">Оформить заказ</span>
              </button>

              <router-link
                  to="/chapters"
                  class="w-full border-2 border-stone-300 text-stone-700 hover:border-yellow-400 hover:bg-yellow-50 font-medium py-2 sm:py-3 px-6 rounded-lg sm:rounded-xl transition-all duration-300 flex items-center justify-center space-x-2"
              >
                <svg class="w-4 h-4 sm:w-5 sm:h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"/>
                </svg>
                <span class="text-sm sm:text-base">Продолжить покупки</span>
              </router-link>
            </div>
          </div>
        </div>
      </div>

      <div v-else class="text-center py-12 sm:py-16 max-w-2xl mx-auto">
        <div class="bg-white rounded-xl sm:rounded-2xl shadow-lg border border-stone-100 p-6 sm:p-12">
          <div class="w-24 h-24 sm:w-32 sm:h-32 mx-auto mb-6 sm:mb-8 bg-gradient-to-br from-yellow-100 to-amber-100 rounded-full flex items-center justify-center">
            <svg class="w-12 h-12 sm:w-16 sm:h-16 text-yellow-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"/>
            </svg>
          </div>
          <h3 class="text-xl sm:text-2xl font-bold text-stone-800 mb-3 sm:mb-4">Ваша корзина пуста</h3>
          <p class="text-sm sm:text-base text-stone-600 mb-6 sm:mb-8">Добавьте товары в корзину, чтобы сделать заказ и порадовать вашего питомца</p>
          <div class="space-y-3 sm:space-y-0 sm:space-x-4 sm:flex sm:justify-center">
            <router-link
                to="/chapters"
                class="inline-flex items-center px-4 py-2 sm:px-6 sm:py-3 bg-gradient-to-r from-yellow-500 to-amber-500 text-white font-semibold rounded-lg sm:rounded-xl shadow-lg hover:shadow-xl transition-all duration-300 transform hover:-translate-y-0.5 text-sm sm:text-base"
            >
              <svg class="w-4 h-4 sm:w-5 sm:h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"/>
              </svg>
              Перейти в магазин
            </router-link>
            <router-link
                to="/"
                class="inline-flex items-center px-4 py-2 sm:px-6 sm:py-3 border-2 border-stone-300 text-stone-700 font-medium rounded-lg sm:rounded-xl hover:border-yellow-300 hover:bg-yellow-50 transition-all duration-300 text-sm sm:text-base"
            >
              На главную
            </router-link>
          </div>
        </div>
      </div>
    </div>

    <AppFooter />
  </div>
</template>

<script setup lang="ts">
import {computed, onMounted} from 'vue'
import { useRouter } from 'vue-router'
import AppHeader from '@/components/AppHeader.vue'
import { useCartStore } from '@/stores/cartStore'
import { MEDIA_URL } from '@/services/baseURL'
import AppFooter from "@/components/AppFooter.vue";
import type {ProductInCart} from "@/types";

const router = useRouter()
const cartStore = useCartStore()

onMounted(async () => {
  await cartStore.fetchCart();
})

const getProductLink = (item: ProductInCart) => {
  return {
    path: `/details/${item.product_variant.product_id}`,
    query: {
      variant: item.product_variant.id.toString()
    }
  }
}

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
