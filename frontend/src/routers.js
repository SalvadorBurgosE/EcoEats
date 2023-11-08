import { createRouter, createWebHistory } from "vue-router";
import RegisterIn from './components/RegisterIn'
import HomePage from './components/HomePage'
import CarritoCompras from './components/CarritoCompras'
import ProductDetails from './components/ProductDetails'

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
    },
    {
        path: '/product/detail/:id', 
        name: 'details',
        component: ProductDetails,
        props: true 
    }

]

const router = createRouter({
    history:createWebHistory(), //Navegación por defecto
    routes,
}) 

export default router;