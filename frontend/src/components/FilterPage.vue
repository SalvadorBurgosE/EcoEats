<template>
  <div>
    <NavBar/>
    <FilterList/>
    <FooterBar/>
  </div>
</template>

<script>
import NavBar from './NavBar.vue';
import FooterBar from './FooterBar.vue';
import FilterList from './FilterList.vue';

export default {
  components: {
    NavBar,
    FooterBar,
    FilterList
  },
}
</script>

<style>

</style>