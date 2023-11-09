<template>
  <div class="products-list-container">
    <div v-for="product in productList" :key="product.id" class="product-card">
      <div>
        <div class="product-card-image-container">
          <img :src="product.image" :alt="product.name" class="product-card-image">
        </div>
        <p class="product-card-title">{{ product.name }}</p>
        <p class="product-card-category">Categoria: {{ product.category }}</p>
        <p class="product-card-price">Precio: ${{ product.price }}</p>
      </div>
      <div class="product-card-button-container">
        <router-link class="link-style" :to="{name:'details', params:{id:product.id}}">
          <button class="product-card-button">Ver producto</button>
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
  position: relative;
  display: flex;
  flex-flow: row wrap;
  justify-content: flex-start;
  align-items: center;
  max-width: 100%;
  padding: 20px;
}

.product-card {
  display: flex;
  flex-flow: column nowrap;
  justify-content: space-between;
  height: 260px;
  width: 225px;
  border: 1px solid #ccc; 
  border-radius: 8px;
  box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1); 
  margin: 10px; 
  padding: 20px; 
}

.product-card-title {
  color: black;
  font-family: 'Poppins';
  font-size: 16px;
  font-weight: 600;
  margin-bottom: 0;
  padding-bottom: 0;
}

.product-card-category {
  margin-top: 0;
  padding-top: 0;
  color: black;
  font-family: 'Poppins';
  font-size: 14px;
  font-weight: 400;
}

.product-card-price {
  color: black;
  font-family: 'Poppins';
  font-size: 16px;
  font-weight: 700;
}

.product-card-button-container {
  display: flex;
  flex-flow: row nowrap;
  justify-content: center;
  align-items: center;
}

.product-card-button {
 
  background-color: #1AC84B;
  border: none;
  border-radius: 4px;
  color: #fff;
  cursor: pointer;
  font-family: 'Poppins';
  font-size: 14px;
  font-weight: 600;
  padding: 10px 20px;
  margin-top: 10px;
  text-align: center;
}

.product-card-image-container {
  display: flex;
  justify-content: center;
  align-items: center;
}

.product-card-image {
  height: 100px;
  width: 100px;
}
</style>