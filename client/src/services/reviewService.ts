import axios from "axios";
import { API_URL } from "./baseURL";
import type {
    CreateReviewBody,
    Review
} from "@/types";

export const getProductReviews = async (productId: number): Promise<Review[]> => {
    try {
        const response = await axios.get<Review[]>(
            `${API_URL}/shop/products/${productId}/reviews/`,
            {
                headers: {
                    Authorization: `Bearer ${localStorage.getItem('token')}`,
                },
            }
        );
        return response.data;
    } catch (err) {
        throw err;
    }
};

export const createReviews = async (body: CreateReviewBody): Promise<void> => {
    try {
        await axios.post(
            `${API_URL}/shop/products/${body.productId}/reviews/create/`,
            {
                title: body.title,
                rating: body.rating,
                comment: body.comment
            },
            {
                headers: {
                    Authorization: `Bearer ${localStorage.getItem('token')}`,
                    "Content-Type": "multipart/form-data",
                },
            }
        );
    } catch (err) {
        throw err;
    }
};

export const deleteReviews = async (reviewId: number, productId: number): Promise<void> => {
    try {
        await axios.delete(
            `${API_URL}/shop/products/${productId}/reviews/${reviewId}/`,
            {
                headers: {
                    Authorization: `Bearer ${localStorage.getItem('token')}`,
                },
            }
        );
    } catch (err) {
        throw err;
    }
};
