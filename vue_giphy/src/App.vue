<template>
  <div id="app">
    <GiphyList name="Hola" url="https://media.giphy.com/media/rnshwCdGdDyg0/giphy.gif"/>
  </div>
</template>

<script>
import GiphyList from "./components/GiphyList.vue";

export default {
  name: "app",
  components: {
    GiphyList
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
