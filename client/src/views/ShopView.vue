<template>
  <div class="min-h-screen flex flex-col bg-white">
    <AppHeader />

    <div class="flex-grow container max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <div class="text-center mb-12">
        <div class="flex flex-row justify-center items-center gap-3">
          <div class="flex justify-center items-center mb-4">
            <div class="w-10 h-10 bg-gradient-to-r from-yellow-400 to-amber-400 rounded-xl flex items-center justify-center shadow-lg">
              <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/>
              </svg>
            </div>
          </div>
          <h1 class="text-4xl font-bold bg-gradient-to-r from-yellow-400 to-amber-400 bg-clip-text text-transparent mb-4">
            Товары из категории
          </h1>
        </div>
        <p class="text-stone-600 max-w-2xl mx-auto text-lg">Найдите всё необходимое для вашего питомца</p>
      </div>

      <div class="lg:hidden mb-6">
        <div class="flex items-center justify-between mb-4">
          <h2 class="text-lg font-semibold text-stone-800">Фильтры</h2>
          <button
              @click="showMobileFilters = !showMobileFilters"
              class="flex items-center gap-2 px-4 py-3 bg-white border border-stone-300 rounded-xl hover:border-yellow-400 hover:bg-yellow-50 transition-all duration-300 shadow-sm"
          >
            <span class="font-medium text-stone-700">Фильтры</span>
            <ChevronUpDownIcon class="h-5 w-5 text-stone-500" aria-hidden="true" />
          </button>
        </div>

        <div class="mb-4">
          <div class="relative">
            <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
              <svg class="h-5 w-5 text-stone-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
              </svg>
            </div>
            <input
                v-model="searchQuery"
                type="text"
                placeholder="Поиск товаров..."
                class="w-full pl-10 pr-4 py-3 bg-white border border-stone-300 rounded-xl shadow-sm focus:outline-none focus:ring-2 focus:ring-yellow-400 focus:border-yellow-400 text-base transition-all duration-200"
            >
          </div>
        </div>

        <transition
            enter-active-class="transition-all duration-300 ease-out"
            enter-from-class="opacity-0 max-h-0"
            enter-to-class="opacity-100 max-h-[800px]"
            leave-active-class="transition-all duration-300 ease-in"
            leave-from-class="opacity-100 max-h-[800px]"
            leave-to-class="opacity-0 max-h-0"
        >
          <div v-show="showMobileFilters" class="overflow-hidden">
            <div class="space-y-3">
              <div class="bg-white rounded-xl border border-stone-200 shadow-sm">
                <Disclosure v-slot="{ open }">
                  <DisclosureButton class="flex justify-between w-full px-4 py-4 text-left hover:bg-stone-50 rounded-xl transition-colors duration-200">
                    <span class="font-medium text-stone-800">{{ getBrandsLabel }}</span>
                    <ChevronUpDownIcon
                        :class="open ? 'rotate-180 transform' : ''"
                        class="h-5 w-5 text-stone-500 transition-transform duration-200"
                    />
                  </DisclosureButton>
                  <DisclosurePanel class="px-4 pb-4 pt-2 border-t border-stone-100">
                    <div class="space-y-3 max-h-60 overflow-y-auto">
                      <div
                          v-for="brand in filtersStore.brands"
                          :key="brand.id"
                          class="flex items-center group cursor-pointer"
                      >
                        <div class="relative flex items-center">
                          <input
                              :id="`mobile-brand-${brand.id}`"
                              v-model="selectedBrands"
                              :value="brand.id"
                              type="checkbox"
                              class="sr-only"
                          >
                          <div class="w-5 h-5 border-2 border-stone-300 rounded flex items-center justify-center transition-all duration-200 mr-3 group-hover:border-yellow-400"
                               :class="{
                                 'bg-yellow-400 border-yellow-400': selectedBrands.includes(brand.id),
                                 'bg-white': !selectedBrands.includes(brand.id)
                               }">
                            <svg v-if="selectedBrands.includes(brand.id)" class="w-3 h-3 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7"></path>
                            </svg>
                          </div>
                        </div>
                        <label
                            :for="`mobile-brand-${brand.id}`"
                            class="text-stone-700 cursor-pointer group-hover:text-yellow-500 transition-colors duration-200"
                        >
                          {{ brand.name }}
                        </label>
                      </div>
                    </div>
                  </DisclosurePanel>
                </Disclosure>
              </div>

              <div class="bg-white rounded-xl border border-stone-200 shadow-sm">
                <Disclosure v-slot="{ open }">
                  <DisclosureButton class="flex justify-between w-full px-4 py-4 text-left hover:bg-stone-50 rounded-xl transition-colors duration-200">
                    <span class="font-medium text-stone-800">{{ getCountriesLabel }}</span>
                    <ChevronUpDownIcon
                        :class="open ? 'rotate-180 transform' : ''"
                        class="h-5 w-5 text-stone-500 transition-transform duration-200"
                    />
                  </DisclosureButton>
                  <DisclosurePanel class="px-4 pb-4 pt-2 border-t border-stone-100">
                    <div class="space-y-3 max-h-60 overflow-y-auto">
                      <div
                          v-for="country in filtersStore.countries"
                          :key="country.id"
                          class="flex items-center group cursor-pointer"
                      >
                        <div class="relative flex items-center">
                          <input
                              :id="`mobile-country-${country.id}`"
                              v-model="selectedCountries"
                              :value="country.id"
                              type="checkbox"
                              class="sr-only"
                          >
                          <div class="w-5 h-5 border-2 border-stone-300 rounded flex items-center justify-center transition-all duration-200 mr-3 group-hover:border-yellow-400"
                               :class="{
                                 'bg-yellow-400 border-yellow-400': selectedCountries.includes(country.id),
                                 'bg-white': !selectedCountries.includes(country.id)
                               }">
                            <svg v-if="selectedCountries.includes(country.id)" class="w-3 h-3 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7"></path>
                            </svg>
                          </div>
                        </div>
                        <label
                            :for="`mobile-country-${country.id}`"
                            class="text-stone-700 cursor-pointer group-hover:text-yellow-500 transition-colors duration-200"
                        >
                          {{ country.name }}
                        </label>
                      </div>
                    </div>
                  </DisclosurePanel>
                </Disclosure>
              </div>

              <div class="bg-white rounded-xl border border-stone-200 shadow-sm">
                <Disclosure v-slot="{ open }">
                  <DisclosureButton class="flex justify-between w-full px-4 py-4 text-left hover:bg-stone-50 rounded-xl transition-colors duration-200">
                    <span class="font-medium text-stone-800">{{ getCategoriesLabel }}</span>
                    <ChevronUpDownIcon
                        :class="open ? 'rotate-180 transform' : ''"
                        class="h-5 w-5 text-stone-500 transition-transform duration-200"
                    />
                  </DisclosureButton>
                  <DisclosurePanel class="px-4 pb-4 pt-2 border-t border-stone-100">
                    <div class="space-y-3 max-h-60 overflow-y-auto">
                      <div
                          v-for="category in filtersStore.productCategories"
                          :key="category.id"
                          class="flex items-center group cursor-pointer"
                      >
                        <div class="relative flex items-center">
                          <input
                              :id="`mobile-category-${category.id}`"
                              v-model="selectedCategories"
                              :value="category.id"
                              type="checkbox"
                              class="sr-only"
                          >
                          <div class="w-5 h-5 border-2 border-stone-300 rounded flex items-center justify-center transition-all duration-200 mr-3 group-hover:border-yellow-400"
                               :class="{
                                 'bg-yellow-400 border-yellow-400': selectedCategories.includes(category.id),
                                 'bg-white': !selectedCategories.includes(category.id)
                               }">
                            <svg v-if="selectedCategories.includes(category.id)" class="w-3 h-3 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7"></path>
                            </svg>
                          </div>
                        </div>
                        <label
                            :for="`mobile-category-${category.id}`"
                            class="text-stone-700 cursor-pointer group-hover:text-yellow-500 transition-colors duration-200"
                        >
                          {{ category.name }}
                        </label>
                      </div>
                    </div>
                  </DisclosurePanel>
                </Disclosure>
              </div>

              <div class="bg-white rounded-xl border border-stone-200 shadow-sm">
                <Disclosure v-slot="{ open }">
                  <DisclosureButton class="flex justify-between w-full px-4 py-4 text-left hover:bg-stone-50 rounded-xl transition-colors duration-200">
                    <span class="font-medium text-stone-800">{{ getPriceLabel }}</span>
                    <ChevronUpDownIcon
                        :class="open ? 'rotate-180 transform' : ''"
                        class="h-5 w-5 text-stone-500 transition-transform duration-200"
                    />
                  </DisclosureButton>
                  <DisclosurePanel class="px-4 pb-4 pt-2 border-t border-stone-100">
                    <div class="space-y-4">
                      <div class="flex space-x-3">
                        <div class="flex-1">
                          <label class="block text-sm font-medium text-stone-700 mb-2">От</label>
                          <input
                              v-model.number="priceMin"
                              type="number"
                              placeholder="0"
                              class="w-full px-3 py-2 border border-stone-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-yellow-400 focus:border-yellow-400 transition-all duration-200"
                          >
                        </div>
                        <div class="flex-1">
                          <label class="block text-sm font-medium text-stone-700 mb-2">До</label>
                          <input
                              v-model.number="priceMax"
                              type="number"
                              placeholder="99999"
                              class="w-full px-3 py-2 border border-stone-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-yellow-400 focus:border-yellow-400 transition-all duration-200"
                          >
                        </div>
                      </div>
                      <div class="flex justify-between items-center">
                        <span class="text-sm text-stone-600 font-medium">
                          {{ priceMin || 0 }} - {{ priceMax || '∞' }} ₽
                        </span>
                        <button
                            v-if="priceMin || priceMax"
                            @click="clearPriceFilter"
                            class="text-yellow-500 hover:text-yellow-500 text-sm font-medium transition-colors duration-200"
                        >
                          Сбросить
                        </button>
                      </div>
                    </div>
                  </DisclosurePanel>
                </Disclosure>
              </div>

              <div class="bg-white rounded-xl border border-stone-200 shadow-sm">
                <Disclosure v-slot="{ open }">
                  <DisclosureButton class="flex justify-between w-full px-4 py-4 text-left hover:bg-stone-50 rounded-xl transition-colors duration-200">
                    <span class="font-medium text-stone-800">{{ getOrderingLabel(ordering) }}</span>
                    <ChevronUpDownIcon
                        :class="open ? 'rotate-180 transform' : ''"
                        class="h-5 w-5 text-stone-500 transition-transform duration-200"
                    />
                  </DisclosureButton>
                  <DisclosurePanel class="px-4 pb-4 pt-2 border-t border-stone-100">
                    <div class="space-y-3">
                      <div
                          v-for="option in sortOptions"
                          :key="option.value"
                          class="flex items-center group cursor-pointer"
                      >
                        <input
                            :id="`mobile-sort-${option.value}`"
                            v-model="ordering"
                            :value="option.value"
                            type="radio"
                            class="sr-only"
                        >
                        <div class="w-5 h-5 border-2 border-stone-300 rounded-full flex items-center justify-center transition-all duration-200 mr-3 group-hover:border-yellow-400"
                             :class="{
                               'border-yellow-400': ordering === option.value
                             }">
                          <div v-if="ordering === option.value" class="w-2.5 h-2.5 bg-yellow-400 rounded-full"></div>
                        </div>
                        <label
                            :for="`mobile-sort-${option.value}`"
                            class="text-stone-700 cursor-pointer group-hover:text-yellow-500 transition-colors duration-200"
                            :class="{ 'font-semibold text-yellow-500': ordering === option.value }"
                        >
                          {{ option.label }}
                        </label>
                      </div>
                    </div>
                  </DisclosurePanel>
                </Disclosure>
              </div>
            </div>
          </div>
        </transition>
      </div>

      <div class="hidden lg:block mb-8">
        <div class="mb-6 flex justify-center">
          <div class="relative w-2/3">
            <div class="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
              <svg class="h-5 w-5 text-stone-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
              </svg>
            </div>
            <input
                v-model="searchQuery"
                type="text"
                placeholder="Поиск товаров..."
                class="w-full pl-12 pr-4 py-4 bg-white border border-stone-300 rounded-2xl shadow-lg focus:outline-none focus:ring-2 focus:ring-yellow-400 focus:border-yellow-400 text-base transition-all duration-200 hover:shadow-xl"
            >
          </div>
        </div>

        <div class="bg-white rounded-2xl shadow-lg border border-stone-300 p-6">
          <div class="flex items-center space-x-2 mb-4">
            <div class="w-8 h-8 bg-yellow-100 rounded-lg flex items-center justify-center">
              <svg class="w-5 h-5 text-yellow-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 4a1 1 0 011-1h16a1 1 0 011 1v2.586a1 1 0 01-.293.707l-6.414 6.414a1 1 0 00-.293.707V17l-4 4v-6.586a1 1 0 00-.293-.707L3.293 7.293A1 1 0 013 6.586V4z"/>
              </svg>
            </div>
            <h3 class="text-lg font-semibold text-stone-800">Фильтры товаров</h3>
          </div>

          <div class="grid grid-cols-5 gap-4">
            <div class="relative">
              <Listbox v-model="selectedBrands" multiple>
                <ListboxButton class="w-full px-4 py-3 bg-white border border-stone-300 rounded-xl text-left focus:outline-none focus:ring-2 focus:ring-yellow-400 focus:border-yellow-400 transition-all duration-200 hover:border-yellow-400 flex justify-between items-center shadow-sm">
                  <span class="block truncate font-medium text-stone-700">
                    {{ getBrandsLabel }}
                  </span>
                  <ChevronUpDownIcon class="h-5 w-5 text-stone-400 transition-transform duration-200" aria-hidden="true" />
                </ListboxButton>

                <transition
                    leave-active-class="transition duration-100 ease-in"
                    leave-from-class="opacity-100"
                    leave-to-class="opacity-0"
                >
                  <ListboxOptions class="absolute top-full left-0 right-0 mt-2 max-h-60 overflow-auto rounded-xl bg-white py-2 text-base shadow-xl ring-1 ring-black ring-opacity-5 focus:outline-none z-20 border border-stone-200">
                    <ListboxOption
                        v-slot="{ active, selected }"
                        v-for="brand in filtersStore.brands"
                        :key="brand.id"
                        :value="brand.id"
                        as="template"
                    >
                      <li
                          :class="[
                          active ? 'bg-yellow-100 text-yellow-900' : 'text-stone-900',
                          'relative cursor-pointer select-none py-3 pl-3 pr-9 transition-colors duration-200',
                        ]"
                      >
                        <div class="flex items-center">
                          <div class="w-5 h-5 border-2 border-stone-300 rounded flex items-center justify-center transition-all duration-200 mr-3"
                               :class="{
                                 'bg-yellow-500 border-yellow-500': selected,
                                 'bg-white': !selected
                               }">
                            <svg v-if="selected" class="w-3 h-3 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7"></path>
                            </svg>
                          </div>
                          <span :class="[selected ? 'font-semibold' : 'font-normal', 'block truncate']">
                            {{ brand.name }}
                          </span>
                        </div>
                      </li>
                    </ListboxOption>
                  </ListboxOptions>
                </transition>
              </Listbox>
            </div>

            <div class="relative">
              <Listbox v-model="selectedCountries" multiple>
                <ListboxButton class="w-full px-4 py-3 bg-white border border-stone-300 rounded-xl text-left focus:outline-none focus:ring-2 focus:ring-yellow-400 focus:border-yellow-400 transition-all duration-200 hover:border-yellow-400 flex justify-between items-center shadow-sm">
                  <span class="block truncate font-medium text-stone-700">
                    {{ getCountriesLabel }}
                  </span>
                  <ChevronUpDownIcon class="h-5 w-5 text-stone-400 transition-transform duration-200" aria-hidden="true" />
                </ListboxButton>

                <transition
                    leave-active-class="transition duration-100 ease-in"
                    leave-from-class="opacity-100"
                    leave-to-class="opacity-0"
                >
                  <ListboxOptions class="absolute top-full left-0 right-0 mt-2 max-h-60 overflow-auto rounded-xl bg-white py-2 text-base shadow-xl ring-1 ring-black ring-opacity-5 focus:outline-none z-20 border border-stone-200">
                    <ListboxOption
                        v-slot="{ active, selected }"
                        v-for="country in filtersStore.countries"
                        :key="country.id"
                        :value="country.id"
                        as="template"
                    >
                      <li
                          :class="[
                          active ? 'bg-yellow-100 text-yellow-900' : 'text-stone-900',
                          'relative cursor-pointer select-none py-3 pl-3 pr-9 transition-colors duration-200',
                        ]"
                      >
                        <div class="flex items-center">
                          <div class="w-5 h-5 border-2 border-stone-300 rounded flex items-center justify-center transition-all duration-200 mr-3"
                               :class="{
                                 'bg-yellow-500 border-yellow-500': selected,
                                 'bg-white': !selected
                               }">
                            <svg v-if="selected" class="w-3 h-3 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7"></path>
                            </svg>
                          </div>
                          <span :class="[selected ? 'font-semibold' : 'font-normal', 'block truncate']">
                            {{ country.name }}
                          </span>
                        </div>
                      </li>
                    </ListboxOption>
                  </ListboxOptions>
                </transition>
              </Listbox>
            </div>

            <div class="relative">
              <Listbox v-model="selectedCategories" multiple>
                <ListboxButton class="w-full px-4 py-3 bg-white border border-stone-300 rounded-xl text-left focus:outline-none focus:ring-2 focus:ring-yellow-400 focus:border-yellow-400 transition-all duration-200 hover:border-yellow-400 flex justify-between items-center shadow-sm">
                  <span class="block truncate font-medium text-stone-700">
                    {{ getCategoriesLabel }}
                  </span>
                  <ChevronUpDownIcon class="h-5 w-5 text-stone-400 transition-transform duration-200" aria-hidden="true" />
                </ListboxButton>

                <transition
                    leave-active-class="transition duration-100 ease-in"
                    leave-from-class="opacity-100"
                    leave-to-class="opacity-0"
                >
                  <ListboxOptions class="absolute top-full left-0 right-0 mt-2 max-h-60 overflow-auto rounded-xl bg-white py-2 text-base shadow-xl ring-1 ring-black ring-opacity-5 focus:outline-none z-20 border border-stone-200">
                    <ListboxOption
                        v-slot="{ active, selected }"
                        v-for="category in filtersStore.productCategories"
                        :key="category.id"
                        :value="category.id"
                        as="template"
                    >
                      <li
                          :class="[
                          active ? 'bg-yellow-100 text-yellow-900' : 'text-stone-900',
                          'relative cursor-pointer select-none py-3 pl-3 pr-9 transition-colors duration-200',
                        ]"
                      >
                        <div class="flex items-center">
                          <div class="w-5 h-5 border-2 border-stone-300 rounded flex items-center justify-center transition-all duration-200 mr-3"
                               :class="{
                                 'bg-yellow-500 border-yellow-500': selected,
                                 'bg-white': !selected
                               }">
                            <svg v-if="selected" class="w-3 h-3 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7"></path>
                            </svg>
                          </div>
                          <span :class="[selected ? 'font-semibold' : 'font-normal', 'block truncate']">
                            {{ category.name }}
                          </span>
                        </div>
                      </li>
                    </ListboxOption>
                  </ListboxOptions>
                </transition>
              </Listbox>
            </div>

            <div class="relative">
              <Popover v-slot="{ open }">
                <PopoverButton
                    class="w-full px-4 py-3 bg-white border border-stone-300 rounded-xl text-left focus:outline-none focus:ring-2 focus:ring-yellow-400 focus:border-yellow-400 transition-all duration-200 hover:border-yellow-400 flex justify-between items-center shadow-sm"
                    :class="{ 'ring-2 ring-yellow-400 border-yellow-400': open }"
                >
                  <span class="block truncate font-medium text-stone-700">
                    {{ getPriceLabel }}
                  </span>
                  <ChevronUpDownIcon
                      class="h-5 w-5 text-stone-400 transition-transform duration-200"
                      :class="{ 'rotate-180': open }"
                      aria-hidden="true"
                  />
                </PopoverButton>

                <transition
                    enter-active-class="transition duration-200 ease-out"
                    enter-from-class="opacity-0 scale-95"
                    enter-to-class="opacity-100 scale-100"
                    leave-active-class="transition duration-150 ease-in"
                    leave-from-class="opacity-100 scale-100"
                    leave-to-class="opacity-0 scale-95"
                >
                  <PopoverPanel
                      class="absolute left-0 right-0 mt-2 bg-white border border-stone-200 rounded-xl shadow-xl z-50 p-4 transform"
                  >
                    <div class="space-y-4">
                      <h4 class="font-semibold text-stone-800">Диапазон цен</h4>
                      <div class="flex space-x-3">
                        <div class="flex-1">
                          <label class="block text-sm font-medium text-stone-700 mb-2">От</label>
                          <input
                              v-model.number="priceMin"
                              type="number"
                              placeholder="0"
                              class="w-full px-3 py-2 border border-stone-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-yellow-400 focus:border-yellow-400 transition-all duration-200"
                          >
                        </div>
                        <div class="flex-1">
                          <label class="block text-sm font-medium text-stone-700 mb-2">До</label>
                          <input
                              v-model.number="priceMax"
                              type="number"
                              placeholder="99999"
                              class="w-full px-3 py-2 border border-stone-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-yellow-400 focus:border-yellow-400 transition-all duration-200"
                          >
                        </div>
                      </div>
                      <div class="flex justify-between items-center">
                        <span class="text-sm text-stone-600 font-medium">
                          {{ priceMin || 0 }} - {{ priceMax || '∞' }} ₽
                        </span>
                        <button
                            v-if="priceMin || priceMax"
                            @click="clearPriceFilter"
                            class="text-yellow-500 hover:text-yellow-600 text-sm font-medium transition-colors duration-200"
                        >
                          Сбросить
                        </button>
                      </div>
                    </div>
                  </PopoverPanel>
                </transition>
              </Popover>
            </div>

            <div class="relative">
              <Listbox v-model="ordering">
                <ListboxButton class="w-full px-4 py-3 bg-white border border-stone-300 rounded-xl text-left focus:outline-none focus:ring-2 focus:ring-yellow-400 focus:border-yellow-400 transition-all duration-200 hover:border-yellow-400 flex justify-between items-center shadow-sm">
                  <span class="block truncate font-medium text-stone-700">{{ getOrderingLabel(ordering) }}</span>
                  <ChevronUpDownIcon class="h-5 w-5 text-stone-400 transition-transform duration-200" aria-hidden="true" />
                </ListboxButton>

                <transition
                    leave-active-class="transition duration-100 ease-in"
                    leave-from-class="opacity-100"
                    leave-to-class="opacity-0"
                >
                  <ListboxOptions class="absolute top-full left-0 right-0 mt-2 max-h-60 overflow-auto rounded-xl bg-white py-2 text-base shadow-xl ring-1 ring-black ring-opacity-5 focus:outline-none z-20 border border-stone-200">
                    <ListboxOption
                        v-slot="{ active, selected }"
                        v-for="option in sortOptions"
                        :key="option.value"
                        :value="option.value"
                        as="template"
                    >
                      <li
                          :class="[
                          active ? 'bg-yellow-100 text-yellow-900' : 'text-stone-900',
                          'relative cursor-pointer select-none py-3 pl-3 pr-9 transition-colors duration-200',
                        ]"
                      >
                        <span :class="[selected ? 'font-semibold text-yellow-500' : 'font-normal', 'block truncate']">
                          {{ option.label }}
                        </span>
                        <span
                            v-if="selected"
                            class="absolute inset-y-0 right-0 flex items-center pr-3 text-yellow-500"
                        >
                          <CheckIcon class="h-5 w-5" aria-hidden="true" />
                        </span>
                      </li>
                    </ListboxOption>
                  </ListboxOptions>
                </transition>
              </Listbox>
            </div>
          </div>
        </div>
      </div>

      <div>
        <div class="flex justify-between items-center mb-8">
          <div class="flex items-center space-x-3">
            <h2 class="text-2xl font-bold text-stone-800">Все товары</h2>
            <div class="px-3 py-1 bg-yellow-100 text-yellow-800 rounded-full text-sm font-medium">
              {{ productStore.totalCount }} товаров
            </div>
          </div>
        </div>

        <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 gap-4 sm:gap-6" v-if="!productStore.isLoading">
          <ProductCard
              v-for="product in productStore.products"
              :key="product.id"
              :product="product"
          />
        </div>

        <div v-else class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 gap-4 sm:gap-6">
          <div v-for="i in 10" :key="i" class="bg-gradient-to-br from-stone-200 to-stone-300 rounded-2xl aspect-[3/4] animate-pulse shadow-sm"></div>
        </div>

        <div class="flex justify-center mt-12" v-if="productStore.totalCount > productStore.pageSize">
          <div class="flex items-center space-x-2 bg-white rounded-2xl shadow-lg border border-stone-100 p-2">
            <button
                @click="loadPage(productStore.currentPage - 1)"
                :disabled="productStore.currentPage === 1"
                class="flex items-center space-x-2 px-4 py-3 rounded-xl text-stone-600 hover:text-yellow-500 hover:bg-indigo-50 transition-all duration-300 disabled:opacity-40 disabled:cursor-not-allowed disabled:hover:bg-transparent"
            >
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/>
              </svg>
              <span class="font-medium">Назад</span>
            </button>

            <div class="flex items-center space-x-1 mx-4">
              <span class="px-4 py-2 bg-gradient-to-r from-yellow-400 to-amber-500 text-white font-semibold rounded-lg">
                {{ productStore.currentPage }}
              </span>
              <span class="text-stone-500 mx-2">из</span>
              <span class="text-stone-700 font-medium">
                {{ Math.ceil(productStore.totalCount / productStore.pageSize) }}
              </span>
            </div>

            <button
                @click="loadPage(productStore.currentPage + 1)"
                :disabled="productStore.currentPage * productStore.pageSize >= productStore.totalCount"
                class="flex items-center space-x-2 px-4 py-3 rounded-xl text-stone-600 hover:text-yellow-500 hover:bg-indigo-50 transition-all duration-300 disabled:opacity-40 disabled:cursor-not-allowed disabled:hover:bg-transparent"
            >
              <span class="font-medium">Вперед</span>
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
              </svg>
            </button>
          </div>
        </div>
      </div>
    </div>

    <AppFooter />
  </div>
</template>

<script setup lang="ts">
import {computed, onMounted, ref, watch} from 'vue'
import {useRoute} from 'vue-router'
import {
  Listbox,
  ListboxButton,
  ListboxOptions,
  ListboxOption,
  Popover,
  PopoverButton,
  PopoverPanel,
  Disclosure,
  DisclosureButton,
  DisclosurePanel,
} from '@headlessui/vue'
import { CheckIcon, ChevronUpDownIcon } from '@heroicons/vue/20/solid'
import AppHeader from '@/components/AppHeader.vue'
import ProductCard from '@/components/ProductCard.vue'
import {useProductStore} from '@/stores/productStore'
import {useProductFiltersStore} from '@/stores/productFiltersStore'
import {ProductOrdering} from '@/types'
import AppFooter from "@/components/AppFooter.vue";

const route = useRoute()
const productStore = useProductStore()
const filtersStore = useProductFiltersStore()

const searchQuery = ref('')
const selectedBrands = ref<number[]>([])
const selectedCountries = ref<number[]>([])
const selectedCategories = ref<number[]>([])
const priceMin = ref<number>()
const priceMax = ref<number>()
const ordering = ref<ProductOrdering>(ProductOrdering.PRICE_DEFAULT)
const showMobileFilters = ref(false)

const sortOptions = [
  { value: ProductOrdering.PRICE_DEFAULT, label: 'По умолчанию' },
  { value: ProductOrdering.PRICE_ASC, label: 'Цена по возрастанию' },
  { value: ProductOrdering.PRICE_DESC, label: 'Цена по убыванию' },
]

const getBrandsLabel = computed(() => {
  if (selectedBrands.value.length === 0) return 'Бренды'
  if (selectedBrands.value.length === 1) {
    const brand = filtersStore.brands.find(b => b.id === selectedBrands.value[0])
    return brand ? brand.name : 'Бренды'
  }
  return `Бренды (${selectedBrands.value.length})`
})

const getCountriesLabel = computed(() => {
  if (selectedCountries.value.length === 0) return 'Страны'
  if (selectedCountries.value.length === 1) {
    const country = filtersStore.countries.find(c => c.id === selectedCountries.value[0])
    return country ? country.name : 'Страны'
  }
  return `Страны (${selectedCountries.value.length})`
})

const getCategoriesLabel = computed(() => {
  if (selectedCategories.value.length === 0) return 'Категории'
  if (selectedCategories.value.length === 1) {
    const category = filtersStore.productCategories.find(c => c.id === selectedCategories.value[0])
    return category ? category.name : 'Категории'
  }
  return `Категории (${selectedCategories.value.length})`
})

const getPriceLabel = computed(() => {
  if (!priceMin.value && !priceMax.value) return 'Цена'
  return `Цена: ${priceMin.value || 0}-${priceMax.value || '∞'} ₽`
})

const getOrderingLabel = (value: ProductOrdering) => {
  const option = sortOptions.find(opt => opt.value === value)
  return option ? option.label : 'По умолчанию'
}

const filters = computed(() => ({
  search: searchQuery.value,
  brand: selectedBrands.value,
  country: selectedCountries.value,
  price_min: priceMin.value,
  price_max: priceMax.value,
  ordering: ordering.value,
  product_category: selectedCategories.value.length > 0
      ? selectedCategories.value
      : route.params.chapterId
          ? [Number(route.params.chapterId)]
          : []
}))

const clearPriceFilter = () => {
  priceMin.value = undefined
  priceMax.value = undefined
}

watch(filters, async () => {
  await productStore.fetchProducts(filters.value)
}, { deep: true })

const loadPage = (page: number) => {
  productStore.currentPage = page
  productStore.fetchProducts(filters.value)
}

onMounted(async () => {
  await productStore.fetchProducts(filters.value)
  await filtersStore.fetchProductCategories(Number(route.params.chapterId))
})
</script>
