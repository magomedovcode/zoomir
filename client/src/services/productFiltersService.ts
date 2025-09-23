import axios from "axios";
import { API_URL } from "./baseURL.ts";
import type {
    Brand,
    Country,
    ProductCategory,
    ProductChapter
} from "../types";

export const getBrands = async (): Promise<Brand[]> => {
    try {
        const response = await axios.get<Brand[]>(
            `${API_URL}/shop/brands-list/`
        );
        return response.data;
    } catch (err) {
        throw err;
    }
};

export const getCountries = async (): Promise<Country[]> => {
    try {
        const response = await axios.get<Country[]>(
            `${API_URL}/shop/countries-list/`
        );
        return response.data;
    } catch (err) {
        throw err;
    }
};

export const getProductChapters = async (): Promise<ProductChapter[]> => {
    try {
        const response = await axios.get<ProductChapter[]>(
            `${API_URL}/shop/product-chapters-list/`
        );
        return response.data;
    } catch (err) {
        throw err;
    }
};

export const getProductCategories = async (chapterId?: number): Promise<ProductCategory[]> => {
    try {
        const response = await axios.get<ProductCategory[]>(
            `${API_URL}/shop/product-categories-list/`,
            {
                params: {
                    product_chapter: chapterId
                }
            }
        );
        return response.data;
    } catch (err) {
        throw err;
    }
};
