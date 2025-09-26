import {defineStore} from "pinia";
import {ref} from "vue";
import {getBrands, getCountries, getProductCategories, getProductChapters} from "@/services/productFiltersService.ts";
import type {Brand, Country, ProductCategory, ProductChapter} from "@/types";

export const useProductFiltersStore = defineStore('productFilters', () => {
    const brands = ref<Brand[]>([]);
    const countries = ref<Country[]>([]);
    const productChapters = ref<ProductChapter[]>([]);
    const productCategories = ref<ProductCategory[]>([]);

    const isLoading = ref<boolean>(false);
    const error = ref<string | null>(null);

    const fetchBrands = async () => {
        isLoading.value = true;
        error.value = null;
        try {
            brands.value = await getBrands();
        } catch (err) {
            error.value = `Ошибка при загрузке брендов: ${err}`;
            console.error(error.value);
        } finally {
            isLoading.value = false;
        }
    };

    const fetchCountries = async () => {
        isLoading.value = true;
        error.value = null;
        try {
            countries.value = await getCountries();
        } catch (err) {
            error.value = `Ошибка при загрузке стран: ${err}`;
            console.error(error.value);
        } finally {
            isLoading.value = false;
        }
    };

    const fetchProductChapters = async () => {
        isLoading.value = true;
        error.value = null;
        try {
            productChapters.value = await getProductChapters();
        } catch (err) {
            error.value = `Ошибка при загрузке глав товаров: ${err}`;
            console.error(error.value);
        } finally {
            isLoading.value = false;
        }
    };

    const fetchProductCategories = async (chapterId: number) => {
        isLoading.value = true;
        error.value = null;
        try {
            productCategories.value = await getProductCategories(chapterId);
        } catch (err) {
            error.value = `Ошибка при загрузке категорий товаров: ${err}`;
            console.error(error.value);
        } finally {
            isLoading.value = false;
        }
    };

    return {
        isLoading,
        error,
        fetchBrands,
        fetchCountries,
        fetchProductChapters,
        fetchProductCategories,
        brands,
        countries,
        productChapters,
        productCategories
    }
});
