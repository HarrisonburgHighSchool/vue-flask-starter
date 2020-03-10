<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png" />
    <b-button v-on:click="get()">Click Me to Send API Request</b-button>
    {{message}}
  </div>
</template>

<script>
// @ is an alias to /src
import axios from "axios"

const URL = "http://127.0.0.1:5000"

export default {
  name: "Home",
  data() {
    return {
      message: "Hello"
    }
  },
  methods: {
    get: function () {
      axios.get(URL + "/api/v1.0/hello")
      .then(response => {
        this.message = response.data.name;
        console.log(response)
      })
    }
  }
};
</script>
