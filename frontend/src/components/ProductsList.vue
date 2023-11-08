<template>
  <div>
    <body>
    <header>
        <h1>Home</h1>
    </header>
    <nav>
        <a href="#">Productos</a>
    </nav>
    <div class="buscarBarra">
        <form >
            <input  v-model="busqueda" type="text" placeholder="Ingrese la categoria ">
            <button>Buscar
                <svg xmlns="http://www.w3.org/2000/svg" width="21" height="21" viewBox="0 0 21 21" fill="none">
                    <path d="M1 20L5.486 15.506M3 9.5C3 11.7543 3.89553 13.9163 5.48959 15.5104C7.08365 17.1045 9.24566 18 11.5 18C13.7543 18 15.9163 17.1045 17.5104 15.5104C19.1045 13.9163 20 11.7543 20 9.5C20 7.24566 19.1045 5.08365 17.5104 3.48959C15.9163 1.89553 13.7543 1 11.5 1C9.24566 1 7.08365 1.89553 5.48959 3.48959C3.89553 5.08365 3 7.24566 3 9.5V9.5Z" stroke="#808080" stroke-width="2" stroke-linecap="round"/>
                </svg>
            </button>
        </form>
    </div>
    <section>
        <table>
            <tr>
              <td>
                    <h2>Pepsi</h2>
                    <p>$300</p>
              </td>
              <td><img src="https://www.freepnglogos.com/uploads/pepsi-png/pepsi-can-please-stop-hotlinking-pics-page-off-topic-10.png" alt="" width="200px" height="200px"></td>
            </tr>
        </table>
        <table>
            <tr>
                <td><img src="https://static.wixstatic.com/media/129c2d_956ff19d6fad43859f24462f491c2d02~mv2.png/v1/fit/w_500,h_500,q_90/file.png" alt="" width="225px" height="300px"></td>
                <td align="left">
                    <h2>Coca Cola 1L</h2>
                    <p>$350</p>
                </td>
            </tr>
        </table>
        <table>
            <tr>
                <td><img src="https://www.ferkulum-koeln.de/wp-content/uploads/2020/08/sprite-1L.png" alt="" width="225px" height="300px"></td>
                <td align="left">
                    <h2>Sprite 1l</h2>
                    <p>$250</p>
                </td>
            </tr>
        </table>
        <table>
            <tr>
                <td><img src="https://images.migrosone.com/sanalmarket/product/08022000/8022000_yan-d36055-1650x1650.png" alt="" width="225px" height="300px"></td>
                <td align="left">
                    <h2>Fanta</h2>
                    <p>$280</p>
                </td>
            </tr>
        </table>
        <table>
            <tr>
                <td><img src="https://www.totalwine.com/dynamic/x1000,sq/media/sys_master/twmmedia/h89/h4a/15687108886558.png" alt="" width="225px" height="300px"></td>
                <td align="left">
                    <h2>Mountain Drew</h2>
                    <p>$320</p>
                </td>           
            </tr>  
        </table>
        <table>
            <tr>
                <td><img src="https://atomoconviene.com/atomo-ecommerce/64833-large_default/galletas-dulces-oreo-reg-tripack-23-354-grs-.jpg" alt="" width="225px" height="300px"></td>
                <td align="left">
                    <h2>Oreo</h2>
                    <p>$300</p>
                </td>
            </tr>
        </table>
        <table>
            <tr>
                <td><img src="https://cdn11.bigcommerce.com/s-3stx4pub31/images/stencil/1280x1280/products/6934/20366/chocolinas-100-g-galletas-dulces-chocolinas-bagley-removebg-preview__52178.1662039755.png?c=2?imbypass=on" alt="" width="225px" height="300px"></td>
                <td align="left">
                    <h2>Chocolinas</h2>
                    <p>$250</p>
                </td>
            </tr>
        </table>
        <table>
            <tr>
                <td><img src="https://i0.wp.com/www.argensend.com/wp-content/uploads/2022/02/D_NQ_NP_924267-MLA43802458632_102020-W-removebg-preview.png?fit=477%2C523&ssl=1" alt="" width="225px" height="300px"></td>
                <td align="left">
                    <h2>Tita</h2>
                    <p>$200</p>
                </td>
            </tr>
        </table>
        <table>
            <tr>
                <td><img src="https://d2r9epyceweg5n.cloudfront.net/stores/001/108/127/products/cerealitasbyb1-78e5364a4c380005d915868224619832-1024-1024.png" alt="" width="225px" height="300px"></td>
                <td align="left">
                    <h2>Cerealitas</h2>
                    <p>$280</p>
                </td>
            </tr>
        </table>
    </section>
    
  </body>

    
    
    <ul>
      <li v-for="product in productList" :key="product.id">
        {{ product.name }} - Precio: ${{ product.price }} - Stock:{{ product.stock }} - Categoría: {{ product.category }}
      </li>
    </ul>
    <div></div>
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
      axios
        .get(`http://localhost:5000/api/products`)
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

<style scoped>
.buscarBarra{
  font-family: 'Fira Sans', sans-serif;
  padding: 10px;
}
template {
    background-color: #FFF0C9;
    color: #FFF0C9;
    font-family: 'Fira Sans', sans-serif;

}

header {
    background-color: rgba(91, 174, 49, 0.485);
    height: 60px;
    color:  #9ff4b7(111, 66, 21);
    padding: 1%;
    display: flex;
    align-items: center;
    font-size: 30px;
    font-family: 'Fira Sans', sans-serif;

}

header img {
    margin-right: 10px;
}

nav {
    background-color:  #3dd23d5c;
    display: flex;
    padding: 5px;
    
}

nav a {
    padding: 10px;
    margin: 10px;
    color: #464544;
    text-decoration: none;
    font-family: 'Fira Sans', sans-serif;
}

nav a:hover {
    background-color: rgb(221, 239, 139);
    border-radius: 4px;
}

section {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: space-around;
    padding: 50px;
}

table {
    background-color:  #dbf9e3;
    margin: 50px;
    width: 25%;
    border-radius: 40px;
    font-family: 'Fira Sans', sans-serif;

}

td {
    padding: 10px;
}

footer {
    background-color: peru;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    font-family: 'Fira Sans', sans-serif;
}

footer a {
    padding: 10px;
    margin: 10px;
    color: #FFF0C9;
    text-decoration: none;
}

footer a:hover {
    background-color: rgb(174, 111, 49);
    border-radius: 5px;
}

.pedido {
    font-size: 30px;
}

img {
    border-radius: 5px;
}

.confirmacion {
    color: rgb(188, 239, 158);
}

.formulario div {
    background-color: peru;
    margin: 10px;
    padding: 10px;
    border-radius: 10px;
}
</style>
