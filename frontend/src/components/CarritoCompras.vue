<template>
  <div class="carrito-container">
    <div v-for="item in cart" :key="item.product.id" class="carrito-list-item">
      <div class="carrito-image-container">
        <img src="#" alt="#" class="carrito-image">
      </div>
      <div class="carrito-text-container">
        <p class="carrito-text">{{ item.product.name }}</p>
        <p>Cantidad: {{ item.quantity }}</p>
      </div>
      <div>
        <button class="delete-button" @click="removeFromCart(item.product.id)">ELIMINAR</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      cart: [],
    };
  },
  methods: {
    removeFromCart(productId) {
      axios.delete(`http://localhost:5000/api/cart/remove/${productId}`)
        .then((response) => {
          if (response.status === 200) {
            this.updateCart();
          }
        })
        .catch((error) => {
          console.error(error);
        });
    },
    updateCart() {
      axios.get('http://localhost:5000/api/cart')
        .then((response) => {
          this.cart = response.data.cart;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  created() {
    this.updateCart();
  },
};
</script>

<style>
.carrito-container {
  display: flex;
  flex-flow: column nowrap;
  justify-content: center;
  align-items: center;
  height: 100%;

}

.carrito-list-item {
  display: flex;
  flex-flow: row nowrap;
  justify-content: space-between;
  align-items: center;
  border: 1px solid #ccc; 
  border-radius: 8px;
  box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1); 
  margin: 10px; 
  padding: 20px; 
  width: 500px;
}

.delete-button {
    background-color: red;
    color: #fff;
    border: none;
    border-radius: 4px;
    font-size: 14px;
    font-weight: 600;
    padding: 10px 20px; 
    margin-top: 10px; 
    font-family: 'Poppins';
}

</style>
