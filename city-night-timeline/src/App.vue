<template>
    <div>
        <app-header></app-header>
        <div class="container">
            <router-view/>
        </div>
    </div>
</template>

<script lang="ts">
    import Header from './components/Header.vue';
    export default {
        name: 'app',
        components: {
            'app-header': Header,
        },
        data() {
            return {
                image: './assets/background.jpg',
            };
        }
    };
</script>