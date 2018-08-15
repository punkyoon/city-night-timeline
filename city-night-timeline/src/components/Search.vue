<template>
    <div>
        <date-picker v-model="date" :timelines="timelines"></date-picker>
        <result-data :timelines="timelines"></result-data>
    </div>
</template>

<script lang="ts">
    import axios from 'axios';
    import DatePicker from './Datepicker.vue';
    import TimelineData from './TimelineData.vue';

    export default {
        name: 'search',
        components: {
            'date-picker': DatePicker,
            'result-data': TimelineData
        },
        data() {
            return {
                date: null,
                timelines: null,
            }
        }
    };
</script>