import axios from "axios";
import { API_URL } from "./baseURL.ts";
import {
    type CreateOrderBody,
    type OrderResponse,
    Status
} from "../types";

export const getOrders = async (
    params: {
        page?: number
    }
): Promise<OrderResponse> => {
    try {
        const response = await axios.get<OrderResponse>(
            `${API_URL}/shop/orders/`,
            {
                params: {
                    page: params.page
                },
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

export const createOrders = async (body: CreateOrderBody): Promise<void> => {
    try {
        await axios.post(
            `${API_URL}/shop/orders/create/`,
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

export const updateOrderStatus = async (orderId: number, status: Status): Promise<void> => {
    try {
        await axios.patch(
            `${API_URL}/shop/orders/${orderId}/status/`,
            { status },
            {
                headers: {
                    Authorization: `Bearer ${localStorage.getItem('token')}`,
                },
            }
        )
    } catch (err) {
        throw err;
    }
}
