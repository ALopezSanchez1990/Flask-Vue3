<template>
  <section id="category-view">
    <ViewTitle :title="titlePage" />
    <Table :columns="columns" :rows="categories" />
  </section>
</template>

<script setup lang="ts">
import { onMounted, ref } from "vue";
import type Categoria from "@/helpers/types/categorias/Categoria.ts";

import Table from '@/components/common/Table.vue';
import ViewTitle from '@/components/common/ViewTitle.vue';

// typing inject
import axios from "axios";
import type Column from "@/helpers/types/table/Column";

const titlePage: string = "Categorías";
const columns: Column[] = [
  {
    key: "id",
    title: "Id",
    type: "text"
  },
  {
    key: "title",
    title: "Nombre",
    type: "text"
  }
]

const categories = ref<Categoria[]>([])

onMounted(() => {
  axios.get("http://localhost:5000/category/").then(
    (res) => {
      categories.value = res.data.categories
    }
  )
})
</script>

<style>
</style>