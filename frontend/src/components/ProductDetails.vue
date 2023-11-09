<template>
  <div class="product-details-container">
    <div class="product-details-card">
      <div class="image-container">
        <img src="#" alt="#">
      </div>
      <div class="text-container">
        <p class="product-text-bold">{{ product.name }}</p>
        <p class="product-text">Categoria: {{ product.category }}</p>
        <p class="product-text-bold">Precio: ${{ product.price }}</p>
      </div>
      <div class="product-button-container">
        <input class="product-input" v-model="quantity" type="number" min="1"  placeholder="Cantidad">
        <button class="product-details-button" @click="addToCart">Agregar al Carrito</button>
        <div v-if="productMessage" class="product-message">{{ productMessage }}</div>
      </div>
    </div>
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
.product-details-container {
  height: 80vh;
  display: flex;
  justify-content: center;
  align-items: center;
}

.product-details-card {
  display: flex;
  flex-flow: row nowrap;
  justify-content: space-between;
  align-items: center;
  border: 1px solid #ccc; 
  border-radius: 8px;
  box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1); 
  margin: 10px; 
  padding: 20px; 
}

.product-text-bold {
  color: black;
  font-family: 'Poppins';
  font-size: 24px;
  font-weight: 600;
  margin-bottom: 0;
  padding-bottom: 0;
}

.product-text {
  margin-top: 0;
  padding-top: 0;
  color: black;
  font-family: 'Poppins';
  font-size: 20px;
  font-weight: 400;
}

.product-button-container {
  height: 100%;
}

.product-input {

  width: 40px;
  margin: 0px 10px 0px 50px;
  padding: 10px; 
  border: 1px solid #ccc;
  border-radius: 4px; 
  font-size: 14px;
  font-family: 'Poppins';
}

.product-details-button {
  background-color: #000;
  color: #fff;
  border: none;
  border-radius: 4px;
  font-size: 14px;
  font-weight: 600;
  padding: 10px 20px; 
  margin-top: 10px; 
  font-family: 'Poppins';
}

button:hover {
  background-color: #333; 
}

.product-message {
  color: #6e6e6e;
  border-radius: 4px;
  font-family: 'Poppins';
  font-size: 14px;
  font-weight: 600;
  margin-left:50px;
  text-align: center;
}

</style>