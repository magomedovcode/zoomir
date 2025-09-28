<template>
  <div class="bg-white rounded-lg shadow-sm border hover:shadow-md transition-shadow duration-300 group">
    <div class="relative">
      <button
          @click.prevent="toggleFavorite"
          class="border-2 absolute -top-5 left-1/2 z-10 p-2 bg-white/90 backdrop-blur-sm rounded-full shadow-lg hover:bg-white transition-all duration-200 group-hover:bg-white transform -translate-x-1/2"
          :class="isFavorite ? 'text-red-500' : 'text-gray-400 hover:text-red-400'"
      >
        <svg
            class="w-5 h-5"
            :class="isFavorite ? 'fill-current' : 'fill-transparent'"
            stroke="currentColor"
            stroke-width="2"
            viewBox="0 0 24 24"
        >
          <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"
          />
        </svg>
      </button>

      <router-link :to="`/details/${product.id}`" class="block">
        <div class="p-5">
          <h3 class="font-semibold text-gray-900 mb-4 line-clamp-2 text-lg leading-tight group-hover:text-indigo-600 transition-colors">
            {{ product.title }}
          </h3>

          <div class="space-y-3">
            <div class="flex items-center justify-between rounded-lg px-3 py-2 border-b transition-colors">
              <span class="text-sm font-medium text-gray-700">Бренд:</span>
              <div class="flex items-center space-x-2">
                <span class="text-sm font-semibold text-indigo-600">{{ product.brand.name }}</span>
                <img
                    :src="product.brand.logo"
                    :alt="product.brand.name"
                    class="w-8 h-8 object-contain rounded-lg border border-gray-200 bg-white p-1"
                >
              </div>
            </div>

            <div class="flex items-center justify-between rounded-lg px-3 py-2 border-b transition-colors">
              <span class="text-sm font-medium text-gray-700">Страна производства:</span>
              <div class="flex items-center space-x-2">
                <span class="text-sm font-semibold text-indigo-600">{{ product.country.name }}</span>
                <img
                    :src="product.country.flag"
                    :alt="product.country.name"
                    class="w-8 h-6 object-contain rounded border border-gray-200 bg-white"
                >
              </div>
            </div>
          </div>
        </div>
      </router-link>
    </div>
  </div>
</template>

<script setup lang="ts">
import type { Product } from "@/types";
import {useFavoriteProductStore} from "@/stores/favoriteProductStore.ts";
import {computed} from "vue";

interface Props {
  product: Product
}

const props = defineProps<Props>()
const favoritesStore = useFavoriteProductStore()

const isFavorite = computed(() => {
  return favoritesStore.favoriteProducts.some(fp => fp.product.id === props.product.id)
})

const toggleFavorite = async () => {
  if (isFavorite.value) {
    await favoritesStore.removeFromFavorite(props.product.id);
    await favoritesStore.fetchFavoriteProducts();
  } else {
    await favoritesStore.addToFavorite(props.product.id);
    await favoritesStore.fetchFavoriteProducts();
  }
}
</script>
