<template>
  <div class="min-h-screen bg-gray-50">
    <AppHeader />

    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <div class="flex flex-col lg:flex-row gap-8">
        <!-- Сайдбар фильтров -->
        <div class="lg:w-1/4">
          <div class="bg-white rounded-lg shadow-sm border p-6 sticky top-4">
            <h3 class="text-lg font-semibold mb-4">Фильтры</h3>

            <!-- Поиск -->
            <div class="mb-6">
              <input
                  v-model="searchQuery"
                  type="text"
                  placeholder="Поиск товаров..."
                  class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500"
              >
            </div>

            <!-- Бренды -->
            <div class="mb-6">
              <h4 class="font-medium mb-3">Бренды</h4>
              <div class="space-y-2">
                <label v-for="brand in filtersStore.brands" :key="brand.id" class="flex items-center">
                  <input
                      type="checkbox"
                      :value="brand.id"
                      v-model="selectedBrands"
                      class="rounded text-indigo-600 focus:ring-indigo-500"
                  >
                  <span class="ml-2 text-sm">{{ brand.name }}</span>
                </label>
              </div>
            </div>

            <!-- Страны -->
            <div class="mb-6">
              <h4 class="font-medium mb-3">Страны</h4>
              <div class="space-y-2">
                <label v-for="country in filtersStore.countries" :key="country.id" class="flex items-center">
                  <input
                      type="checkbox"
                      :value="country.id"
                      v-model="selectedCountries"
                      class="rounded text-indigo-600 focus:ring-indigo-500"
                  >
                  <span class="ml-2 text-sm">{{ country.name }}</span>
                </label>
              </div>
            </div>

            <!-- Цена -->
            <div class="mb-6">
              <h4 class="font-medium mb-3">Цена</h4>
              <div class="flex space-x-2">
                <input
                    v-model.number="priceMin"
                    type="number"
                    placeholder="От"
                    class="w-full px-3 py-2 border rounded-lg text-sm"
                >
                <input
                    v-model.number="priceMax"
                    type="number"
                    placeholder="До"
                    class="w-full px-3 py-2 border rounded-lg text-sm"
                >
              </div>
            </div>

            <!-- Сортировка -->
            <div>
              <h4 class="font-medium mb-3">Сортировка</h4>
              <select
                  v-model="ordering"
                  class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500"
              >
                <option value="">По умолчанию</option>
                <option value="price">Цена по возрастанию</option>
                <option value="-price">Цена по убыванию</option>
              </select>
            </div>
          </div>
        </div>

        <!-- Основной контент -->
        <div class="lg:w-3/4">
          <div class="flex justify-between items-center mb-6">
            <h1 class="text-2xl font-bold">Все товары</h1>
            <span class="text-gray-600">{{ productStore.totalCount }} товаров</span>
          </div>

          <!-- Товары -->
          <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6" v-if="!productStore.isLoading">
            <ProductCard
                v-for="product in productStore.products"
                :key="product.id"
                :product="product"
            />
          </div>

          <!-- Загрузка -->
          <div v-else class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
            <div v-for="i in 12" :key="i" class="bg-gray-200 rounded-lg h-80 animate-pulse"></div>
          </div>

          <!-- Пагинация -->
          <div class="flex justify-center mt-12" v-if="productStore.totalCount > productStore.pageSize">
            <button
                @click="loadPage(productStore.currentPage - 1)"
                :disabled="productStore.currentPage === 1"
                class="px-4 py-2 border rounded-l-lg hover:bg-gray-50 disabled:opacity-50"
            >
              Назад
            </button>
            <span class="px-4 py-2 border-t border-b">{{ productStore.currentPage }}</span>
            <button
                @click="loadPage(productStore.currentPage + 1)"
                :disabled="productStore.currentPage * productStore.pageSize >= productStore.totalCount"
                class="px-4 py-2 border rounded-r-lg hover:bg-gray-50 disabled:opacity-50"
            >
              Вперед
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import {computed, onMounted, ref, watch} from 'vue'
import {useRoute} from 'vue-router'
import AppHeader from '@/components/AppHeader.vue'
import ProductCard from '@/components/ProductCard.vue'
import {useProductStore} from '@/stores/productStore'
import {useProductFiltersStore} from '@/stores/productFiltersStore'
import {ProductOrdering} from '@/types'

const route = useRoute()
const productStore = useProductStore()
const filtersStore = useProductFiltersStore()

const searchQuery = ref('')
const selectedBrands = ref<number[]>([])
const selectedCountries = ref<number[]>([])
const priceMin = ref<number>()
const priceMax = ref<number>()
const ordering = ref<ProductOrdering>(ProductOrdering.PRICE_DEFAULT)

const filters = computed(() => ({
  search: searchQuery.value,
  brand: selectedBrands.value,
  country: selectedCountries.value,
  price_min: priceMin.value,
  price_max: priceMax.value,
  ordering: ordering.value,
  product_category: route.params.chapterId ? [Number(route.params.chapterId)] : []
}))

watch(filters, async () => {
  await productStore.fetchProducts(filters.value)
}, { deep: true })

const loadPage = (page: number) => {
  productStore.currentPage = page
  productStore.fetchProducts(filters.value)
}

onMounted(async () => {
  await filtersStore.fetchBrands()
  await filtersStore.fetchCountries()
  await productStore.fetchProducts(filters.value)
})
</script>
