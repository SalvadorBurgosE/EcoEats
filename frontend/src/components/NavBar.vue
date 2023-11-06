<template>
  <nav>
    <div>
      <svg xmlns="http://www.w3.org/2000/svg" width="24" height="21" viewBox="0 0 24 21" fill="none">
      <path fill-rule="evenodd" clip-rule="evenodd" d="M0 3.86203C0 -0.417471 5.35289 -1.36017 7.80629 2.14625C10.2648 5.65994 11.7134 9.93466 11.7301 14.5475C11.7301 9.97523 13.1371 5.73215 15.5409 2.2291C17.8898 -1.19396 23.0647 -0.289425 23.0647 3.86204V9.35365C23.0647 15.7228 17.9015 20.886 11.5324 20.886C5.16321 20.886 0 15.7228 0 9.35364V3.86203Z" fill="#1AC84B"/>
      </svg>
      <p>EcoEats</p>
    </div>
    <div>
      <ul>
        <li>
          <router-link to="/home">Inicio</router-link>
        </li>
        <li>
          <!-- <router-link to="/ayuda">Ayuda</router-link> -->
        </li>
        <li>
          <!-- <router-link to="/sobre-nostros">Sobre Nosotros</router-link> -->
        </li>
        <li>
          <router-link to="/carro">
            <svg xmlns="http://www.w3.org/2000/svg" width="30" height="31" viewBox="0 0 30 31" fill="none">
              <path d="M19.2859 14.4285V7.88092C19.2859 6.49169 18.778 5.15936 17.8738 4.17702C16.9696 3.19469 15.7432 2.64282 14.4645 2.64282C13.1858 2.64282 11.9594 3.19469 11.0552 4.17702C10.151 5.15936 9.64307 6.49169 9.64307 7.88092V14.4285" stroke="#202020" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/> 
              <rect x="5.28564" y="10.0714" width="18.3571" height="18.3571" rx="3.6" stroke="#202020" stroke-width="2"/>
            </svg>
          </router-link>
        </li>
      </ul>
    </div>
    <hr>
  </nav>
  
</template>

<script>

export default {
  components: {
  },
}
</script>

<style>
</style>