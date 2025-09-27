<template>
  <div class="min-h-screen bg-gray-50">
    <AppHeader />

    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8" v-if="productStore.productDetail">
      <!-- Хлебные крошки -->
      <nav class="flex mb-8" aria-label="Breadcrumb">
        <ol class="flex items-center space-x-4">
          <li>
            <router-link to="/" class="text-gray-400 hover:text-gray-500">Главная</router-link>
          </li>
          <li>
            <span class="text-gray-400">/</span>
          </li>
          <li>
            <router-link :to="`/shop/${productStore.productDetail.product_category.product_chapter.id}`" class="text-gray-400 hover:text-gray-500">
              {{ productStore.productDetail.product_category.product_chapter.name }}
            </router-link>
          </li>
          <li>
            <span class="text-gray-400">/</span>
          </li>
          <li>
            <span class="text-gray-600">{{ productStore.productDetail.title }}</span>
          </li>
        </ol>
      </nav>

      <div class="lg:grid lg:grid-cols-2 lg:gap-x-8">
        <!-- Галерея изображений -->
        <div class="flex flex-col-reverse">
          <div class="w-full max-w-2xl mx-auto mt-6 sm:block lg:max-w-none">
            <div class="grid grid-cols-4 gap-2" aria-orientation="horizontal">
              <button
                  v-for="(variant, variantIndex) in productStore.productDetail.product_variants"
                  :key="variant.id"
                  class="relative h-24 bg-white rounded-md flex items-center justify-center text-sm font-medium uppercase text-gray-900 cursor-pointer hover:bg-gray-50 focus:outline-none focus:ring focus:ring-offset-4 focus:ring-opacity-50"
                  :class="{ 'ring-2 ring-indigo-500': selectedVariantIndex === variantIndex }"
                  @click="selectedVariantIndex = variantIndex"
              >
                <img
                    v-if="variant.product_images.length > 0"
                    :src="MEDIA_URL + variant.product_images[0].image"
                    :alt="variant.name"
                    class="h-full w-full object-cover object-center rounded-md"
                >
                <span v-else class="text-gray-400">Нет изображения</span>
              </button>
            </div>
          </div>

          <div class="w-full aspect-w-1 aspect-h-1">
            <img
                v-if="currentVariant.product_images.length > 0"
                :src="MEDIA_URL + currentVariant.product_images[0].image"
                :alt="currentVariant.name"
                class="w-full h-96 object-cover object-center rounded-lg"
            >
            <div v-else class="w-full h-96 bg-gray-200 rounded-lg flex items-center justify-center">
              <span class="text-gray-400">Нет изображения</span>
            </div>
          </div>
        </div>

        <!-- Информация о товаре -->
        <div class="mt-10 px-4 sm:px-0 sm:mt-16 lg:mt-0">
          <h1 class="text-3xl font-extrabold tracking-tight text-gray-900">{{ productStore.productDetail.title }}</h1>

          <div class="mt-3">
            <h2 class="sr-only">Информация о товаре</h2>
            <p class="text-3xl text-gray-900">{{ currentVariant.price }} ₽</p>
          </div>

          <div class="mt-6">
            <h3 class="sr-only">Описание</h3>
            <div class="text-base text-gray-700 space-y-6">
              <p>{{ productStore.productDetail.description }}</p>
            </div>
          </div>

          <!-- Варианты -->
          <div class="mt-6">
            <div class="flex items-center">
              <h3 class="text-sm text-gray-600">Вариант:</h3>
              <span class="ml-2 text-sm font-medium text-gray-900">{{ currentVariant.name }}</span>
            </div>

            <div class="mt-2">
              <div class="flex items-center space-x-2">
                <button
                    v-for="(variant, index) in productStore.productDetail.product_variants"
                    :key="variant.id"
                    @click="selectedVariantIndex = index"
                    class="relative flex items-center justify-center rounded-md border border-gray-300 bg-white px-4 py-3 text-sm font-medium uppercase text-gray-900 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2"
                    :class="{ 'ring-2 ring-indigo-500': selectedVariantIndex === index }"
                >
                  {{ variant.name }}
                </button>
              </div>
            </div>
          </div>

          <!-- Атрибуты -->
          <div class="mt-6" v-for="attrCategory in currentVariant.attributes" :key="attrCategory.id">
            <h3 class="text-sm font-medium text-gray-900">{{ attrCategory.name }}</h3>
            <div class="mt-2">
              <div class="flex flex-wrap gap-2">
                <span
                    v-for="attr in attrCategory.attributes"
                    :key="attr.id"
                    class="inline-flex items-center px-3 py-1 rounded-full text-xs font-medium bg-gray-100 text-gray-800"
                >
                  {{ attr.name }}: {{ attr.value }}
                </span>
              </div>
            </div>
          </div>

          <!-- Бренд и страна -->
          <div class="mt-6">
            <div class="flex items-center space-x-4">
              <span class="text-sm text-gray-600">Бренд: {{ productStore.productDetail.brand.name }}</span>
              <span class="text-sm text-gray-600">Страна: {{ productStore.productDetail.country.name }}</span>
            </div>
          </div>

          <!-- Кнопки действий -->
          <div class="mt-10 flex space-x-4">
            <button
                @click="addToCart"
                class="flex-1 bg-indigo-600 border border-transparent rounded-md py-3 px-8 flex items-center justify-center text-base font-medium text-white hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
                :disabled="cartStore.isLoading"
            >
              {{ cartStore.isLoading ? 'Добавление...' : 'В корзину' }}
            </button>
            <button
                @click="toggleFavorite"
                class="flex items-center justify-center px-4 py-3 border border-gray-300 rounded-md text-gray-700 hover:bg-gray-50"
            >
              <svg
                  class="w-6 h-6"
                  :class="isFavorite ? 'text-red-500 fill-current' : 'text-gray-400'"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
              >
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/>
              </svg>
            </button>
          </div>
        </div>
      </div>

      <!-- Отзывы -->
      <section aria-labelledby="reviews-heading" class="mt-16 sm:mt-24">
        <h2 id="reviews-heading" class="text-lg font-medium text-gray-900">Отзывы</h2>

        <div class="mt-4">
          <div class="flex items-center mb-4">
            <div class="flex items-center">
              <svg v-for="rating in [0,1,2,3,4]" :key="rating" class="w-5 h-5" :class="rating < productStore.productDetail.average_rating ? 'text-yellow-400' : 'text-gray-300'" fill="currentColor" viewBox="0 0 20 20">
                <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/>
              </svg>
            </div>
            <p class="ml-3 text-sm text-gray-700">{{ productStore.productDetail.average_rating }} из 5</p>
            <p class="ml-3 text-sm text-gray-500">на основе {{ productStore.productDetail.reviews_count }} отзывов</p>
          </div>

          <button
              v-if="authStore.isAuthenticated"
              @click="showReviewForm = true"
              class="bg-indigo-600 text-white px-4 py-2 rounded-md hover:bg-indigo-700"
          >
            Написать отзыв
          </button>

          <div v-if="showReviewForm" class="mt-4 bg-white p-4 rounded-lg shadow-sm border">
            <h3 class="text-lg font-medium mb-4">Добавить отзыв</h3>
            <form @submit.prevent="submitReview">
              <div class="mb-4">
                <label for="title" class="block text-sm font-medium text-gray-700">Заголовок</label>
                <input type="text" id="title" v-model="reviewForm.title" required class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm p-2">
              </div>
              <div class="mb-4">
                <label for="rating" class="block text-sm font-medium text-gray-700">Оценка</label>
                <select id="rating" v-model.number="reviewForm.rating" required class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm p-2">
                  <option value="5">5 - Отлично</option>
                  <option value="4">4 - Хорошо</option>
                  <option value="3">3 - Удовлетворительно</option>
                  <option value="2">2 - Плохо</option>
                  <option value="1">1 - Ужасно</option>
                </select>
              </div>
              <div class="mb-4">
                <label for="comment" class="block text-sm font-medium text-gray-700">Комментарий</label>
                <textarea id="comment" v-model="reviewForm.comment" required rows="4" class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm p-2"></textarea>
              </div>
              <div class="flex space-x-2">
                <button type="submit" class="bg-indigo-600 text-white px-4 py-2 rounded-md hover:bg-indigo-700">Отправить</button>
                <button type="button" @click="showReviewForm = false" class="bg-gray-300 text-gray-700 px-4 py-2 rounded-md hover:bg-gray-400">Отмена</button>
              </div>
            </form>
          </div>

          <div class="mt-4 space-y-4">
            <div v-for="review in productStore.productDetail.reviews" :key="review.id" class="bg-white p-4 rounded-lg shadow-sm border">
              <div class="flex items-center">
                <div class="flex items-center">
                  <svg v-for="rating in [0,1,2,3,4]" :key="rating" class="w-5 h-5" :class="rating < review.rating ? 'text-yellow-400' : 'text-gray-300'" fill="currentColor" viewBox="0 0 20 20">
                    <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/>
                  </svg>
                </div>
                <p class="ml-3 text-sm font-medium text-gray-900">{{ review.title }}</p>
              </div>
              <p class="mt-1 text-sm text-gray-700">{{ review.comment }}</p>
              <p class="mt-1 text-sm text-gray-500">От {{ review.user }} · {{ formatDate(review.date) }}</p>
            </div>
          </div>
        </div>
      </section>
    </div>

    <div v-else-if="productStore.isLoading" class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <div class="animate-pulse">
        <div class="h-6 bg-gray-200 rounded w-1/4 mb-8"></div>
        <div class="grid lg:grid-cols-2 lg:gap-x-8">
          <div class="space-y-4">
            <div class="h-96 bg-gray-200 rounded"></div>
            <div class="grid grid-cols-4 gap-2">
              <div class="h-24 bg-gray-200 rounded" v-for="i in 4" :key="i"></div>
            </div>
          </div>
          <div class="space-y-4 mt-10 lg:mt-0">
            <div class="h-8 bg-gray-200 rounded w-3/4"></div>
            <div class="h-6 bg-gray-200 rounded w-1/4"></div>
            <div class="h-4 bg-gray-200 rounded w-full" v-for="i in 6" :key="i"></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted, watch } from 'vue'
import { useRoute } from 'vue-router'
import AppHeader from '@/components/AppHeader.vue'
import { useProductStore } from '@/stores/productStore'
import { useCartStore } from '@/stores/cartStore'
import { useAuthStore } from '@/stores/authStore'
import { useFavoriteProductStore } from '@/stores/favoriteProductStore'
import { useReviewStore } from '@/stores/reviewStore'
import { MEDIA_URL } from '@/services/baseURL'
import type { CreateReviewBody } from '@/types'

const route = useRoute()
const productStore = useProductStore()
const cartStore = useCartStore()
const authStore = useAuthStore()
const favoritesStore = useFavoriteProductStore()
const reviewStore = useReviewStore()

const selectedVariantIndex = ref(0)
const showReviewForm = ref(false)

const reviewForm = ref({
  title: '',
  rating: 5,
  comment: ''
})

const productId = computed(() => Number(route.params.id))

const currentVariant = computed(() => {
  if (!productStore.productDetail) {
    return {} as any
  }
  return productStore.productDetail.product_variants[selectedVariantIndex.value]
})

const isFavorite = computed(() => {
  if (!productStore.productDetail) return false
  return favoritesStore.favoriteProducts.some(fp => fp.product.id === productStore.productDetail!.id)
})

onMounted(async () => {
  await productStore.fetchProductDetails(productId.value)
})

watch(() => route.params.id, async (newId) => {
  await productStore.fetchProductDetails(Number(newId))
})

const addToCart = async () => {
  await cartStore.addToCart({
    product_variant: currentVariant.value.id,
    quantity: 1
  })
}

const toggleFavorite = async () => {
  if (isFavorite.value) {
    await favoritesStore.removeFromFavorite(productStore.productDetail!.id)
  } else {
    await favoritesStore.addToFavorite(productStore.productDetail!.id)
  }
}

const formatDate = (dateString: string) => {
  return new Date(dateString).toLocaleDateString('ru-RU')
}

const submitReview = async () => {
  const reviewData: CreateReviewBody = {
    productId: productId.value,
    ...reviewForm.value
  }
  await reviewStore.createReview(reviewData)
  showReviewForm.value = false
  // Перезагружаем отзывы
  await productStore.fetchProductDetails(productId.value)
}
</script>
