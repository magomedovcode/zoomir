<template>
  <div
      class="bg-white rounded-lg sm:rounded-2xl shadow-md sm:shadow-lg border border-stone-300 hover:shadow-xl sm:hover:shadow-2xl transition-all duration-500 group relative overflow-hidden"
  >
    <router-link
        :to="getProductLink"
        class="block relative z-10"
    >
      <div
          class="relative overflow-hidden rounded-t-lg sm:rounded-t-2xl aspect-[4/5] sm:aspect-[4/4]"
      >
        <img
            :src="MEDIA_URL + product.first_image"
            :alt="product.product_title"
            class="w-full h-full object-contain transform group-hover:scale-105 sm:group-hover:scale-110 transition-transform duration-700"
        />
        <div
            class="absolute inset-0 bg-gradient-to-t from-black/10 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500"
        ></div>

        <button
            @click.prevent="toggleFavorite"
            class="absolute top-2 right-2 sm:top-3 sm:right-3 w-7 h-7 sm:w-10 sm:h-10 bg-white/90 backdrop-blur-sm rounded-full shadow flex items-center justify-center transform transition-all duration-300 hover:scale-110 hover:bg-white"
        >
          <svg
              class="w-4 h-4 sm:w-5 sm:h-5 transition-transform duration-300"
              :class="
              isFavorite
                ? 'text-red-500 fill-current drop-shadow-sm'
                : 'text-stone-400 hover:text-red-400'
            "
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
          >
            <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"
            />
          </svg>
        </button>
      </div>

      <div class="p-3 sm:p-4 md:p-5 relative z-10">
        <h3
            class="font-medium sm:font-semibold text-stone-800 mb-2 line-clamp-2 group-hover:text-yellow-500 transition-colors duration-300 leading-snug text-sm sm:text-base"
        >
          {{ product.product_title }}
        </h3>

        <div class="mb-3 sm:mb-4">
          <span
              class="block text-base sm:text-xl md:text-2xl font-bold bg-gradient-to-r from-yellow-500 to-amber-500 bg-clip-text text-transparent mb-1 sm:mb-2"
          >
            {{
              Intl.NumberFormat("ru-RU", {
                style: "currency",
                currency: "RUB",
              }).format(+product.price)
            }}
          </span>

          <div class="flex items-center space-x-1">
            <svg
                class="w-4 h-4 sm:w-5 sm:h-5 text-yellow-500 fill-current"
                viewBox="0 0 20 20"
            >
              <path
                  d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"
              />
            </svg>
            <span class="text-xs sm:text-sm font-medium text-stone-700">
              {{ product.average_rating || 0 }}
            </span>
            <span class="text-xs sm:text-sm text-gray-500 whitespace-nowrap">
              - {{ product.reviews_count || 0 }} оценок
            </span>
          </div>
        </div>

        <button
            @click.prevent="addToCart"
            :disabled="cartStore.isLoading"
            class="relative w-full py-2 sm:py-3 px-3 sm:px-4 rounded-lg sm:rounded-xl font-semibold transition-all duration-500 overflow-hidden text-sm sm:text-base"
            :class="
            isInCart
              ? 'bg-gradient-to-r from-red-500 to-pink-600 hover:from-red-600 hover:to-pink-700 text-white shadow'
              : 'bg-gradient-to-r from-yellow-500 to-amber-500 hover:from-yellow-600 hover:to-amber-600 text-white shadow'
          "
        >
          <span
              class="relative z-10 flex items-center justify-center whitespace-nowrap"
          >
            <svg
                v-if="cartStore.isLoading"
                class="animate-spin -ml-1 mr-2 h-3 w-3 sm:h-4 sm:w-4 text-white"
                fill="none"
                viewBox="0 0 24 24"
            >
              <circle
                  class="opacity-25"
                  cx="12"
                  cy="12"
                  r="10"
                  stroke="currentColor"
                  stroke-width="4"
              ></circle>
              <path
                  class="opacity-75"
                  fill="currentColor"
                  d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
              ></path>
            </svg>

            <svg
                v-else-if="isInCart"
                class="w-4 h-4 sm:w-5 sm:h-5 mr-1 sm:mr-2"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
            >
              <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M5 13l4 4L19 7"
              />
            </svg>

            <svg
                v-else
                class="w-4 h-4 sm:w-5 sm:h-5 mr-1 sm:mr-2"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
            >
              <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M12 6v6m0 0v6m0-6h6m-6 0H6"
              />
            </svg>

            {{ isInCart ? "В корзине" : "В корзину" }}
          </span>
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

const getProductLink = computed(() => {
  return {
    path: `/details/${props.product.product_id}`,
    query: {
      variant: props.product.id
    }
  }
})

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
