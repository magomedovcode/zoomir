import { defineStore } from "pinia";
import { ref } from "vue";
import type { OrderProduct, Cart } from "@/types";
import {
    addToCarts,
    getCart,
    removeFromCarts
} from "@/services/cartService.ts";

export const useCartStore = defineStore('cart', () => {
    const cart = ref<Cart>();

    const isLoading = ref<boolean>(false);
    const error = ref<string | null>(null);

    const fetchCart = async () => {
        isLoading.value = true;
        error.value = null;
        try {
            cart.value = await getCart();
        } catch (err) {
            error.value = `Ошибка при получении корзины: ${err}`;
            console.error(error.value);
        } finally {
            isLoading.value = false;
        }
    }

    const addToCart = async (body: OrderProduct) => {
        isLoading.value = true;
        error.value = null;
        try {
            await addToCarts(body);
        } catch (err) {
            error.value = `Ошибка при добавлении товара в корзину: ${err}`;
            console.error(error.value);
        } finally {
            isLoading.value = false;
        }
    }

    const removeFromCart = async (productId: number) => {
        isLoading.value = true;
        error.value = null;
        try {
            await removeFromCarts(productId);
        } catch (err) {
            error.value = `Ошибка при удалении товара из корзины: ${err}`;
            console.error(error.value);
        } finally {
            isLoading.value = false;
        }
    }

    return {
        cart,
        isLoading,
        error,
        fetchCart,
        addToCart,
        removeFromCart
    }
});
