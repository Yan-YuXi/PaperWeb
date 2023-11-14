<script setup>
import { onMounted, onUnmounted } from "vue";
import { ref, watch, getCurrentInstance } from "vue";

//example components
import NavbarDefault from "../..//examples/navbars/NavbarDefault.vue";
import DefaultFooter from "../../examples/footers/FooterDefault.vue";
import Header from "../../examples/Header.vue";

//Vue Material Kit 2 components
// import MaterialSocialButton from "@/components/MaterialSocialButton.vue";

// sections
import PresentationCounter from "./Sections/PresentationCounter.vue";

//images
import vueMkHeader from "@/assets/img/vue-mk-header.jpg";

import { Search } from '@element-plus/icons-vue'

//hooks
const body = document.getElementsByTagName("body")[0];
onMounted(() => {
  body.classList.add("presentation-page");
  body.classList.add("bg-gray-200");
});
onUnmounted(() => {
  body.classList.remove("presentation-page");
  body.classList.remove("bg-gray-200");
});

// 相等 或者 包含
// 1 包含
// 0 相等
const equal_or_contain = ref("1")

// 数据
const input_info = ref("");
const select_type = ref("title");
const paper_list = ref([])

// 函数
const currentInstance = getCurrentInstance()
const { proxy } = currentInstance
async function onSubmit() {
  if(input_info.value.length === 0) {
    alert("请输入相关查询信息")
    return
  }
  const res = await proxy.$http.get('get_paper', {
    params: {
      type: select_type.value,
      title: input_info.value,
      isequal: equal_or_contain.value,
    }
  })
  console.log(res)
  if(res.status === 200) {
    if(res.data.status === true) {
      // console.log(res.data)
      paper_list.value = res.data.main_data
      console.log(paper_list.value)
    }
    else {
      alert(res.data.msg)
    }
  }
  else {
    alert("请求数据或服务器错误")
  }
}

// 侦听器
watch(input_info, (newVal) => {
  input_info.value = newVal.trim()
})

watch(paper_list, (newVal) => {
  if(newVal.length !== 0) {
    let obj = {
      "val": newVal,
      "input": input_info.value,
      "select": select_type.value,
      "isequal": equal_or_contain.value
    }
    proxy.$store.commit('setPaper', obj)
    proxy.$router.push('show_paper')
    // console.log(newVal)
  }
})

</script>

<template>
  <div class="container position-sticky z-index-sticky top-0">
    <div class="row">
      <div class="col-12">
        <NavbarDefault :sticky="true" />
      </div>
    </div>
  </div>
  <Header>
    <div
      class="page-header min-vh-75"
      :style="`background-image: url(${vueMkHeader})`"
      loading="lazy"
    >
      <div class="container">
        <div class="row">
          <div class="col-lg-8 text-center mx-auto position-relative">
            <h1
              class="text-white pt-3 mt-n5 me-2"
              :style="{ display: 'inline-block ' }"
            >
              文献检索系统

            </h1>
            <el-input
                v-model="input_info"
                placeholder="关键词组合查询，请以;分隔"
                class="input-with-select input-box"
                style="width: 100%; max-width: 1024px; height: 50px; margin-top: 10px; --el-border-radius-base: 20px; --el-component-size-large:50px"
                @keyup.enter="onSubmit"
                size="large"
                autofocus="true"
            >
              <template #prepend>
                <el-select v-model="select_type" placeholder="Select" style="max-width: 115px; margin-left: -20px; margin-right: 20px" size="large">
                  <el-option label="标题" value="title"/>
                  <el-option label="作者" value="author" />
                  <el-option label="期刊" value="source" />
                  <el-option label="关键字" value="keywords" />
                  <el-option label="摘要" value="abstract" />
                </el-select>
                <el-select v-model="equal_or_contain" placeholder="Select" style="max-width: 75px; --el-border-radius-base: 0px" size="large">
                  <el-option label="包含" value="1" />
                  <el-option label="等于" value="0" />
                </el-select>
              </template>
              <template #append>
                <el-button :icon="Search" @click="onSubmit"></el-button>
                <!--            <el-button type="primary" @click="onSubmit">Create</el-button>-->
              </template>
            </el-input>
<!--            <p class="lead text-white px-5 mt-3" :style="{ fontWeight: '500' }">-->
<!--              Start the Development With Bootstrap 5 Design System inspired by-->
<!--              Material Design.-->
<!--            </p>-->

          </div>
        </div>
      </div>
    </div>
  </Header>

  <div class="card card-body blur shadow-blur mx-3 mx-md-4 mt-n6">
    <PresentationCounter />
    <div class="py-5">
      <div class="container">
        <div class="row">
          <div class="col-lg-5 ms-auto">
            <h4 class="mb-1">感谢您的支持</h4>
            <p class="lead mb-0">如果有任何问题，请及时与我们联系</p>
          </div>
          <div class="col-lg-5 me-lg-auto my-lg-auto text-lg-end mt-5">
            <p>技术支持：<b>装备腐蚀仿真技术课题组</b></p>
<!--            <p>邮箱：kyguo@icost.ac.cn</p>-->
<!--            <MaterialSocialButton-->
<!--              route="https://twitter.com/intent/tweet?text=Check%20Material%20Design%20System%20made%20by%20%40CreativeTim%20%23webdesign%20%23designsystem%20%23bootstrap5&url=https%3A%2F%2Fwww.creative-tim.com%2Fproduct%2Fmaterial-design-system-pro"-->
<!--              component="twitter"-->
<!--              color="twitter"-->
<!--              label="Tweet"-->
<!--            />-->
<!--            <MaterialSocialButton-->
<!--              route="https://www.facebook.com/sharer/sharer.php?u=https://www.creative-tim.com/product/material-design-system-pro"-->
<!--              component="facebook-square"-->
<!--              color="facebook"-->
<!--              label="Share"-->
<!--            />-->
<!--            <MaterialSocialButton-->
<!--              route=""-->
<!--              component="pinterest"-->
<!--              color="pinterest"-->
<!--              label="Pin it"-->
<!--            />-->
          </div>
        </div>
      </div>
    </div>
  </div>
  <DefaultFooter />
</template>
