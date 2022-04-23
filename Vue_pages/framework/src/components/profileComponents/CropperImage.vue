<template>
  <div class="cropper-content">
    <div class="cropper-box">
      <div class="cropper">
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
      <!--底部操作工具按钮-->
<!--      <div class="footer-btn">-->
<!--        <div class="scope-btn">-->
<!--          <label class="btn" for="uploads">选择封面</label>-->
<!--          <input type="file" id="uploads" style="position:absolute; clip:rect(0 0 0 0);" accept="image/png, image/jpeg, image/gif, image/jpg" @change="selectImg($event)">-->
<!--          <button size="mini" type="danger" plain icon="el-icon-zoom-in" @click="changeScale(1)">放大</button>-->
<!--          <button size="mini" type="danger" plain icon="el-icon-zoom-out" @click="changeScale(-1)">缩小</button>-->
<!--          <button size="mini" type="danger" plain @click="rotateLeft">↺ 左旋转</button>-->
<!--          <button size="mini" type="danger" plain @click="rotateRight">↻ 右旋转</button>-->
<!--        </div>-->
<!--        <div class="upload-btn">-->
<!--          <button size="mini" type="success" @click="uploadImg('blob')">上传封面 <i class="el-icon-upload"></i></button>-->
<!--        </div>-->
<!--      </div>-->
    </div>
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
    realTime (data) {
      this.previews = data
    },
  }
}
</script>

<style scoped>
.cropper-content{
  height: 300px;
  width: 200px;
}
</style>