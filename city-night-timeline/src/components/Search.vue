<template>
    <div>
        <h1>Search</h1>

        <form>
            <div class="input-group">
                <input type="date" class="form-control" id="search" placeholder="date">
                <div class="input-group-append" id="button">
                    <button class="btn btn-outline-secondary" type="button">Search</button>
                </div>
            </div>

            <!-- temporary example -->
            <div class="card">
                <div class="card-body">
                    This is some text within a card body.
                </div>
            </div>
        </form>
    </div>
</template>

<script lang="ts">
    export default {
        name: 'Search',
        data() {
            return {
                msg: 'search..'
            }
        }
    };
</script>

<style>
    .card {
        margin-top: 2%;
    }
</style>