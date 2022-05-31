<script setup lang="ts">
import { RouterView } from 'vue-router'
import MenuContainer from "@/components/menu/MenuContainer.vue";
</script>

<template>
  <div>
    <header>
      <MenuContainer />
    </header>
    <main>
      <div class="container container-xl">
        <RouterView />
      </div>
    </main>
  </div>
</template>

<style>
@import '@/assets/css/base.css';
</style>
