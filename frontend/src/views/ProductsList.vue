<template>
  <v-container fluid class="pa-4">
    <v-row>
      <v-col>
        <v-card elevation="8" class="pa-6">
          <v-card-title class="text-h4 font-weight-bold primary white--text mb-4">
            📦 Товары маркетплейса
          </v-card-title>
          
          <!-- Поиск + обновление -->
          <v-row class="mb-4">
            <v-col cols="6">
              <v-text-field
                v-model="search"
                label="🔍 Поиск по SKU/Артикул/Название"
                prepend-inner-icon="mdi-magnify"
                single-line
                clearable
                density="compact"
                variant="outlined"
              />
            </v-col>
            <v-col cols="6" class="text-right">
              <v-btn 
                color="primary" 
                @click="loadProducts"
                :loading="loading"
                prepend-icon="mdi-refresh"
                size="large"
              >
                Обновить
              </v-btn>
            </v-col>
          </v-row>

          <!-- 🔥 Крутая таблица Vuetify -->
          <v-data-table
            :headers="headers"
            :items="products"
            :search="search"
            class="elevation-1"
            :loading="loading"
            item-key="id"
            density="comfortable"
          >
            <!-- Кастомный слот для цены закупки -->
            <template #item.purchase_price="{ item }">
              <span class="font-weight-medium">
                ₽{{ formatPrice(item.purchase_price) }}
              </span>
            </template>

            <!-- Кастомный слот для цены розницы -->
            <template #item.retail_price="{ item }">
              <span class="font-weight-medium">
                ₽{{ formatPrice(item.retail_price) }}
              </span>
            </template>

            <!-- ✅ Маржа с цветами -->
            <template #item.margin="{ item }">
              <v-chip 
                :color="getMarginColor(item)"
                size="small"
                class="font-weight-bold ma-0"
              >
                {{ formatMargin(item) }}%
              </v-chip>
            </template>

            <!-- ✅ Статус -->
            <template #item.status="{ item }">
              <v-chip 
                :color="getStatusColor(item)"
                size="small"
                class="font-weight-bold ma-0"
              >
                {{ getStatusText(item) }}
              </v-chip>
            </template>

            <!-- ✅ Пустое состояние (ИСПРАВЛЕНО!) -->
            <template #no-data>
              <v-card flat class="pa-8 text-center">
                <v-icon size="64" color="grey-lighten-1">mdi-database-off</v-icon>
                <div class="text-h6 mt-2" style="color: #757575;">Нет товаров</div>
                <v-btn 
                  color="primary" 
                  @click="loadProducts"
                  class="mt-4"
                >
                  🔄 Загрузить с API
                </v-btn>
                <div class="mt-2 text-caption" style="color: #9e9e9e;">
                  Проверьте: <a href="http://localhost:8000/api/v1/products/" target="_blank">API</a>
                </div>
              </v-card>
            </template>
          </v-data-table>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import api from '@/services/api'
import type { DataTableHeader } from 'vuetify/lib/components/index.mjs'

interface Product {
  id: number
  sku: string
  article: string
  name: string
  purchase_price: number
  retail_price: number
  quantity_sold: number
}

const products = ref<Product[]>([])
const loading = ref(false)
const search = ref('')

// ✅ Заголовки таблицы
const headers = [
  { title: 'SKU', key: 'sku', sortable: true },
  { title: 'Артикул', key: 'article', sortable: true },
  { title: 'Товар', key: 'name', sortable: false },
  { title: 'Закуп', key: 'purchase_price', sortable: true },
  { title: 'Розница', key: 'retail_price', sortable: true },
  { title: 'Маржа', key: 'margin', sortable: true },
  { title: 'Продано', key: 'quantity_sold', sortable: true },
  { title: 'Статус', key: 'status', sortable: false }
] as DataTableHeader<Product>[]

// ✅ Форматирование
const formatPrice = (price: number) => price.toLocaleString()

const formatMargin = (item: Product) => {
  const margin = ((item.retail_price - item.purchase_price) / item.purchase_price * 100)
  return margin.toFixed(1)
}

const getMarginColor = (item: Product) => {
  const margin = ((item.retail_price - item.purchase_price) / item.purchase_price * 100)
  if (margin > 50) return 'success'
  if (margin > 20) return 'warning'
  return 'error'
}

const getStatusText = (item: Product) => {
  const margin = ((item.retail_price - item.purchase_price) / item.purchase_price * 100)
  if (margin > 50) return '🔥 Супер'
  if (margin > 20) return '✅ Хорошая'
  return '⚠️ Слабая'
}

const getStatusColor = (item: Product) => {
  const margin = ((item.retail_price - item.purchase_price) / item.purchase_price * 100)
  if (margin > 50) return 'success'
  if (margin > 20) return 'warning'
  return 'error'
}

const loadProducts = async () => {
  loading.value = true
  try {
    const { data } = await api.get('/v1/products/')
    products.value = data
    console.log('✅ Загружено:', data.length, 'товаров')
  } catch (error) {
    console.error('❌ API Error:', error)
  } finally {
    loading.value = false
  }
}

onMounted(loadProducts)
</script>
