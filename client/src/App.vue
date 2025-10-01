<template>
  <div id="app">
      <router-view />
  </div>
</template>

<script setup lang="ts">
import { onMounted, watch } from "vue";
import { useAuthStore } from "@/stores/authStore";
import { useProductFiltersStore } from "@/stores/productFiltersStore";
import { useCartStore } from "@/stores/cartStore";
import { useFavoriteProductStore } from "@/stores/favoriteProductStore";

const authStore = useAuthStore();
const filtersStore = useProductFiltersStore();
const favoritesStore = useFavoriteProductStore();
const cartStore = useCartStore();

onMounted(async () => {
  await filtersStore.fetchProductChapters();
  await filtersStore.fetchBrands();
  await filtersStore.fetchCountries();
});

watch(
    () => authStore.isAuthenticated,
    async (isAuthenticated) => {
      if (isAuthenticated) {
        await cartStore.fetchCart();
        await favoritesStore.fetchFavoriteProducts();
        await authStore.fetchUsername();
      } else {
        cartStore.cart = undefined;
        favoritesStore.favoriteProducts = [];
      }
    },
    { immediate: true }
);
</script>

<style>
*::selection {
  background: #fcc800;
  color: #1c1917;
}
</style>
