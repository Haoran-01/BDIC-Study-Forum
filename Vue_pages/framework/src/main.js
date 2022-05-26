import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import VueGridLayout from 'vue3-grid-layout';
import toast from 'vue-toastification'
import VueCropper from 'vue-cropper';
import 'vue-cropper/dist/index.css';

import naive from 'naive-ui'
// 通用字体
import 'vfonts/Lato.css'
// 等宽字体
import 'vfonts/FiraCode.css'




createApp(App).use(store).use(router).use(VueGridLayout).use(toast).use(VueCropper).use(naive).mount('#app')

