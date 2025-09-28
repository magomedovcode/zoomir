<template>
  <footer class="bg-white shadow-sm border-t">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mt-4">
      <div class="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-4 gap-8">
        <div>
          <h3 class="text-lg font-bold mb-4 text-gray-700">О нас</h3>
          <p class="text-gray-700">
            Zoomir — всё для ваших любимых питомцев.
          </p>
        </div>

        <div>
          <h3 class="text-lg font-bold mb-4 text-gray-700">Быстрые ссылки</h3>
          <ul class="space-y-2">
            <li>
              <router-link
                  to="/"
                  class="text-gray-700 hover:text-indigo-600 transition duration-300"
              >
                Главная
              </router-link>
            </li>
            <li>
              <router-link
                  to="/cart"
                  class="text-gray-700 hover:text-indigo-600 transition duration-300"
                  :class="{ 'text-indigo-600 font-medium': $route.path.includes('/cart') }"
              >
                Корзина
              </router-link>
            </li>
            <li>
              <router-link
                  to="/favorites"
                  class="text-gray-700 hover:text-indigo-600 transition duration-300"
                  :class="{ 'text-indigo-600 font-medium': $route.path.includes('/favorites') }"
              >
                Избранное
              </router-link>
            </li>
            <li>
              <router-link
                  to="/orders"
                  class="text-gray-700 hover:text-indigo-600 transition duration-300"
                  :class="{ 'text-indigo-600 font-medium': $route.path.includes('/orders') }"
              >
                Заказы
              </router-link>
            </li>
            <li>
              <router-link
                  to="/chapters"
                  class="text-gray-700 hover:text-indigo-600 transition duration-300"
                  :class="{ 'text-indigo-600 font-medium': $route.path.includes('/chapters') }"
              >
                Категории
              </router-link>
            </li>
            <li>
              <router-link
                  to="/shop"
                  class="text-gray-700 hover:text-indigo-600 transition duration-300"
                  :class="{ 'text-indigo-600 font-medium': $route.path.includes('/shop') }"
              >
                Все товары
              </router-link>
            </li>
          </ul>
        </div>

        <div>
          <h3 class="text-lg font-bold mb-4 text-gray-700">Контакты</h3>
          <ul class="space-y-2">
            <li class="text-gray-700">Email: zoomir@gmail.com</li>
            <li class="text-gray-700">Телефон: +1 (999) 999-99-99</li>
            <li class="text-gray-700">Адрес: Россия, г. Ставрополь, ул. Зоомирная 14, магазин 88</li>
          </ul>
        </div>

        <div>
          <h3 class="text-lg font-bold mb-4 text-gray-700">Социальные сети</h3>
          <ul class="space-y-2">
            <li class="text-gray-700 hover:text-indigo-600 transition duration-300">
              <a href="#">
                GitGub
              </a>
            </li>
            <li class="text-gray-700 hover:text-indigo-600 transition duration-300">
              <a href="#">
                Telegram
              </a>
            </li>
            <li class="text-gray-700 hover:text-indigo-600 transition duration-300">
              <a href="#">
                ВКонтакте
              </a>
            </li>
          </ul>
        </div>
      </div>

      <div class="border-t text-gray-700 mt-8 pt-8 text-center">
        <p class="text-gray-700 mb-8">&copy; {{ Intl.DateTimeFormat('ru-RU', { year: 'numeric' }).format(new Date()) }} Zoomir. Все права защищены.</p>
      </div>
    </div>
  </footer>
</template>

<script setup lang="ts">
</script>
