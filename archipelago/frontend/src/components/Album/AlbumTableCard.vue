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
        <el-dialog v-model="dialogFormVisible" title="Add New Album">
          <el-form>
            <el-form-item label="Album Name" :label-width="formLabelWidth">
              <el-input id="albumName" autocomplete="off" />
            </el-form-item>

            <el-form-item label="Price" :label-width="formLabelWidth">
              <el-input id="price" autocomplete="off" />
            </el-form-item>

            <el-form-item label="Author" :label-width="formLabelWidth">
              <el-input id="author" autocomplete="off" />
            </el-form-item>

            <el-form-item label="Releaser" :label-width="formLabelWidth">
              <el-input id="releaser" autocomplete="off" />
            </el-form-item>

            <el-form-item label="Release Year" :label-width="formLabelWidth">
              <el-date-picker
                  id="releaseYear"
                  curType="year"
                  placeholder="Pick a year"
              />
            </el-form-item>

            <el-form-item label="Album Cover" :label-width="formLabelWidth">
              <el-input id="cover" autocomplete="off" />
            </el-form-item>

            <el-form-item label="Album Type" :label-width="formLabelWidth">
              <el-select  placeholder="Choose 1 Type" style="width: 77.9%" id="type">
                <el-option v-for="item in albumType" :key="item.label" :label="item.value" :value="item.value">
                  <span>{{ item.value }}</span>
                </el-option>
              </el-select>
            </el-form-item>

            <el-form-item label="Resource Link" :label-width="formLabelWidth">
              <el-input v-model.lazy="curResource" autocomplete="off" />
            </el-form-item>

          </el-form>
          <template #footer>
      <span class="dialog-footer">
        <el-button @click="dialogFormVisible = false">Cancel</el-button>
        <el-button curType="primary" @click="confirmInfo()"
        >Confirm</el-button
        >
      </span>
          </template>
        </el-dialog>
      </div>
    </template>

    <el-table :data="this.showAlbumList" style="width: 100%" v-loading="loading">
      <el-table-column prop="albumName" label="Album Name" width="150" />
      <el-table-column prop="price" label="Price" width="150" />
      <el-table-column prop="author" label="Author" width="150" />
      <el-table-column prop="releaser" label="Releaser" width="150" />
      <el-table-column prop="releaseYear" label="Release Year" width="150" />
      <el-table-column prop="type" label="Type" width="150" />
      <el-table-column prop="resource" label="Resource" />
    </el-table>
  </el-card>
</template>

<script>
import axios from "axios";
import qs from "qs";
axios.defaults.withCredentials = true;
export default {
  name: 'AlbumTableCard',
  data() {
    return {
      dialogFormVisible: false,
      formLabelWidth: '140px',
      loading: true,
      albumList: [{
        albumName: '',
        price: '',
        author: '',
        releaser: '',
        releaseYear: '',
        type: '',
        resource: ''
      }],
      showAlbumList: this.albumList,
      albumType: [
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
    }
  },
  mounted() {
    this.getAlbumList()
  },
  methods: {
    getAlbumList: function () {
      let that = this
      that.loading = true
      axios.request({
        url: "",     // TODO
        method: 'get'
      })
          .then(function (response) {
            console.log(response.data)
            that.loading = false
            that.albumList = response.data
            that.showAlbumList = response.data
          }).catch(function (error) {
            console.log(error)
            that.loading = false
      })
    },

    confirmInfo: function () {
      let newAlbumData;
      let that = this;
      newAlbumData = {
        albumName: document.getElementById('albumName').value,
        price: document.getElementById('price').value,
        author: document.getElementById('author').value,
        releaser: document.getElementById('releaser').value,
        releaseYear: document.getElementById('releaseYear').value,
        cover: document.getElementById('cover').value,
        type: document.getElementById('type').value,
        resource: document.getElementById('resource').value
      };
      axios({
        method: 'post',
        url: "",     // TODO
        data: JSON.stringify(newAlbumData)
      })
          .then(res => {
            console.log(res.data)
            if (res.data.errno === 0) {
              this.$message({
                message: "Successfully upload a album!",
                type: 'success',
                showClose: true
              })
            } else {
                this.$message({
                  message: "Fail to upload this album.",
                  type: 'error',
                  showClose: true
                })
            }
            that.dialogFormVisible = false;
            location.reload();
          })
          .catch(err => {
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
