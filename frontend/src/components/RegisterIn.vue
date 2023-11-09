<template>
    <div class=login-card>
        <div class ="logo-container">
            <svg xmlns="http://www.w3.org/2000/svg" width="64" height="61" viewBox="0 0 24 21" fill="none">
                <path fill-rule="evenodd" clip-rule="evenodd" d="M0 3.86203C0 -0.417471 5.35289 -1.36017 7.80629 2.14625C10.2648 5.65994 11.7134 9.93466 11.7301 14.5475C11.7301 9.97523 13.1371 5.73215 15.5409 2.2291C17.8898 -1.19396 23.0647 -0.289425 23.0647 3.86204V9.35365C23.0647 15.7228 17.9015 20.886 11.5324 20.886C5.16321 20.886 0 15.7228 0 9.35364V3.86203Z" fill="#1AC84B"/>
            </svg>
            <p class = "texto_icono">EcoEats</p>
        </div>
        <div class="login-form-container">
            <form @submit.prevent="login">
                <label for="nombre">Usuario</label><input v-model="username" type="text" placeholder="Ingrese su usuario" tabindex="1">
                <label for="nombre">Contraseña</label><input v-model="password" type="password" placeholder="Ingrese su contraseña" tabindex="2">
                <button type="submit">INGRESAR</button>
            </form>
            <div v-if="loginMessage" class="login-message">{{ loginMessage }}</div>
        </div>
    </div>

</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            username: '',
            password: '',
            loginMessage: '',
        };
    },
    methods: {
        login() {
            const data = {
                username: this.username,
                password: this.password
            };
        axios.post(`http://localhost:5000/api/login`, data)
            .then(response => {
                console.log(response.data);
                this.$router.push('/home');
            })
            .catch(error => {
                console.error(error);
                this.loginMessage = 'Usuario o contraseña incorrectos';
            });
        }
    },
};
</script>

<style>
.login-card {
    display: flex;
    flex-flow: column nowrap;
    justify-content: center;
    align-items: center;
}
.logo-container {
    display: flex;
    flex-flow: row nowrap;
    align-items: center;
    height: 100px;
    margin: 20px;
}

.logo-container svg {
    padding: 5px;
}

.logo-container p {
    padding: 5px;
    color: #202020;
    font-family: Poppins;
    font-size: 60px;
    font-weight: bolder;
}

.login-form-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    border: 2px solid #adadad; 
    border-radius: 10px; 
    box-shadow: 3px 3px 5px rgba(0, 0, 0, 0.1); 
    padding: 20px; 
    font-family: 'Poppins', sans-serif;
    width: 300px;
    height: 270px;
}

.login-form-container form {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}

.login-form-container form label {
    padding: 5px;
    color: #202020;
    font-family: Poppins;
    font-size: 20px;
    font-weight: bolder;
    letter-spacing: 0,75px;
}

.login-form-container form input {
    width: 100%;
    padding: 10px;
    border: 2px solid #ccc;
    border-radius: 10px;
    font-family: 'Poppins', sans-serif;
}

.login-form-container form input::placeholder {
  font-family: 'Poppins', sans-serif; 
  color: #999;
  text-align: center;
  letter-spacing: 0,75px;
}

.login-form-container form button {
    width: 100%;
    padding: 10px;
    margin-top: 10px;
    border: 1px solid #ccc;
    border-radius: 10px;
    font-family: 'Poppins', sans-serif;
    font-weight: bolder;
    background-color: #1AC84B;
    color: #fff;
    cursor: pointer;
}

.login-message {
    padding: 5px;
    color: #202020;
    font-family: Poppins;
    font-size: 12px;
    font-weight: bolder;
}

</style>

