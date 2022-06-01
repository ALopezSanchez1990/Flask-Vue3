import { createApp, inject, type InjectionKey } from 'vue';
import { createPinia } from 'pinia';

import "jquery";
import "bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";

import http from "@/providers/axios/http";
import { AxiosKey } from '@/providers/axios/symbols';

import App from './App.vue'
import router from './router'


const app = createApp(App)
app.provide(AxiosKey, http);

app.use(createPinia())
app.use(router)

app.mount('#app')

export function injectStrict<T>(key: InjectionKey<T>, fallback?: T) {
    const resolved = inject(key, fallback)
    if (!resolved) {
        throw new Error(`Could not resolve ${key.description}`)
    }
    return resolved
}
