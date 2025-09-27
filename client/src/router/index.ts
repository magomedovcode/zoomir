import HomeView from '@/views/HomeView.vue';
import FavoriteProductView from "@/views/FavoriteProductView.vue";
import OrdersView from "@/views/OrdersView.vue";
import CartView from "@/views/CartView.vue";
import LoginView from "@/views/LoginView.vue";
import RegisterView from "@/views/RegisterView.vue";
import ShopView from "@/views/ShopView.vue";
import ProductDetailsView from "@/views/ProductDetailsView.vue";
import {
    createRouter,
    createWebHistory
} from 'vue-router';
import ProductChaptersView from "@/views/ProductChaptersView.vue";

const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/',
            component: HomeView
        },
        {
            path: '/login',
            component: LoginView
        },
        {
            path: '/register',
            component: RegisterView
        },
        {
            path: '/shop',
            component: ShopView
        },
        {
            path: '/chapters',
            component: ProductChaptersView
        },
        {
            path: "/shop/:chapterId",
            name: "ShopView",
            component: ShopView,
            props: true,
        },
        {
            path: '/details/:id',
            component: ProductDetailsView
        },
        {
            path: '/favorites',
            component: FavoriteProductView,
            meta: {
                requiresAuth: true
            }
        },
        {
            path: '/orders',
            component: OrdersView,
            meta: {
                requiresAuth: true
            }
        },
        {
            path: '/cart',
            component: CartView,
            meta: {
                requiresAuth: true
            }
        }
    ],
});

router.beforeEach((to, _, next) => {
    const requiresAuth = to.matched.some(record => record.meta.requiresAuth);
    const isAuthenticated = !!localStorage.getItem('token');

    if (requiresAuth && !isAuthenticated) {
        next('/login');
    } else {
        next();
    }
});

export default router;
