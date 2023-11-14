<script setup>
import DefaultCounterCard from "../../../examples/cards/counterCards/DefaultCounterCard.vue";
import { ref } from "vue";
import { onBeforeMount, getCurrentInstance } from "vue";

const paper_count = ref(231000)
const paper_recount = ref(1000)
const { proxy }  = getCurrentInstance()
// onBeforeMount(() => {
//   get_count()
// })

// async function get_count() {
//   const res = await proxy.$http.get('get_paper_count')
//   // console.log(res.data[0].count)
//   paper_count.value = res.data[0].count
//   paper_recount.value = res.data[0].recount
//   // console.log(paper_recount.value)
// }
// const TotalPaper = ref(0);
</script>

<template>
  <section class="pt-3 pb-4" id="count-stats">
    <div class="container">
      <div class="row">
        <div class="col-lg-9 z-index-2 border-radius-xl mx-auto py-3">
          <div class="row">
            <div class="col-md-6 position-relative">
              <DefaultCounterCard
                color="success"
                title="目前拥有文献数量"
                description=""
                :count=paper_count
                suffix="+"
                :duration="3000"
                divider="vertical"
              />
            </div>
            <div class="col-md-6 position-relative">
              <DefaultCounterCard
                color="success"
                title="最近更新数量"
                description=""
                :count="1000"
                suffix="+"
                :duration="3000"
              />
            </div>
<!--            <div class="col-md-4">-->
<!--              <DefaultCounterCard-->
<!--                color="success"-->
<!--                title="Pages"-->
<!--                description="Save 3-4 weeks of work when you use our pre-made pages for-->
<!--                  your website"-->
<!--                :count="4"-->
<!--                :duration="3000"-->
<!--              />-->
<!--            </div>-->
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
