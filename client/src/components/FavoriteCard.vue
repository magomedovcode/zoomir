<template>
  <div class="bg-white rounded-2xl shadow-lg border border-gray-100 hover:shadow-2xl transition-all duration-500 group transform hover:-translate-y-1 relative overflow-hidden">
    <div class="absolute inset-0 bg-gradient-to-br from-indigo-50/0 to-purple-50/0 group-hover:from-indigo-50/50 group-hover:to-purple-50/30 transition-all duration-500 rounded-2xl"></div>

    <div class="relative z-10">
      <router-link :to="`/details/${product.id}`" class="block">
        <div class="p-6">
          <h3 class="font-bold text-gray-800 mb-6 line-clamp-2 text-xl leading-tight group-hover:text-indigo-700 transition-colors duration-300 min-h-[3.5rem]">
            {{ product.title }}
          </h3>

          <div class="space-y-4">
            <div class="flex items-center justify-between p-4 bg-gradient-to-r from-gray-50 to-indigo-50/30 rounded-xl border border-gray-100 hover:border-indigo-200 transition-all duration-300 group/brand">
              <div class="flex items-center space-x-3">
                <div class="w-10 h-10 bg-white rounded-lg shadow-sm border border-gray-200 flex items-center justify-center p-1.5">
                  <img
                      v-if="product.brand.logo"
                      :src="product.brand.logo"
                      :alt="product.brand.name"
                      class="w-full h-full object-contain"
                  >
                  <svg v-else class="w-6 h-6 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"/>
                  </svg>
                </div>
                <div>
                  <p class="text-xs font-medium text-gray-500 uppercase tracking-wide">Бренд</p>
                  <p class="text-sm font-semibold text-gray-800 group-hover/brand:text-indigo-700 transition-colors duration-300">
                    {{ product.brand.name }}
                  </p>
                </div>
              </div>
            </div>

            <div class="flex items-center justify-between p-4 bg-gradient-to-r from-gray-50 to-purple-50/30 rounded-xl border border-gray-100 hover:border-purple-200 transition-all duration-300 group/country">
              <div class="flex items-center space-x-3">
                <div class="w-10 h-10 bg-white rounded-lg shadow-sm border border-gray-200 flex items-center justify-center p-0.5">
                  <img
                      v-if="product.country.flag"
                      :src="product.country.flag"
                      :alt="product.country.name"
                      class="w-full h-full object-contain rounded"
                  >
                  <svg v-else class="w-6 h-6 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
                  </svg>
                </div>
                <div>
                  <p class="text-xs font-medium text-gray-500 uppercase tracking-wide">Страна</p>
                  <p class="text-sm font-semibold text-gray-800 group-hover/country:text-purple-700 transition-colors duration-300">
                    {{ product.country.name }}
                  </p>
                </div>
              </div>
            </div>
          </div>

          <div v-if="product.description" class="mt-6 pt-4 border-t border-gray-100">
            <p class="text-sm text-gray-600 line-clamp-2 leading-relaxed">
              {{ product.description }}
            </p>
          </div>

          <div class="mt-6 pt-4 border-t border-gray-100">
            <div class="flex items-center justify-center space-x-2 text-indigo-600 hover:text-indigo-700 font-semibold transition-colors duration-300 group/details cursor-pointer">
              <span>Подробнее о товаре</span>
              <svg class="w-4 h-4 transform group-hover/details:translate-x-1 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
              </svg>
            </div>
          </div>
        </div>
      </router-link>
    </div>
  </div>
</template>

<script setup lang="ts">
import type { Product } from "@/types";

interface Props {
  product: Product
}

defineProps<Props>()
</script>
