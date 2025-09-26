<template>
  <div class="min-h-screen bg-gray-50">
    <header class="bg-white shadow-sm sticky top-0 z-10">
      <div class="max-w-7xl mx-auto px-6 py-4 flex justify-between items-center">
        <h1 class="text-2xl font-bold text-gray-800">🛍 Магазин</h1>
        <p class="text-gray-500">Выберите категорию товаров</p>
      </div>
    </header>

    <main class="max-w-7xl mx-auto px-6 py-6 grid grid-cols-12 gap-6">
      <div v-if="!selectedChapter" class="col-span-12">
        <h2 class="text-xl font-semibold mb-4">Категории товаров</h2>
        <div v-if="filtersStore.isLoading" class="text-gray-500">Загрузка категорий...</div>
        <div v-else-if="filtersStore.error" class="text-red-500">{{ filtersStore.error }}</div>
        <div v-else class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 gap-4">
          <div
              v-for="chapter in filtersStore.productChapters"
              :key="chapter.id"
              @click="selectChapter(chapter)"
              class="cursor-pointer bg-white rounded-xl shadow hover:shadow-lg transition p-4 flex justify-between items-center"
          >
            <h3 class="font-medium text-gray-800">{{ chapter.name }}</h3>
            <span class="text-gray-400">→</span>
          </div>
        </div>
      </div>

      <div v-else class="col-span-12 grid grid-cols-12 gap-6">
        <aside class="col-span-3 bg-white rounded-xl shadow p-4 space-y-6">
          <div class="flex items-center justify-between">
            <button @click="clearSelection" class="text-blue-600 hover:underline">← Все главы</button>
          </div>
          <h2 class="text-lg font-semibold">{{ selectedChapter.name }}</h2>

          <div class="flex justify-between items-center">
            <h3 class="font-medium">Фильтры</h3>
            <button
                v-if="hasActiveFilters"
                @click="clearFilters"
                class="text-sm text-red-500 hover:underline"
            >
              Сбросить
            </button>
          </div>

          <div>
            <label class="block text-sm font-medium mb-1">Сортировка</label>
            <select
                v-model="filters.ordering"
                @change="applyFilters"
                class="w-full border rounded-lg px-3 py-2"
            >
              <option :value="ProductOrdering.PRICE_DEFAULT">По умолчанию</option>
              <option :value="ProductOrdering.PRICE_ASC">Цена ↑</option>
              <option :value="ProductOrdering.PRICE_DESC">Цена ↓</option>
            </select>
          </div>

          <div>
            <label class="block text-sm font-medium mb-1">Цена</label>
            <div class="flex items-center space-x-2">
              <input
                  type="number"
                  v-model="filters.price_min"
                  placeholder="От"
                  @change="applyFilters"
                  class="w-1/2 border rounded-lg px-2 py-1"
              />
              <input
                  type="number"
                  v-model="filters.price_max"
                  placeholder="До"
                  @change="applyFilters"
                  class="w-1/2 border rounded-lg px-2 py-1"
              />
            </div>
          </div>

          <div>
            <label class="block text-sm font-medium mb-1">Бренды</label>
            <div class="space-y-1 max-h-32 overflow-y-auto">
              <label
                  v-for="brand in filtersStore.brands"
                  :key="brand.id"
                  class="flex items-center space-x-2"
              >
                <input type="checkbox" :value="brand.id" v-model="filters.brand" @change="applyFilters" />
                <span>{{ brand.name }}</span>
              </label>
            </div>
          </div>

          <div>
            <label class="block text-sm font-medium mb-1">Страны</label>
            <div class="space-y-1 max-h-32 overflow-y-auto">
              <label
                  v-for="country in filtersStore.countries"
                  :key="country.id"
                  class="flex items-center space-x-2"
              >
                <input type="checkbox" :value="country.id" v-model="filters.country" @change="applyFilters" />
                <span>{{ country.name }}</span>
              </label>
            </div>
          </div>

          <div>
            <label class="block text-sm font-medium mb-1">Категории</label>
            <div class="space-y-1 max-h-32 overflow-y-auto">
              <label
                  v-for="category in filtersStore.productCategories"
                  :key="category.id"
                  class="flex items-center space-x-2"
              >
                <input type="checkbox" :value="category.id" v-model="filters.country" @change="applyFilters" />
                <span>{{ category.name }}</span>
              </label>
            </div>
          </div>
        </aside>

        <section class="col-span-9">
          <h2 class="text-xl font-semibold mb-4">
            Товары ({{ productStore.totalCount }})
          </h2>

          <div v-if="productStore.isLoading" class="text-gray-500">Загрузка...</div>
          <div v-if="productStore.error" class="text-red-500">{{ productStore.error }}</div>

          <div
              v-if="!productStore.isLoading && productStore.products.length === 0"
              class="text-gray-500"
          >
            Товары не найдены. Попробуйте изменить фильтры.
          </div>

          <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-6">
            <div
                v-for="product in productStore.products"
                :key="product.id"
                @click="$router.push(`/details/${product.product_id}`)"
                class="bg-white rounded-xl shadow hover:shadow-lg transition cursor-pointer overflow-hidden"
            >
              <img
                  :src="MEDIA_URL + product.first_image"
                  :alt="product.product_title"
                  class="w-full h-40 object-cover"
              />
              <div class="p-4">
                <h3 class="font-medium text-gray-800 truncate">{{ product.product_title }}</h3>
                <p class="text-blue-600 font-semibold mt-2">{{ product.price }} ₽</p>
                <div class="flex items-center text-sm text-gray-500 mt-1">
                  <span>★ {{ product.average_rating }}</span>
                  <span class="ml-2">({{ product.reviews_count }})</span>
                </div>
              </div>
            </div>
          </div>

          <div v-if="totalPages > 1" class="flex items-center justify-center mt-6 space-x-4">
            <button
                :disabled="productStore.currentPage === 1"
                @click="changePage(productStore.currentPage - 1)"
                class="px-4 py-2 border rounded-lg disabled:opacity-50"
            >
              Назад
            </button>
            <span class="text-gray-600">
              Страница {{ productStore.currentPage }} из {{ totalPages }}
            </span>
            <button
                :disabled="productStore.currentPage === totalPages"
                @click="changePage(productStore.currentPage + 1)"
                class="px-4 py-2 border rounded-lg disabled:opacity-50"
            >
              Вперед
            </button>
          </div>
        </section>
      </div>
    </main>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted, watch } from "vue";
import { useProductFiltersStore } from "@/stores/productFiltersStore";
import { useProductStore } from "@/stores/productStore";
import { ProductOrdering } from "@/types";
import type { ProductChapter, GetProductsParams } from "@/types";
import { MEDIA_URL } from "@/services/baseURL.ts";
import { useRoute, useRouter } from "vue-router";

const filtersStore = useProductFiltersStore();
const productStore = useProductStore();
const route = useRoute();
const router = useRouter();

const selectedChapter = ref<ProductChapter | null>(null);

const filters = ref<GetProductsParams>({
  ordering: ProductOrdering.PRICE_DEFAULT,
  price_min: undefined,
  price_max: undefined,
  brand: [],
  country: [],
  product_category: [],
  page: 1,
  page_size: 40,
});

const hasActiveFilters = computed(() => {
  return (
      filters.value.ordering !== ProductOrdering.PRICE_DEFAULT ||
      filters.value.price_min !== undefined ||
      filters.value.price_max !== undefined ||
      filters.value.brand!.length > 0 ||
      filters.value.country!.length > 0 ||
      filters.value.product_category!.length > 0
  );
});

const totalPages = computed(() => {
  return Math.ceil(productStore.totalCount / productStore.pageSize);
});

const currentChapterCategoryIds = computed(() => {
  if (!selectedChapter.value) return [];
  return filtersStore.productCategories
      .filter((category) => category.product_chapter.id === selectedChapter.value!.id)
      .map((category) => category.id);
});

onMounted(async () => {
  await filtersStore.fetchProductChapters();
  await filtersStore.fetchBrands();
  await filtersStore.fetchCountries();

  // Загружаем главу из URL
  const chapterId = route.params.chapterId;
  if (chapterId) {
    const chapter = filtersStore.productChapters.find((c) => c.id === Number(chapterId));
    if (chapter) {
      selectChapter(chapter);
    }
  }
});

watch(selectedChapter, async (newChapter) => {
  if (newChapter) {
    await filtersStore.fetchProductCategories(newChapter.id)
    await loadProducts()
  }
})

const selectChapter = (chapter: ProductChapter) => {
  selectedChapter.value = chapter
  resetFilters()
  router.push({ name: "ShopChapter", params: { chapterId: chapter.id } })
};

const clearSelection = () => {
  selectedChapter.value = null;
  productStore.products = [];
  router.push({ name: "Shop" });
};

const resetFilters = () => {
  filters.value = {
    ordering: ProductOrdering.PRICE_DEFAULT,
    price_min: undefined,
    price_max: undefined,
    brand: [],
    country: [],
    product_category: [],
    page: 1,
    page_size: 40,
  };
};

const clearFilters = () => {
  resetFilters();
  applyFilters();
};

const applyFilters = () => {
  filters.value.page = 1;
  loadProducts();
};

const changePage = (page: number) => {
  filters.value.page = page;
  loadProducts();
  window.scrollTo({ top: 0, behavior: "smooth" });
};

const loadProducts = async () => {
  if (!selectedChapter.value) return;

  const activeCategoryFilters =
      filters.value.product_category!.length > 0
          ? filters.value.product_category
          : currentChapterCategoryIds.value;

  if (activeCategoryFilters?.length === 0) {
    productStore.products = [];
    productStore.totalCount = 0;
    return;
  }

  await productStore.fetchProducts({
    ...filters.value,
    product_category: activeCategoryFilters,
  });
};
</script>
