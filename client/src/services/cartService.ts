import type { OrderProduct, Cart } from "@/types";
import axios from "axios";
import { API_URL } from "./baseURL.ts";

export const getCart = async (): Promise<Cart> => {
    try {
        const response = await axios.get<Cart>(
            `${API_URL}/shop/cart/`,
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

export const addToCarts = async (body: OrderProduct): Promise<void> => {
    try {
        await axios.post(
            `${API_URL}/shop/cart/add/`,
            { ...body },
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

export const removeFromCarts = async (productId: number): Promise<void> => {
    try {
        await axios.delete(
            `${API_URL}/shop/cart/remove/${productId}/`,
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

export const updateCartItemQuantity = async (productId: number, quantity: number): Promise<void> => {
    try {
        await axios.patch(
            `${API_URL}/shop/cart/update/${productId}/`,
            { quantity },
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
