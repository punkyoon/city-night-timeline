<template>
    <div>
        <div v-if="timelines !== undefined && timelines !== null && timelines.length == 0">
            <p>Cannot Find!</p>
        </div>
        <div v-else>
            <div class="panel" v-for="value in timelines" :key=value._id>
                <div class="panel-body">
                    <p>{{ value.message }}</p>
                    <small>{{ value.time }}</small>
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
    export default {
        name: 'timeline-data',
        props: ['timelines'],
    }
</script>

<style>
    .panel {
        display: block;
        width: 600px;
        margin-left: auto;
        margin-right: auto;
        margin-bottom: 5px;
        word-wrap: break-word;
    }
</style>