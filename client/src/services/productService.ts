import axios from "axios";
import { API_URL } from "./baseURL.ts";
import type {
    GetProductsParams,
    ProductDetail,
    ProductVariantResponse
} from "../types";

export const getProducts = async (params: GetProductsParams): Promise<ProductVariantResponse> => {
    try {
        const response = await axios.get<ProductVariantResponse>(
            `${API_URL}/shop/products-list/`,
            { params }
        );
        return response.data;
    } catch (err) {
        throw err;
    }
};

export const getProductDetails = async (productId: number): Promise<ProductDetail> => {
    try {
        const response = await axios.get<ProductDetail>(
            `${API_URL}/shop/products/${productId}/`
        );
        return response.data;
    } catch (err) {
        throw err;
    }
};
