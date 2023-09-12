<script setup>
import { onMounted, onUnmounted, ref, getCurrentInstance, watch } from "vue";

//example components
import DefaultFooter from "../../../examples/footers/FooterDefault.vue";

//image
import bg0 from "@/assets/img/bg9.jpg";

//dep
import Typed from "typed.js";

//sections
import Information from "./Sections/AboutInformation.vue";
import NavbarDefault from "@/examples/navbars/NavbarDefault.vue";
import { Search } from "@element-plus/icons-vue";

const body = document.getElementsByTagName("body")[0];
const { proxy } = getCurrentInstance()

//hooks
onMounted(() => {
  get_paper()
  body.classList.add("about-us");
  body.classList.add("bg-gray-200");

  if (document.getElementById("typed")) {
    // eslint-disable-next-line no-unused-vars
    var typed = new Typed("#typed", {
      stringsElement: "#typed-strings",
      typeSpeed: 90,
      backSpeed: 90,
      backDelay: 200,
      startDelay: 500,
      loop: true,
    });
  };
});

onUnmounted(() => {
  body.classList.remove("about-us");
  body.classList.remove("bg-gray-200");
});


// 页码总数
const page_count = ref(2)
const paper_list = ref([])
const per_page = ref(10)
const input_info = ref("")
const select_type = ref("")
// 当前页码
const current_page = ref(1)
const type = ref(1)

function get_paper() {
  let count = proxy.$store.state.PaperList.length
  // console.log(count)
  if(count <= 0) {
    alert('没有数据，跳转至首页')
    proxy.$router.push('get_paper')
  }
  else {
    page_count.value = Math.ceil(count / per_page.value)
    current_page.value = 1
    get_per_page_paper(current_page.value)
    input_info.value = proxy.$store.state.title
    select_type.value = proxy.$store.state.type

  }
}
function handlePageChange(val) {
  // console.log(val)
  current_page.value = val
}

async function onSubmit() {
  if(input_info.value.length === 0) {
    alert("请输入相关查询信息")
    return
  }
  const res = await proxy.$http.get('get_paper', {
    params: {
      type: select_type.value,
      title: input_info.value
    }
  })
  console.log(res)
  if(res.status === 200) {
    if(res.data.status === true) {
      // console.log(res.data)
      // paper_list.value = res.data.main_data
      let obj = {
        "val": res.data.main_data,
        "input": input_info.value,
        "select": select_type.value
      }
      // console.log(typeof res.data.main_data)
      proxy.$store.commit('setPaper', obj)
      get_paper()
    }
    else {
      alert(res.data.msg)
    }
  }
  else {
    alert("请求数据或服务器错误")
  }
}

function get_per_page_paper(page) {
  paper_list.value = proxy.$store.getters.perPagePaper(page, per_page.value)
}
function sort_type(val) {
  // console.log('所选类型：',val)
  let data = proxy.$store.state.PaperList
  if(val === 1) {
    data.sort((a, b) => {
      return Number(a.pk)-Number(b.pk)
    })
  }
  else if(val === 2) {
    data.sort((a, b) => {
      return Number(b.publish_year)-Number(a.publish_year)
    })
  }
  else if(val === 3) {
    data.sort((a, b) => {
      return Number(a.publish_year)-Number(b.publish_year)
    })
  }
  else if(val === 4) {
    data.sort((a, b) => {
      return Number(b.download)-Number(a.download)
    })
  }
  else {
    data.sort((a, b) => {
      return Number(a.download)-Number(b.download)
    })
  }
  let obj = {
    "val": data,
    "input": input_info.value,
    "select": select_type.value
  }
  proxy.$store.commit('setPaper', obj)
  get_paper()
  // console.log(typeof data)
  // console.log(data)
}

// 监视器
watch(current_page, (newVal) => {
  get_per_page_paper(newVal)
})
</script>
<template>
<!--  <DefaultNavbar-->
<!--    transparent-->
<!--  />-->
  <div class="container position-sticky z-index-sticky top-0">
    <div class="row">
      <div class="col-12">
        <NavbarDefault :sticky="true" />
      </div>
    </div>
  </div>
  <header class="bg-gradient-dark">
    <div
      class="page-header min-vh-75"
      :style="{ backgroundImage: `url(${bg0})` }"
    >
      <span class="mask bg-gradient-dark opacity-6"></span>
      <div class="container">
        <div class="row justify-content-center">
          <div class="col-lg-8 text-center mx-auto my-auto">
            <h1 class="text-white">
<!--              Work with an amazing <span class="text-white" id="typed"></span>-->
              <el-input
                v-model="input_info"
                placeholder="关键词组合查询，请以;分隔"
                class="input-with-select input-box"
                style="width: 100%; max-width: 1024px; height: auto"
                @keyup.enter="onSubmit"
                size="large"
                autofocus="true"
              >
                <template #prepend>
                  <el-select v-model="select_type" placeholder="Select" style="max-width: 115px;" size="large">
                    <el-option label="标题" value="title"/>
                    <el-option label="作者" value="author" />
                    <el-option label="期刊" value="source" />
                    <el-option label="关键词" value="keywords" />
                    <el-option label="摘要" value="abstract" />
                  </el-select>
                </template>
                <template #append>
                  <el-button :icon="Search" @click="onSubmit"></el-button>
                  <!--            <el-button type="primary" @click="onSubmit">Create</el-button>-->
                </template>
              </el-input>
            </h1>
<!--            <div id="typed-strings">-->
<!--              <h1>team</h1>-->
<!--              <h1>design</h1>-->
<!--              <h1>tool</h1>-->
<!--            </div>-->
          </div>
        </div>
      </div>
    </div>
  </header>
  <div class="card card-body shadow-xl mx-3 mx-md-4 mt-n6">
    <Information
      :paper_list="paper_list"
      @sort_type="sort_type"
      :type="type"
    />
    <div class="col-12" style="width: 100%; display: flex; justify-content: center;">
      <el-pagination
        background
        :hidden="paper_list.length === 0"
        layout="prev, pager, next"
        @update:current-page="handlePageChange"
        :current-page="current_page"
        :page-count="page_count"
        class="page-style"
      />
    </div>

<!--    <AboutTeam />-->
<!--    <Featuring />-->
<!--    <Newsletter />-->
  </div>
  <DefaultFooter />
</template>
