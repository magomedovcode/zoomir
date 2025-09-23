import {defineStore} from "pinia";
import { ref } from "vue";
import type {
    CreateReviewBody,
    Review
} from "../types";
import {
    createReviews,
    deleteReviews,
    getProductReviews
} from "../services/reviewService.ts";

export const useReviewStore = defineStore('review', () => {
    const reviews = ref<Review[]>([]);

    const isLoading = ref<boolean>(false);
    const error = ref<string | null>(null);

    const fetchReviews = async (productId: number) => {
        isLoading.value = true;
        error.value = null;
        try {
            reviews.value = await getProductReviews(productId);
        } catch (err) {
            error.value = `Ошибка при загрузке отзывов: ${err}`
            console.error(error.value);
        } finally {
            isLoading.value = false;
        }
    }

    const createReview = async (body: CreateReviewBody) => {
        isLoading.value = true;
        error.value = null;
        try {
            await createReviews(body);
        } catch (err) {
            error.value = `Ошибка при создании отзыва: ${err}`;
            console.error(error.value);
        } finally {
            isLoading.value = false;
        }
    }

    const deleteReview = async (reviewId: number, productId: number) => {
        isLoading.value = true;
        error.value = null;
        try {
            await deleteReviews(reviewId, productId);
        } catch (err) {
            error.value = `Ошибка при удалении отзыва: ${err}`;
            console.error(error.value);
        } finally {
            isLoading.value = false;
        }
    }

    return {
        reviews,
        isLoading,
        error,
        fetchReviews,
        createReview,
        deleteReview
    }
});
