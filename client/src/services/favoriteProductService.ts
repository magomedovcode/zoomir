import type { FavoriteProduct } from "@/types";
import axios from "axios";
import { API_URL } from "./baseURL.ts";

export const getFavoriteProducts = async (): Promise<FavoriteProduct[]> => {
    try {
        const response = await axios.get<FavoriteProduct[]>(
            `${API_URL}/shop/favorites/`,
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

export const addToFavorites = async (productId: number): Promise<void> => {
    try {
        await axios.post(
            `${API_URL}/shop/favorites/add/`,
            {
                product: productId
            },
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

export const removeFromFavorites = async (productId: number): Promise<void> => {
    try {
        await axios.delete(
            `${API_URL}/shop/favorites/remove/${productId}/`,
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

export const clearFavorites = async (): Promise<void> => {
    try {
        await axios.delete(
            `${API_URL}/shop/favorites/clear/`,
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
