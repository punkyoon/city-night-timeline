<template>
    <div>
        <div v-if="service">
            <story-form id="story-form" :getTimeline="getTimeline"></story-form>
            <timeline-data id="timelien-data" :timelines="timelines"></timeline-data>
        </div>
        <div v-else>
            <div id="not-available">
                <iframe width="560" height="315" src="https://www.youtube.com/embed/8Ee4QjCEHHc?autohide=1&autoplay=1" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen />
                <p>Service hours: 9PM - 6AM (Seoul)</p>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
    import axios from 'axios';
    import StoryForm from './StoryForm.vue';
    import TimelineData from './TimelineData.vue';

    export default {
        name: 'timeline',
        components: {
            'story-form': StoryForm,
            'timeline-data': TimelineData
        },
        data(this: any) {
            return {
                timelines: null,
                service: false,
            }
        },
        created(this: any) {
            this.getTimeline();
        },
        methods: {
            getTimeline: function(this:any): void {
                axios.get('/').then(
                    result => {
                        if(!result.data.timelines)
                            this.service = false;
                        else {
                            this.timelines = result.data.timelines;
                            this.service = true;
                        }
                    }
                );
            },
        }
    }
</script>

<style>
    #not-available {
        display: block;
        width: 600px;
        text-align: center;
        margin-left: auto;
        margin-right: auto;
    }
</style>