<template>
  <div id="app">
    <ul>
      <li v-for="giphy in giphys" :key="giphy.id">
            <GiphyList :name="giphy.name" :url="giphy.url"/>
      </li>
    </ul>
  </div>
</template>

<script>
import GiphyList from "./components/GiphyList.vue";

export default {
  name: "app",
  components: {
    GiphyList
  },
  data: function() {
    return {
      giphys: []
    };
  },
  methods: {
    fetchData: function() {
      fetch("http://127.0.0.1:8000/giphy-app/list/")
        .then(response => {
          return response.json();
        })
        .then(data => {
          console.log(data);
          this.giphys = data;
        })
        .catch(error => {
          throw error;
        });
    }
  },
  mounted() {
    this.fetchData();
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

#app ul {
  list-style: none;
}
</style>
