<template>
  <section id="articles-view">
    <ViewTitle :title="tituloPagina" />
    <Table :columns="columns" :rows="articles" />
    <div class="row">
      <div class="col d-flex justify-content-end">
        <button type="button" class="btn btn-success" data-bs-toggle="modal" data-bs-target="#modal-new-article">Crear
          Artículo
        </button>
      </div>
    </div>
    <ModalNewArticle />
    <ModalEditArticle ref="editModal" :row="state.rowSelected" :confirmEdit="editArticle"/>
  </section>
</template>

<script setup lang="ts">
import axios from "axios";
import { reactive, ref, onMounted } from "vue";

import ModalEditArticle from "@/components/articles/ModalEditArticle.vue";
import ModalNewArticle from "@/components/articles/ModalNewArticle.vue";
import Table from "@/components/common/Table.vue";
import ViewTitle from "@/components/common/ViewTitle.vue";

import type Articulo from "@/helpers/types/articulos/Articulo";
import type BotonAccion from "@/helpers/types/table/BotonAccion";
import type Column from "@/helpers/types/table/Column";

// Variables
const state = reactive({
  rowSelected: ref<Articulo>()
});

// Articles requests
const editArticle = () => {
  console.log("Test");
}

// Modal References
let editModal= ref(null);

// Action Functions
const editButtonAction = (row: Articulo) => {
  state.rowSelected = row;
  editModal?.value.show();
}

const deleteButtonAction = (row: any) => {
  console.log(row);
}

const actionButtons: BotonAccion[] = [
  {
    class: "btn btn-warning",
    text: "Editar",
    icon: null,
    action: editButtonAction
  },
  {
    class: "btn btn-danger",
    text: "Eliminar",
    icon: null,
    action: deleteButtonAction
  }
]

// Data
const articles = ref<Articulo[]>();
onMounted(() => {
  axios.get("http://localhost:5000/articles/").then(
    (res) => {
      articles.value = res.data.articles;
    }
  )
})
const columns: Column[] = [
  { title: "Titulo", key: "titulo", type: "text" },
  { title: "Cuerpo", key: "cuerpo", type: "text" },
  { title: "Categoria", key: "categoria", type: "text" },
  { title: "Fecha Publicación", key: "fechaDePublicacion", type: "text"},
  { title: "Acciones", key: "acciones", type: "actions", actions: actionButtons }
];

const tituloPagina: string = "Listado Artículos";
</script>
