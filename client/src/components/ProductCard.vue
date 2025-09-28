<template>
  <div class="bg-white rounded-lg shadow-sm border hover:shadow-md transition-shadow duration-300 group">
    <router-link :to="`/details/${product.id}`" class="block">
      <div class="aspect-w-3 aspect-h-4 relative">
        <img
            :src="MEDIA_URL + product.first_image"
            :alt="product.product_title"
            class="w-full h-48 object-cover rounded-t-lg"
        >
        <button
            @click.prevent="toggleFavorite"
            class="border-2 absolute -top-5 left-1/2 transform -translate-x-1/2 p-2 bg-white rounded-full shadow-md hover:bg-gray-50"
        >
          <svg
              class="w-5 h-5"
              :class="isFavorite ? 'text-red-500 fill-current' : 'text-gray-400'"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
          >
            <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"
            />
          </svg>
        </button>
      </div>

      <div class="p-4">
        <h3 class="font-medium text-gray-900 mb-2 line-clamp-2 group-hover:text-indigo-600 transition-colors">{{ product.product_title }}</h3>

        <div class="flex items-center justify-between mb-2">
          <span class="text-lg font-bold text-indigo-600">{{ product.price }} ₽</span>
          <div class="flex items-center space-x-1">
            <svg
                class="w-4 h-4 text-yellow-400"
                fill="currentColor"
                viewBox="0 0 20 20"
            >
              <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/>
            </svg>
            <span class="text-sm text-gray-600">{{ product.average_rating || 0 }}</span>
            <span class="text-sm text-gray-400">({{ product.reviews_count }})</span>
          </div>
        </div>

        <button
            @click.prevent="addToCart"
            :class="isInCart ?
            'w-full bg-red-600 text-white py-2 rounded-lg hover:bg-red-700 transition-colors' :
            'w-full bg-indigo-600 text-white py-2 rounded-lg hover:bg-indigo-700 transition-colors'"
            :disabled="cartStore.isLoading"
        >
          {{ isInCart ? 'Удалить' : 'В корзину' }}
        </button>
      </div>
    </router-link>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import type { ProductVariant } from '@/types'
import { useFavoriteProductStore } from '@/stores/favoriteProductStore'
import { useCartStore } from '@/stores/cartStore'
import { MEDIA_URL } from '@/services/baseURL'

interface Props {
  product: ProductVariant
}

const props = defineProps<Props>()
const favoritesStore = useFavoriteProductStore()
const cartStore = useCartStore()

const isFavorite = computed(() => {
  return favoritesStore.favoriteProducts.some(fp => fp.product.id === props.product.product_id)
})

const isInCart = computed(() => {
  return cartStore.cart?.products_in_cart.some(item => item.product_variant.id === props.product.id);
});

const addToCart = async () => {
  if (isInCart.value) {
    await cartStore.removeFromCart(props.product.id);
    await cartStore.fetchCart();
  } else {
    await cartStore.addToCart({
      product_variant: props.product.id,
      quantity: 1
    })
    await cartStore.fetchCart();
  }
}

const toggleFavorite = async () => {
  if (isFavorite.value) {
    await favoritesStore.removeFromFavorite(props.product.product_id);
    await favoritesStore.fetchFavoriteProducts();
  } else {
    await favoritesStore.addToFavorite(props.product.product_id);
    await favoritesStore.fetchFavoriteProducts();
  }
}
</script>
