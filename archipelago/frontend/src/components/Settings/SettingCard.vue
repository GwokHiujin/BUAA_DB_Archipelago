<template>
  <el-card class="box-card" >
    <template #header>
      <div class="card-header">
        <img src="src/assets/img/avatar-default.jpg" class="avatar"/>
        <span class="username">
          MusicLover
          <el-space/>
          <el-tag style="font-family: 'Candara Light'">
            Audience User
          </el-tag>
        </span>
        <el-button class="button" text @click="outerVisible = true">
          Edit
        </el-button>
        <el-dialog
            v-model="outerVisible"
            title="Edit Your Profile"
            style="border-radius: 5%"
            width="30%"
            align-center
        >
          <el-form :model="form">
            <el-form-item label="Nickname" :label-width="formLabelWidth">
              <el-input v-model="form.name" autocomplete="off" placeholder="Enter New Nickname"/>
            </el-form-item>
            <el-form-item label="Password" :label-width="formLabelWidth">
              <el-button class="el-button--danger" @click="innerVisible = true">
                Edit Password
              </el-button>
            </el-form-item>

            <el-dialog
              v-model="innerVisible"
              title="Edit Password"
              style="border-radius: 5%"
              width="40%"
              append-to-body
              align-center
            >
              <el-form-item label="Old Password" :label-width="formLabelWidth">
                <el-input v-model="form.name" autocomplete="off" placeholder="Enter Old Password" show-password="false"/>
              </el-form-item>
              <el-form-item label="New Password" :label-width="formLabelWidth">
                <el-input v-model="form.name" autocomplete="off" placeholder="Enter New Password" show-password="false"/>
              </el-form-item>
              <el-form-item label="Confirm" :label-width="formLabelWidth">
                <el-input v-model="form.name" autocomplete="off" placeholder="Enter New Password Again" show-password="false"/>
              </el-form-item>
              <template #footer>
                <span class="dialog-footer">
                  <el-button @click="innerVisible = false">
                    Cancel
                  </el-button>
                  <el-button type="primary" @click="innerVisible = false">
                    Submit
                  </el-button>
                </span>
              </template>
            </el-dialog>

          </el-form>
          <template #footer>
            <span class="dialog-footer">
              <el-button @click="outerVisible = false">
                Cancel
              </el-button>
              <el-button type="primary" @click="outerVisible = false">
                Confirm
              </el-button>
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
            Nickname
          </div>
        </template>
        kooriookami
      </el-descriptions-item>
      <el-descriptions-item>
        <template #label>
          <div class="cell-item">
            <el-icon><Message /></el-icon>
            Register Email
          </div>
        </template>
        test@example.com
      </el-descriptions-item>
      <el-descriptions-item>
        <template #label>
          <div class="cell-item">
            <el-icon><ChatDotRound /></el-icon>
            Bio
          </div>
        </template>
        Hello world! Just love music...
      </el-descriptions-item>
    </el-descriptions>
  </el-card>
</template>

<script lang="ts" setup>
import { reactive, ref } from 'vue'

const outerVisible = ref(false)
const innerVisible = ref(false)
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
  border-radius: 100%;
  border: 1px solid transparent;
  box-shadow: 0px 2px 4px 0px rgba(0, 0, 0, 0.12);
  background: white;
  transition: all .2s ease-in-out;
}
</style>