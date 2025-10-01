<template>
  <div class="min-h-screen flex flex-col bg-gradient-to-br from-gray-50 to-blue-50/30">
    <AppHeader />

    <main class="flex-grow container max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <div class="text-center mb-8 sm:mb-12">
        <h1 class="text-2xl sm:text-4xl font-bold bg-gradient-to-r from-indigo-600 to-purple-700 bg-clip-text text-transparent mb-2 sm:mb-4">
          Оформление заказа
        </h1>
        <p class="text-sm sm:text-base text-gray-600 max-w-2xl mx-auto">Укажите детали оплаты и получения товара</p>
      </div>

      <div v-if="orderStore.error" class="mb-6 p-4 bg-red-50 border border-red-200 rounded-xl">
        <p class="text-red-700 text-sm">{{ orderStore.error }}</p>
      </div>

      <div v-if="!cartStore.cart?.products_in_cart?.length" class="text-center py-12">
        <div class="bg-white rounded-2xl shadow-lg border border-gray-100 p-12 max-w-md mx-auto">
          <div class="w-20 h-20 mx-auto mb-6 bg-gradient-to-br from-indigo-100 to-purple-100 rounded-full flex items-center justify-center">
            <svg class="w-10 h-10 text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z"/>
            </svg>
          </div>
          <h3 class="text-xl font-bold text-gray-800 mb-3">Корзина пуста</h3>
          <p class="text-gray-600 mb-6">Добавьте товары в корзину перед оформлением заказа</p>
          <router-link
              to="/chapters"
              class="inline-flex items-center px-6 py-3 bg-gradient-to-r from-indigo-600 to-purple-700 text-white font-semibold rounded-xl shadow-lg hover:shadow-xl transition-all duration-300"
          >
            Перейти в магазин
          </router-link>
        </div>
      </div>

      <div v-else-if="cartStore.cart?.products_in_cart?.length" class="lg:grid lg:grid-cols-12 lg:gap-8">
        <div class="lg:col-span-7">
          <div class="bg-white rounded-2xl shadow-lg border border-gray-100 overflow-hidden">
            <div class="p-6 border-b border-gray-100">
              <h2 class="text-xl font-semibold text-gray-800 flex items-center">
                <svg class="w-6 h-6 text-indigo-600 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/>
                </svg>
                Контактная информация
              </h2>
            </div>

            <form @submit.prevent="submitOrder" class="p-6 space-y-6">
              <div>
                <label for="address" class="block text-sm font-medium text-gray-700 mb-2">
                  Адрес доставки *
                </label>
                <textarea
                    id="address"
                    v-model="formData.address"
                    rows="3"
                    placeholder="Введите полный адрес доставки"
                    class="w-full px-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition-all duration-300 resize-none"
                    :class="{ 'border-red-500': errors.address }"
                    required
                ></textarea>
                <p v-if="errors.address" class="mt-1 text-sm text-red-600">{{ errors.address }}</p>
              </div>

              <div>
                <label for="phone" class="block text-sm font-medium text-gray-700 mb-2">
                  Номер телефона *
                </label>
                <input
                    id="phone"
                    v-model="formData.phone"
                    type="tel"
                    placeholder="+7 (999) 123-45-67"
                    class="w-full px-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition-all duration-300"
                    :class="{ 'border-red-500': errors.phone }"
                    required
                >
                <p v-if="errors.phone" class="mt-1 text-sm text-red-600">{{ errors.phone }}</p>
                <p class="mt-1 text-xs text-gray-500">Формат: +79991234567 или 89991234567</p>
              </div>

              <div>
                <label for="delivery_date" class="block text-sm font-medium text-gray-700 mb-2">
                  Дата доставки *
                </label>
                <input
                    id="delivery_date"
                    v-model="formData.delivery_date"
                    type="date"
                    :min="minDeliveryDate"
                    class="w-full px-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition-all duration-300"
                    :class="{ 'border-red-500': errors.delivery_date }"
                    required
                >
                <p v-if="errors.delivery_date" class="mt-1 text-sm text-red-600">{{ errors.delivery_date }}</p>
              </div>
            </form>
          </div>
        </div>

        <div class="mt-6 lg:mt-0 lg:col-span-5">
          <div class="bg-gradient-to-br from-white to-gray-50 rounded-2xl shadow-lg border border-gray-100 p-6 lg:sticky lg:top-8">
            <div class="flex items-center space-x-3 mb-6">
              <div class="w-10 h-10 bg-gradient-to-r from-indigo-500 to-purple-600 rounded-xl flex items-center justify-center">
                <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z"/>
                </svg>
              </div>
              <h2 class="text-xl font-bold text-gray-800">Ваш заказ</h2>
            </div>

            <div class="space-y-4 mb-6 max-h-96 overflow-y-auto">
              <div
                  v-for="item in cartStore.cart.products_in_cart"
                  :key="item.id"
                  class="flex items-center space-x-4 p-4 bg-white rounded-xl border border-gray-100 shadow-sm"
              >
                <img
                    :src="MEDIA_URL + item.product_variant.first_image"
                    :alt="item.product_variant.product_title"
                    class="w-16 h-16 rounded-lg object-cover object-center flex-shrink-0"
                >
                <div class="flex-1 min-w-0">
                  <h3 class="text-sm font-semibold text-gray-800 truncate">
                    {{ item.product_variant.product_title }}
                  </h3>
                  <p class="text-xs text-gray-600 mt-1">Вариант: {{ item.product_variant.name }}</p>
                  <div class="flex items-center justify-between mt-2">
                    <span class="text-sm text-gray-500">
                      {{ Intl.NumberFormat('ru-RU', { style: 'currency', currency: 'RUB' }).format(+item.product_variant.price) }} × {{ item.quantity }}
                    </span>
                    <span class="text-sm font-bold text-gray-900">
                      {{ Intl.NumberFormat('ru-RU', { style: 'currency', currency: 'RUB' }).format(+item.product_variant.price * item.quantity) }}
                    </span>
                  </div>
                </div>
              </div>
            </div>

            <dl class="space-y-4 border-t border-gray-200 pt-4">
              <div class="flex items-center justify-between">
                <dt class="text-base text-gray-600">Товары ({{ cartStore.cart.total_items }})</dt>
                <dd class="font-medium text-gray-900">
                  {{ Intl.NumberFormat('ru-RU', { style: 'currency', currency: 'RUB' }).format(+cartStore.cart.total_price) }}
                </dd>
              </div>

              <div class="flex items-center justify-between">
                <dt class="text-base text-gray-600">Доставка</dt>
                <dd class="font-medium text-green-600">Бесплатно</dd>
              </div>

              <div class="flex items-center justify-between pt-4 border-t border-gray-300">
                <dt class="text-lg font-bold text-gray-800">Общая стоимость</dt>
                <dd class="text-xl font-bold bg-gradient-to-r from-indigo-600 to-purple-700 bg-clip-text text-transparent">
                  {{ Intl.NumberFormat('ru-RU', { style: 'currency', currency: 'RUB' }).format(+cartStore.cart.total_price) }}
                </dd>
              </div>
            </dl>

            <div class="mt-6 space-y-4">
              <button
                  @click="submitOrder"
                  :disabled="orderStore.isLoading || !isFormValid"
                  class="w-full bg-gradient-to-r from-indigo-600 to-purple-700 hover:from-indigo-700 hover:to-purple-800 disabled:from-gray-400 disabled:to-gray-500 text-white font-semibold py-4 px-6 rounded-xl shadow-lg hover:shadow-xl disabled:shadow-none transition-all duration-300 flex items-center justify-center space-x-2 disabled:cursor-not-allowed"
              >
                <svg v-if="orderStore.isLoading" class="w-5 h-5 animate-spin" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"/>
                </svg>
                <svg v-else class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
                </svg>
                <span>{{ orderStore.isLoading ? 'Оформляем заказ...' : 'Подтвердить заказ' }}</span>
              </button>

              <router-link
                  to="/cart"
                  class="w-full border-2 border-gray-300 text-gray-700 hover:border-indigo-300 hover:bg-indigo-50 font-medium py-3 px-6 rounded-xl transition-all duration-300 flex items-center justify-center space-x-2"
              >
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"/>
                </svg>
                <span>Вернуться в корзину</span>
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </main>

    <AppFooter />
  </div>
</template>

<script setup lang="ts">
import { onMounted, reactive, computed } from 'vue'
import { useRouter } from 'vue-router'
import AppHeader from '@/components/AppHeader.vue'
import AppFooter from '@/components/AppFooter.vue'
import { useCartStore } from '@/stores/cartStore'
import { useOrderStore } from '@/stores/orderStore'
import { MEDIA_URL } from '@/services/baseURL'
import type { CreateOrderBody } from '@/types'

const router = useRouter()
const cartStore = useCartStore()
const orderStore = useOrderStore()

const formData = reactive({
  address: '',
  phone: '',
  delivery_date: ''
})

const errors = reactive({
  address: '',
  phone: '',
  delivery_date: ''
})

const minDeliveryDate = computed(() => {
  const tomorrow = new Date()
  tomorrow.setDate(tomorrow.getDate() + 1)
  return tomorrow.toISOString().split('T')[0]
})

const isFormValid = computed(() => {
  const hasProducts = !!cartStore.cart?.products_in_cart?.length
  return formData.address.trim() &&
      formData.phone.trim() &&
      formData.delivery_date &&
      validatePhone(formData.phone) &&
      validateDeliveryDate(formData.delivery_date) &&
      hasProducts
})

const validatePhone = (phone: string): boolean => {
  const phoneRegex = /^\+?\d{7,15}$/
  return phoneRegex.test(phone.replace(/\s/g, ''))
}

const validateDeliveryDate = (date: string): boolean => {
  const deliveryDate = new Date(date)
  const today = new Date()
  today.setHours(0, 0, 0, 0)
  return deliveryDate >= today
}

const submitOrder = async () => {
  Object.keys(errors).forEach(key => {
    errors[key as keyof typeof errors] = ''
  })

  let hasErrors = false

  if (!formData.address.trim()) {
    errors.address = 'Введите адрес доставки'
    hasErrors = true
  }

  if (!formData.phone.trim()) {
    errors.phone = 'Введите номер телефона'
    hasErrors = true
  } else if (!validatePhone(formData.phone)) {
    errors.phone = 'Неверный формат телефона. Пример: +79991234567'
    hasErrors = true
  }

  if (!formData.delivery_date) {
    errors.delivery_date = 'Выберите дату доставки'
    hasErrors = true
  } else if (!validateDeliveryDate(formData.delivery_date)) {
    errors.delivery_date = 'Дата доставки не может быть в прошлом'
    hasErrors = true
  }

  if (!cartStore.cart?.products_in_cart?.length) {
    errors.address = 'Корзина пуста. Добавьте товары в корзину перед оформлением заказа.'
    hasErrors = true
  }

  if (hasErrors) return

  try {
    if (!cartStore.cart?.products_in_cart) {
      throw new Error('Нет товаров для заказа')
    }

    const orderData: CreateOrderBody = {
      address: formData.address.trim(),
      phone: formData.phone.replace(/\s/g, ''),
      delivery_date: formData.delivery_date,
      products: cartStore.cart.products_in_cart.map(item => ({
        product_variant: item.product_variant.id,
        quantity: item.quantity
      }))
    }

    await orderStore.createOrder(orderData)

    if (!orderStore.error) {
      await cartStore.fetchCart()
      await router.push('/orders')
    }
  } catch (error) {
    console.error('Ошибка при создании заказа:', error)
    errors.address = 'Произошла ошибка при создании заказа. Попробуйте еще раз.'
  }
}

onMounted(async () => {
  await cartStore.fetchCart()
  if (!cartStore.cart?.products_in_cart?.length) {
    await router.push('/cart')
  }
})
</script>