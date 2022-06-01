<template>
    <section id="common-table">
        <table class="table table-striped">
            <thead class="table-head">
                <tr>
                    <th v-for="col in props.columns" :key="col" class="text-center">{{ col.title }}</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(row, index) in props.rows" :key="index">
                    <td v-for="(col, indexCol) in props.columns" :key="index + indexCol">
                        <div v-if="col.type == 'text'" class="text-center">{{ row[col.key] }}</div>
                        <div v-if="col.type == 'actions'" class="d-flex justify-content-around">
                            <button v-for="action in col.actions" class="rounded" :class="action.class" :key="index + action.text + indexCol" @click="action.action(row)">{{action.text}}</button>
                        </div>
                    </td>
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