<template>
  <div class="min-h-screen flex flex-col bg-gradient-to-br from-gray-50 to-blue-50/30">
    <AppHeader />

    <div class="flex-grow container max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <!-- Заголовок с градиентом -->
      <div class="text-center mb-12">
        <h1 class="text-4xl font-bold bg-gradient-to-r from-indigo-600 to-purple-700 bg-clip-text text-transparent mb-4">
          Корзина покупок
        </h1>
        <p class="text-gray-600 max-w-2xl mx-auto">Проверьте выбранные товары перед оформлением заказа</p>
      </div>

      <!-- Содержимое корзины -->
      <div v-if="cartStore.cart?.products_in_cart?.length" class="lg:grid lg:grid-cols-12 lg:gap-8">
        <!-- Список товаров -->
        <div class="lg:col-span-8">
          <div class="bg-white rounded-2xl shadow-lg border border-gray-100 overflow-hidden">
            <div class="p-6 border-b border-gray-100">
              <h2 class="text-xl font-semibold text-gray-800 flex items-center">
                <svg class="w-6 h-6 text-indigo-600 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z"/>
                </svg>
                Товары в корзине ({{ cartStore.cart.total_items }})
              </h2>
            </div>

            <ul class="divide-y divide-gray-100">
              <li v-for="item in cartStore.cart.products_in_cart" :key="item.id" class="p-6 hover:bg-gray-50/50 transition-all duration-300">
                <div class="flex space-x-6">
                  <!-- Изображение товара -->
                  <div class="flex-shrink-0 relative">
                    <img
                        :src="MEDIA_URL + item.product_variant.first_image"
                        :alt="item.product_variant.product_title"
                        class="w-24 h-24 rounded-xl object-cover object-center sm:w-32 sm:h-32 shadow-md transition-transform duration-300 hover:scale-105"
                    >
                    <div class="absolute -top-2 -right-2 bg-indigo-500 text-white text-xs font-medium px-2 py-1 rounded-full shadow-sm">
                      {{ item.quantity }} шт
                    </div>
                  </div>

                  <!-- Информация о товаре -->
                  <div class="flex-1 min-w-0">
                    <div class="flex items-start justify-between">
                      <div class="flex-1">
                        <h3 class="text-lg font-semibold text-gray-800 hover:text-indigo-600 transition-colors duration-300">
                          {{ item.product_variant.product_title }}
                        </h3>
                        <p class="mt-1 text-gray-600">Вариант: {{ item.product_variant.name }}</p>
                        <p class="mt-2 text-sm text-gray-500">
                          Цена за штуку:
                          <span class="font-medium text-indigo-600">
                            {{ Intl.NumberFormat('ru-RU', { style: 'currency', currency: 'RUB' }).format(+item.product_variant.price) }}
                          </span>
                        </p>
                      </div>

                      <!-- Цена за позицию -->
                      <div class="text-right ml-4">
                        <p class="text-xl font-bold text-gray-900">
                          {{ Intl.NumberFormat('ru-RU', { style: 'currency', currency: 'RUB' }).format(+item.product_variant.price * item.quantity) }}
                        </p>
                      </div>
                    </div>

                    <!-- Управление количеством -->
                    <div class="mt-6 flex items-center justify-between">
                      <div class="flex items-center space-x-4">
                        <span class="text-sm font-medium text-gray-700">Количество:</span>
                        <div class="flex items-center space-x-3 bg-gray-100 rounded-xl p-1">
                          <button
                              @click="updateQuantity(item.product_variant.id, item.quantity - 1)"
                              class="w-10 h-10 rounded-lg bg-white shadow-sm flex items-center justify-center text-gray-600 hover:text-indigo-600 hover:bg-indigo-50 transition-all duration-300 disabled:opacity-40 disabled:cursor-not-allowed disabled:hover:bg-white disabled:hover:text-gray-600"
                              :disabled="item.quantity <= 1 || cartStore.isLoading"
                          >
                            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 12H4"/>
                            </svg>
                          </button>

                          <span class="text-gray-800 font-semibold min-w-[2rem] text-center text-lg">{{ item.quantity }}</span>

                          <button
                              @click="updateQuantity(item.product_variant.id, item.quantity + 1)"
                              class="w-10 h-10 rounded-lg bg-white shadow-sm flex items-center justify-center text-gray-600 hover:text-indigo-600 hover:bg-indigo-50 transition-all duration-300 disabled:opacity-40 disabled:cursor-not-allowed"
                              :disabled="cartStore.isLoading"
                          >
                            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/>
                            </svg>
                          </button>
                        </div>
                      </div>

                      <!-- Кнопка удаления -->
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

        <!-- Блок итого -->
        <div class="mt-8 lg:mt-0 lg:col-span-4">
          <div class="bg-gradient-to-br from-white to-gray-50 rounded-2xl shadow-lg border border-gray-100 p-6 sticky top-8">
            <div class="flex items-center space-x-2 mb-6">
              <div class="w-10 h-10 bg-gradient-to-r from-indigo-500 to-purple-600 rounded-xl flex items-center justify-center">
                <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
                </svg>
              </div>
              <h2 class="text-xl font-bold text-gray-800">Итог заказа</h2>
            </div>

            <dl class="space-y-4">
              <div class="flex items-center justify-between py-3">
                <dt class="text-gray-600">Товары ({{ cartStore.cart.total_items }})</dt>
                <dd class="font-medium text-gray-900">{{ Intl.NumberFormat('ru-RU', { style: 'currency', currency: 'RUB' }).format(+cartStore.cart.total_price) }}</dd>
              </div>

              <div class="flex items-center justify-between py-3 border-t border-gray-200">
                <dt class="text-gray-600">Доставка</dt>
                <dd class="font-medium text-green-600">Бесплатно</dd>
              </div>

              <div class="flex items-center justify-between py-3 border-t border-gray-200">
                <dt class="text-sm text-gray-500">Налоги</dt>
                <dd class="text-sm text-gray-500">Рассчитываются при оформлении</dd>
              </div>

              <div class="flex items-center justify-between pt-4 border-t border-gray-300 mt-2">
                <dt class="text-lg font-bold text-gray-800">Общая стоимость</dt>
                <dd class="text-2xl font-bold bg-gradient-to-r from-indigo-600 to-purple-700 bg-clip-text text-transparent">
                  {{ Intl.NumberFormat('ru-RU', { style: 'currency', currency: 'RUB' }).format(+cartStore.cart.total_price) }}
                </dd>
              </div>
            </dl>

            <div class="mt-8 space-y-4">
              <button
                  @click="checkout"
                  class="w-full bg-gradient-to-r from-indigo-600 to-purple-700 hover:from-indigo-700 hover:to-purple-800 text-white font-semibold py-4 px-6 rounded-xl shadow-lg hover:shadow-xl transition-all duration-300 transform hover:-translate-y-0.5 flex items-center justify-center space-x-2"
              >
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
                </svg>
                <span>Оформить заказ</span>
              </button>

              <router-link
                  to="/chapters"
                  class="w-full border-2 border-gray-300 text-gray-700 hover:border-indigo-300 hover:bg-indigo-50 font-medium py-3 px-6 rounded-xl transition-all duration-300 flex items-center justify-center space-x-2"
              >
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"/>
                </svg>
                <span>Продолжить покупки</span>
              </router-link>
            </div>

            <!-- Дополнительная информация -->
            <div class="mt-6 pt-6 border-t border-gray-200">
              <div class="flex items-center space-x-2 text-sm text-gray-500">
                <svg class="w-4 h-4 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
                </svg>
                <span>Бесплатная доставка от 2000 ₽</span>
              </div>
              <div class="flex items-center space-x-2 text-sm text-gray-500 mt-2">
                <svg class="w-4 h-4 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
                </svg>
                <span>Возврат в течение 30 дней</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Пустая корзина -->
      <div v-else class="text-center py-16 max-w-2xl mx-auto">
        <div class="bg-white rounded-2xl shadow-lg border border-gray-100 p-12">
          <div class="w-32 h-32 mx-auto mb-8 bg-gradient-to-br from-indigo-100 to-purple-100 rounded-full flex items-center justify-center">
            <svg class="w-16 h-16 text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"/>
            </svg>
          </div>
          <h3 class="text-2xl font-bold text-gray-800 mb-4">Ваша корзина пуста</h3>
          <p class="text-gray-600 mb-8">Добавьте товары в корзину, чтобы сделать заказ и порадовать вашего питомца</p>
          <div class="space-y-4 sm:space-y-0 sm:space-x-4 sm:flex sm:justify-center">
            <router-link
                to="/chapters"
                class="inline-flex items-center px-6 py-3 bg-gradient-to-r from-indigo-600 to-purple-700 text-white font-semibold rounded-xl shadow-lg hover:shadow-xl transition-all duration-300 transform hover:-translate-y-0.5"
            >
              <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"/>
              </svg>
              Перейти в магазин
            </router-link>
            <router-link
                to="/"
                class="inline-flex items-center px-6 py-3 border-2 border-gray-300 text-gray-700 font-medium rounded-xl hover:border-indigo-300 hover:bg-indigo-50 transition-all duration-300"
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
import { onMounted } from 'vue'
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