<template>
  <div class="carrito-container">
    <div v-for="item in cart" :key="item.product.id" class="carrito-list-item">
      <div class="carrito-image-container">
        <img :src="item.product.image" alt="Imagen del producto" class="carrito-image">
      </div>
      <div class="carrito-text-container">
        <p class="carrito-text">{{ item.product.name }}</p>
        <p class="carrito-text">Cantidad: {{ item.quantity }}</p>
      </div>
      <div>
        <button class="delete-button" @click="removeFromCart(item.product.id)"><svg style="color: white" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-trash-fill" viewBox="0 0 16 16"> <path d="M2.5 1a1 1 0 0 0-1 1v1a1 1 0 0 0 1 1H3v9a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2V4h.5a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1H10a1 1 0 0 0-1-1H7a1 1 0 0 0-1 1H2.5zm3 4a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 .5-.5zM8 5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7A.5.5 0 0 1 8 5zm3 .5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 1 0z" fill="white"></path> </svg> ELIMINAR</button>
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

.carrito-text {
  color: black;
  font-family: 'Poppins';
  font-size: 16px;
  font-weight: 700;
}

</style>
