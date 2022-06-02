<template>
    <section id="delete-element">
    <!-- Modal -->
    <div class="modal fade" id="modal-edit-article" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true" ref="deleteModalRef">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="exampleModalLabel">Eliminar Artículo</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    Esta seguro de que desea eliminar este/a {{ data.elementToDelete }} ? 
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                    <button type="button" class="btn btn-danger" @click="confirmDelete()">Eliminar Articulo</button>
                </div>
            </div>
        </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { Modal } from "bootstrap";
import { onMounted, reactive, ref } from "vue";

let deleteModalRef = ref(null);
let thisModalObj: any = null;

//Reactive
const data = reactive({
    elementToDelete: ref("")
});

//Props
const props = defineProps({
    confirm: {
        type: Function,
        required: true
    }
});

// Show for parent
function _show(element: string) {
    data.elementToDelete = element;
    thisModalObj.show();
}

function _hide(element: string) {
    data.elementToDelete = element;
    thisModalObj.hide();
}

// Mounted 
onMounted(() => {
    thisModalObj = new Modal(deleteModalRef.value);
})

// Implicit
defineExpose({ show: _show, hide: _hide });

//Component Functions
const confirmDelete = () => {
    props.confirm();
}
</script>

<style>

</style>