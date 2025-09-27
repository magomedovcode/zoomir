<template>
  <div class="min-h-screen bg-gray-50">
    <AppHeader />

    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <h1 class="text-3xl font-bold text-center mb-12">Категории товаров</h1>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        <div
            v-for="chapter in filtersStore.productChapters"
            :key="chapter.id"
            class="bg-white rounded-lg shadow-sm border p-8 hover:shadow-md transition-shadow cursor-pointer text-center"
            @click="$router.push(`/shop/${chapter.id}`)"
        >
          <h3 class="text-xl font-semibold">{{ chapter.name }}</h3>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { onMounted } from 'vue'
import AppHeader from '@/components/AppHeader.vue'
import { useProductFiltersStore } from '@/stores/productFiltersStore'

const filtersStore = useProductFiltersStore()

onMounted(async () => {
  await filtersStore.fetchProductChapters()
})
</script>
