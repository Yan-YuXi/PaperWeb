<script>
/*
=========================================================
* Vue Material Kit 2 - v2.0.0
=========================================================

* Product Page: https://www.creative-tim.com/product/vue-material-kit
* Copyright 2022 Creative Tim (https://www.creative-tim.com)

Coded by www.creative-tim.com

 =========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
*/
import { RouterView } from "vue-router";
// import { getCurrentInstance } from 'vue'

// const { proxy } = getCurrentInstance()
// setup() {
//   if(sessionStorage.getItem("store")) {
//     proxy.$store.replaceState(Object.assign({}, proxy.$store.state, JSON.parse(sessionStorage.getItem("store"))))
//   }
//
//   window.addEventListener("beforeunload", () => {
//     sessionStorage.setItem("store",JSON.stringify(proxy.$store.state))
//   })
// }
export default {
  name: 'APP',
  components: {
    RouterView
  },
  created() {
    if(sessionStorage.getItem('store')) {
      this.$store.replaceState(
        Object.assign(
          {},
          this.$store.state,
          JSON.parse(sessionStorage.getItem('store'))
        )
      )
    }

    window.addEventListener('beforeunload', () => {
      sessionStorage.setItem('store', JSON.stringify(this.$store.state))
    })
  }
}
</script>

<template>
  <router-view />
</template>
