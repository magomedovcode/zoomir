import { defineStore } from "pinia";
import { ref } from "vue";
import {
    type CreateOrderBody,
    type Order,
    Status
} from "../types";
import {
    createOrders,
    getOrders,
    updateOrderStatus
} from "../services/orderService.ts";

export const useOrderStore = defineStore('order', () => {
    const orders = ref<Order[]>([]);

    const isLoading = ref<boolean>(false);
    const error = ref<string | null>(null);

    const currentPage = ref(1);
    const pageSize = ref(40);
    const totalCount = ref(0);

    const fetchOrders = async () => {
        isLoading.value = true;
        error.value = null;
        try {
            const response = await getOrders({ page: currentPage.value });
            orders.value = response.results;
            totalCount.value = response.count;
        } catch (err) {
            error.value = `Ошибка при загрузке заказов: ${err}`;
            console.error(error.value);
        } finally {
            isLoading.value = false;
        }
    }

    const createOrder = async (body: CreateOrderBody) => {
        isLoading.value = true;
        error.value = null;
        try {
            await createOrders(body);
        } catch (err) {
            error.value = `Ошибка при создании заказа: ${err}`;
            console.error(error.value);
        } finally {
            isLoading.value = false;
        }
    }

    const updateStatus = async (orderId: number, status: Status) => {
        isLoading.value = true;
        error.value = null;
        try {
            await updateOrderStatus(orderId, status);
        } catch (err) {
            error.value = `Ошибка при обновлении статуса заказа: ${err}`;
            console.error(error.value);
        } finally {
            isLoading.value = false;
        }
    }

    return {
        orders,
        isLoading,
        error,
        currentPage,
        pageSize,
        totalCount,
        fetchOrders,
        createOrder,
        updateStatus
    }
});