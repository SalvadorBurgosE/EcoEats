<template>
  <div>
    <!-- Contenido del carrito -->
    <ul>
      <li v-for="item in cart" :key="item.product.id">
        {{ item.product.name }} (Cantidad: {{ item.quantity }})
        <button @click="removeFromCart(item.product.id)">Eliminar</button>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      cart: [], // Almacena los productos del carrito
    };
  },
  methods: {
    removeFromCart(productId) {
      // Realizar una solicitud DELETE al endpoint para eliminar el producto del carrito
      axios
        .delete(`http://localhost:5000/api/cart/remove/${productId}`)
        .then((response) => {
          if (response.status === 200) {
            // Producto eliminado con éxito, actualiza la vista del carrito
            this.updateCart();
          }
        })
        .catch((error) => {
          console.error(error);
        });
    },
    updateCart() {
      // Realizar una solicitud GET para obtener la última vista actualizada del carrito
      axios
        .get('http://localhost:5000/api/cart')
        .then((response) => {
          this.cart = response.data.cart;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  created() {
    // Cargar la vista inicial del carrito cuando se carga el componente
    this.updateCart();
  },
};
</script>

<style>
</style>
