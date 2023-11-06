<template>
  <div>
    <NavBar/>
    <h1>Home</h1>
    <ProductsList/>
    <FooterBar/>
  </div>
</template>

<script>
import NavBar from './NavBar.vue';
import FooterBar from './FooterBar.vue';
import ProductsList from './ProductsList.vue';

export default {
  components: {
    NavBar,
    FooterBar,
    ProductsList
  },
}
</script>

<style>

</style>