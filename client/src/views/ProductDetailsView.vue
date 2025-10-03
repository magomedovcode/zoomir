<template>
  <div class="min-h-screen flex flex-col bg-white">
    <AppHeader />

    <main class="flex-grow container max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <nav class="flex mb-8 animate-fade-in-up">
        <ol class="flex items-center space-x-2 text-sm">
          <li>
            <router-link to="/" class="text-yellow-500 hover:text-yellow-600 font-medium transition-colors duration-300">
              Главная
            </router-link>
          </li>
          <li class="flex items-center">
            <svg class="w-4 h-4 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
            </svg>
          </li>
          <li>
            <router-link
                :to="`/shop/${productDetail?.product_category?.product_chapter?.id}`"
                class="text-yellow-500 hover:text-yellow-600 font-medium transition-colors duration-300"
            >
              {{ productDetail?.product_category?.product_chapter?.name }}
            </router-link>
          </li>
          <li class="flex items-center">
            <svg class="w-4 h-4 text-stone-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
            </svg>
          </li>
          <li class="text-stone-600">{{ productDetail?.title }}</li>
        </ol>
      </nav>

      <div v-if="productDetail" class="grid grid-cols-1 lg:grid-cols-2 gap-8 lg:gap-12 mb-8">
        <div class="animate-fade-in-up">
          <div class="bg-white rounded-2xl shadow-lg border border-stone-300 p-6 lg:sticky top-20">
            <div class="relative mb-4 rounded-xl overflow-hidden bg-stone-100 cursor-zoom-in">
              <img
                  :src="currentImage"
                  :alt="productDetail.title"
                  class="w-full h-full object-cover rounded-xl transform transition-transform duration-700"
                  :class="{'scale-105': isZoomed}"
                  @click="openFullscreen"
              />

              <button
                  v-if="currentVariantImages.length > 1"
                  @click="previousImage"
                  class="absolute left-4 top-1/2 transform -translate-y-1/2 w-10 h-10 bg-white/90 backdrop-blur-sm rounded-full shadow-lg flex items-center justify-center border hover:bg-white hover:shadow-xl transition-all duration-300 group/nav"
                  :disabled="currentImageIndex === 0"
              >
                <svg class="w-5 h-5 text-stone-700 group-hover/nav:text-yellow-500 transition-colors duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/>
                </svg>
              </button>

              <button
                  v-if="currentVariantImages.length > 1"
                  @click="nextImage"
                  class="absolute right-4 top-1/2 transform -translate-y-1/2 w-10 h-10 bg-white/90 backdrop-blur-sm rounded-full shadow-lg flex items-center justify-center border hover:bg-white hover:shadow-xl transition-all duration-300 group/nav"
                  :disabled="currentImageIndex === currentVariantImages.length - 1"
              >
                <svg class="w-5 h-5 text-stone-700 group-hover/nav:text-yellow-500 transition-colors duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
                </svg>
              </button>

              <div v-if="currentVariantImages.length > 1" class="absolute bottom-4 left-1/2 transform -translate-x-1/2 flex space-x-2">
                <div
                    v-for="(_, index) in currentVariantImages"
                    :key="index"
                    class="w-2 h-2 rounded-full transition-all duration-300"
                    :class="index === currentImageIndex ? 'bg-white scale-125' : 'bg-white/50'"
                ></div>
              </div>

              <button
                  @click="toggleFavorite"
                  class="absolute top-4 right-4 w-12 h-12 bg-white/90 backdrop-blur-sm rounded-full shadow-lg flex items-center justify-center transform transition-all duration-300 hover:scale-110 hover:bg-white hover:shadow-xl group/fav"
              >
                <svg
                    class="w-6 h-6 transform transition-all duration-300 group-hover/fav:scale-110"
                    :class="isFavorite ?
                    'text-red-500 fill-current drop-shadow-sm' :
                    'text-stone-400 hover:text-red-400'"
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

              <button
                  @click="openFullscreen"
                  class="absolute top-4 left-4 w-12 h-12 bg-white/90 backdrop-blur-sm rounded-full shadow-lg flex items-center justify-center transform transition-all duration-300 hover:scale-110 hover:bg-white hover:shadow-xl group/fullscreen"
              >
                <svg class="w-6 h-6 text-stone-700 group-hover/fullscreen:text-yellow-500 transition-colors duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0zM10 7v3m0 0v3m0-3h3m-3-3H7"/>
                </svg>
              </button>
            </div>

            <div class="grid grid-cols-5 gap-3" v-if="currentVariantImages.length > 1">
              <button
                  v-for="(image, index) in currentVariantImages"
                  :key="image.id"
                  @click="setCurrentImage(index)"
                  class="relative rounded-lg border-2 transition-all duration-300 overflow-hidden group/thumb"
                  :class="currentImageIndex === index ?
                  'border-yellow-500 shadow-md' :
                  'border-stone-200 hover:border-yellow-400'"
              >
                <img
                    :src="image.image"
                    :alt="`${productDetail.title} - изображение ${index + 1}`"
                    class="w-full h-20 object-cover transform group-hover/thumb:scale-110 transition-transform duration-500"
                />
              </button>
            </div>
          </div>
        </div>

        <div class="animate-fade-in-up animation-delay-300">
          <div class="bg-white rounded-2xl shadow-lg border border-stone-300 p-8">
            <div class="mb-4">
              <h1 class="text-3xl font-bold text-stone-800 mb-4">{{ productDetail.title }}</h1>
              <div class="flex items-center space-x-4">
                <div class="flex items-center space-x-2">
                  <div class="flex">
                    <svg
                        v-for="star in 5"
                        :key="star"
                        class="w-5 h-5"
                        :class="star <= Math.round(productDetail.average_rating || 0) ?
                        'text-yellow-400 fill-current' :
                        'text-stone-300 fill-current'"
                        viewBox="0 0 20 20"
                    >
                      <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/>
                    </svg>
                  </div>
                  <span class="text-lg font-semibold text-stone-700">{{ productDetail.average_rating || 0 }}</span>
                  <span class="text-stone-500">({{ productDetail.reviews_count }} отзывов)</span>
                </div>
              </div>
            </div>

            <div class="flex items-center justify-between mb-4">
              <div>
                <p class="text-4xl font-bold bg-gradient-to-r from-yellow-500 to-amber-600 bg-clip-text text-transparent">
                  {{ Intl.NumberFormat('ru-RU').format(+(currentVariant?.price || productDetail.product_variants[0]?.price)) }} ₽
                </p>
              </div>
            </div>

            <div class="mt-4 mb-8">
              <h3 class="text-sm font-medium text-stone-700 mb-3">Варианты товара:</h3>
              <div class="flex flex-wrap gap-2">
                <button
                    v-for="variant in productDetail.product_variants"
                    :key="variant.id"
                    @click="selectVariant(variant)"
                    class="px-3 py-2 rounded-lg border-2 transition-all duration-300 text-sm font-medium"
                    :class="currentVariant?.id === variant.id ?
                    'border-yellow-500 bg-yellow-50 text-yellow-600 shadow-sm' :
                    'border-stone-300 text-stone-700 hover:border-yellow-300 hover:bg-yellow-50/50'"
                >
                  {{ variant.name }}
                </button>
              </div>
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 mb-6">
              <router-link
                  :to="getBrandLink"
                  class="flex items-center space-x-3 p-4 rounded-xl hover:bg-yellow-100"
              >
                <div class="w-12 h-12 bg-white rounded-lg shadow-sm border border-stone-300 flex items-center justify-center p-2">
                  <img
                      v-if="productDetail.brand.logo"
                      :src="productDetail.brand.logo"
                      :alt="productDetail.brand.name"
                      class="w-full h-full object-contain"
                  >
                </div>
                <div>
                  <p class="text-sm text-stone-500">Бренд</p>
                  <p class="font-semibold text-stone-800">{{ productDetail.brand.name }}</p>
                </div>
              </router-link>
              <router-link
                  :to="getCountryLink"
                  class="flex items-center space-x-3 p-4  rounded-xl hover:bg-yellow-100"
              >
                <div class="w-12 h-12 bg-white rounded-lg shadow-sm border border-stone-300 flex items-center justify-center p-1">
                  <img
                      v-if="productDetail.country.flag"
                      :src="productDetail.country.flag"
                      :alt="productDetail.country.name"
                      class="w-full h-full object-contain rounded"
                  >
                </div>
                <div>
                  <p class="text-sm text-stone-500">Страна произоводства</p>
                  <p class="font-semibold text-stone-800">{{ productDetail.country.name }}</p>
                </div>
              </router-link>
            </div>

            <div class="mb-6">
              <h3 class="text-lg font-semibold text-stone-800 mb-4">Характеристики</h3>
              <div class="space-y-3">
                <div
                    v-for="(attribute, index) in displayedAttributes"
                    :key="attribute.id"
                    class="flex justify-between py-2 border-b border-stone-200 last:border-b-0"
                    :class="{'animate-fade-in': index < 3}"
                >
                  <span class="text-sm text-stone-600 w-1/2">{{ attribute.name }}:</span>
                  <span class="text-sm font-medium text-stone-800 text-right w-1/2">{{ attribute.value }}</span>
                </div>

                <button
                    v-if="allAttributes.length > 3"
                    @click="showAllAttributes = !showAllAttributes"
                    class="w-full mt-3 px-4 py-2 text-yellow-500 hover:text-yellow-600 font-medium text-sm transition-all duration-300 rounded-lg hover:bg-yellow-100 flex items-center justify-center space-x-2"
                >
                  <span>{{ showAllAttributes ? 'Скрыть' : 'Показать все' }}</span>
                  <svg
                      class="w-4 h-4 transform transition-transform duration-300"
                      :class="{'rotate-180': showAllAttributes}"
                      fill="none"
                      stroke="currentColor"
                      viewBox="0 0 24 24"
                  >
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
                  </svg>
                </button>
              </div>
            </div>

            <div class="border-t border-stone-300 pt-6">
              <button
                  @click="addToCart"
                  :disabled="cartStore.isLoading"
                  class="group/btn relative w-full py-4 px-6 rounded-xl font-bold text-lg transition-all duration-500 transform overflow-hidden"
                  :class="isInCart ?
                  'bg-gradient-to-r from-red-500 to-pink-600 hover:from-red-600 hover:to-pink-700 text-white shadow-lg hover:shadow-xl' :
                  'bg-gradient-to-r from-yellow-500 to-amber-600 hover:from-yellow-600 hover:to-amber-700 text-white shadow-lg hover:shadow-xl'"
              >
                <span class="relative z-10 flex items-center justify-center">
                  <svg
                      v-if="cartStore.isLoading"
                      class="animate-spin -ml-1 mr-3 h-5 w-5 text-white"
                      fill="none"
                      viewBox="0 0 24 24"
                  >
                    <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                    <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                  </svg>

                  <svg
                      v-else-if="isInCart"
                      class="w-6 h-6 mr-3 transform group-hover/btn:scale-110 transition-transform duration-300"
                      fill="none"
                      stroke="currentColor"
                      viewBox="0 0 24 24"
                  >
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
                  </svg>

                  <svg
                      v-else
                      class="w-6 h-6 mr-3 transform group-hover/btn:scale-110 transition-transform duration-300"
                      fill="none"
                      stroke="currentColor"
                      viewBox="0 0 24 24"
                  >
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6"/>
                  </svg>

                  {{ isInCart ? 'Товар в корзине' : 'Добавить в корзину' }}
                </span>
              </button>
            </div>
          </div>
        </div>
      </div>

      <div v-if="productDetail" class="mb-8 animate-fade-in-up animation-delay-500">
        <div class="bg-white rounded-2xl shadow-lg border border-stone-300 p-8">
          <h2 class="text-2xl font-bold text-stone-800 mb-6">Описание товара</h2>
          <div class="prose prose-lg max-w-none">
            <div
                class="text-stone-600 leading-relaxed transition-all duration-500"
                :class="showFullDescription ? 'max-h-none' : 'max-h-32 overflow-hidden'"
            >
              <p>{{ productDetail.description }}</p>
            </div>

            <button
                v-if="productDetail.description.length > 200"
                @click="showFullDescription = !showFullDescription"
                class="mt-4 px-6 py-2 text-yellow-500 hover:text-yellow-600 font-medium text-sm transition-all duration-300 rounded-lg hover:bg-yellow-100 flex items-center space-x-2"
            >
              <span>{{ showFullDescription ? 'Скрыть' : 'Показать всё' }}</span>
              <svg
                  class="w-4 h-4 transform transition-transform duration-300"
                  :class="{'rotate-180': showFullDescription}"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
              >
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
              </svg>
            </button>
          </div>
        </div>
      </div>

      <div v-if="authStore.isAuthenticated && !userHasReviewed" class="mb-8">
        <div class="bg-gradient-to-r from-stone-800 to-stone-700 rounded-2xl p-6">
          <h3 class="text-lg font-semibold text-white mb-4">Оставить отзыв</h3>
          <form @submit.prevent="submitReview" class="space-y-4">
            <div>
              <label class="block text-base font-medium text-white mb-2">Оценка</label>
              <div class="flex space-x-1">
                <button
                    v-for="star in 5"
                    :key="star"
                    type="button"
                    @click="newReview.rating = star"
                    class="transform transition-all duration-300 hover:scale-110"
                >
                  <svg
                      class="w-8 h-8"
                      :class="star <= newReview.rating ?
                          'text-yellow-400 fill-current' :
                          'text-stone-500 fill-current hover:text-yellow-300'"
                      viewBox="0 0 20 20"
                  >
                    <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/>
                  </svg>
                </button>
              </div>
            </div>

            <div>
              <label for="reviewTitle" class="block text-base font-medium text-white mb-2">Заголовок</label>
              <input
                  id="reviewTitle"
                  v-model="newReview.title"
                  type="text"
                  required
                  class="w-full px-4 py-3 bg-stone-700 placeholder:text-stone-400 text-white rounded-xl focus:outline-none focus:ring-2 focus:ring-yellow-500 focus:border-yellow-500 transition-all duration-300"
                  placeholder="Краткое описание отзыва"
              >
            </div>

            <div>
              <label for="reviewComment" class="block text-base font-medium text-white mb-2">Комментарий</label>
              <textarea
                  id="reviewComment"
                  v-model="newReview.comment"
                  required
                  rows="4"
                  class="w-full px-4 py-3 bg-stone-700 placeholder:text-stone-400 text-white rounded-xl focus:outline-none focus:ring-2 focus:ring-yellow-500 focus:border-yellow-500 resize-none transition-all duration-300"
                  placeholder="Подробно опишите ваш опыт использования товара"
              ></textarea>
            </div>

            <button
                type="submit"
                :disabled="reviewStore.isLoading"
                class="px-6 py-3 bg-gradient-to-r from-yellow-500 to-amber-600 text-stone-800 font-semibold rounded-xl hover:shadow-lg transition-all duration-300 transform hover:-translate-y-0.5 disabled:opacity-50"
            >
              {{ reviewStore.isLoading ? 'Отправка...' : 'Опубликовать отзыв' }}
            </button>
          </form>
        </div>
      </div>

      <section class="mb-16 animate-fade-in-up animation-delay-500">
        <div class="bg-white rounded-2xl shadow-lg border border-stone-300 p-8">
          <div class="flex items-center justify-between mb-8">
            <h2 class="text-2xl font-bold text-stone-800">Отзывы покупателей</h2>
            <div class="flex items-center space-x-4">
              <div class="text-center">
                <p class="text-3xl font-bold bg-gradient-to-r from-yellow-500 to-amber-600 bg-clip-text text-transparent">
                  {{ productDetail?.average_rating || 0 }}
                </p>
                <div class="flex justify-center">
                  <svg
                      v-for="star in 5"
                      :key="star"
                      class="w-4 h-4"
                      :class="star <= Math.round(productDetail?.average_rating || 0) ?
                      'text-yellow-400 fill-current' :
                      'text-stone-300 fill-current'"
                      viewBox="0 0 20 20"
                  >
                    <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/>
                  </svg>
                </div>
                <p class="text-sm text-stone-500 mt-1">{{ productDetail?.reviews_count }} отзывов</p>
              </div>
            </div>
          </div>

          <div class="space-y-6">
            <div
                v-for="review in productDetail?.reviews"
                :key="review.id"
                class="border border-stone-300 rounded-2xl p-6 hover:shadow-md transition-all duration-300"
            >
              <div class="flex items-start justify-between mb-4">
                <div class="flex items-center space-x-3">
                  <div class="w-12 h-12 bg-gradient-to-r from-yellow-500 to-amber-600 rounded-full flex items-center justify-center text-white font-bold text-lg">
                    {{ review.user.charAt(0).toUpperCase() }}
                  </div>
                  <div>
                    <p class="font-semibold text-stone-800">{{ review.user }}</p>
                    <p class="text-sm text-stone-500">{{ formatDate(review.date) }}</p>
                  </div>
                </div>
                <div class="flex items-center space-x-4">
                  <div class="flex items-center space-x-1">
                    <div class="flex">
                      <svg
                          class="w-4 h-4 sm:w-5 sm:h-5 text-yellow-400 fill-current"
                          viewBox="0 0 20 20"
                      >
                        <path
                            d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"
                        />
                      </svg>
                    </div>
                    <span class="text-sm font-medium text-stone-700">{{ review.rating }}</span>
                  </div>

                  <button
                      v-if="authStore.isAuthenticated && review.user === authStore.user?.username"
                      @click="deleteReview(review.id)"
                      class="text-red-500 hover:text-red-700 transition-colors duration-300 p-2 rounded-lg hover:bg-red-50"
                      title="Удалить отзыв"
                  >
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"/>
                    </svg>
                  </button>
                </div>
              </div>

              <h4 class="font-semibold text-stone-800 mb-2">{{ review.title }}</h4>
              <p class="text-stone-600 leading-relaxed">{{ review.comment }}</p>
            </div>

            <div v-if="productDetail?.reviews.length === 0" class="text-center py-12">
              <div class="w-24 h-24 mx-auto mb-4 bg-stone-100 rounded-full flex items-center justify-center">
                <svg class="w-12 h-12 text-stone-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"/>
                </svg>
              </div>
              <h3 class="text-lg font-semibold text-stone-800 mb-2">Отзывов пока нет</h3>
              <p class="text-stone-600">Будьте первым, кто оставит отзыв об этом товаре!</p>
            </div>
          </div>
        </div>
      </section>

      <section class="animate-fade-in-up animation-delay-700">
        <h2 class="text-2xl font-bold text-stone-800 mb-8">Похожие товары</h2>
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
          <ProductCard
              v-for="similarProduct in similarProducts"
              :key="similarProduct.id"
              :product="similarProduct"
              class="transform transition-all duration-500 hover:scale-105"
          />
        </div>
      </section>
    </main>

    <AppFooter />

    <div v-if="isFullscreen" class="fixed inset-0 bg-black/90 z-50 flex items-center justify-center p-4">
      <div class="relative w-full h-full flex items-center justify-center">
        <button
            @click="closeFullscreen"
            class="absolute top-4 right-4 z-10 w-12 h-12 bg-white/20 backdrop-blur-sm rounded-full flex items-center justify-center hover:bg-white/30 transition-all duration-300 group/close"
        >
          <svg class="w-6 h-6 text-white group-hover/close:scale-110 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
          </svg>
        </button>

        <button
            v-if="currentVariantImages.length > 1"
            @click="previousImage"
            class="absolute left-4 top-1/2 transform -translate-y-1/2 z-10 w-12 h-12 bg-white/20 backdrop-blur-sm rounded-full flex items-center justify-center hover:bg-white/30 transition-all duration-300 group/nav"
            :disabled="currentImageIndex === 0"
        >
          <svg class="w-6 h-6 text-white group-hover/nav:scale-110 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/>
          </svg>
        </button>

        <button
            v-if="currentVariantImages.length > 1"
            @click="nextImage"
            class="absolute right-4 top-1/2 transform -translate-y-1/2 z-10 w-12 h-12 bg-white/20 backdrop-blur-sm rounded-full flex items-center justify-center hover:bg-white/30 transition-all duration-300 group/nav"
            :disabled="currentImageIndex === currentVariantImages.length - 1"
        >
          <svg class="w-6 h-6 text-white group-hover/nav:scale-110 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
          </svg>
        </button>

        <img
            :src="currentImage"
            :alt="productDetail?.title"
            class="max-w-full max-h-full object-contain rounded-lg transform transition-transform duration-500"
            :style="{ transform: `scale(${fullscreenZoom})` }"
        />

        <div v-if="currentVariantImages.length > 1" class="absolute bottom-4 left-1/2 transform -translate-x-1/2 flex space-x-2 z-10">
          <div
              v-for="(_, index) in currentVariantImages"
              :key="index"
              class="w-3 h-3 rounded-full transition-all duration-300 cursor-pointer"
              :class="index === currentImageIndex ? 'bg-white scale-125' : 'bg-white/50 hover:bg-white/70'"
              @click="setCurrentImage(index)"
          ></div>
        </div>

        <div class="absolute bottom-4 right-4 z-10 text-white/80 text-sm">
          {{ currentImageIndex + 1 }} / {{ currentVariantImages.length }}
        </div>

        <div class="absolute bottom-4 left-4 z-10 flex space-x-2">
          <button
              @click="zoomOut"
              class="w-10 h-10 bg-white/20 backdrop-blur-sm rounded-full flex items-center justify-center hover:bg-white/30 transition-all duration-300 group/zoom"
              :disabled="fullscreenZoom <= 1"
          >
            <svg class="w-5 h-5 text-white group-hover/zoom:scale-110 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 12H4"/>
            </svg>
          </button>
          <button
              @click="zoomIn"
              class="w-10 h-10 bg-white/20 backdrop-blur-sm rounded-full flex items-center justify-center hover:bg-white/30 transition-all duration-300 group/zoom"
              :disabled="fullscreenZoom >= 3"
          >
            <svg class="w-5 h-5 text-white group-hover/zoom:scale-110 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/>
            </svg>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router' // Добавьте useRouter
import AppHeader from '@/components/AppHeader.vue'
import AppFooter from '@/components/AppFooter.vue'
import ProductCard from '@/components/ProductCard.vue'
import { useProductStore } from '@/stores/productStore'
import { useAuthStore } from '@/stores/authStore'
import { useCartStore } from '@/stores/cartStore'
import { useFavoriteProductStore } from '@/stores/favoriteProductStore'
import { useReviewStore } from '@/stores/reviewStore'
import type { VariantInProduct, CreateReviewBody, ProductVariant, ProductImage, Attribute } from '@/types'

const route = useRoute()
const router = useRouter()
const productStore = useProductStore()
const authStore = useAuthStore()
const cartStore = useCartStore()
const favoritesStore = useFavoriteProductStore()
const reviewStore = useReviewStore()

const showAllAttributes = ref(false)
const showFullDescription = ref(false)

const productId = computed(() => Number(route.params.id))
const productDetail = computed(() => productStore.productDetail)
const currentVariant = ref<VariantInProduct>()
const currentImageIndex = ref(0)
const isZoomed = ref(false)
const isFullscreen = ref(false)
const fullscreenZoom = ref(1)

const getBrandLink = computed(() => {
  return {
    path: `/shop/${productDetail.value?.product_category.product_chapter.id}`,
    query: {
      brands: productDetail.value?.brand.id
    }
  }
})

const getCountryLink = computed(() => {
  return {
    path: `/shop/${productDetail.value?.product_category.product_chapter.id}`,
    query: {
      countries: productDetail.value?.country.id
    }
  }
})

const variantIdFromUrl = computed(() => {
  const variantId = route.query.variant
  return variantId ? Number(variantId) : null
})

const allAttributes = computed<Attribute[]>(() => {
  if (!currentVariant.value?.attributes && !productDetail.value?.product_variants[0]?.attributes) {
    return []
  }

  const attributes = currentVariant.value?.attributes || productDetail.value?.product_variants[0]?.attributes || []
  return attributes.flatMap(category =>
      category.attributes.map(attr => ({
        ...attr,
        categoryName: category.name
      }))
  )
})

const displayedAttributes = computed(() => {
  return showAllAttributes.value ? allAttributes.value : allAttributes.value.slice(0, 3)
})

const currentVariantImages = computed<ProductImage[]>(() => {
  return currentVariant.value?.product_images || productDetail.value?.product_variants[0]?.product_images || []
})

const currentImage = computed(() => {
  return currentVariantImages.value[currentImageIndex.value]?.image || ''
})

const userHasReviewed = computed(() => {
  if (!authStore.isAuthenticated || !authStore.user) return false
  return productDetail.value?.reviews?.some(review => review.user === authStore.user?.username) || false
})

const isInCart = computed(() => {
  if (!cartStore.cart || !currentVariant.value) return false
  return cartStore.cart.products_in_cart.some(item =>
      item.product_variant.id === currentVariant.value?.id
  )
})

const isFavorite = computed(() => {
  return favoritesStore.favoriteProducts.some(fp => fp.product.id === productDetail.value?.id)
})

const similarProducts = computed<ProductVariant[]>(() => {
  return productStore.products
      .filter(product => product.product_id !== productDetail.value?.id)
      .slice(0, 4)
      .map(product => ({
        ...product,
        average_rating: product.average_rating || 0,
        reviews_count: product.reviews_count || 0
      }))
})

onMounted(async () => {
  await loadProductData()
})

watch(() => route.params.id, async () => {
  await loadProductData()
})

watch(() => route.query.variant, (newVariantId) => {
  if (newVariantId && productDetail.value) {
    applyVariantFromUrl(Number(newVariantId))
  }
})

const loadProductData = async () => {
  await productStore.fetchProductDetails(productId.value)

  if (productDetail.value?.product_variants?.length) {
    if (variantIdFromUrl.value) {
      applyVariantFromUrl(variantIdFromUrl.value)
    } else {
      currentVariant.value = productDetail.value.product_variants[0]
      currentImageIndex.value = 0
    }
  }

  if (authStore.isAuthenticated) {
    await cartStore.fetchCart()
    await favoritesStore.fetchFavoriteProducts()
  }
}

const applyVariantFromUrl = (variantId: number) => {
  if (!productDetail.value) return

  const variant = productDetail.value.product_variants.find(v => v.id === variantId)
  if (variant) {
    currentVariant.value = variant
    currentImageIndex.value = 0
  } else {
    currentVariant.value = productDetail.value.product_variants[0]
    currentImageIndex.value = 0
  }
}

const updateUrlWithVariant = (variantId: number) => {
  router.replace({
    query: {
      ...route.query,
      variant: variantId.toString()
    }
  })
}

const nextImage = () => {
  if (currentImageIndex.value < currentVariantImages.value.length - 1) {
    currentImageIndex.value++
    fullscreenZoom.value = 1
  }
}

const previousImage = () => {
  if (currentImageIndex.value > 0) {
    currentImageIndex.value--
    fullscreenZoom.value = 1
  }
}

const setCurrentImage = (index: number) => {
  currentImageIndex.value = index
  isZoomed.value = false
  fullscreenZoom.value = 1
}

const zoomIn = () => {
  if (fullscreenZoom.value < 3) {
    fullscreenZoom.value += 0.25
  }
}

const zoomOut = () => {
  if (fullscreenZoom.value > 1) {
    fullscreenZoom.value -= 0.25
  }
}

const openFullscreen = () => {
  isFullscreen.value = true
  fullscreenZoom.value = 1
  document.body.style.overflow = 'hidden'
}

const closeFullscreen = () => {
  isFullscreen.value = false
  fullscreenZoom.value = 1
  document.body.style.overflow = 'auto'
}

const handleKeydown = (e: KeyboardEvent) => {
  if (!isFullscreen.value) return

  switch (e.key) {
    case 'Escape':
      closeFullscreen()
      break
    case 'ArrowLeft':
      previousImage()
      break
    case 'ArrowRight':
      nextImage()
      break
    case '+':
    case '=':
      zoomIn()
      break
    case '-':
      zoomOut()
      break
  }
}

onMounted(() => {
  document.addEventListener('keydown', handleKeydown)
})

const selectVariant = (variant: VariantInProduct) => {
  currentVariant.value = variant
  currentImageIndex.value = 0
  isZoomed.value = false
  fullscreenZoom.value = 1
  updateUrlWithVariant(variant.id)
}

const addToCart = async () => {
  if (!currentVariant.value) return

  if (isInCart.value) {
    await cartStore.removeFromCart(currentVariant.value.id)
  } else {
    await cartStore.addToCart({
      product_variant: currentVariant.value.id,
      quantity: 1
    })
  }
  await cartStore.fetchCart()
}

const toggleFavorite = async () => {
  if (!productDetail.value) return

  if (isFavorite.value) {
    await favoritesStore.removeFromFavorite(productDetail.value.id)
  } else {
    await favoritesStore.addToFavorite(productDetail.value.id)
  }
  await favoritesStore.fetchFavoriteProducts()
}

const submitReview = async () => {
  if (!newReview.value.title || !newReview.value.comment) return

  await reviewStore.createReview({
    ...newReview.value,
    productId: productId.value
  })

  newReview.value = {
    productId: productId.value,
    title: '',
    rating: 5,
    comment: ''
  }

  await productStore.fetchProductDetails(productId.value)
}

const deleteReview = async (reviewId: number) => {
  if (confirm('Вы уверены, что хотите удалить этот отзыв?')) {
    await reviewStore.deleteReview(reviewId, productId.value)
    await productStore.fetchProductDetails(productId.value)
  }
}

const formatDate = (dateString: string) => {
  return new Date(dateString).toLocaleDateString('ru-RU', {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  })
}

const newReview = ref<CreateReviewBody>({
  productId: productId.value,
  title: '',
  rating: 5,
  comment: ''
})
</script>
