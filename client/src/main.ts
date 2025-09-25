import { createApp } from 'vue';
import { createPinia } from 'pinia';
import App from './App.vue';
import router from './router';
import { create } from 'naive-ui'
import './assets/tailwind.css';

const app = createApp(App);

app.use(createPinia());
app.use(create())
app.use(router);

app.mount('#app');

