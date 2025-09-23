import { defineStore } from "pinia";
import { ref } from "vue";
import type {
    GetProductsParams,
    ProductDetail,
    ProductVariant
} from "../types";
import {
    getProductDetails,
    getProducts
} from "../services/productService.ts";

export const useProductStore = defineStore('product', () => {
    const products = ref<ProductVariant[]>([]);
    const productDetail = ref<ProductDetail>();

    const isLoading = ref<boolean>(false);
    const error = ref<string | null>(null);

    const currentPage = ref(1);
    const pageSize = ref(40);
    const totalCount = ref(0);

    const fetchProducts = async (params: GetProductsParams) => {
        isLoading.value = true;
        error.value = null;
        try {
            const response = await getProducts({
                ...params,
                page: currentPage.value,
            });
            products.value = response.results;
            totalCount.value = response.count;
        } catch (err) {
            error.value = `Ошибка при загрузке продуктов: ${err}`;
            console.error(error.value);
        } finally {
            isLoading.value = false;
        }
    };

    const fetchProductDetails = async (productId: number) => {
        isLoading.value = true;
        error.value = null;
        try {
            productDetail.value = await getProductDetails(productId);
        } catch (err) {
            error.value = `Ошибка при загрузке деталей продукта: ${err}`;
            console.error(error.value);
        } finally {
            isLoading.value = false;
        }
    };

    return {
        isLoading,
        error,
        currentPage,
        pageSize,
        totalCount,
        products,
        fetchProducts,
        fetchProductDetails
    };
});
