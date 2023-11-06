<template>
  <div>
    <h1>Filtered List</h1>
    <ul>
      <li v-for="product in filteredList" :key="product.id">
        {{ product.name }} - Precio: ${{ product.price }} - Stock: {{ product.stock }} - Categoría: {{ product.category }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
    components: {
    },
    data() {
    return {
      filteredList: []
    };
  },
  methods: {
    fetchProducts() {
      axios.get(`http://localhost:5000/api/products/`)
        .then(response => {
          this.filteredList = response.data.products;
        })
        .catch(error => {
          console.error('Error al obtener los productos:', error);
        });
    }
  },
  created() {
      this.fetchProducts();
  }
};
</script>

<style>

</style>