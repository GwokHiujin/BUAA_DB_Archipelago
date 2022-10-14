<template>
  <el-affix>
    <el-menu
        default-active="activeIndex"
        class="el-menu-demo"
        mode="horizontal"
        :ellipsis="false"
    >

      <el-menu-item index="1" @click="this.$router.push('/SettingPage')">
        <img src="../../assets/img/avatar-default.jpg" class="head-avatar" />
      </el-menu-item>

      <div class="flex-grow" />
      <el-menu-item index="2" @click="logOut()">
        <el-icon><Promotion /></el-icon>
        LOG OUT
      </el-menu-item>
      <el-menu-item index="3" @click="dialogVisible = true" style="color: #b21a20">
        <el-icon><DeleteFilled /></el-icon>
        Delete
      </el-menu-item>

      <el-dialog
          v-model="dialogVisible"
          title="Delete this account"
          width="30%"
          align-center
      >
        <span>For security, please enter the password of your account</span>
        <el-divider/>
        <el-form-item label="Password" :label-width="formLabelWidth">
          <el-input v-model.lazy="password0" autocomplete="off" placeholder="Enter Old Password" show-password="false"/>
        </el-form-item>
        <el-form-item label="Confirm" :label-width="formLabelWidth">
          <el-input v-model.lazy="password1" autocomplete="off" placeholder="Enter Old Password" show-password="false"/>
        </el-form-item>

        <template #footer>
      <span class="dialog-footer">
        <el-button @click="dialogVisible = false">
          Cancel
        </el-button>
        <el-button type="primary" @click="deleteAccount()">
          Delete
        </el-button>
      </span>
        </template>
      </el-dialog>

    </el-menu>
  </el-affix>
</template>

<script>
export default {
  name: 'UserHeader',
  data() {
    return {
      dialogVisible: false,
      formLabelWidth: '100px',
      password0: '',
      password1: ''
    }
  },
  methods: {
    logOut: function () {
      this.$store.state.isLogin = false;
      this.$router.push('/');
    },
    deleteAccount: function () {
      let that = this;
      if (that.password0 !== this.$store.state.userInfo.password ||
          that.password1 !== this.$store.state.userInfo.password) {
        that.$message.error("Wrong password! Fail to delete this account");
      } else {
        this.axios.request({
          method: 'post',
          url: "", // TODO
          data: qs.stringify({
            userEmail: this.$store.state.userInfo.email
          })
        }).then(res => {
          console.log(res.data)
          if (res.data.errno === 0) {
            this.$message({
              message: "Successfully delete this account!",
              type: 'success',
              showClose: true
            })
            this.dialogVisible = false;
            this.$store.state.userInfo.isLogin = false;
            this.$router.push('/');
          } else {
            this.$message({
              message: "Fail to delete this account",
              type: 'error',
              showClose: true
            })
            this.dialogVisible = false;
            location.reload();
          }
        }).catch(err => {
          console.log(err)
        })
      }
    }
  }
}
</script>

<style>
.flex-grow {
  flex-grow: 1;
}

.el-menu-demo {
  font-family: "Berlin Sans FB";
  font-size: larger;
}

.head-avatar {
  width: 45px;
  border-radius: 100%;
  margin-top: auto;
  margin-bottom: auto;
  margin-left: 10px;
  border: 2px solid transparent;
  box-shadow: 0px 2px 4px 0px rgba(0, 0, 0, 0.24);
  background: white;
}
</style>
