<template>
  <nav>
    <div class="nav-logo-container">
      <svg xmlns="http://www.w3.org/2000/svg" width="24" height="21" viewBox="0 0 24 21" fill="none">
        <path fill-rule="evenodd" clip-rule="evenodd" d="M0 3.86203C0 -0.417471 5.35289 -1.36017 7.80629 2.14625C10.2648 5.65994 11.7134 9.93466 11.7301 14.5475C11.7301 9.97523 13.1371 5.73215 15.5409 2.2291C17.8898 -1.19396 23.0647 -0.289425 23.0647 3.86204V9.35365C23.0647 15.7228 17.9015 20.886 11.5324 20.886C5.16321 20.886 0 15.7228 0 9.35364V3.86203Z" fill="#1AC84B"/>
      </svg>
      <router-link class="nav-logo-text" to="/home">
        <p>EcoEats</p>
      </router-link>
    </div>
    <div>
      <ul class="nav-item-list">
        <li>
          <router-link to="/home" class="nav-item-text">Inicio</router-link>
        </li>
        <li>
          <p>Ayuda</p>
        </li>
        <li>
          <p>Sobre Nosotros</p>
        </li>
        <li>
          <p>Contáctanos</p>
        </li>
        <li>
          <router-link to="/carro">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class=" nav-item-carrito feather feather-shopping-cart">
            <circle cx="9" cy="21" r="1"></circle>
            <circle cx="20" cy="21" r="1"></circle>
            <path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"></path></svg>
          </router-link>
        </li>
      </ul>
    </div>
  </nav>
  
</template>

<script>

export default {
}
</script>

<style>
nav {
  height: 60px;
  display: flex;
  flex-flow: row nowrap;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
  border-bottom: 1px solid #ccc;
  box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
  max-width: 100%;
}


.nav-logo-container {
  display: flex;
  flex-flow: row nowrap;
  align-items: center;
  margin-left: 20px;
}

.nav-logo-text {
  color: black;
  font-family: 'Poppins';
  font-size: 30px;
  font-weight: 600;
  margin-left: 10px;
  text-decoration: none;
}

.nav-logo-container svg {
  height: 30px;
  width: 30px;
}

.nav-item-list {
  display: flex;
  flex-flow: row nowrap;
  align-items: center;
  justify-content: space-between;
}

.nav-item-list li {
  list-style: none;
  padding: 0px 10px;
  color: rgb(41, 40, 40);
  font-family: 'Poppins';
  font-weight: 600;
}

.nav-item-text {
  color: rgb(41, 40, 40);
  font-family: 'Poppins';
  font-weight: 600;
  text-decoration: none;

}

.nav-item-list li:hover {
  color: rgb(0, 0, 0);
  text-decoration: underline;
}

.nav-item-carrito {
  color: rgb(41, 40, 40);
}

</style>