"use strict";(self["webpackChunkframework"]=self["webpackChunkframework"]||[]).push([[845],{3136:function(t,e,i){i.r(e),i.d(e,{default:function(){return Le}});var a=i(6252);function o(t,e,i,o,n,s){const r=(0,a.up)("FrameWorkProfile");return(0,a.wg)(),(0,a.j4)(r)}const n={class:"Identify"},s={class:"contentFrame"},r={class:"navigator"},l={class:"nav"},d={class:"choice"},m=(0,a.Uk)("My posts"),c={class:"choice"},u=(0,a.Uk)("My favourite"),p={class:"content"};function h(t,e,i,o,h,g){const f=(0,a.up)("IdentificationCard"),_=(0,a.up)("router-link"),v=(0,a.up)("router-view");return(0,a.wg)(),(0,a.iD)(a.HY,null,[(0,a._)("div",n,[(0,a.Wm)(f)]),(0,a._)("div",s,[(0,a._)("div",r,[(0,a._)("nav",l,[(0,a._)("div",d,[(0,a.Wm)(_,{to:{path:"/profile/posts",query:{email:this.email}}},{default:(0,a.w5)((()=>[m])),_:1},8,["to"])]),(0,a._)("div",c,[(0,a.Wm)(_,{to:{path:"/profile/favourite",query:{email:this.email}}},{default:(0,a.w5)((()=>[u])),_:1},8,["to"])])])]),(0,a._)("div",p,[(0,a.Wm)(v)])])],64)}var g=i(3577),f=i(9963);const _=t=>((0,a.dD)("data-v-75c796b6"),t=t(),(0,a.Cn)(),t),v=_((()=>(0,a._)("div",{class:"rightBar"},null,-1))),b={class:"informationArea"},C={class:"pictureUpload"},w=["src"],S={key:0,class:"Otherselfie"},E={key:1,class:"selfie"},I={class:"directionBar"},y={class:"part1"};function U(t,e,i,o,n,s){const r=(0,a.up)("CropperImage"),l=(0,a.up)("n-modal"),d=(0,a.up)("InforCollection"),m=(0,a.up)("InforCollectionSpan");return(0,a.wg)(),(0,a.iD)("div",{class:(0,g.C_)([n.animate,"Frame"])},[v,(0,a._)("div",b,[(0,a._)("div",C,[(0,a._)("img",{class:"Heading",src:this.profile_url},null,8,w),(0,a.wy)((0,a._)("button",{type:"button",class:"changeButton",onClick:e[0]||(e[0]=t=>n.showModal=!0)}," Avatar ",512),[[f.F8,n.IsHost]]),(0,a.Wm)(l,{show:n.showModal,"onUpdate:show":e[1]||(e[1]=t=>n.showModal=t),class:"modal","transform-origin":"center"},{default:(0,a.w5)((()=>[(0,a._)("div",null,[(0,a.Wm)(r)])])),_:1},8,["show"])]),n.IsHost?((0,a.wg)(),(0,a.iD)("div",E,[(0,a.Wm)(f.uT,null,{default:(0,a.w5)((()=>[(0,a.wy)((0,a.Wm)(m,null,null,512),[[f.F8,n.animate.frameSpan]])])),_:1}),(0,a.Wm)(f.uT,null,{default:(0,a.w5)((()=>[(0,a.wy)((0,a.Wm)(d,null,null,512),[[f.F8,n.animate.frame]])])),_:1})])):((0,a.wg)(),(0,a.iD)("div",S,[(0,a.Wm)(d)]))]),(0,a.wy)((0,a._)("div",I,[(0,a._)("div",y,[(0,a._)("button",{class:(0,g.C_)([n.animateButton,"SpanButton"]),onClick:e[2]||(e[2]=(...t)=>s.HandleClick&&s.HandleClick(...t))},null,2)])],512),[[f.F8,n.IsHost]])],2)}const k=t=>((0,a.dD)("data-v-0c05ba10"),t=t(),(0,a.Cn)(),t),A={class:"Shorten"},B={class:"header"},M={class:"Username"},F=k((()=>(0,a._)("div",{class:"title"},"Introduction",-1))),x=k((()=>(0,a._)("div",{class:"line"},null,-1))),D={class:"content"},j={class:"e-mail contentText"},W=k((()=>(0,a._)("span",null,"E-mail:",-1)));function R(t,e,i,o,n,s){return(0,a.wg)(),(0,a.iD)("div",A,[(0,a._)("div",B,[(0,a._)("div",M,(0,g.zw)(n.currentName),1),F,x]),(0,a._)("div",D,[(0,a._)("div",j,[W,(0,a._)("span",null,(0,g.zw)(n.currentEmail),1)])])])}var N=i(9669),T=i.n(N),z={name:"InforCollection",data(){return{currentEmail:"",currentName:""}},created(){this.currentEmail=this.$route.query.email,T().get("/get_profile",{params:{user_email:this.currentEmail}}).then((t=>{this.currentName=t.data.user_name})).catch((function(t){console.log(t)}))}},G=i(3744);const H=(0,G.Z)(z,[["render",R],["__scopeId","data-v-0c05ba10"]]);var L=H;const Z=t=>((0,a.dD)("data-v-b4ebb644"),t=t(),(0,a.Cn)(),t),K={class:"Span"},P={class:"header"},V=Z((()=>(0,a._)("div",{class:"title"},"Introduction",-1))),q=Z((()=>(0,a._)("div",{class:"line"},null,-1))),X={class:"content"},J=Z((()=>(0,a._)("div",{class:"Ti contentText"},"E-mail",-1))),O=Z((()=>(0,a._)("div",{class:"line"},null,-1))),Q={class:"e-mail contentText"},Y=Z((()=>(0,a._)("div",{class:"Ti contentText"},"Grade",-1))),$=Z((()=>(0,a._)("div",{class:"line"},null,-1))),tt=Z((()=>(0,a._)("div",{class:"Ti contentText"},"Department",-1))),et=Z((()=>(0,a._)("div",{class:"line"},null,-1))),it=Z((()=>(0,a._)("div",{class:"Ti contentText"},"Major",-1))),at=Z((()=>(0,a._)("div",{class:"line"},null,-1)));function ot(t,e,i,o,n,s){const r=(0,a.up)("UsernameForm"),l=(0,a.up)("IntroForm"),d=(0,a.up)("GradeForm"),m=(0,a.up)("DepartmentForm"),c=(0,a.up)("MajorForm");return(0,a.wg)(),(0,a.iD)("div",K,[(0,a._)("div",P,[(0,a.Wm)(r,{"infor-msg":n.Username,EditName:"Edit your user name",onSubmitUsername:s.handleUsername},null,8,["infor-msg","onSubmitUsername"]),V,q]),(0,a._)("div",X,[(0,a.Wm)(l,{"infor-msg":n.Intro,EditName:"Add your personalities",onSubmitIntro:s.handleIntro},null,8,["infor-msg","onSubmitIntro"]),J,O,(0,a._)("div",Q,(0,g.zw)(n.UserEmail),1),Y,$,(0,a.Wm)(d,{"infor-msg":n.Grade,EditName:"Edit your grade",onSubmitGrade:s.handleGrade},null,8,["infor-msg","onSubmitGrade"]),tt,et,(0,a.Wm)(m,{"infor-msg":n.Department,EditName:"Edit your department",onSubmitDepartment:s.handleDepartment},null,8,["infor-msg","onSubmitDepartment"]),it,at,(0,a.Wm)(c,{"infor-msg":n.Major,EditName:"Edit your major",onSubmitMajor:s.handleMajor},null,8,["infor-msg","onSubmitMajor"])])])}var nt=i(4554);const st=t=>((0,a.dD)("data-v-9646dd6e"),t=t(),(0,a.Cn)(),t),rt={class:"Field-Content"},lt={class:"UserContent"},dt=st((()=>(0,a._)("span",{class:"imgShow"},[(0,a._)("img",{src:nt})],-1))),mt={class:"Input"},ct={class:"InputArea"},ut={class:"ButtonArea"};function pt(t,e,i,o,n,s){return(0,a.wg)(),(0,a.iD)("form",{class:"Field",onSubmit:e[4]||(e[4]=(0,f.iM)((()=>{}),["prevent"]))},[(0,a._)("div",rt,[(0,a.wy)((0,a._)("div",lt,[(0,a._)("div",null,(0,g.zw)(i.inforMsg),1),(0,a._)("button",{type:"button",class:"ButtonEdit",onClick:e[0]||(e[0]=(...t)=>s.edit&&s.edit(...t))},[dt,(0,a.Uk)(" "+(0,g.zw)(i.EditName),1)])],512),[[f.F8,n.flag]]),(0,a.wy)((0,a._)("div",mt,[(0,a._)("div",ct,[(0,a.wy)((0,a._)("input",{id:"UserInput",type:"text","onUpdate:modelValue":e[1]||(e[1]=t=>n.Submit=t)},null,512),[[f.nr,n.Submit]])]),(0,a._)("div",ut,[(0,a._)("button",{type:"submit",class:"ButtonChoice",onClick:e[2]||(e[2]=(...t)=>s.submitContent&&s.submitContent(...t))},"Save"),(0,a._)("button",{type:"button",class:"ButtonChoice",onClick:e[3]||(e[3]=(...t)=>s.edit&&s.edit(...t))},"Back")])],512),[[f.F8,n.flagEdit]])])],32)}var ht={name:"UsernameForm",props:["EditName","inforMsg"],emits:["SubmitUsername"],data(){return{flag:!0,flagEdit:!1,Submit:""}},methods:{edit(){this.flag=!this.flag,this.flagEdit=!this.flagEdit},submitContent(){this.$emit("SubmitUsername",this.Submit),this.flag=!this.flag,this.flagEdit=!this.flagEdit}}};const gt=(0,G.Z)(ht,[["render",pt],["__scopeId","data-v-9646dd6e"]]);var ft=gt;const _t=t=>((0,a.dD)("data-v-2c2bc983"),t=t(),(0,a.Cn)(),t),vt={class:"Field-Content"},bt={class:"UserContent"},Ct={id:"infor"},wt=_t((()=>(0,a._)("span",{class:"imgShow"},[(0,a._)("img",{src:nt})],-1))),St={class:"Input"},Et={class:"InputArea"},It={class:"ButtonArea"};function yt(t,e,i,o,n,s){return(0,a.wg)(),(0,a.iD)("form",{class:"Field",onSubmit:e[4]||(e[4]=(0,f.iM)((()=>{}),["prevent"]))},[(0,a._)("div",vt,[(0,a.wy)((0,a._)("div",bt,[(0,a._)("div",Ct,(0,g.zw)(i.inforMsg),1),(0,a._)("button",{type:"button",class:"ButtonEdit",onClick:e[0]||(e[0]=(...t)=>s.edit&&s.edit(...t))},[wt,(0,a.Uk)(" "+(0,g.zw)(i.EditName),1)])],512),[[f.F8,n.flag]]),(0,a.wy)((0,a._)("div",St,[(0,a._)("div",Et,[(0,a.wy)((0,a._)("input",{id:"UserInput",type:"text","onUpdate:modelValue":e[1]||(e[1]=t=>n.Submit=t)},null,512),[[f.nr,n.Submit]])]),(0,a._)("div",It,[(0,a._)("button",{type:"submit",class:"ButtonChoice",onClick:e[2]||(e[2]=(...t)=>s.submitContent&&s.submitContent(...t))},"Save"),(0,a._)("button",{type:"button",class:"ButtonChoice",onClick:e[3]||(e[3]=(...t)=>s.edit&&s.edit(...t))},"Back")])],512),[[f.F8,n.flagEdit]])])],32)}var Ut={name:"IntroForm",props:["EditName","inforMsg"],emits:["SubmitIntro"],data(){return{flag:!0,flagEdit:!1,Submit:""}},methods:{edit(){this.flag=!this.flag,this.flagEdit=!this.flagEdit},submitContent(){this.$emit("SubmitIntro",this.Submit),this.flag=!this.flag,this.flagEdit=!this.flagEdit}}};const kt=(0,G.Z)(Ut,[["render",yt],["__scopeId","data-v-2c2bc983"]]);var At=kt;const Bt=t=>((0,a.dD)("data-v-638a0f8a"),t=t(),(0,a.Cn)(),t),Mt={class:"Field-Content"},Ft={class:"UserContent"},xt={id:"infor"},Dt=Bt((()=>(0,a._)("span",{class:"imgShow"},[(0,a._)("img",{src:nt})],-1))),jt={class:"Input"},Wt={class:"InputArea"},Rt={class:"ButtonArea"};function Nt(t,e,i,o,n,s){return(0,a.wg)(),(0,a.iD)("form",{class:"Field",onSubmit:e[4]||(e[4]=(0,f.iM)((()=>{}),["prevent"]))},[(0,a._)("div",Mt,[(0,a.wy)((0,a._)("div",Ft,[(0,a._)("div",xt,(0,g.zw)(i.inforMsg),1),(0,a._)("button",{type:"button",class:"ButtonEdit",onClick:e[0]||(e[0]=(...t)=>s.edit&&s.edit(...t))},[Dt,(0,a.Uk)(" "+(0,g.zw)(i.EditName),1)])],512),[[f.F8,n.flag]]),(0,a.wy)((0,a._)("div",jt,[(0,a._)("div",Wt,[(0,a.wy)((0,a._)("input",{id:"UserInput",type:"text","onUpdate:modelValue":e[1]||(e[1]=t=>n.Submit=t)},null,512),[[f.nr,n.Submit]])]),(0,a._)("div",Rt,[(0,a._)("button",{type:"submit",class:"ButtonChoice",onClick:e[2]||(e[2]=(...t)=>s.submitContent&&s.submitContent(...t))},"Save"),(0,a._)("button",{type:"button",class:"ButtonChoice",onClick:e[3]||(e[3]=(...t)=>s.edit&&s.edit(...t))},"Back")])],512),[[f.F8,n.flagEdit]])])],32)}var Tt={name:"GradeForm",props:["EditName","inforMsg"],emits:["SubmitGrade"],data(){return{flag:!0,flagEdit:!1,Submit:""}},methods:{edit(){this.flag=!this.flag,this.flagEdit=!this.flagEdit},submitContent(){this.$emit("SubmitGrade",this.Submit),this.flag=!this.flag,this.flagEdit=!this.flagEdit}}};const zt=(0,G.Z)(Tt,[["render",Nt],["__scopeId","data-v-638a0f8a"]]);var Gt=zt;const Ht=t=>((0,a.dD)("data-v-4e4bee22"),t=t(),(0,a.Cn)(),t),Lt={class:"Field-Content"},Zt={class:"UserContent"},Kt={id:"infor"},Pt=Ht((()=>(0,a._)("span",{class:"imgShow"},[(0,a._)("img",{src:nt})],-1))),Vt={class:"Input"},qt={class:"InputArea"},Xt={class:"ButtonArea"};function Jt(t,e,i,o,n,s){return(0,a.wg)(),(0,a.iD)("form",{class:"Field",onSubmit:e[4]||(e[4]=(0,f.iM)((()=>{}),["prevent"]))},[(0,a._)("div",Lt,[(0,a.wy)((0,a._)("div",Zt,[(0,a._)("div",Kt,(0,g.zw)(i.inforMsg),1),(0,a._)("button",{type:"button",class:"ButtonEdit",onClick:e[0]||(e[0]=(...t)=>s.edit&&s.edit(...t))},[Pt,(0,a.Uk)(" "+(0,g.zw)(i.EditName),1)])],512),[[f.F8,n.flag]]),(0,a.wy)((0,a._)("div",Vt,[(0,a._)("div",qt,[(0,a.wy)((0,a._)("input",{id:"UserInput",type:"text","onUpdate:modelValue":e[1]||(e[1]=t=>n.Submit=t)},null,512),[[f.nr,n.Submit]])]),(0,a._)("div",Xt,[(0,a._)("button",{type:"submit",class:"ButtonChoice",onClick:e[2]||(e[2]=(...t)=>s.submitContent&&s.submitContent(...t))},"Save"),(0,a._)("button",{type:"button",class:"ButtonChoice",onClick:e[3]||(e[3]=(...t)=>s.edit&&s.edit(...t))},"Back")])],512),[[f.F8,n.flagEdit]])])],32)}var Ot={name:"DepartmentForm",props:["EditName","inforMsg"],emits:["SubmitDepartment"],data(){return{flag:!0,flagEdit:!1,Submit:""}},methods:{edit(){this.flag=!this.flag,this.flagEdit=!this.flagEdit},submitContent(){this.$emit("SubmitDepartment",this.Submit),this.flag=!this.flag,this.flagEdit=!this.flagEdit}}};const Qt=(0,G.Z)(Ot,[["render",Jt],["__scopeId","data-v-4e4bee22"]]);var Yt=Qt;const $t=t=>((0,a.dD)("data-v-2d449012"),t=t(),(0,a.Cn)(),t),te={class:"Field-Content"},ee={class:"UserContent"},ie={id:"infor"},ae=$t((()=>(0,a._)("span",{class:"imgShow"},[(0,a._)("img",{src:nt})],-1))),oe={class:"Input"},ne={class:"InputArea"},se={class:"ButtonArea"};function re(t,e,i,o,n,s){return(0,a.wg)(),(0,a.iD)("form",{class:"Field",onSubmit:e[4]||(e[4]=(0,f.iM)((()=>{}),["prevent"]))},[(0,a._)("div",te,[(0,a.wy)((0,a._)("div",ee,[(0,a._)("div",ie,(0,g.zw)(i.inforMsg),1),(0,a._)("button",{type:"button",class:"ButtonEdit",onClick:e[0]||(e[0]=(...t)=>s.edit&&s.edit(...t))},[ae,(0,a.Uk)(" "+(0,g.zw)(i.EditName),1)])],512),[[f.F8,n.flag]]),(0,a.wy)((0,a._)("div",oe,[(0,a._)("div",ne,[(0,a.wy)((0,a._)("input",{id:"UserInput",type:"text","onUpdate:modelValue":e[1]||(e[1]=t=>n.Submit=t)},null,512),[[f.nr,n.Submit]])]),(0,a._)("div",se,[(0,a._)("button",{type:"submit",class:"ButtonChoice",onClick:e[2]||(e[2]=(...t)=>s.submitContent&&s.submitContent(...t))},"Save"),(0,a._)("button",{type:"button",class:"ButtonChoice",onClick:e[3]||(e[3]=(...t)=>s.edit&&s.edit(...t))},"Back")])],512),[[f.F8,n.flagEdit]])])],32)}var le={name:"MajorForm",props:["EditName","inforMsg"],emits:["SubmitMajor"],data(){return{flag:!0,flagEdit:!1,Submit:""}},methods:{edit(){this.flag=!this.flag,this.flagEdit=!this.flagEdit},submitContent(){this.$emit("SubmitMajor",this.Submit),this.flag=!this.flag,this.flagEdit=!this.flagEdit}}};const de=(0,G.Z)(le,[["render",re],["__scopeId","data-v-2d449012"]]);var me=de,ce={name:"InforCollectionSpan",components:{UsernameForm:ft,IntroForm:At,GradeForm:Gt,DepartmentForm:Yt,MajorForm:me},data(){return{Username:"",Intro:"",Grade:"",Department:"",Major:"",UserEmail:""}},methods:{handleUsername(t){this.Username=t,T().post("/profile",{user_name:this.Username,introduction:this.Intro,grade:this.Grade,major:this.Major,department:this.Department,user_email:this.UserEmail}).then((t=>{console.log(t)})).catch((t=>{console.log(t)}))},handleIntro(t){this.Intro=t,T().post("/profile",{user_name:this.Username,introduction:this.Intro,grade:this.Grade,major:this.Major,department:this.Department,user_email:this.UserEmail}).then((t=>{console.log(t)})).catch((t=>{console.log(t)}))},handleGrade(t){this.Grade=t,T().post("/profile",{user_name:this.Username,introduction:this.Intro,grade:this.Grade,major:this.Major,department:this.Department,user_email:this.UserEmail}).then((t=>{console.log(t)})).catch((t=>{console.log(t)}))},handleDepartment(t){this.Department=t,T().post("/profile",{user_name:this.Username,introduction:this.Intro,grade:this.Grade,major:this.Major,department:this.Department,user_email:this.UserEmail}).then((t=>{console.log(t)})).catch((t=>{console.log(t)}))},handleMajor(t){this.Major=t,T().post("/profile",{user_name:this.Username,introduction:this.Intro,grade:this.Grade,major:this.Major,department:this.Department,user_email:this.UserEmail}).then((t=>{console.log(t)})).catch((t=>{console.log(t)}))}},created(){T().get("/get_session").then((t=>{this.UserEmail=t.data.message})).catch((function(t){console.log(t)})),T().get("/get_profile",{params:{user_email:this.$route.query.email}}).then((t=>{this.Username=t.data.user_name,this.Intro=t.data.introduction,this.Grade=t.data.grade,this.Major=t.data.major,this.Department=t.data.department})).catch((function(t){console.log(t)}))}};const ue=(0,G.Z)(ce,[["render",ot],["__scopeId","data-v-b4ebb644"]]);var pe=ue;const he=t=>((0,a.dD)("data-v-70fad60f"),t=t(),(0,a.Cn)(),t),ge={class:"show-info"},fe=he((()=>(0,a._)("h3",null,"Edit avatar",-1))),_e={class:"cropper-content"},ve={class:"test-button"},be=he((()=>(0,a._)("label",{class:"btn",for:"uploads"},"upload",-1))),Ce=(0,a.Uk)("+"),we=(0,a.Uk)("-"),Se=(0,a.Uk)("rotateLeft"),Ee=(0,a.Uk)("rotateRight"),Ie=(0,a.Uk)("Submit"),ye=he((()=>(0,a._)("h3",null,"Preview",-1))),Ue={class:"show-preview"},ke=["src"];function Ae(t,e,i,o,n,s){const r=(0,a.up)("vueCropper"),l=(0,a.up)("n-button"),d=(0,a.up)("n-button-group");return(0,a.wg)(),(0,a.iD)("div",ge,[fe,(0,a._)("div",_e,[(0,a.Wm)(r,{ref:"cropper",img:n.option.img,outputSize:n.option.outputSize,outputType:n.option.outputType,info:n.option.info,canScale:n.option.canScale,autoCrop:n.option.autoCrop,autoCropWidth:n.option.autoCropWidth,autoCropHeight:n.option.autoCropHeight,fixed:n.option.fixed,fixedNumber:n.option.fixedNumber,full:n.option.full,fixedBox:n.option.fixedBox,canMove:n.option.canMove,canMoveBox:n.option.canMoveBox,original:n.option.original,centerBox:n.option.centerBox,height:n.option.height,infoTrue:n.option.infoTrue,maxImgSize:n.option.maxImgSize,enlarge:n.option.enlarge,mode:n.option.mode,onRealTime:s.realTime,onImgLoad:s.imgLoad},null,8,["img","outputSize","outputType","info","canScale","autoCrop","autoCropWidth","autoCropHeight","fixed","fixedNumber","full","fixedBox","canMove","canMoveBox","original","centerBox","height","infoTrue","maxImgSize","enlarge","mode","onRealTime","onImgLoad"])]),(0,a._)("div",ve,[be,(0,a._)("input",{type:"file",id:"uploads",style:{position:"absolute",clip:"rect(0 0 0 0)"},accept:"image/png, image/jpeg, image/gif, image/jpg",onChange:e[0]||(e[0]=t=>s.selectImg(t))},null,32),(0,a.Wm)(d,{size:"small"},{default:(0,a.w5)((()=>[(0,a.Wm)(l,{onClick:e[1]||(e[1]=t=>s.changeScale(1)),class:"btn-1",id:"first",style:{width:"10px"}},{default:(0,a.w5)((()=>[Ce])),_:1}),(0,a.Wm)(l,{onClick:e[2]||(e[2]=t=>s.changeScale(-1)),class:"btn-1",style:{width:"10px"}},{default:(0,a.w5)((()=>[we])),_:1})])),_:1}),(0,a.Wm)(d,{size:"small"},{default:(0,a.w5)((()=>[(0,a.Wm)(l,{onClick:s.rotateLeft,class:"btn-2",style:{width:"80px"}},{default:(0,a.w5)((()=>[Se])),_:1},8,["onClick"]),(0,a.Wm)(l,{onClick:s.rotateRight,class:"btn-2",style:{width:"80px"}},{default:(0,a.w5)((()=>[Ee])),_:1},8,["onClick"])])),_:1}),(0,a.Wm)(l,{onClick:e[3]||(e[3]=t=>s.uploadImg("blob")),class:"Submit",type:"info",style:{"background-color":"#00B8FF"}},{default:(0,a.w5)((()=>[Ie])),_:1})]),ye,(0,a._)("div",Ue,[(0,a._)("div",{style:(0,g.j5)(n.previews.div),class:"preview"},[(0,a._)("img",{src:n.previews.url,style:(0,g.j5)(n.previews.img)},null,12,ke)],4)])])}var Be=i(3087),Me={name:"CropperImage",components:{VueCropper:Be.AK},data(){return{name:this.Name,previews:{},option:{img:"",outputSize:1,outputType:"jpeg",info:!0,canScale:!0,autoCrop:!0,autoCropWidth:100,autoCropHeight:100,fixed:!0,fixedNumber:[1,1],full:!1,fixedBox:!0,canMove:!1,canMoveBox:!0,original:!1,centerBox:!1,height:!0,infoTrue:!1,maxImgSize:3e3,enlarge:1,mode:"230px 150px"}}},methods:{imgLoad(t){console.log("工具初始化函数====="+t)},changeScale(t){t=t||1,this.$refs.cropper.changeScale(t)},rotateLeft(){this.$refs.cropper.rotateLeft()},rotateRight(){this.$refs.cropper.rotateRight()},realTime(t){this.previews=t},selectImg(t){let e=t.target.files[0];if(!/\.(jpg|jpeg|png|JPG|PNG)$/.test(t.target.value))return!1;let i=new FileReader;i.onload=t=>{let e;e="object"===typeof t.target.result?window.URL.createObjectURL(new Blob([t.target.result])):t.target.result,this.option.img=e},i.readAsDataURL(e)},uploadImg(t){"blob"===t&&this.$refs.cropper.getCropBlob((t=>{let e=new FormData;e.append("file",t,"DX.jpg");let i={headers:{"Content-Type":"multipart/form-data"}};console.log(e.get("file")),T().post("/profile/post_photo",e,i).then((t=>{console.log(t)}))}))}}};const Fe=(0,G.Z)(Me,[["render",Ae],["__scopeId","data-v-70fad60f"]]);var xe=Fe,De=i(2262),je={name:"IdentificationCard",components:{InforCollectionSpan:pe,InforCollection:L,CropperImage:xe},data(){return{showModal:(0,De.iH)(!1),animate:{transition:!0,frame:!0,frameSpan:!1},animateButton:{Rotate:!1,RotateBack:!0},IsHost:!0,accessEmail:"",hostEmail:"",profile_url:""}},methods:{HandleClick(){this.$store.commit("changeSpanState"),this.animate.frame=!this.animate.frame,this.animate.frameSpan=!this.animate.frameSpan,this.animateButton.Rotate=!this.animateButton.Rotate,this.animateButton.RotateBack=!this.animateButton.RotateBack}},created(){this.hostEmail=this.$route.query.email,T().get("/get_session").then((t=>{this.accessEmail=t.data.message,console.log(this.hostEmail),console.log(this.accessEmail),this.accessEmail!=this.hostEmail?this.IsHost=!1:this.IsHost=!0})).catch((function(t){console.log(t)})),T().get("/get_profile",{params:{user_email:this.hostEmail}}).then((t=>{this.profile_url=t.data.profile})).catch((function(t){console.log(t)}))}};const We=(0,G.Z)(je,[["render",U],["__scopeId","data-v-75c796b6"]]);var Re=We,Ne={name:"FrameWorkProfile",data(){return{email:""}},components:{IdentificationCard:Re},created(){this.email=this.$route.query.email}};const Te=(0,G.Z)(Ne,[["render",h],["__scopeId","data-v-679cc9b2"]]);var ze=Te,Ge={components:{FrameWorkProfile:ze}};const He=(0,G.Z)(Ge,[["render",o]]);var Le=He},4554:function(t){t.exports="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACkAAAA/CAYAAAB97+FwAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAMGSURBVHgBzZo/ehMxEMWfAk2ocgS7o8wRQhenIh0d5gSBE8ScIPgEWU4QV5ikgRskN4g4AVRAEwuNleVb78oraWck5/d9W9jWep9HejP6Y2AXXJmDlOZ7KM21ucA+fuKrMfa6xNKMQrcolOTanMNg5vmksu9/xERp323lRFLEFO57Wmh7zXGsPrU/KNfdCueBFiN7XdghcG9/0HTz1hLQQxUukcb/IVBGJEXHRSoVjQecPkNubsyZjcgbDOPADsiXecckmWWF9+CgcJBXpDPLCBwM7vKNyXDKicNgnC+S6W72UZG784h0ee4IPPQ6BSFXMg8n7jCNMikvkuoz1ywUxYmq6heyIt2MhpdyiBU+NF/KiqRuNkiaK3qocKIWm18rhWDKaU/Z5CKp8A1ctswpZUS6lDMCDw3qag/87qb1yj5uwS9/75qObsKP5AucQTjltOFFMqNZmvAiKVFZHuszeh8zlKU5EnL0OCRyeCQlZjk9y9jNRw1h2MKqjbbL13FMw/RIOrPIzHIiSRe5J5Jy7vpSTpu07i6UctqkRbJQymkTL9LV5yl46JSxWBMvUiaK89QoEnEiaRdCoj57dsxiCIuU2IUgBnRzTVikxC6EM0uFgfSnoB2lnDb9kVS4ApfVMLM02S7SpZxD8ND2hw4yS5PtIoV3ITj4RWbYheDQFUlm8R9jpEELKyG6IuXq83cI0U1BdFLFhZly2vgi+QschMzSpCvyYXj5ApnlLz/ltOmKPLGTADfoNVKhKJ4qXk94CJXFaULtjl5YpdJfFinPGbyy12eEoHaZcCKXZrZe7PsgE0zUdO1YYLHleyppszRRrZlOFXRndwjodRQLiqzfneG3nb30meCLeU1HatbNixxm2ZRD+BO4foxqhR3TJ7Ime3eGcMbprzJuOET+qSMHTqSJKoVT2/rWTuPeojBpOxh0RmPYZ4bJ1CJ1RFu9LpfHSmyeGMvziDY7d7kTafCjU8XJTHTG9wRSUDeSTtwcf+yUK3OSjsWJJGFPUNwmN+Yw9Z94JfkHjtwdlXov9hoAAAAASUVORK5CYII="}}]);
//# sourceMappingURL=profile.768cc6e1.js.map