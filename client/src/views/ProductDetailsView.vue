<template>
  <div class="max-w-7xl mx-auto px-6 py-6">
    <nav class="text-sm text-gray-500 mb-4 flex items-center space-x-2">
      <router-link
          v-if="chapterIdFromQuery"
          :to="`/shop/${chapterIdFromQuery}`"
          class="hover:text-blue-600"
      >
        ← Назад в магазин
      </router-link>
      <span class="text-gray-800">{{ productDetail?.title }}</span>
    </nav>

    <div v-if="productStore.isLoading" class="text-gray-500">Загрузка товара...</div>
    <div v-else-if="productStore.error" class="text-red-500 space-y-2">
      <p>{{ productStore.error }}</p>
      <button
          @click="fetchProductDetails"
          class="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700"
      >
        Попробовать снова
      </button>
    </div>

    <div v-else-if="productDetail" class="grid grid-cols-12 gap-8">
      <div class="col-span-5 space-y-4">
        <div class="aspect-square bg-gray-100 flex items-center justify-center rounded-xl overflow-hidden">
          <img
              v-if="currentImage"
              :src="currentImage"
              :alt="productDetail.title"
              class="object-contain max-h-full"
          />
          <span v-else class="text-gray-400">Нет изображения</span>
        </div>
        <div class="flex space-x-2 overflow-x-auto">
          <div
              v-for="(image, index) in currentVariant?.product_images || []"
              :key="image.id"
              @click="currentImageIndex = index"
              class="w-16 h-16 rounded-lg overflow-hidden cursor-pointer border"
              :class="currentImageIndex === index ? 'border-blue-600' : 'border-gray-200'"
          >
            <img :src="image.image" class="object-cover w-full h-full"  alt=""/>
          </div>
        </div>
      </div>

      <div class="col-span-7 space-y-6">
        <h1 class="text-2xl font-bold text-gray-800">{{ productDetail.title }}</h1>

        <div class="text-gray-600 space-y-1">
          <p><span class="font-medium">Бренд:</span> {{ productDetail.brand.name }}</p>
          <p><span class="font-medium">Страна:</span> {{ productDetail.country.name }}</p>
          <p><span class="font-medium">Категория:</span> {{ productDetail.product_category.name }}</p>
        </div>

        <div class="flex items-center space-x-2">
          <div class="flex text-yellow-400">
            <span
                v-for="n in 5"
                :key="n"
                :class="n <= Math.round(productDetail.average_rating) ? 'text-yellow-400' : 'text-gray-300'"
            >
              ★
            </span>
          </div>
          <span class="text-gray-600">
            {{ productDetail.average_rating.toFixed(1) }} ({{ productDetail.reviews_count }} отзывов)
          </span>
        </div>

        <div v-if="productDetail.product_variants?.length" class="space-y-2">
          <h3 class="font-semibold">Варианты:</h3>
          <div class="grid grid-cols-2 gap-4">
            <div
                v-for="variant in productDetail.product_variants"
                :key="variant.id"
                @click="selectVariant(variant)"
                class="p-3 border rounded-lg cursor-pointer hover:shadow"
                :class="currentVariant?.id === variant.id ? 'border-blue-600' : 'border-gray-200'"
            >
              <h4 class="mt-2 font-medium">{{ variant.name }}</h4>
              <p class="text-blue-600 font-semibold">{{ variant.price }} ₽</p>
            </div>
          </div>
        </div>

        <div v-if="currentVariant?.attributes?.length" class="space-y-3">
          <h3 class="font-semibold">Характеристики:</h3>
          <div
              v-for="attributeCategory in currentVariant.attributes"
              :key="attributeCategory.id"
          >
            <h4 class="font-medium">{{ attributeCategory.name }}</h4>
            <ul class="ml-4 list-disc text-gray-600">
              <li
                  v-for="attribute in attributeCategory.attributes"
                  :key="attribute.id"
              >
                {{ attribute.name }}: {{ attribute.value }}
              </li>
            </ul>
          </div>
        </div>

        <div class="flex space-x-4">
          <button
              @click="addToCart"
              :disabled="!currentVariant"
              class="px-6 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 disabled:opacity-50"
          >
            Добавить в корзину
          </button>
          <button
              @click="toggleFavorite"
              :class="isInFavorites ? 'text-red-500' : 'text-gray-400'"
              class="text-2xl"
          >
            ♥
          </button>
        </div>
      </div>
    </div>

    <div v-if="productDetail?.description" class="mt-8 bg-white p-6 rounded-xl shadow">
      <h3 class="text-lg font-semibold mb-2">Описание</h3>
      <p class="text-gray-700 leading-relaxed">{{ productDetail.description }}</p>
    </div>

    <div class="mt-8">
      <div class="flex items-center justify-between mb-4">
        <h3 class="text-lg font-semibold">Отзывы ({{ productDetail?.reviews_count }})</h3>
        <button
            v-if="isAuthenticated"
            @click="showReviewForm = !showReviewForm"
            class="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700"
        >
          Добавить отзыв
        </button>
      </div>

      <div v-if="showReviewForm && isAuthenticated" class="mb-6 bg-gray-50 p-4 rounded-lg">
        <h4 class="font-medium mb-2">Оставить отзыв</h4>
        <form @submit.prevent="submitReview" class="space-y-3">
          <input v-model="newReview.title" type="text" placeholder="Заголовок" required
                 class="w-full border rounded px-3 py-2" />
          <div>
            <span v-for="n in 5" :key="n"
                  class="cursor-pointer text-2xl"
                  :class="n <= newReview.rating ? 'text-yellow-400' : 'text-gray-300'"
                  @click="newReview.rating = n">★</span>
          </div>
          <textarea v-model="newReview.comment" required
                    placeholder="Комментарий"
                    class="w-full border rounded px-3 py-2">
          </textarea>
          <div class="flex space-x-2">
            <button type="submit"
                    class="px-4 py-2 bg-green-600 text-white rounded hover:bg-green-700"
                    :disabled="reviewStore.isLoading">
              {{ reviewStore.isLoading ? 'Отправка...' : 'Отправить' }}
            </button>
            <button type="button" @click="cancelReview"
                    class="px-4 py-2 border rounded">Отмена</button>
          </div>
        </form>
      </div>

      <div v-if="productDetail?.reviews?.length" class="space-y-4">
        <div
            v-for="review in productDetail?.reviews"
            :key="review.id"
            class="p-4 bg-white rounded-lg shadow"
        >
          <div class="flex justify-between items-center mb-2">
            <div class="flex items-center space-x-2">
              <span class="font-medium">{{ review.user }}</span>
              <div class="text-yellow-400">
                <span v-for="n in 5" :key="n"
                      :class="n <= review.rating ? 'text-yellow-400' : 'text-gray-300'">★</span>
              </div>
            </div>
            <span class="text-gray-500 text-sm">{{ formatDate(review.date) }}</span>
          </div>
          <h4 class="font-semibold">{{ review.title }}</h4>
          <p class="text-gray-700">{{ review.comment }}</p>
        </div>
      </div>
      <p v-else class="text-gray-500">Пока нет отзывов. Будьте первым!</p>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted, watch } from "vue";
import { useRoute, useRouter } from "vue-router";
import { useProductStore } from "@/stores/productStore";
import { useFavoriteProductStore } from "@/stores/favoriteProductStore";
import { useReviewStore } from "@/stores/reviewStore";
import type { VariantInProduct, CreateReviewBody } from "@/types";

const route = useRoute();
const router = useRouter();
const productStore = useProductStore();
const favoriteStore = useFavoriteProductStore();
const reviewStore = useReviewStore();

const productId = computed(() => Number(route.params.id));
const chapterIdFromQuery = computed(() => route.query.chapterId);
const currentVariant = ref<VariantInProduct>();
const currentImageIndex = ref(0);
const showReviewForm = ref(false);
const isInFavorites = ref(false);

const newReview = ref({
  title: "",
  rating: 5,
  comment: ""
});

const isAuthenticated = computed(() => !!localStorage.getItem("token"));
const productDetail = computed(() => productStore.productDetail);
const currentImage = computed(() =>
    currentVariant.value?.product_images?.[currentImageIndex.value]
        ? currentVariant.value.product_images[currentImageIndex.value].image
        : null
);

onMounted(async () => {
  await fetchProductDetails();
  await checkIfInFavorites();
});

watch(productId, async (newId) => {
  if (newId) {
    await fetchProductDetails();
    await checkIfInFavorites();
  }
});

watch(productDetail, (newDetail) => {
  if (newDetail?.product_variants?.length) {
    currentVariant.value = newDetail.product_variants[0];
  } else {
    currentVariant.value = undefined;
  }
});

const fetchProductDetails = async () => {
  if (productId.value) {
    await productStore.fetchProductDetails(productId.value);
  }
};

const checkIfInFavorites = async () => {
  if (!isAuthenticated.value) return;
  await favoriteStore.fetchFavoriteProducts();
  isInFavorites.value = favoriteStore.favoriteProducts.some(
      (fav) => fav.product.id === productId.value
  );
};

const selectVariant = (variant: VariantInProduct) => {
  currentVariant.value = variant;
  currentImageIndex.value = 0;
};

const toggleFavorite = async () => {
  if (!isAuthenticated.value) {
    await router.push("/login");
    return;
  }
  if (isInFavorites.value) {
    await favoriteStore.removeFromFavorite(productId.value);
  } else {
    await favoriteStore.addToFavorite(productId.value);
  }
  isInFavorites.value = !isInFavorites.value;
};

const addToCart = async () => {
  if (!isAuthenticated.value) {
    await router.push("/login");
    return;
  }
  if (!currentVariant.value) return;
  console.log("Добавление в корзину:", currentVariant.value);
};

const submitReview = async () => {
  if (!productId.value) return;
  const reviewData: CreateReviewBody = {
    productId: productId.value,
    title: newReview.value.title,
    rating: newReview.value.rating,
    comment: newReview.value.comment
  };
  await reviewStore.createReview(reviewData);
  await fetchProductDetails();
  cancelReview();
};

const cancelReview = () => {
  showReviewForm.value = false;
  newReview.value = { title: "", rating: 5, comment: "" };
};

const formatDate = (dateString: string) =>
    new Date(dateString).toLocaleDateString("ru-RU");
</script>
