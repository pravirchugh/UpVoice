import 'primevue/resources/themes/aura-light-green/theme.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import PrimeVue from 'primevue/config'
import Card from 'primevue/card'
import Button from 'primevue/button'
import Fieldset from 'primevue/fieldset'
import Dropdown from 'primevue/dropdown'
import InputText from 'primevue/inputtext';
import RadioButton from 'primevue/radiobutton';


const app = createApp(App)

app.use(PrimeVue)
app.use(router)
app.component('Card', Card)
app.component('Card', Card)
app.component('Button', Button)
app.component('Fieldset', Fieldset)
app.component('Dropdown', Dropdown)
app.component('InputText', InputText)
app.component('RadioButton', RadioButton)

app.mount('#app')
