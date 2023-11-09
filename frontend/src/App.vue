<template>
  <div id="app">
    <NavBar v-if="showComponent"/>
    <router-view/>
    <FooterBar v-if="showComponent"/>
  </div>
  
</template>

<script>
import NavBar from './components/NavBar.vue';
import FooterBar from './components/FooterBar.vue';
export default {
  name: 'App',
  components: {
    NavBar,
    FooterBar
  },
  computed: {
    showComponent() {
      return this.$route.path !== '/';
    },
  },
}
</script>

<style>
#app {
  display: flex;
  flex-flow: column nowrap;
  justify-content: center;
  height: 100%;
  width: 100%;
}
</style>
