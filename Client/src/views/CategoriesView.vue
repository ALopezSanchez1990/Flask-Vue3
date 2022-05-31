<template>
  <section id="category-view">
      <ViewTitle :title="titlePage" />
  </section>
</template>

<script setup lang="ts">
import ViewTitle from '@/components/common/ViewTitle.vue';
const titlePage: string = "Categorías";
</script>

<style>

</style>