<template>
    <!-- Modal -->
    <div class="modal fade" id="modal-new-article" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="exampleModalLabel">Crear Artículo</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <div class="modal-body">
                        <div class="row mb-3">
                            <div class="col">
                                <label for="formGroupExampleInput" class="form-label">Título</label>
                                <input type="text" class="form-control" placeholder="First name"
                                    aria-label="First name" v-model="titulo"/>
                            </div>
                        </div>
                        <div class="row mb-3">
                            <div class="col">
                                <label for="formGroupExampleInput" class="form-label">Cuerpo</label>
                                <div class="form-floating">
                                    <textarea class="form-control" placeholder="Cuerpo del artículo"
                                        id="floatingTextarea2" style="height: 100px" v-model="cuerpo"/>
                                    <label for="floatingTextarea2">Cuerpo del artículo</label>
                                </div>
                            </div>
                        </div>
                        <div class="row mb-3">
                            <div class="col">
                                <label for="formGroupExampleInput" class="form-label">Categoría</label>
                                <select class="form-select" aria-label="Default select example" v-model="categoria">
                                    <option v-for="category in categories" :value="category.id"
                                        :key="'cat_' + category.id">{{ category.title }}</option>
                                </select>
                            </div>
                        </div>
                        <div class="row mb-3">
                            <div class="col">
                                <label for="formGroupExampleInput" class="form-label">Etiqueta</label>
                                <input type="text" class="form-control" placeholder="First name"
                                    aria-label="First name" v-model="etiqueta" />
                            </div>
                        </div>
                    </div>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                    <button type="button" class="btn btn-primary" @click="crearArticulo()">Crear Articulo</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import axios from "axios";
import { onMounted, ref } from "vue";

import type Articulo from "@/helpers/types/articulos/Articulo";
import type Categoria from "@/helpers/types/categorias/Categoria";

// Props
const props = defineProps({
    row: {
        type: Object as () => Articulo,
        required: true
    },
    confirmEdit: {
        type: Function,
        required: true
    }
});

// Data
const categories = ref<Categoria[]>([])
let categoria = ref(1);
let titulo = ref(null);
let cuerpo = ref("");
let etiqueta = ref(null);

//Mounted
onMounted(() => {
    axios.get("http://localhost:5000/category").then(
        (res) => {
            categories.value = res.data.categories
        }
    )

})

//Functions
const crearArticulo = () => {
    const request = {
        titulo: titulo.value,
        cuerpo: cuerpo.value,
        categoria: categoria.value,
        etiqueta: etiqueta.value
    }
    axios.post("http://localhost:5000/articles/", request);
}
</script>

<style>
</style>