<template>
    <nav class="navbar navbar-expand-lg sticky-top">
        <div class="container-fluid">
            <a class="navbar-brand">
                <img src="@/assets/img/logo.png" width="80" height="80"/>
            </a>
            <div class="collapse navbar-collapse d-flex justify-content-around" id="navbarNavAltMarkup">
                <ul class="navbar-nav">
                    <li>
                        <a class="nav-link" aria-current="page">
                            <RouterLink to="/">Articulos</RouterLink>
                        </a>
                    </li>
                    <li>
                        <a class="nav-link" aria-current="page">
                            <RouterLink to="/categories">Categorías</RouterLink>
                        </a>
                    </li>
                </ul>
            </div>

        </div>
    </nav>
</template>

<script setup lang="ts">
</script>

<style>
</style>