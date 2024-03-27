<template>
  <div>
    <h1>Optimal mapping</h1>

    <table>
      <tr>
        <th>Truck name</th>
        <th>Cargo</th>
        <th>Distance between truck and cargo</th>
      </tr>
    </table>
  </div>
</template>

<script>
export default {
  name: "OptimalMappingView",
  data() {
    return {
      items: [],
    };
  },
  mounted() {
    axios
      .get("http://localhost:8000/api/mapping/")
      .then((response) => {
        this.items = response.data;
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

th,
td {
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