<template>
    <div>
    <h1>Cargo list</h1>

    <table>
      <tr>
        <th>Cargo name</th>
        <th>Origin state</th>
        <th>Origin city</th>
        <th>Destination state</th>
        <th>Destination city</th>
      </tr>
      <tr v-for="item in items" :key="item.id">
        <td>{{ item.product }}</td>
        <td>{{ item.origin_state }}</td>
        <td>{{ item.origin_city }}</td>
        <td>{{ item.destination_state }}</td>
        <td>{{ item.destination_city }}</td>
      </tr>
    </table>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "CargosView",
  data() {
    return {
      items: [],
    };
  },
  mounted() {
    axios
      .get("http://localhost:8000/api/cargo/")
      .then((response) => {
        this.items = response.data;
        console.log(response.data);
      })
      .catch((error) => {
        console.error(error);
      });
  },
};
</script>


<style scoped>
h1 {
  font-size: 50px;
  margin-top: 40px;
  margin-left: 67px;
  margin-bottom: 30px;
}

table {
  border-collapse: collapse;
  width: 50%;
  text-align: center;
  margin-left: 25%;
}

th, td {
  border: 1px solid black;
  padding: 10px;
}

th {
  background-color: #404040;
  color: white;
}

td:hover {
  background-color: #42b983;
}
</style>