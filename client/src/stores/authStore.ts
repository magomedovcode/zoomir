import { defineStore } from 'pinia';
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import type {User, Username} from "@/types";
import {
    getUsername,
    loginUser,
    registerUser
} from '@/services/authService';

export const useAuthStore = defineStore('auth', () => {
    const token = ref<string | null>(localStorage.getItem('token'));
    const isAuthenticated = ref<boolean>(!!token.value);
    const user = ref<Username | null>(null);
    const router = useRouter();

    const isLoading = ref<boolean>(false);
    const error = ref<string | null>(null);

    const login = async (userData: User) => {
        isLoading.value = true;
        error.value = null;
        try {
            const response = await loginUser(userData);
            token.value = response.access;
            isAuthenticated.value = true;
            localStorage.setItem('token', response.access);
            await router.push('/');
        } catch (err) {
            error.value = `Ошибка авторизации: ${err}`
            console.error(error.value);
        } finally {
            isLoading.value = false;
        }
    };

    const register = async (userData: User) => {
        isLoading.value = true;
        error.value = null;
        try {
            const response = await registerUser(userData);
            token.value = response.access;
            isAuthenticated.value = true;
            localStorage.setItem('token', response.access);
            user.value = { username: response.username };
            await router.push('/');
        } catch (err) {
            error.value = `Ошибка регистрации: ${err}`;
            console.error(error.value);
        } finally {
            isLoading.value = false;
        }
    };

    const fetchUsername = async () => {
        isLoading.value = true;
        error.value = null;
        try {
            user.value = await getUsername();
        } catch (err) {
            error.value = `Ошибка получения логина: ${err}`;
            console.error(error.value);
        } finally {
            isLoading.value = false;
        }
    };

    const logout = async () => {
        token.value = null;
        isAuthenticated.value = false;
        localStorage.removeItem('token');
        isLoading.value = true;
        user.value = null;
        error.value = null;
        try {
            await router.push('/login');
        } catch (err) {
            error.value = `Ошибка навигации: ${err}`;
            console.error(error.value);
        } finally {
            isLoading.value = false;
        }
    };

    return {
        isLoading,
        error,
        token,
        isAuthenticated,
        user,
        login,
        register,
        logout,
        fetchUsername
    };
});
