<template>
    <div class="header">
        <ul class="tab tab-block">
            <router-link to="/" activeClass="active" tag="li" class="tab-item"><a>Timeline</a></router-link>
            <router-link to="/search" activeClass="active" tag="li" class="tab-item"><a>Search</a></router-link>
            <router-link to="/info" activeClass="active" tag="li" class="tab-item"><a>Info</a></router-link>
        </ul>
    </div>
</template>

<script lang="ts">
    export default {
        name: 'app-header'
    };
</script>

<style>
    .header {
        display: block;
        width: 400px;
        margin-left: auto;
        margin-right: auto;
        margin-bottom: 5%;
    }
</style>