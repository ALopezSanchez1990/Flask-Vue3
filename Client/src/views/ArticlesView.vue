<template>
  <section id="articles-view">
    <ViewTitle :title="tituloPagina" />
    <Table :columns="columns" :rows="articles" />
  </section>
</template>

<script setup lang="ts">
import ViewTitle from "@/components/common/ViewTitle.vue";
import Table from "@/components/common/Table.vue";
import { defineComponent } from "@vue/runtime-core";

const tituloPagina: String = "Listado Artículos";
const columns = [
  { title: "Uno", key: "descripcion" },
  { title: "Dos", key: "descripcion" },
  { title: "tres", key: "descripcion" },
];
const articles = [
  { id: 1, descripcion: "uno" },
  { id: 1, descripcion: "dos" },
  { id: 1, descripcion: "tres" }
]
</script>
