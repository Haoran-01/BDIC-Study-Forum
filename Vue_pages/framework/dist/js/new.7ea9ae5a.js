"use strict";(self["webpackChunkframework"]=self["webpackChunkframework"]||[]).push([[536],{93:function(t,e,n){n.r(e),n.d(e,{default:function(){return h}});var s=n(6252);function o(t,e,n,o,a,r){const i=(0,s.up)("post-entrance");return(0,s.wg)(!0),(0,s.iD)(s.HY,null,(0,s.Ko)(a.postData,((t,e)=>((0,s.wg)(),(0,s.iD)("div",{class:"postListLogic",key:e},[(0,s.Wm)(i,(0,s.dG)({item:t,index:e},{width:1e3,onSendShareInfo:r.handleShare}),null,16,["onSendShareInfo"])])))),128)}var a=n(9669),r=n.n(a),i=n(8938),u=n(3002),c=(n(343),{setup(){const t=(0,u.pm)();return{tip:t}},name:"NewPosts",components:{PostEntrance:i.Z},data(){return{section:"",postData:{}}},methods:{handleShare(){this.tip.info("Link Copied Successfully")}},created(){r().get("/forum/section/get_new_posts",{params:{type_name:this.$route.query.typeName}}).then((t=>{const e=t.status;200===e?(this.postData=t.data.data,this.postVisibility=!0):201===e&&(this.postVisibility=!1)}))},beforeRouteEnter(t,e,n){n((t=>{t.section=t.$store.state.currentSection}))}}),p=n(3744);const d=(0,p.Z)(c,[["render",o]]);var h=d}}]);
//# sourceMappingURL=new.7ea9ae5a.js.map