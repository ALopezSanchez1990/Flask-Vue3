import type BotonAccion from "./BotonAccion";

export default interface Column {
    key: string,
    title: string,
    type: string,
    actions?: BotonAccion[]
}