<template>
    <section id="editar-modal">
        <!-- Modal -->
        <div class="modal fade" id="modal-edit-article" tabindex="-1" aria-labelledby="exampleModalLabel"
            aria-hidden="true" ref="modalRef">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="exampleModalLabel">Editar Artículo</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <div class="row mb-3">
                            <div class="col">
                                <label for="formGroupExampleInput" class="form-label">Título</label>
                                <input type="text" class="form-control" placeholder="First name" aria-label="First name"
                                    v-model="dataR.titulo" />
                            </div>
                        </div>
                        <div class="row mb-3">
                            <div class="col">
                                <label for="formGroupExampleInput" class="form-label">Cuerpo</label>
                                <div class="form-floating">
                                    <textarea class="form-control" placeholder="Cuerpo del artículo"
                                        id="floatingTextarea2" style="height: 100px"  v-model="dataR.titulo"/>
                                    <label for="floatingTextarea2">Cuerpo del artículo</label>
                                </div>
                            </div>
                        </div>
                        <div class="row mb-3">
                            <div class="col">
                                <label for="formGroupExampleInput" class="form-label">Categoría</label>
                                <select class="form-select" aria-label="Default select example"  v-model="dataR.categoria">
                                    <option v-for="category in categories" :value="category.id"
                                        :key="'cat_' + category.id">{{ category.title }}</option>
                                </select>
                            </div>
                        </div>
                        <div class="row mb-3">
                            <div class="col">
                                <label for="formGroupExampleInput" class="form-label">Etiqueta</label>
                                <input type="text" class="form-control" placeholder="First name"
                                    aria-label="First name" v-model="dataR.etiqueta"/>
                            </div>
                        </div>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                        <button type="button" class="btn btn-primary" @click="editArticle()">Editar Articulo</button>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>

<script setup lang="ts">
import axios from "axios";
import { Modal } from "bootstrap";
import { onMounted, ref, onUpdated, reactive } from "vue";

import type Articulo from "@/helpers/types/articulos/Articulo";
import type Categoria from "@/helpers/types/categorias/Categoria";

let modalRef = ref(null);
let thisModalObj: any = null;

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

// Show for parent
function _show() {
    thisModalObj.show();
}

// Implicit
defineExpose({ show: _show });

// Confirm Modal Function
const editArticle = () => {
    props.confirmEdit();
}

// Data
const categories = ref<Categoria[]>([])
let formData = ref<Articulo>();
let titulo = "";
const dataR = reactive({
    titulo: ref(""),
    cuerpo: ref(""),
    categoria: ref(0),
    etiqueta: ref(""),
});
// Mounted 
onMounted(() => {
    thisModalObj = new Modal(modalRef.value);
    axios.get("http://localhost:5000/category/").then(
        (res) => {
            categories.value = res.data.categories
        }
    )
})
onUpdated(() => {
    if (props?.row?.id) {
        const urlGetCategory = `${"http://localhost:5000/articles"}/${props.row.id}`;
        axios.get(urlGetCategory).then(
            (res) => {
                dataR.titulo = res.data.titulo;
                dataR.cuerpo = res.data.cuerpo;
                dataR.categoria = res.data.categoria;
                dataR.etiqueta = res.data.etiqueta;
            }
        )
    }
});
</script>

<style>
</style>