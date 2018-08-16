<template>
    <div>
        <form method="POST" @submit.prevent="postStory(message)" id="timeline-form">
            <div class="form-group">
                <label class="form-label">Timeline</label>
                <textarea class="form-input" placeholder="Your message" rows="4" v-model="message"></textarea>
            </div>
            
            <button class="btn btn-primary">Submit</button>
        </form>
    </div>
</template>

<script lang="ts">
    import axios from 'axios';

    export default {
        name: 'story-form',
        props: ['getTimeline'],
        data(this: any) {
            return {
                message: ''
            }
        },
        methods: {
            postStory: async function(this: any) {
                // Upload messages
                await axios.post('/', {'message': this.message});
                // Reset textarea
                this.message = '';
                // Update timeline feed
                this.getTimeline();

                // Count uploaded message today
                this.$store.state.todayCount++;
            },
        }
    }
</script>

<style>
    #timeline-form {
        display: block;
        width: 450px;
        margin-left: auto;
        margin-right: auto;
        margin-bottom: 30px;
    }
</style>