<template>
  <div id="app">
    <table>
      <thead>
        <tr>
          <th @click="sort('name')">Name</th>
          <th @click="sort('quantity')">Quantity</th>
          <th @click="sort('distance')">Distance</th>
          <th @click="sort('date')">Date</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="sample in sortedSamples" :key="sample">
          <td>{{ sample.name }}</td>
          <td>{{ sample.quantity }}</td>
          <td>{{ sample.distance }}</td>
          <td>{{ sample.date }}</td>
        </tr>
      </tbody>
    </table>
    <p>
      <button @click="prevPage">Previous</button>
      <button @click="nextPage">Next</button>
    </p>

    debug: sort={{ currentSort }}, dir={{ currentSortDir }}, page={{
      currentPage
    }}
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      samples: [],
      currentSort: "name",
      currentSortDir: "asc",
      pageSize: 3,
      currentPage: 1,
    };
  },
  created: function () {
    fetch("https://protected-journey-46414.herokuapp.com/samples/")
      .then((res) => res.json())
      .then((res) => {
        this.samples = res;
      });
  },
  methods: {
    sort: function (s) {
      //if s == current sort, reverse
      if (s === this.currentSort) {
        this.currentSortDir = this.currentSortDir === "asc" ? "desc" : "asc";
      }
      this.currentSort = s;
    },
    nextPage: function () {
      if (this.currentPage * this.pageSize < this.samples.length)
        this.currentPage++;
    },
    prevPage: function () {
      if (this.currentPage > 1) this.currentPage--;
    },
  },
  computed: {
    sortedSamples: function () {
      return this.samples
        .sort((a, b) => {
          let modifier = 1;
          if (this.currentSortDir === "desc") modifier = -1;
          if (a[this.currentSort] < b[this.currentSort]) return -1 * modifier;
          if (a[this.currentSort] > b[this.currentSort]) return 1 * modifier;
          return 0;
        })
        .filter((row, index) => {
          let start = (this.currentPage - 1) * this.pageSize;
          let end = this.currentPage * this.pageSize;
          if (index >= start && index < end) return true;
        });
    },
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
