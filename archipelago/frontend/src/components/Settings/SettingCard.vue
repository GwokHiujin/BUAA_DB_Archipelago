<template>
  <el-card class="box-card" >
    <template #header>
      <div class="card-header">
        <img src="src/assets/img/avatar-default.jpg" class="avatar" v-if="userInfo.useravatar === ''"/>
        <img src={{userInfo.useravatar}} class="avatar" v-else/>
        <span class="username">
          {{userInfo.nickname}}
          <el-space/>
          <el-tag style="font-family: 'Candara Light'" v-if="userInfo.type === 0">
            Audience User
          </el-tag>
          <el-tag style="font-family: 'Candara Light'" v-if="userInfo.type === 1">
            Musician User
          </el-tag>
        </span>
        <el-button class="button" text @click="outerVisible = true">
          Edit
        </el-button>
        <el-dialog
            v-model.lazy="outerVisible"
            title="Edit Your Profile"
            style="border-radius: 5%"
            width="30%"
            align-center
        >
          <el-form>
            <el-form-item label="Nickname" :label-width="formLabelWidth">
              <el-input id="nickname" autocomplete="off" placeholder="Enter New Nickname"/>
            </el-form-item>
            <el-form-item label="Bio" :label-width="formLabelWidth">
              <el-input id="bio" autocomplete="off" placeholder="Enter your bio"/>
            </el-form-item>
            <el-form-item label="Password" :label-width="formLabelWidth">
              <el-button class="el-button--danger" @click="innerVisible = true">
                Edit Password
              </el-button>
            </el-form-item>

            <el-dialog
              v-model.lazy="innerVisible"
              title="Edit Password"
              style="border-radius: 5%"
              width="40%"
              append-to-body
              align-center
            >
              <el-form-item label="Old Password" :label-width="formLabelWidth">
                <el-input v-model.lazy="password0" autocomplete="off" placeholder="Enter Old Password" show-password="false"/>
              </el-form-item>
              <el-form-item label="New Password" :label-width="formLabelWidth">
                <el-input v-model.lazy="password1" autocomplete="off" placeholder="Enter New Password" show-password="false"/>
              </el-form-item>
              <el-form-item label="Confirm" :label-width="formLabelWidth">
                <el-input v-model.lazy="password2" autocomplete="off" placeholder="Enter New Password Again" show-password="false"/>
              </el-form-item>
              <template #footer>
                <span class="dialog-footer">
                  <el-button @click="innerVisible = false">
                    Cancel
                  </el-button>
                  <el-button type="primary" @click="innerVisible = false; changePWD = true">
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
              <el-button type="primary" @click="confirmChanges()">
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
        {{userInfo.nickname}}
      </el-descriptions-item>
      <el-descriptions-item>
        <template #label>
          <div class="cell-item">
            <el-icon><Message /></el-icon>
            Register Email
          </div>
        </template>
        {{userInfo.email}}
      </el-descriptions-item>
      <el-descriptions-item v-if="userInfo.bio !== ''">
        <template #label>
          <div class="cell-item">
            <el-icon><ChatDotRound /></el-icon>
            Bio
          </div>
        </template>
        {{userInfo.bio}}
      </el-descriptions-item>
      <el-descriptions-item v-else>
        <template #label>
          <div class="cell-item">
            <el-icon><ChatDotRound /></el-icon>
            Bio
          </div>
        </template>
        A music lover......
      </el-descriptions-item>
    </el-descriptions>
  </el-card>
</template>

<script>
import axios from "axios";

export default {
  name: 'SettingCard',
  data() {
    return {
      outerVisible: false,
      innerVisible: false,
      formLabelWidth: '160px',
      userInfo: {
        email: this.$store.state.userInfo.email,
        nickname: this.$store.state.userInfo.username,
        useravatar: this.$store.state.userInfo.avatar,
        type: this.$store.state.userInfo.usertype,
        bio: this.$store.state.userInfo.profile
      },
      showUserInfo: this.userInfo,
      password0: '',
      password1: '',
      password2: '',
      changePWD: false,
      loading: true
    }
  },
  mounted() {
    this.getSettingInfo()
  },
  methods: {
    getSettingInfo: function () {
      let that = this
      that.loading = true
      axios.request({
        url: "/api/get_user_info/",     // TODO
        method: 'get'
      })
          .then(function (response) {
            console.log(response.data)
            console.log('imhere_1')
            that.loading = false
            that.userInfo = response.data,
            that.showUserInfo = response.data
            console.log('imhere_2')
            this.$store.state.userInfo.nickname = this.userInfo.nickname
            console.log('imhere_3')
            this.$store.state.userInfo.password = this.userInfo.password
            console.log('imhere_4')
          }).catch(function (error) {
        console.log(error)
        that.loading = false
      })
    },
    confirmChanges: function () {
      let newNickname;
      let newPWD;
      let that = this;
      newNickname = document.getElementById('nickname').value;
      newPWD = this.$store.state.userInfo.password;
      if (that.changePWD === true) {
        if (that.password0 === '' || that.password1 === '' || that.password2 === '') {
          that.$message.error("Please refill all the blocks!");
        } else {
          if (that.password1 !== that.password2) {
            that.$message.error("The new password are different!");
          } else if (that.password0 !== this.$store.state.userInfo.password) {
            that.$message.error("Wrong origin password!");
          } else {
            newPWD = that.password1;
          }
        }
      }
      axios.request({
        method: 'post',
        url: "/api/set_user_info/",    // TODO
        data: JSON.stringify({
          nickname: newNickname,
          password: newPWD
        })
      }).then(res => {
        console.log(res.data)
        if (res.data.errno === 0) {
          this.$message({
            message: "Successfully edit your profile!",
            type: 'success',
            showClose: true
          })
        } else {
          this.$message({
            message: "Fail to edit your profile.",
            type: 'error',
            showClose: true
          })
        }
        that.changePWD = false;
        that.outerVisible = false;
        location.reload();
      }).catch(err => {
        console.log(err)
      })
    }
  }
}

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