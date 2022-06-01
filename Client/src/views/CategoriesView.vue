<template>
  <section id="category-view">
    <ViewTitle :title="titlePage" />
    <Table :columns="columns" :rows="categories" />
  </section>
</template>

<script setup lang="ts">
import type Categoria from "@/helpers/types/categorias/Categoria.ts";
import Table from '@/components/common/Table.vue';
import ViewTitle from '@/components/common/ViewTitle.vue';
const titlePage: string = "Categorías";
const columns: any[] = [
  {
    key: "id",
    title: "Id",
  },
  {
    key: "title",
    title: "Nombre"
  }
]
const categories: Categoria[]  = [
  {
    id: 1,
    title: "Noticias"
  },
  {
    id: 2,
    title: "Deportes"
  },
  {
    id: 3,
    title: "Politica"
  },
];

</script>

<style>
</style>