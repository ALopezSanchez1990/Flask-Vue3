import type Categoria from "@/helpers/types/categorias/Categoria";

export default interface Articulo {
    id?: number,
    titulo: string, 
    cuerpo: string,
    categoria: Categoria,
    fechaDePublicacion: Date,
    etiqueta: string
}