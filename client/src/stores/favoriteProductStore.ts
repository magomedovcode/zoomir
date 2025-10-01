import {defineStore} from "pinia";
import {ref} from "vue";
import type {FavoriteProduct} from "@/types";
import {
    addToFavorites,
    clearFavorites,
    getFavoriteProducts,
    removeFromFavorites
} from "@/services/favoriteProductService.ts";

export const useFavoriteProductStore = defineStore('favoriteProduct', () => {
    const favoriteProducts = ref<FavoriteProduct[]>([]);

    const isLoading = ref<boolean>(false);
    const error = ref<string | null>(null);

    const fetchFavoriteProducts = async () => {
        isLoading.value = true;
        error.value = null;
        try {
            favoriteProducts.value = await getFavoriteProducts();
        } catch (err) {
            error.value = `Ошибка при загрузке избранных товаров: ${err}`;
            console.error(error.value);
        } finally {
            isLoading.value = false;
        }
    }

    const addToFavorite = async (productId: number) => {
        isLoading.value = true;
        error.value = null;
        try {
            await addToFavorites(productId);
        } catch (err) {
            error.value = `Ошибка при добавлении товара в избранное: ${err}`;
            console.error(error.value);
        } finally {
            isLoading.value = false;
        }
    }

    const removeFromFavorite = async (productId: number) => {
        isLoading.value = true;
        error.value = null;
        try {
            await removeFromFavorites(productId);
        } catch (err) {
            error.value = `Ошибка при удалении товара из избранного: ${err}`;
            console.error(error.value);
        } finally {
            isLoading.value = false;
        }
    }

    const clearFavorite = async () => {
        isLoading.value = true;
        error.value = null;
        try {
            await clearFavorites();
        } catch (err) {
            error.value = `Ошибка при очистке избранных товаров: ${err}`;
            console.error(error.value);
        } finally {
            isLoading.value = false;
        }
    }

    return {
        favoriteProducts,
        isLoading,
        error,
        fetchFavoriteProducts,
        addToFavorite,
        removeFromFavorite,
        clearFavorite
    }
});
