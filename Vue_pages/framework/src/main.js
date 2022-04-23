import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import VueGridLayout from 'vue3-grid-layout';
import toast from 'vue-toastification'

createApp(App).use(store).use(router).use(VueGridLayout).use(toast).mount('#app')

