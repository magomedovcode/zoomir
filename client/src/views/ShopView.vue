<template>
  <div class="min-h-screen flex flex-col bg-gray-50">
    <AppHeader />

    <div class="flex-grow container max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <div class="flex flex-col lg:flex-row gap-4 items-start mb-6">
        <div class="lg:flex-1">
          <input
              v-model="searchQuery"
              type="text"
              placeholder="Поиск товаров..."
              class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500"
          >
        </div>

        <div class="relative">
          <Listbox v-model="selectedBrands" multiple>
            <div class="relative">
              <ListboxButton class="w-full lg:w-48 px-3 py-2 border rounded-lg bg-white text-left focus:outline-none focus:ring-2 focus:ring-indigo-500 flex justify-between items-center">
                <span class="block truncate">
                  {{ getBrandsLabel }}
                </span>
                <span class="pointer-events-none flex items-center">
                  <ChevronUpDownIcon class="h-4 w-4 text-gray-400" aria-hidden="true" />
                </span>
              </ListboxButton>

              <transition
                  leave-active-class="transition duration-100 ease-in"
                  leave-from-class="opacity-100"
                  leave-to-class="opacity-0"
              >
                <ListboxOptions class="absolute top-full left-0 right-0 mt-1 max-h-60 overflow-auto rounded-lg bg-white py-1 text-base shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none sm:text-sm z-20">
                  <ListboxOption
                      v-slot="{ active, selected }"
                      v-for="brand in filtersStore.brands"
                      :key="brand.id"
                      :value="brand.id"
                      as="template"
                  >
                    <li
                        :class="[
                          active ? 'bg-indigo-100 text-indigo-900' : 'text-gray-900',
                          'relative cursor-default select-none py-2 pl-3 pr-9',
                        ]"
                    >
                      <div class="flex items-center">
                        <div class="w-5 h-5 border-2 border-gray-300 rounded flex items-center justify-center transition-all duration-200 mr-3"
                             :class="{
                               'bg-indigo-500 border-indigo-500': selected,
                               'bg-white': !selected
                             }">
                          <svg v-if="selected" class="w-3 h-3 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7"></path>
                          </svg>
                        </div>
                        <span :class="[selected ? 'font-semibold' : 'font-normal', 'block truncate']">
                          {{ brand.name }}
                        </span>
                      </div>
                    </li>
                  </ListboxOption>
                </ListboxOptions>
              </transition>
            </div>
          </Listbox>
        </div>

        <div class="relative">
          <Listbox v-model="selectedCountries" multiple>
            <div class="relative">
              <ListboxButton class="w-full lg:w-48 px-3 py-2 border rounded-lg bg-white text-left focus:outline-none focus:ring-2 focus:ring-indigo-500 flex justify-between items-center">
                <span class="block truncate">
                  {{ getCountriesLabel }}
                </span>
                <span class="pointer-events-none flex items-center">
                  <ChevronUpDownIcon class="h-4 w-4 text-gray-400" aria-hidden="true" />
                </span>
              </ListboxButton>

              <transition
                  leave-active-class="transition duration-100 ease-in"
                  leave-from-class="opacity-100"
                  leave-to-class="opacity-0"
              >
                <ListboxOptions class="absolute top-full left-0 right-0 mt-1 max-h-60 overflow-auto rounded-lg bg-white py-1 text-base shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none sm:text-sm z-20">
                  <ListboxOption
                      v-slot="{ active, selected }"
                      v-for="country in filtersStore.countries"
                      :key="country.id"
                      :value="country.id"
                      as="template"
                  >
                    <li
                        :class="[
                          active ? 'bg-indigo-100 text-indigo-900' : 'text-gray-900',
                          'relative cursor-default select-none py-2 pl-3 pr-9',
                        ]"
                    >
                      <div class="flex items-center">
                        <div class="w-5 h-5 border-2 border-gray-300 rounded flex items-center justify-center transition-all duration-200 mr-3"
                             :class="{
                               'bg-indigo-500 border-indigo-500': selected,
                               'bg-white': !selected
                             }">
                          <svg v-if="selected" class="w-3 h-3 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7"></path>
                          </svg>
                        </div>
                        <span :class="[selected ? 'font-semibold' : 'font-normal', 'block truncate']">
                          {{ country.name }}
                        </span>
                      </div>
                    </li>
                  </ListboxOption>
                </ListboxOptions>
              </transition>
            </div>
          </Listbox>
        </div>

        <div class="relative">
          <Listbox v-model="selectedCategories" multiple>
            <div class="relative">
              <ListboxButton class="w-full lg:w-48 px-3 py-2 border rounded-lg bg-white text-left focus:outline-none focus:ring-2 focus:ring-indigo-500 flex justify-between items-center">
                <span class="block truncate">
                  {{ getCategoriesLabel }}
                </span>
                <span class="pointer-events-none flex items-center">
                  <ChevronUpDownIcon class="h-4 w-4 text-gray-400" aria-hidden="true" />
                </span>
              </ListboxButton>

              <transition
                  leave-active-class="transition duration-100 ease-in"
                  leave-from-class="opacity-100"
                  leave-to-class="opacity-0"
              >
                <ListboxOptions class="absolute top-full left-0 right-0 mt-1 max-h-60 overflow-auto rounded-lg bg-white py-1 text-base shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none sm:text-sm z-20">
                  <ListboxOption
                      v-slot="{ active, selected }"
                      v-for="category in filtersStore.productCategories"
                      :key="category.id"
                      :value="category.id"
                      as="template"
                  >
                    <li
                        :class="[
                          active ? 'bg-indigo-100 text-indigo-900' : 'text-gray-900',
                          'relative cursor-default select-none py-2 pl-3 pr-9',
                        ]"
                    >
                      <div class="flex items-center">
                        <div class="w-5 h-5 border-2 border-gray-300 rounded flex items-center justify-center transition-all duration-200 mr-3"
                             :class="{
                               'bg-indigo-500 border-indigo-500': selected,
                               'bg-white': !selected
                             }">
                          <svg v-if="selected" class="w-3 h-3 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7"></path>
                          </svg>
                        </div>
                        <span :class="[selected ? 'font-semibold' : 'font-normal', 'block truncate']">
                          {{ category.name }}
                        </span>
                      </div>
                    </li>
                  </ListboxOption>
                </ListboxOptions>
              </transition>
            </div>
          </Listbox>
        </div>

        <div class="relative">
          <Popover v-slot="{ open }">
            <PopoverButton class="w-full lg:w-48 px-3 py-2 border rounded-lg bg-white text-left focus:outline-none focus:ring-2 focus:ring-indigo-500 flex justify-between items-center">
              <span class="block truncate">
                {{ getPriceLabel }}
              </span>
              <span class="pointer-events-none flex items-center">
                <ChevronUpDownIcon class="h-4 w-4 text-gray-400" aria-hidden="true" />
              </span>
            </PopoverButton>

            <transition
                enter-active-class="transition duration-200 ease-out"
                enter-from-class="translate-y-1 opacity-0"
                enter-to-class="translate-y-0 opacity-100"
                leave-active-class="transition duration-150 ease-in"
                leave-from-class="translate-y-0 opacity-100"
                leave-to-class="translate-y-1 opacity-0"
            >
              <PopoverPanel class="absolute top-full left-0 right-0 mt-1 bg-white border rounded-lg shadow-lg z-10 p-4">
                <div class="space-y-3">
                  <h4 class="font-medium text-sm text-gray-900">Диапазон цен</h4>
                  <div class="flex space-x-2">
                    <div class="flex-1">
                      <label class="block text-xs text-gray-500 mb-1">От</label>
                      <input
                          v-model.number="priceMin"
                          type="number"
                          placeholder="0"
                          class="w-full px-3 py-2 border rounded-lg text-sm focus:outline-none focus:ring-1 focus:ring-indigo-500"
                      >
                    </div>
                    <div class="flex-1">
                      <label class="block text-xs text-gray-500 mb-1">До</label>
                      <input
                          v-model.number="priceMax"
                          type="number"
                          placeholder="99999"
                          class="w-full px-3 py-2 border rounded-lg text-sm focus:outline-none focus:ring-1 focus:ring-indigo-500"
                      >
                    </div>
                  </div>
                  <div class="flex justify-between items-center text-sm text-gray-600">
                    <span v-if="priceMin || priceMax">
                      {{ priceMin || 0 }} - {{ priceMax || '∞' }} ₽
                    </span>
                    <span v-else>Любая цена</span>
                    <button
                        v-if="priceMin || priceMax"
                        @click="clearPriceFilter"
                        class="text-indigo-600 hover:text-indigo-800 text-xs"
                    >
                      Сбросить
                    </button>
                  </div>
                </div>
              </PopoverPanel>
            </transition>
          </Popover>
        </div>

        <div class="relative">
          <Listbox v-model="ordering">
            <div class="relative">
              <ListboxButton class="w-full lg:w-48 px-3 py-2 border rounded-lg bg-white text-left focus:outline-none focus:ring-2 focus:ring-indigo-500 flex justify-between items-center">
                <span class="block truncate">{{ getOrderingLabel(ordering) }}</span>
                <span class="pointer-events-none flex items-center">
                  <ChevronUpDownIcon class="h-4 w-4 text-gray-400" aria-hidden="true" />
                </span>
              </ListboxButton>

              <transition
                  leave-active-class="transition duration-100 ease-in"
                  leave-from-class="opacity-100"
                  leave-to-class="opacity-0"
              >
                <ListboxOptions class="absolute top-full left-0 right-0 mt-1 max-h-60 overflow-auto rounded-lg bg-white py-1 text-base shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none sm:text-sm z-20">
                  <ListboxOption
                      v-slot="{ active, selected }"
                      v-for="option in sortOptions"
                      :key="option.value"
                      :value="option.value"
                      as="template"
                  >
                    <li
                        :class="[
                          active ? 'bg-indigo-100 text-indigo-900' : 'text-gray-900',
                          'relative cursor-default select-none py-2 pl-3 pr-9',
                        ]"
                    >
                      <span :class="[selected ? 'font-semibold' : 'font-normal', 'block truncate']">
                        {{ option.label }}
                      </span>
                      <span
                          v-if="selected"
                          class="absolute inset-y-0 right-0 flex items-center pr-3 text-indigo-600"
                      >
                        <CheckIcon class="h-4 w-4" aria-hidden="true" />
                      </span>
                    </li>
                  </ListboxOption>
                </ListboxOptions>
              </transition>
            </div>
          </Listbox>
        </div>
      </div>

      <div>
        <div class="flex justify-between items-center mb-6">
          <h1 class="text-2xl font-bold">Все товары</h1>
          <span class="text-gray-600">{{ productStore.totalCount }} товаров</span>
        </div>

        <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-5 gap-6" v-if="!productStore.isLoading">
          <ProductCard
              v-for="product in productStore.products"
              :key="product.id"
              :product="product"
          />
        </div>

        <div v-else class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
          <div v-for="i in 12" :key="i" class="bg-gray-200 rounded-lg h-80 animate-pulse"></div>
        </div>

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

    <AppFooter />
  </div>
</template>

<script setup lang="ts">
import {computed, onMounted, ref, watch} from 'vue'
import {useRoute} from 'vue-router'
import {
  Listbox,
  ListboxButton,
  ListboxOptions,
  ListboxOption,
  Popover,
  PopoverButton,
  PopoverPanel,
} from '@headlessui/vue'
import { CheckIcon, ChevronUpDownIcon } from '@heroicons/vue/20/solid'
import AppHeader from '@/components/AppHeader.vue'
import ProductCard from '@/components/ProductCard.vue'
import {useProductStore} from '@/stores/productStore'
import {useProductFiltersStore} from '@/stores/productFiltersStore'
import {ProductOrdering} from '@/types'
import AppFooter from "@/components/AppFooter.vue";

const route = useRoute()
const productStore = useProductStore()
const filtersStore = useProductFiltersStore()

const searchQuery = ref('')
const selectedBrands = ref<number[]>([])
const selectedCountries = ref<number[]>([])
const selectedCategories = ref<number[]>([])
const priceMin = ref<number>()
const priceMax = ref<number>()
const ordering = ref<ProductOrdering>(ProductOrdering.PRICE_DEFAULT)

const sortOptions = [
  { value: ProductOrdering.PRICE_DEFAULT, label: 'По умолчанию' },
  { value: ProductOrdering.PRICE_ASC, label: 'Цена по возрастанию' },
  { value: ProductOrdering.PRICE_DESC, label: 'Цена по убыванию' },
]

const getBrandsLabel = computed(() => {
  if (selectedBrands.value.length === 0) return 'Бренды'
  if (selectedBrands.value.length === 1) {
    const brand = filtersStore.brands.find(b => b.id === selectedBrands.value[0])
    return brand ? brand.name : 'Бренды'
  }
  return `Бренды (${selectedBrands.value.length})`
})

const getCountriesLabel = computed(() => {
  if (selectedCountries.value.length === 0) return 'Страны'
  if (selectedCountries.value.length === 1) {
    const country = filtersStore.countries.find(c => c.id === selectedCountries.value[0])
    return country ? country.name : 'Страны'
  }
  return `Страны (${selectedCountries.value.length})`
})

const getCategoriesLabel = computed(() => {
  if (selectedCategories.value.length === 0) return 'Категории'
  if (selectedCategories.value.length === 1) {
    const category = filtersStore.productCategories.find(c => c.id === selectedCategories.value[0])
    return category ? category.name : 'Категории'
  }
  return `Категории (${selectedCategories.value.length})`
})

const getPriceLabel = computed(() => {
  if (!priceMin.value && !priceMax.value) return 'Цена'
  return `Цена: ${priceMin.value || 0}-${priceMax.value || '∞'} ₽`
})

const getOrderingLabel = (value: ProductOrdering) => {
  const option = sortOptions.find(opt => opt.value === value)
  return option ? option.label : 'По умолчанию'
}

const filters = computed(() => ({
  search: searchQuery.value,
  brand: selectedBrands.value,
  country: selectedCountries.value,
  price_min: priceMin.value,
  price_max: priceMax.value,
  ordering: ordering.value,
  product_category: selectedCategories.value.length > 0
      ? selectedCategories.value
      : route.params.chapterId
      ? [Number(route.params.chapterId)]
      : []
}))

const clearPriceFilter = () => {
  priceMin.value = undefined
  priceMax.value = undefined
}

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
  await filtersStore.fetchProductCategories(Number(route.params.chapterId))
})
</script>
