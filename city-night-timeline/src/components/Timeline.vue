<template>
    <div>
        <h1>Timeline</h1>

        <form>
            <div class="form-group">
                <label for="story">Your story</label>
                <textarea class="form-control" id="story" rows="3"></textarea>
            </div>
            <button type="submit" class="btn btn-secondary mb-2">Write</button>
        </form>

        <!-- temporary example -->
        <div class="card">
            <div class="card-body">
                This is some text within a card body.
            </div>
        </div>
    </div>
</template>

<script lang="ts">
    export default {
        name: 'Timeline',
        data() {
            return {
                msg: 'timeline'
            }
        }
    }
</script>

<style>
    .card {
        margin-top: 2%;
    }
</style>