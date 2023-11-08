<template>
  <div>
    <p>{{ product.name }}</p>
    <p>Precio: ${{ product.price }}</p>
    <p>Stock Disponible: {{ product.stock }}</p>
    <input v-model="quantity" type="number" min="1"  placeholder="Cantidad">
    <button @click="addToCart">Agregar al Carrito</button>
    <div v-if="productMessage" class="">{{ productMessage }}</div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
    data(){
        return {
            product:{},
            quantity:1,
            productMessage:''
        }
    },
    props:{
        id: {
            type: [Number, String],
            required:true
        }
    },
    methods: {
        getProductData(){
            fetch(`http://localhost:5000/api/products/${this.id}`,{
            method:"GET",
            headers:{
                'Content-Type': 'application/json'
          }
        })
        .then(resp => resp.json())
        .then(data => {
          let producto = data.product;
          console.log(producto);
          this.product = producto;
        })
        .catch(error =>{
          console.log(error);
        })
      },
      addToCart() {
      const productToAdd = {
        id: this.product.id,
        name: this.product.name,
        price: this.product.price,
        category: this.product.category,
      };
      const data = {
        product: productToAdd,
        quantity: this.quantity,
      };

      axios.post('http://localhost:5000/api/cart/add', data, {
          headers: {
            'Content-Type': 'application/json',
          },
        })
        .then((response) => {
          if (response.status === 200) {
            this.productMessage = 'El producto se agregó al carrito';
            setTimeout(() => {
              this.productMessage = '';
            }, 1200);
          }
        })
        .catch((error) => {
          console.error(error);
          this.productMessage = 'Error al agregar el producto al carrito';
          setTimeout(() => {
              this.productMessage = '';
            }, 1200);
        });
    },
  },
    created(){
        this.getProductData();
    }

}
</script>

<style>

</style>