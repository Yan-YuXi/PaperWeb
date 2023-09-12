<script setup>
import { ref, watch } from "vue";
const emit = defineEmits(['getInput'])
defineProps({
  id: {
    type: String,
    default: "message",
  },
  rows: {
    type: Number,
    default: 4,
  },
  placeholder: {
    type: String,
    default: "",
  },
  labelClass: {
    type: String,
    default: "",
  },
});

const val = ref('')

function sendInput() {
  emit('getInput', val.value)
}

watch(val, (newVal) => {
  val.value = newVal.trim()
})
</script>
<template>
  <div class="input-group">
    <label :for="id" :class="labelClass"><slot /></label>
    <textarea
      name="message"
      class="form-control"
      :id="id"
      :placeholder="placeholder"
      :rows="rows"
      v-model="val"
      @blur="sendInput"
    />
  </div>
</template>
