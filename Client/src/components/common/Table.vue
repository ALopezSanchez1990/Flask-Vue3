<template>
    <section id="common-table">
        <table class="table table-striped">
            <thead class="table-head">
                <tr>
                    <th v-for="col in props.columns" :key="col">{{ col.title }}</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(row, index) in props.rows" :key="index">
                    <th v-for="(col, indexCol) in props.columns" :key="index + indexCol">{{ row[col.key] }}</th>
                </tr>
            </tbody>
        </table>
    </section>
</template>

<script setup lang="ts">
const props = defineProps({
    columns: { type: [Object], required: true },
    rows: { type: [Object], required: true }
});
</script>