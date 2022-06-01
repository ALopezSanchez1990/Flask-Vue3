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
import { reactive, ref } from "vue";

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

const articles: Articulo[] = [
  { id: 1, titulo: "Articulo 1", cuerpo: "Cuerpo 1", categoria: 1, fechaDePublicacion: new Date(), etiqueta: "etiqueta 1" },
  { id: 2, titulo: "Articulo 2", cuerpo: "Cuerpo 2", categoria: 2, fechaDePublicacion: new Date(), etiqueta: "etiqueta 2" },
  { id: 3, titulo: "Articulo 3", cuerpo: "Cuerpo 3", categoria: 3, fechaDePublicacion: new Date(), etiqueta: "etiqueta 3" },
]

const columns: Column[] = [
  { title: "Titulo", key: "titulo", type: "text" },
  { title: "Cuerpo", key: "cuerpo", type: "text" },
  { title: "categoria", key: "categoria", type: "text" },
  { title: "Acciones", key: "acciones", type: "actions", actions: actionButtons }
];

const tituloPagina: string = "Listado Artículos";
</script>
