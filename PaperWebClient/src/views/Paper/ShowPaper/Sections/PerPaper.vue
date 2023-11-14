<script setup>
import { onMounted, ref, watch, getCurrentInstance, defineEmits } from "vue";
// import proxy from "http-proxy";
// example components
const props = defineProps(['paper_list', 'type'])
const emit = defineEmits(['sort_type'])

onMounted(() => {
  // let ele = document.getElementById('my_table')
  // table_width.value = parseInt(window.getComputedStyle(ele).width);
  radio.value = props.type
})

// function setColWidth(type) {
//   let res = 0
//   switch (type) {
//     case 1:
//       res = table_width.value * 0.57
//       break;
//     case 2:
//       res = table_width.value * 0.08
//       break;
//     case 3:
//       res = table_width.value * 0.08
//       break;
//     case 4:
//       res = table_width.value * 0.08
//       break;
//     case 5:
//       res = table_width.value * 0.04
//       break;
//     case 6:
//       res = table_width.value * 0.08
//       break;
//     case 7:
//       res = table_width.value * 0.04
//       break;
//     default:
//       res = table_width.value * 0.03
//   }
//   return res
// }

// const table_width = ref(1960);
const { proxy } = getCurrentInstance();
const radio = ref(1)
const activeNames = ref(['1'])
// async function handleRowClick(row, col, event) {
//   console.log('点击的是第',row.pk)
//   let res = await proxy.$http.get('get_paper_detail_data', {
//     params: {
//         pk: row.pk
//     }
//   })
//   // console.log(res)
//   if(res.status === 200) {
//     if(res.data.status === true) {
//       // console.log(res.data)
//       proxy.$store.commit('setPaperInfo', res.data.detail_data)
//       // proxy.$store.replaceState(
//       //     Object.assign(
//       //         {},
//       //         proxy.$store.state,
//       //         JSON.parse(sessionStorage.getItem('store'))
//       //     )
//       // )
//       sessionStorage.setItem('store', JSON.stringify(proxy.$store.state))
//       // console.log(res.data.detail_data)
//       // 在新窗口打开路由
//       let routeData = proxy.$router.resolve('detail_paper')
//       window.open(routeData.href)
//     }
//     else {
//       alert(res.data.msg)
//     }
//   }
//   else {
//     alert("请求数据或服务器错误")
//   }
// }

async function handlePaperInfo(pk) {
  // console.log("点击的主键是：", pk)
  let res = await proxy.$http.get('get_paper_detail_data', {
    params: {
      pk: pk
    }
  })
  // console.log(res)
  if(res.status === 200) {
    if(res.data.status === true) {
      // console.log(res.data)
      proxy.$store.commit('setPaperInfo', res.data.detail_data)
      sessionStorage.setItem('store', JSON.stringify(proxy.$store.state))
      // console.log(res.data.detail_data)
      // 在新窗口打开路由
      let routeData = proxy.$router.resolve('detail_paper')
      window.open(routeData.href)
    }
    else {
      alert(res.data.msg)
    }
  }
  else {
    alert("请求数据或服务器错误")
  }
}

watch(radio, (newVal) => {
  emit('sort_type', newVal)
})

</script>
<template>
  <section class="py-7" style="padding-top: 3rem !important;">
    <div class="container">
<!--      <div class="row align-items-center">-->
      <div class="row">
        <div class="col-2">
          <div class="demo-collapse">
            <el-collapse class="demo-col" v-model="activeNames">
<!--              <el-collapse-item title="筛选" name="1">-->
<!--                <div>-->
<!--                </div>-->
<!--&lt;!&ndash;                <div>&ndash;&gt;-->
<!--&lt;!&ndash;                  Consistent within interface: all elements should be consistent, such&ndash;&gt;-->
<!--&lt;!&ndash;                  as: design style, icons and texts, position of elements, etc.&ndash;&gt;-->
<!--&lt;!&ndash;                </div>&ndash;&gt;-->
<!--              </el-collapse-item>-->
              <el-collapse-item title="排序" name="1">
                <div>
                  <el-radio-group v-model="radio">
                    <el-radio :label="1">默认排序</el-radio>
                    <el-radio :label="2">时间降序</el-radio>
                    <el-radio :label="3">时间升序</el-radio>
                    <el-radio :label="4">下载降序</el-radio>
                    <el-radio :label="5">下载升序</el-radio>
                  </el-radio-group>
                </div>
              </el-collapse-item>
            </el-collapse>
          </div>
        </div>

        <div class="col-10">
          <el-card v-for="paper in paper_list" class="box-card">
<!--            <h6>A Dual-stage Large-scale Multi-objective Evolutionary Algorithm with Dynamic Learning Strategy</h6>-->

            <h6 style="cursor: pointer; text-align: justify" @click="handlePaperInfo(paper.pk)">{{ paper.title }}</h6>

            <div class="paper-base-info">
              <div class="paper-img-style">
                <img class="img-style" src="@/assets/img/author.png" />
                {{ paper.author }}
              </div>
              <div class="font-weight-normal">{{ paper.publish_year }}年 《{{ paper.source }}》</div>
              <div class="font-weight-normal" style="font-size: 13px">{{ paper.download }}次下载</div>
            </div>
          </el-card>
        </div>
      </div>
    </div>
  </section>
</template>

<style>
.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 2vh;
}
span {
  font-size: 14px;
}

span:nth-child(1) {
  width: 60%;
  margin-left: -10px;
}
span:nth-child(2) {
  width: 8%;
}
span:nth-child(3) {
  width: 8%;
}
span:nth-child(4) {
  width: 8%;
}
span:nth-child(5) {
  width: 4%;
}
span:nth-child(6) {
  width: 8%;
}
span:nth-child(7) {
  width: 4%;
  margin-right: -10px;
}

.box-card span {
  font-size: 18px;
  font-weight: bold;
}

.img-class {
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 20px;
}
/*.text {*/
/*  font-size: 14px;*/
/*}*/

/*.item {*/
/*  margin-bottom: 18px;*/
/*}*/

/*.box-card {*/
/*  width: 100%;*/
/* } */
.demo-collapse {
  font-weight: 700;
}
.demo-col {
  /*width: 200px;*/
  //height: 200px;
  //background-color: red;
}
.el-radio-group span {
  width: 100% !important;
  padding-left: 10px;
}

.text {
  font-size: 14px;
}

.item {
  padding: 18px 0;
}

.box-card {
  width: 100%;
  border-radius: 10px;
  margin-bottom: 10px;
}

.paper-base-info {
  font-family: "Microsoft YaHei";
  font-weight: bold;
  font-size: 15px;

}
.paper-img-style {
  display: flex;
  align-items: center;
}

.img-style {
  height: 21px;
  margin-right: 5px;
}
</style>
