<template>
  <el-card class="box-card" >
    <template #header>
      <div class="card-header">
        <img src="src/assets/img/photo-default.jpg" class="avatar"/>
        <span class="username">
          BUAA HAPPY BAND
        </span>
        <el-button class="button" text @click="dialogFormVisible = true">
          Edit
        </el-button>
        <el-dialog v-model="dialogFormVisible" title="Shipping address">
          <el-form :model="form">
            <el-form-item label="Promotion name" :label-width="formLabelWidth">
              <el-input v-model="form.name" autocomplete="off" />
            </el-form-item>
            <el-form-item label="Zones" :label-width="formLabelWidth">
              <el-select v-model="form.region" placeholder="Please select a zone">
                <el-option label="Zone No.1" value="shanghai" />
                <el-option label="Zone No.2" value="beijing" />
              </el-select>
            </el-form-item>
          </el-form>
          <template #footer>
      <span class="dialog-footer">
        <el-button @click="dialogFormVisible = false">Cancel</el-button>
        <el-button type="primary" @click="dialogFormVisible = false"
        >Confirm</el-button
        >
      </span>
          </template>
        </el-dialog>
      </div>
    </template>

    <el-descriptions
        column="2"
        size="large"
        border>
      <el-descriptions-item>
        <template #label>
          <div class="cell-item">
            <el-icon><UserFilled /></el-icon>
            Musician Name
          </div>
        </template>
        BUAA HAPPY BAND
      </el-descriptions-item>
      <el-descriptions-item>
        <template #label>
          <div class="cell-item">
            <el-icon><Message /></el-icon>
            Origin Country
          </div>
        </template>
        CN
      </el-descriptions-item>
      <el-descriptions-item>
        <template #label>
          <div class="cell-item">
            <el-icon><Message /></el-icon>
            Location
          </div>
        </template>
        Beijing
      </el-descriptions-item>
      <el-descriptions-item>
        <template #label>
          <div class="cell-item">
            <el-icon><Message /></el-icon>
            Lyrical Themes
          </div>
        </template>
        School Style, Folk
      </el-descriptions-item>
      <el-descriptions-item>
        <template #label>
          <div class="cell-item">
            <el-icon><Message /></el-icon>
            Formed Year
          </div>
        </template>
        2022
      </el-descriptions-item>
      <el-descriptions-item>
        <template #label>
          <div class="cell-item">
            <el-icon><ChatDotRound /></el-icon>
            Introduction
          </div>
        </template>
        Hello world! Just love music...
      </el-descriptions-item>
    </el-descriptions>
  </el-card>
</template>

<script lang="ts" setup>
import { reactive, ref } from 'vue'

const dialogTableVisible = ref(false)
const dialogFormVisible = ref(false)
const formLabelWidth = '140px'

const form = reactive({
  name: '',
  region: '',
  date1: '',
  date2: '',
  delivery: false,
  type: [],
  resource: '',
  desc: '',
})

const gridData = [
  {
    date: '2016-05-02',
    name: 'John Smith',
    address: 'No.1518,  Jinshajiang Road, Putuo District',
  },
  {
    date: '2016-05-04',
    name: 'John Smith',
    address: 'No.1518,  Jinshajiang Road, Putuo District',
  },
  {
    date: '2016-05-01',
    name: 'John Smith',
    address: 'No.1518,  Jinshajiang Road, Putuo District',
  },
  {
    date: '2016-05-03',
    name: 'John Smith',
    address: 'No.1518,  Jinshajiang Road, Putuo District',
  },
]
</script>

<style>
.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.text {
  font-size: 14px;
}

.item {
  margin-bottom: 18px;
}

.box-card {
  width: 100vh;
}

.username {
  font-family: "Matura MT Script Capitals";
  font-size: 24px;
  margin-left: 20px;
}

.cell-item {
  font-family: "Berlin Sans FB";
  font-size: 14px;
}

.avatar {
  width: 80px;
  height: 80px;
  overflow: hidden;
  border-radius: 10%;
  background: white;
  transition: all .2s ease-in-out;
}
</style>
