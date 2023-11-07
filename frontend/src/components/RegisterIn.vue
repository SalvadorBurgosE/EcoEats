<template>
    <div class=logPrincipal>
        <div class ="logo">
            <svg xmlns="http://www.w3.org/2000/svg" width="64" height="61" viewBox="0 0 24 21" fill="none">
            <path fill-rule="evenodd" clip-rule="evenodd" d="M0 3.86203C0 -0.417471 5.35289 -1.36017 7.80629 2.14625C10.2648 5.65994 11.7134 9.93466 11.7301 14.5475C11.7301 9.97523 13.1371 5.73215 15.5409 2.2291C17.8898 -1.19396 23.0647 -0.289425 23.0647 3.86204V9.35365C23.0647 15.7228 17.9015 20.886 11.5324 20.886C5.16321 20.886 0 15.7228 0 9.35364V3.86203Z" fill="#1AC84B"/>
            </svg>
            <p class = "texto_icono">EcoEats</p>
        </div>
        <div class=login>
            <form @submit.prevent="login">
                <label for="nombre">Usuario </label><input v-model="username" type="text" placeholder="Username" tabindex="1">
                <br>
                
                <label for="nombre">Contraseña </label><input v-model="password" type="password" placeholder="Password" tabindex="2">
                <button type="submit">Login</button>
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
template{
    overflow:hidden;
}
.logo {
    display: flex;
    align-items: center;
    flex-direction: row;
    justify-content: center;
    height: 100vh;
    
}

.icono_ecoeats{
    width: 60px;
    margin-top: 50px;
    margin-left: 80px;
    position: relative;
}

.texto_icono{
    margin-top: 45px;
    margin-left: 10px;
    font-family: 'Fira Sans', sans-serif;
    font-size: 90px;
}

.login{
    display: flex;
    align-items: center;
    flex-direction: column;
    justify-content: center;
    margin-top: 10px;
}
</style>

