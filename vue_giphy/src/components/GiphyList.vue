<template>
    <div id="giphy_wrapper">
        <p>{{name}}</p>
        <img :src="url">
    </div>
</template>

<script>
export default {
  name: "GiphyList",
  props: {
    name: String,
    url: String
  }
};
</script>

<style>
</style>




