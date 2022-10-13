<template>
  <el-card class="box-card" >
    <template #header>
      <div class="card-header">
        <span class="username" style="margin-left: 250px;">
          DiscoGraphy
        </span>
        <el-button class="button" text @click="dialogFormVisible = true">
          Add Album
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

    <el-table :data="tableData" style="width: 100%">
      <el-table-column prop="date" label="Name" width="150" />
      <el-table-column prop="name" label="Price" width="150" />
      <el-table-column prop="name" label="Author" width="150" />
      <el-table-column prop="name" label="Releaser" width="150" />
      <el-table-column prop="name" label="Release Year" width="150" />
      <el-table-column prop="name" label="Type" width="150" />
      <el-table-column prop="address" label="Resource" />
    </el-table>
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

const tableData = [
  {
    date: '2016-05-03',
    name: 'Tom',
    address: 'No. 189, Grove St, Los Angeles',
  },
  {
    date: '2016-05-02',
    name: 'Tom',
    address: 'No. 189, Grove St, Los Angeles',
  },
  {
    date: '2016-05-04',
    name: 'Tom',
    address: 'No. 189, Grove St, Los Angeles',
  },
  {
    date: '2016-05-01',
    name: 'Tom',
    address: 'No. 189, Grove St, Los Angeles',
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
  border-radius: 100%;
  border: 1px solid transparent;
  box-shadow: 0px 2px 4px 0px rgba(0, 0, 0, 0.12);
  background: white;
  transition: all .2s ease-in-out;
}
</style>
