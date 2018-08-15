<template>
    <div>
        <form method="GET" @submit.prevent="searchTimeline" id="date-form">
            <div class="input-group">
                <input class="form-input" type="date" name="date" v-model="date">
                <button class="btn btn-primary input-group-btn">Search</button>
            </div>
        </form>
    </div>
</template>

<script lang="ts">
    import axios from 'axios';

    export default {
        name: 'date-picker',
        data(this: any) {
            return {
                date: null
            }
        },
        methods: {
            searchTimeline: function(this: any) {
                axios.get('/search', {params: {'date': this.date}}).then(
                    result =>this.$parent.timelines = result.data.timelines
                );
            }
        }
    }
</script>

<style>
    #date-form {
        width: 300px;
        display: block;
        margin-left: auto;
        margin-right: auto;
        margin-bottom: 30px;
    }
</style>