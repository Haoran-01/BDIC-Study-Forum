import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import VueGridLayout from 'vue3-grid-layout';
import toast from 'vue-toastification'
import VueCropper from 'vue-cropper';
import 'vue-cropper/dist/index.css'

createApp(App).use(store).use(router).use(VueGridLayout).use(toast).use(VueCropper).mount('#app')

