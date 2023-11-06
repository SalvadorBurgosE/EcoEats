<template>
    <div>
        <h1>Login</h1>
        <form @submit.prevent="login">
            <input v-model="username" type="text" placeholder="Username">
            <input v-model="password" type="password" placeholder="Password">
            <button type="submit">Login</button>
        </form>
        <div v-if="loginMessage" class="login-message">{{ loginMessage }}</div>
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

</style>

