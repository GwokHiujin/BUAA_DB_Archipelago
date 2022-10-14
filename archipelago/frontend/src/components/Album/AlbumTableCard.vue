<template>
  <el-card class="box-card" >
    <template #header>
      <div class="card-header">
        <span class="username" style="margin-left: 250px;">
          DiscoGraphy
        </span>
        <el-button class="button" text @click="dialogFormVisible = true">
          Add 1 Album
        </el-button>
        <el-dialog v-model="dialogFormVisible" title="Add 1 Album">
          <el-form>
            <el-form-item label="Album Name" :label-width="formLabelWidth">
              <el-input v-model.lazy="albumName" autocomplete="off" />
            </el-form-item>

            <el-form-item label="Price" :label-width="formLabelWidth">
              <el-input v-model.number.lazy="price" autocomplete="off" />
            </el-form-item>

            <el-form-item label="Author" :label-width="formLabelWidth">
              <el-input v-model.lazy="author" autocomplete="off" />
            </el-form-item>

            <el-form-item label="Releaser" :label-width="formLabelWidth">
              <el-input v-model.lazy="releaser" autocomplete="off" />
            </el-form-item>

            <el-form-item label="Release Year" :label-width="formLabelWidth">
              <el-date-picker
                  v-model.lazy="releaseYear"
                  type="year"
                  placeholder="Pick a year"
              />
            </el-form-item>

            <el-form-item label="Album Cover" :label-width="formLabelWidth">
              <el-input v-model.lazy="cover" autocomplete="off" />
            </el-form-item>

            <el-form-item label="Album Type" :label-width="formLabelWidth">
              <el-select  placeholder="Choose 1 Type" style="width: 77.9%" v-model.lazy.number="type">
                <el-option v-for="item in albumType" :key="item.label" :label="item.value" :value="item.label">
                  <span>{{ item.value }}</span>
                </el-option>
              </el-select>
            </el-form-item>

            <el-form-item label="Resource Link" :label-width="formLabelWidth">
              <el-input v-model.lazy="resource" autocomplete="off" />
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
      <el-table-column prop={{albumName}} label="Album Name" width="150" />
      <el-table-column prop={{price}} label="Price" width="150" />
      <el-table-column prop={{author}} label="Author" width="150" />
      <el-table-column prop={{releaser}} label="Releaser" width="150" />
      <el-table-column prop={{releaseYear}} label="Release Year" width="150" />
      <el-table-column prop={{type}} label="Type" width="150" />
      <el-table-column prop={{resource}} label="Resource" />
    </el-table>
  </el-card>
</template>

<script lang="ts" setup>
import { reactive, ref } from 'vue'

const dialogTableVisible = ref(false)
const dialogFormVisible = ref(false)
const formLabelWidth = '140px'

const albumid = ref('')
const albumName = ref('')
const price = ref('')
const author = ref('')
const releaser = ref('')
const releaseYear = ref('')
const cover = ref('')
const type = ref(null)
const resource = ref(null)

const albumType = [
  {
    label: '0',
    value: 'EP'
  },
  {
    label: '1',
    value: 'Single'
  },
  {
    label: '2',
    value: 'Album'
  },
  {
    label: '3',
    value: 'Live'
  },
  {
    label: '4',
    value: 'Demo'
  },
  {
    label: '5',
    value: 'Split'
  },
  {
    label: '6',
    value: 'Compilations'
  },
  {
    label: '7',
    value: 'Various Artists'
  },
  {
    label: '8',
    value: 'Original Soundtrack'
  }
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
