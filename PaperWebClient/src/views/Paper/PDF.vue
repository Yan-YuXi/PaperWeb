<script setup>
import { onMounted, ref, getCurrentInstance } from "vue";
const { proxy } = getCurrentInstance()
const file_path = ref('')
const file_name = ref('')
const bHeight = ref('1024px')
const bWidth = ref('100%')
onMounted(() => {
  file_name.value = proxy.$store.state.fileName
  file_path.value = "../../../" + proxy.$store.state.paperPath
  bHeight.value = document.documentElement.scrollHeight
  bWidth.value = document.documentElement.scrollWidth
})
</script>

<template>
  <div>
    <object type="application/pdf" :data="file_path" width="100%" :height="bHeight"></object>
  </div>
</template>

<style scoped>

</style>