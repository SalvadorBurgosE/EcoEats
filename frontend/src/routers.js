import { createRouter, createWebHistory } from "vue-router";
import RegisterIn from './components/RegisterIn'
import HomePage from './components/HomePage'
import CarritoCompras from './components/CarritoCompras'

const routes = [
    {
        path: '/', 
        name: 'login',
        component:RegisterIn
    },
    {
        path: '/home', 
        name: 'home',
        component:HomePage
    },
    {
        path: '/carro',
        name: 'carro',
        component: CarritoCompras
    }

]

const router = createRouter({
    history:createWebHistory(), //Navegación por defecto
    routes,
}) 

export default router;