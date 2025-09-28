import axios from 'axios';
import {API_URL} from "./baseURL.ts";
import type {User, Username} from "@/types";

export const loginUser = async (userData: User) => {
    try {
        const response = await axios.post(
            `${API_URL}/token/`,
            { ...userData }
        );
        return response.data;
    } catch (err) {
        throw err;
    }
};

export const registerUser = async (userData: User) => {
    try {
        const response = await axios.post(
            `${API_URL}/register/`,
            { ...userData }
        );
        return response.data;
    } catch (err) {
        throw err;
    }
};

export const getUsername = async (): Promise<Username> => {
    try {
        const response = await axios.get(
            `${API_URL}/auth/`,
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
}
