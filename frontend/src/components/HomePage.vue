<template>
  <div>
    <h1>Home Page</h1>
    <p>Home page content</p>
    <div class="products-list-container">
      <div v-for="product in productList" :key="product.id" class="item-container">
        <p>{{ product.name }}</p>
        <p>{{ product.price }}</p>
        <p>{{ product.stock }}</p>
        <p>{{ product.category }}</p>
        <router-link class="link-style" :to="{name:'details', params:{id:product.id}}">
          <button>Ver producto</button>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      productList: [],
    };
  },
  methods: {
    fetchProducts() {
      axios.get(`http://localhost:5000/api/products`)
      .then((response) => {
        this.productList = response.data.products;
      })
      .catch((error) => {
        console.error("Error al obtener los productos:", error);
      });
    },
  },
  created() {
    this.fetchProducts();
  },
};
</script>

<style>
.products-list-container {
  display: flex;
  flex-flow: row wrap;

}

.item-container{
  width: 200px;
  border: 1px solid black;
  margin: 5px;
  padding: 5px;
}
</style>