<template>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <!-- logo가 있으면 좋을 것 같다 -->
        <router-link to="/" activeClass="active" class="navbar-brand">LOGO</router-link>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav">
                <router-link to="/" activeClass="active" tag="li"><a class="nav-link">Timeline</a></router-link>
                <router-link to="/search" activeClass="active" tag="li"><a class="nav-link">Search</a></router-link>
                <router-link to="/info" activeClass="active" tag="li"><a class="nav-link">Info</a></router-link>
            </ul>
        </div>
    </nav>
</template>

<script lang="ts">
    export default {
        name: 'app-header'
    };
</script>