<script setup>
import { onMounted, ref, watch, getCurrentInstance, defineEmits } from "vue";
// import proxy from "http-proxy";
// example components
const props = defineProps(['paper_list', 'type'])
const emit = defineEmits(['sort_type'])

onMounted(() => {
  let ele = document.getElementById('my_table')
  table_width.value = parseInt(window.getComputedStyle(ele).width)

  radio.value = props.type
})

function setColWidth(type) {
  let res = 0
  switch (type) {
    case 1:
      res = table_width.value * 0.57
      break;
    case 2:
      res = table_width.value * 0.08
      break;
    case 3:
      res = table_width.value * 0.08
      break;
    case 4:
      res = table_width.value * 0.08
      break;
    case 5:
      res = table_width.value * 0.04
      break;
    case 6:
      res = table_width.value * 0.08
      break;
    case 7:
      res = table_width.value * 0.04
      break;
    default:
      res = table_width.value * 0.03
  }
  return res
}

const table_width = ref(1960)
const { proxy } = getCurrentInstance()
const radio = ref(1)
const activeNames = ref(['1'])
async function handleRowClick(row, col, event) {
  console.log('点击的是第',row.pk)
  let res = await proxy.$http.get('get_paper_detail_data', {
    params: {
        pk: row.pk
    }
  })
  // console.log(res)
  if(res.status === 200) {
    if(res.data.status === true) {
      // console.log(res.data)
      proxy.$store.commit('setPaperInfo', res.data.detail_data)
      // proxy.$store.replaceState(
      //     Object.assign(
      //         {},
      //         proxy.$store.state,
      //         JSON.parse(sessionStorage.getItem('store'))
      //     )
      // )
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
  <section class="py-7">
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
<!--        <div class="col-1"></div>-->
        <div class="col-10">
          <el-card class="box-card">
            <div class="card-header">
              <span>标题</span>
              <span>作者</span>
              <span>来源</span>
              <span>发表年份</span>
              <span>被引</span>
              <span>下载量</span>
              <span>下载</span>
            </div>
          </el-card>
          <el-table
            :data="paper_list"
            id="my_table"
            ref="my_table"
            stripe
            @row-click="handleRowClick"
          >
            <el-table-column prop="title" :width="setColWidth(1)"/>
            <el-table-column prop="author" :width="setColWidth(2)" />
            <el-table-column prop="source" :width="setColWidth(3)" />
            <el-table-column prop="publish_year" :width="setColWidth(4)" />
            <el-table-column prop="cited" :width="setColWidth(5)" />
            <el-table-column prop="download" :width="setColWidth(6)"/>
            <el-table-column :width="setColWidth(7)">
              <img class="img-class"  src="@/assets/img/download.png" alt="" />
            </el-table-column>
            <el-table-column :width="setColWidth(8)" prop="" />
          </el-table>
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
</style>
