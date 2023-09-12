<script setup>
import { onMounted, getCurrentInstance, ref } from "vue";

//Vue Material Kit 2 components
import MaterialAvatar from "@/components/MaterialAvatar.vue";
import MaterialButton from "@/components/MaterialButton.vue";

// image
import profilePic from "@/assets/img/bruce-mars.jpg";

// material-input
import setMaterialInput from "@/assets/js/material-input";
onMounted(() => {
  setMaterialInput();
  paper_info();
  let paper = Object.assign(
    {},
    proxy.$store.state,
    JSON.parse(sessionStorage.getItem('store'))
  )
  if(Object.keys(paper.PaperInfo).length === 0) {
    alert('没有数据，跳转至首页')
    proxy.$router.push('get_paper')
  }
});

const data = ref({})

const { proxy } = getCurrentInstance()
function paper_info() {
  data.value = proxy.$store.state.PaperInfo
}

async function download_file() {
  let res = await proxy.$http.get('download_file', {
    params: {
      pk: data.value.pk
    }
  })

  console.log(res)
  if(res.status === 200) {
    let blob = new Blob([res.data], { type: "application/octet-stream" });

    let url = window.URL.createObjectURL(blob)

    let link = document.createElement("a")
    link.href = url
    link.download = String(data.value.pk) + ".pdf"
    link.click()

    // 释放URL 对象，避免内存溢出
    window.URL.revokeObjectURL(url)
  }
  else {
    alert("下载出现错误")
  }
}
</script>
<template>
  <section class="py-sm-7 py-5 position-relative">
    <div class="container">
      <div class="row">
        <div class="col-12 mx-auto">
          <div class="mt-n8 mt-md-n9 text-center">
            <div class="blur-shadow-avatar">
<!--              <MaterialAvatar-->
<!--                size="xxl"-->
<!--                class="shadow-xl position-relative z-index-2"-->
<!--                :image="profilePic"-->
<!--                alt="Avatar"-->
<!--              />-->
            </div>
          </div>
          <div class="row py-7">
            <div
              class="col-lg-7 col-md-7 z-index-2 position-relative px-md-2 px-sm-5 mx-auto"
              style="font-family: 'Times New Roman', 'Microsoft YaHei', 'Helvetica Neue', 'Helvetica', 'PingFang SC', 'Hiragino Sans GB', '微软雅黑', 'Arial', 'sans-serif'"
            >
              <div
                class="d-flex justify-content-between align-items-center mb-2"
              >
                <h3 class="mb-0">{{ data.title }}</h3>
                <div class="d-block">
                  <MaterialButton
                    class="text-nowrap mb-0"
                    variant="outline"
                    color="dark"
                    size="sm"
                    @click="download_file"
                  >
                    下载
                    <img class="img-no-margin" src="@/assets/img/down.png" alt="" />
                  </MaterialButton>
<!--                  <h5>下载量：</h5>-->
                </div>
              </div>
              <div class="row mb-4 div-style">
                <div class="col-auto">
                  <span>作者: </span>
                  <span class="h6 me-1">{{ data.author }}</span>
                </div>
              </div>
              <div class="row mb-4 div-style">
                <div class="col-auto">
                  <span>机构: </span>
                  <span class="h6 me-1">{{ data.affiliations }}</span>
                </div>
              </div>
              <div class="row mb-4 div-style">
                <div class="col-auto">
                  <span>来源: </span>
                  <span class="h6 me-1">{{ data.source }}</span>
                </div>
              </div>
              <div class="row mb-4 div-style">
                <div class="col-auto">
                  <span>摘要: </span>
                  <span>
<!--                    justify 是两端对齐  -->
                     <p v-if="data.abstract" style="text-align: justify" class="text-lg mb-0">{{ data.abstract }}</p>
                    <p v-else>暂无此论文摘要数据</p>
                  </span>
                </div>
                <!--                <div class="col-auto">-->
                <!--                  <span>Issue:</span>-->
                <!--                  -->

                <!--                </div>-->
                <!--                <div class="col-auto">-->
                <!--                  <span>Pages:</span>-->
                <!--                  <span class="h6 me-1">260</span>-->
                <!--                </div>-->
              </div>
<!--              <p class="text-lg mb-0">-->
<!--                Decisions: If you can’t decide, the answer is no. If two equally-->
<!--                difficult paths, choose the one more painful in the short term-->
<!--                (pain avoidance is creating an illusion of equality). Choose the-->
<!--                path that leaves you more equanimous.-->
<!--                <br />-->
<!--&lt;!&ndash;                <a&ndash;&gt;-->
<!--&lt;!&ndash;                  href="javascript:;"&ndash;&gt;-->
<!--&lt;!&ndash;                  class="text-success icon-move-right"&ndash;&gt;-->
<!--&lt;!&ndash;                  >More about me&ndash;&gt;-->
<!--&lt;!&ndash;                  <i class="fas fa-arrow-right text-sm ms-1"></i>&ndash;&gt;-->
<!--&lt;!&ndash;                </a>&ndash;&gt;-->
<!--              </p>-->
<!--              <hr />-->
<!--              <h6>关键字：</h6>-->
              <div class="row mb-4 div-style">
                <div class="col-auto">
                  <span>关键词: </span>
                  <span class="h6 me-1" v-for="keyword in data.keysords">{{ keyword }}</span>
<!--                  <span class="h6 me-1">3.5k; </span>-->
<!--                  <span class="h6 me-1">3.5k; </span>-->
                </div>
<!--                <div class="col-auto">-->
<!--                  <span>Issue:</span>-->
<!--                  -->

<!--                </div>-->
<!--                <div class="col-auto">-->
<!--                  <span>Pages:</span>-->
<!--                  <span class="h6 me-1">260</span>-->
<!--                </div>-->
              </div>
              <div class="row mb-4 div-style">
                <div class="col-auto">
                  <span>年份: </span>
                  <span class="h6 me-1">{{ data.publish_year }}年</span>
                </div>
                <div v-if="data.volume" class="col-auto">
                  <span>卷: </span>
                  <span class="h6 me-1">{{ data.volume }}</span>
                </div>
                <div v-if="data.issue" class="col-auto">
                  <span>期: </span>
                  <span class="h6 me-1">{{ data.issue }}</span>

                </div>
                <div v-if="data.page" class="col-auto">
                  <span>页: </span>
                  <span class="h6 me-1">{{ data.page }}</span>
                </div>
              </div>
              <div class="row mb-4 div-style">
                <div class="col-auto">
                  <span>下载量: </span>
                  <span class="h6 me-1">{{ data.download }}</span>
                </div>
                <div class="col-auto">
                  <span>被引数: </span>
                  <span class="h6 me-1">{{ data.cited_times }}</span>
                </div>
<!--                <div class="col-auto">-->
<!--                  <span>Issue: </span>-->
<!--                  <span class="h6 me-1">3.5k</span>-->

<!--                </div>-->
<!--                <div class="col-auto">-->
<!--                  <span>Pages: </span>-->
<!--                  <span class="h6 me-1">260</span>-->
<!--                </div>-->
              </div>
              <h6>
                <a v-if="data.doi" :href="`https://dx.doi.org/${data.doi}`" target="_blank">点击查看原文</a>
              </h6>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<style>
.div-style {
  padding-left: 10px;
}
.img-no-margin {
  height: 15px;
  margin-right: 0;
}
</style>
