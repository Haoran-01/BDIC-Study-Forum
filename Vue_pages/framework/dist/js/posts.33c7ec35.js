"use strict";(self["webpackChunkframework"]=self["webpackChunkframework"]||[]).push([[287],{3156:function(t,s,i){i.r(s),i.d(s,{default:function(){return h}});var e=i(6252);const n={key:0,class:"postList"};function a(t,s,i,a,o,r){const p=(0,e.up)("post-entrance");return o.postVisibility?((0,e.wg)(),(0,e.iD)("div",n,[((0,e.wg)(!0),(0,e.iD)(e.HY,null,(0,e.Ko)(o.postData,((t,s)=>((0,e.wg)(),(0,e.iD)("div",{class:"postListLogic",key:s},[(0,e.Wm)(p,(0,e.dG)({item:t,index:s},{width:998,onSendShareInfo:r.handleShare}),null,16,["onSendShareInfo"])])))),128))])):(0,e.kq)("",!0)}var o=i(9669),r=i.n(o),p=i(928),c=i(3002),l=(i(343),{setup(){const t=(0,c.pm)();return{tip:t}},name:"MyPost",components:{PostEntrance:p.Z},data(){return{postData:{},postVisibility:!1}},methods:{handleShare(){this.tip.info("Link Copied Successfully")}},created(){r().get("http://127.0.0.1:4523/mock/831624/profile/my_post",{email:this.$route.params.email}).then((t=>{const s=t.status;200===s?(this.postData=t.data.data,this.postVisibility=!0):201===s&&(this.postVisibility=!1)}))}}),u=i(3744);const d=(0,u.Z)(l,[["render",a]]);var h=d}}]);
//# sourceMappingURL=posts.33c7ec35.js.map