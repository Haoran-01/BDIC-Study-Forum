"use strict";(self["webpackChunkframework"]=self["webpackChunkframework"]||[]).push([[287],{2840:function(t,e,s){s.r(e),s.d(e,{default:function(){return k}});var a=s(6252);const i=t=>((0,a.dD)("data-v-3a06c684"),t=t(),(0,a.Cn)(),t),o={key:0,class:"postList"},n={key:1,class:"createPostTip"},r=i((()=>(0,a._)("div",{class:"createPostSlogan"},"Glad to see your interaction!",-1))),c=i((()=>(0,a._)("div",{class:"createPostButtonText"},"Create Post",-1)));function l(t,e,s,i,l,d){const u=(0,a.up)("post-entrance"),p=(0,a.up)("router-link");return l.postVisibility?((0,a.wg)(),(0,a.iD)("div",o,[((0,a.wg)(!0),(0,a.iD)(a.HY,null,(0,a.Ko)(l.postData,((t,e)=>((0,a.wg)(),(0,a.iD)("div",{class:"postListLogic",key:e},[(0,a.Wm)(u,(0,a.dG)({item:t,index:e},{width:998,onSendShareInfo:d.handleShare}),null,16,["onSendShareInfo"])])))),128))])):((0,a.wg)(),(0,a.iD)("div",n,[r,(0,a.Wm)(p,{class:"createPostButton",to:"/create_post"},{default:(0,a.w5)((()=>[c])),_:1})]))}var d=s(9669),u=s.n(d),p=s(5100),h=s(3002),f=(s(343),{setup(){const t=(0,h.pm)();return{tip:t}},name:"MyPost",components:{PostEntrance:p.Z},data(){return{postData:{},postVisibility:!1}},methods:{handleShare(){this.tip.info("Link Copied Successfully")}},created(){u().get("/profile/my_post",{email:this.$route.query.email}).then((t=>{const e=t.status;200===e?(this.postData=t.data.data,this.postVisibility=!0):201===e&&(this.postVisibility=!1)}))}}),m=s(3744);const y=(0,m.Z)(f,[["render",l],["__scopeId","data-v-3a06c684"]]);var k=y}}]);
//# sourceMappingURL=posts.a1ee0022.js.map