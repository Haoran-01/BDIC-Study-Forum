<template>
  <div class="show-info">
    <h3>Edit avatar</h3>
    <div class="cropper-content">
      <vueCropper
          ref="cropper"
          :img="option.img"
          :outputSize="option.outputSize"
          :outputType="option.outputType"
          :info="option.info"
          :canScale="option.canScale"
          :autoCrop="option.autoCrop"
          :autoCropWidth="option.autoCropWidth"
          :autoCropHeight="option.autoCropHeight"
          :fixed="option.fixed"
          :fixedNumber="option.fixedNumber"
          :full="option.full"
          :fixedBox="option.fixedBox"
          :canMove="option.canMove"
          :canMoveBox="option.canMoveBox"
          :original="option.original"
          :centerBox="option.centerBox"
          :height="option.height"
          :infoTrue="option.infoTrue"
          :maxImgSize="option.maxImgSize"
          :enlarge="option.enlarge"
          :mode="option.mode"
          @realTime="realTime"
          @imgLoad="imgLoad">
      </vueCropper>
    </div>
    <div class="test-button">
      <label class="btn" for="uploads">upload</label>
      <input type="file" id="uploads" style="position:absolute; clip:rect(0 0 0 0);" accept="image/png, image/jpeg, image/gif, image/jpg" @change="selectImg($event)">
      <button @click="changeScale(1)" class="btn-1" id="first">+</button>
      <button @click="changeScale(-1)" class="btn-1">-</button>
      <button @click="rotateLeft" class="btn-2">rotateLeft</button>
      <button @click="rotateRight" class="btn-2">rotateRight</button>
      <div class="upload-btn">
        <button @click="uploadImg('blob')" class="Submit">Submit</button>
      </div>
    </div>


    <h3>Preview</h3>
    <!--预览效果图-->
    <div class="show-preview">
      <div :style="previews.div" class="preview">
        <img :src="previews.url" :style="previews.img">
      </div>
    </div>
  </div>
</template>


<script>
import 'vue-cropper/dist/index.css'
import { VueCropper }  from "vue-cropper";
import axios from "axios";

export default {
  name: "CropperImage",
  components: {VueCropper},

  data() {
    return {
      name:this.Name,
      previews: {},
      option:{
        img: '',             //裁剪图片的地址
        outputSize: 1,       //裁剪生成图片的质量(可选0.1 - 1)
        outputType: 'jpeg',  //裁剪生成图片的格式（jpeg || png || webp）
        info: true,          //图片大小信息
        canScale: true,      //图片是否允许滚轮缩放
        autoCrop: true,      //是否默认生成截图框
        autoCropWidth: 230,  //默认生成截图框宽度
        autoCropHeight: 150, //默认生成截图框高度
        fixed: true,         //是否开启截图框宽高固定比例
        fixedNumber: [1.53, 1], //截图框的宽高比例
        full: false,         //false按原比例裁切图片，不失真
        fixedBox: true,      //固定截图框大小，不允许改变
        canMove: false,      //上传图片是否可以移动
        canMoveBox: true,    //截图框能否拖动
        original: false,     //上传图片按照原始比例渲染
        centerBox: false,    //截图框是否被限制在图片里面
        height: true,        //是否按照设备的dpr 输出等比例图片
        infoTrue: false,     //true为展示真实输出图片宽高，false展示看到的截图框宽高
        maxImgSize: 3000,    //限制图片最大宽度和高度
        enlarge: 1,          //图片根据截图框输出比例倍数
        mode: '230px 150px'  //图片默认渲染方式
      }
    };
  },
  methods: {
    imgLoad (msg) {
      console.log("工具初始化函数====="+msg)
    },
    //图片缩放
    changeScale (num) {
      num = num || 1
      this.$refs.cropper.changeScale(num)
    },
    //向左旋转
    rotateLeft () {
      this.$refs.cropper.rotateLeft()
    },
    //向右旋转
    rotateRight () {
      this.$refs.cropper.rotateRight()
    },
    //实时预览函数
    realTime (data) {
      this.previews = data
    },
    selectImg (e) {
      let file = e.target.files[0]
      if (!/\.(jpg|jpeg|png|JPG|PNG)$/.test(e.target.value)) {
        return false
      }
      //转化为blob
      let reader = new FileReader()
      reader.onload = (e) => {
        let data
        if (typeof e.target.result === 'object') {
          data = window.URL.createObjectURL(new Blob([e.target.result]))
        } else {
          data = e.target.result
        }
        this.option.img = data
      }
      //转化为base64
      reader.readAsDataURL(file)
    },
    //上传图片
    uploadImg (type) {
      let _this = this;
      if (type === 'blob') {
        //获取截图的blob数据
        this.$refs.cropper.getCropBlob(async (data) => {
          let formData = new FormData();
          formData.append('file',data,"DX.jpg")
          //调用axios上传

          let {data: res} = await axios.post("http://127.0.0.1:4523/mock/831624/profile/post_photo", formData)
          // let {data: res} = await _this.$http.post('/api/file/imgUpload', formData)

          //await表示暂停运行，指代码运行到这里就停止了，等待await后面的操作运行完再运行
          if(res.code === 200){
            let data = res.data.replace('[','').replace(']','').split(',');
            let imgInfo = {
              name : _this.Name,
              url : data[0]
            };
            _this.$emit('uploadImgSuccess',imgInfo);
          }
        })
      }
    },
  }
}
</script>

<style scoped>
.cropper-content{
  height: 300px;
  width: 450px;
  justify-content: center;
}
.show-preview{
  flex: 1;
  -webkit-flex: 1;
  display: flex;
  display: -webkit-flex;
  justify-content: center;

}

.preview{
  overflow: hidden;
  border:1px solid #67c23a;
  background: #cccccc;
}



.preview img{
  display: block;
}

button{
  font-weight: bold;
  width: 100px;
  height: 25px;
  border-radius: 4px;
  border: 1px solid rgba(0, 0, 0, 0.2);
  cursor: pointer;
  margin: 15px;
  background-color: #FFFFFF;

}

#first{
  margin-left: 30px;
}

.btn-1{
  transition: 0.5s ease-out;
  width: 25px;
}

.btn-1:hover{
  background-color: #35c703;
  color: #FFFFFF;
  border-style: none;
}

.btn-2{
  transition: 0.5s ease-out;
}

.btn-2:hover{
  background-color: #35c703;
  color: #FFFFFF;
  border-style: none;
}

.Submit{
  transition: 0.5s ease-in;
  margin: 0;
}

.Submit:hover{
  background-color: #00B8FF;
  color: #FFFFFF;
  border-style: none;
}

.btn{
  padding: 5px 5px;
  cursor: pointer;
  border: 1px solid rgba(0, 0, 0, 0.1);
  border-radius: 100px;
}

.btn:hover{
  background-color: #b47a7a;
  color: #FFFFFF;
}


</style>
