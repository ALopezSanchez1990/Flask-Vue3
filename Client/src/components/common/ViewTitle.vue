<template>
    <div class="row mt-3">
        <div class="col">
            <h3 class="text-center">{{ props.title }}</h3>
        </div>
    </div>
</template>

<script setup lang="ts">
const props = defineProps({
    title: { type: String, required: true }
});
</script>

<style scoped>

</style>