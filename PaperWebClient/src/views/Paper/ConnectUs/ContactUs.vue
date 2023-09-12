<script setup>
import { onMounted, ref, getCurrentInstance } from "vue";

//example components
import DefaultNavbar from "@/examples/navbars/NavbarDefault.vue";
import DefaultFooter from "@/examples/footers/FooterDefault.vue";

//image
import image from "@/assets/img/illustrations/illustration-signin.jpg";

//material components
import MaterialInput from "@/components/MaterialInput.vue";
import MaterialTextArea from "@/components/MaterialTextArea.vue";
import MaterialButton from "@/components/MaterialButton.vue";

// material-input
import setMaterialInput from "@/assets/js/material-input";
onMounted(() => {
  setMaterialInput();
});

const name = ref("");
const email = ref("");
const comment = ref("");
const centerDialogVisible = ref(false);

const { proxy } = getCurrentInstance();
function getName(val) {
  name.value = val;
  // console.log(val)
}
function getEmail(val) {
  email.value = val.trim();
  // console.log(val)
}

function getComment(val) {
  comment.value = val.trim();
  // console.log(val)
}
async function sendInput() {
  if (!comment.value.length) {
    alert("请输入您的意见");
    centerDialogVisible.value = false
  } else {
    console.log("姓名：", name.value);
    console.log("邮箱：", email.value);
    console.log("意见：", comment.value);
    let res = await proxy.$http.get("send_comment", {
      params: {
        name: name.value,
        email: email.value,
        comment: comment.value,
      },
    });
    if (res.status === 200) {
      alert(res.data.msg);
    } else {
      alert("由于服务请某些错误，提交数据失败");
    }
    proxy.$router.push("get_paper");
  }
}
</script>
<template>
  <div class="container position-sticky z-index-sticky top-0">
    <div class="row">
      <div class="col-12">
        <DefaultNavbar
          :sticky="true"
          :action="{
            route: 'https://www.creative-tim.com/product/vue-material-kit-pro',
            color: 'bg-gradient-success',
            label: 'Buy Now',
          }"
        />
      </div>
    </div>
  </div>
  <section>
    <div class="page-header min-vh-100">
      <div class="container">
        <div class="row">
          <div
            class="col-6 d-lg-flex d-none h-100 my-auto pe-0 position-absolute top-0 start-0 text-center justify-content-center flex-column"
          >
            <div
              class="position-relative h-100 m-3 px-7 border-radius-lg d-flex flex-column justify-content-center"
              :style="{
                backgroundImage: `url(${image})`,
                backgroundSize: 'cover',
              }"
              loading="lazy"
            ></div>
          </div>
          <div
            class="mt-8 col-xl-5 col-lg-6 col-md-7 d-flex flex-column ms-auto me-auto ms-lg-auto me-lg-5"
          >
            <div
              class="card d-flex blur justify-content-center shadow-lg my-sm-0 my-sm-6 mt-8 mb-5"
            >
              <div
                class="card-header p-0 position-relative mt-n4 mx-3 z-index-2 bg-transparent"
              >
                <h3 class="text-success text-success mb-0">提交意见</h3>
                <div
                  class="bg-gradient-success shadow-success border-radius-lg p-3"
                ></div>
              </div>
              <div class="card-body">
                <p class="pb-3">
                  如果在使用本系统过程中，您有什么意见和建议，或者您发现了什么BUG，烦请您描述相关情况，我们将及时与您联系并解决相关问题
                </p>
                <form id="contact-form" method="post" autocomplete="off">
                  <div class="card-body p-0 my-3">
                    <div class="row">
                      <div class="col-md-6">
                        <MaterialInput
                          class="input-group-static mb-4"
                          type="text"
                          label="姓名"
                          placeholder="姓名"
                          @getInput="getName"
                          @keyup.enter="centerDialogVisible = true"
                        />
                      </div>
                      <div class="col-md-6 ps-md-2">
                        <MaterialInput
                          class="input-group-static mb-4"
                          type="email"
                          label="邮箱"
                          placeholder="XXX@icost.ac.cn"
                          @getInput="getEmail"
                          @keyup.enter="centerDialogVisible = true"
                        />
                      </div>
                    </div>
                    <div class="form-group mb-0 mt-md-0 mt-4">
                      <MaterialTextArea
                        id="message"
                        class="input-group-static mb-4"
                        :rows="6"
                        placeholder="请描述您的意见或建议"
                        @getInput="getComment"
                        @keyup.enter="centerDialogVisible = true"
                      >
                        您的意见或建议</MaterialTextArea
                      >
                    </div>
                    <div class="row">
                      <div class="col-md-12 text-center btn-style">
                        <!--                        <MaterialButton-->
                        <!--                          variant="gradient"-->
                        <!--                          color="success"-->
                        <!--                          class="mt-3 mb-0"-->
                        <!--                          >提交</MaterialButton-->
                        <!--                        >-->
                        <el-button
                          type="success"
                          plain
                          @click="centerDialogVisible = true"
                          @keyup.enter="centerDialogVisible = true"
                        >
                          提交
                        </el-button>
                      </div>
                    </div>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>
        <el-dialog
          v-model="centerDialogVisible"
          title="&nbsp;&nbsp;请确认"
          width="30%"
          align-center
          @keyup.enter="sendInput"
        >
          <h6>姓名：{{ name }} 邮箱：{{ email }}</h6>
          <!--          <span></span>-->
          <span>
            <h6>意见：</h6>
            {{ comment }}
          </span>
          <template #footer>
            <span class="dialog-footer btn-style">
              <el-button
                type="info"
                @keyup.esc="centerDialogVisible = false"
                @click="centerDialogVisible = false"
                >取消</el-button
              >
              <el-button type="success" @click="sendInput"> 确认 </el-button>
            </span>
          </template>
        </el-dialog>
      </div>
    </div>
  </section>
  <DefaultFooter />
</template>

<style>
.btn-style button span {
  width: 100%;
  margin: 0;
}
.dialog-footer button:first-child {
  margin-right: 10px;
}
</style>
