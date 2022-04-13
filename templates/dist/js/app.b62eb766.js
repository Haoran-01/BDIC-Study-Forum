(function(){"use strict";var e={498:function(e,t,n){var o=n(963),i=n(252);const a={class:"navigator"};function r(e,t,n,o,r,s){const c=(0,i.up)("NavigatorBar");return(0,i.wg)(),(0,i.iD)("div",a,[(0,i.Wm)(c)])}const s=e=>((0,i.dD)("data-v-4e102d58"),e=e(),(0,i.Cn)(),e),c={class:"navigatorMain"},u=s((()=>(0,i._)("div",{class:"logo"},null,-1))),l={class:"navOptions",id:"navOptions"},d=(0,i.Uk)(" Home "),m=(0,i.Uk)("Forum"),f={class:"mainView"};function v(e,t,n,a,r,s){const v=(0,i.up)("router-link"),p=(0,i.up)("NavUserMenu"),h=(0,i.up)("router-view");return(0,i.wg)(),(0,i.iD)(i.HY,null,[(0,i._)("div",c,[u,(0,i._)("div",l,[(0,i._)("nav",null,[(0,i.Wm)(v,{class:"home",to:"/",Style:"cursor: pointer;"},{default:(0,i.w5)((()=>[d])),_:1}),(0,i.Wm)(v,{class:"forum",to:"/forum",Style:"cursor: pointer;"},{default:(0,i.w5)((()=>[m])),_:1})])]),(0,i._)("button",{class:"userMenuButton",id:"userMenuButton",onClick:t[0]||(t[0]=(...e)=>s.handleUserMenu&&s.handleUserMenu(...e)),onBlur:t[1]||(t[1]=(...e)=>s.deleteUserMenu&&s.deleteUserMenu(...e))},null,32),(0,i.Wm)(o.uT,null,{default:(0,i.w5)((()=>[r.userMenuVisibility?((0,i.wg)(),(0,i.j4)(p,{key:0,class:"userMenu"})):(0,i.kq)("",!0)])),_:1})]),(0,i._)("div",f,[(0,i.Wm)(h)])],64)}const p=e=>((0,i.dD)("data-v-1df88a53"),e=e(),(0,i.Cn)(),e),h={class:"menuMain"},g=p((()=>(0,i._)("div",{class:"menuItemIcon",id:"profileIcon"},null,-1))),b=p((()=>(0,i._)("div",{class:"menuItemText"}," Profile ",-1))),y=p((()=>(0,i._)("div",{class:"menuItem"},[(0,i._)("div",{class:"menuItemIcon",id:"logoutIcon"}),(0,i._)("div",{class:"menuItemText"},"Log Out")],-1)));function w(e,t,n,o,a,r){const s=(0,i.up)("router-link");return(0,i.wg)(),(0,i.iD)("div",h,[(0,i.Wm)(s,{class:"menuItem",to:"/profile"},{default:(0,i.w5)((()=>[g,b])),_:1}),y])}var k={name:"NavUserMenu"},_=n(744);const I=(0,_.Z)(k,[["render",w],["__scopeId","data-v-1df88a53"]]);var N=I,L={name:"NavigatorBar",components:{NavUserMenu:N},data(){return{userMenuVisibility:!1}},methods:{changeOptionsVisibility(){const e=document.getElementById("navOptions");!1===this.$store.state.mainFunctionsVisibility?(e.style.opacity="1",e.style.pointerEvents="auto"):(e.style.opacity="0",e.style.pointerEvents="none")},handleUserMenu(){if(!1===this.$data.userMenuVisibility){const e=document.getElementById("userMenuButton");e.focus()}this.$data.userMenuVisibility=!this.$data.userMenuVisibility},deleteUserMenu(){this.$data.userMenuVisibility=!1}},watch:{$route(e,t){e.path,t.path,this.changeOptionsVisibility()}},mounted(){window.addEventListener("scroll",this.changeOptionsVisibility,!0)},unmounted(){window.removeEventListener("scroll",this.changeOptionsVisibility,!0)}};const C=(0,_.Z)(L,[["render",v],["__scopeId","data-v-4e102d58"]]);var T=C,M={components:{NavigatorBar:T}};const F=(0,_.Z)(M,[["render",r]]);var S=F,U=n(119),E=n(907),x=(0,E.MT)({state:{mainFunctionsVisibility:!0,Span:!1},getters:{},mutations:{changeMainFunctionsInvisible(){this.state.mainFunctionsVisibility=!1},changeMainFunctionsVisible(){this.state.mainFunctionsVisibility=!0},changeSpanState(){this.Span=!this.Span}},actions:{},modules:{}}),D=n(577);const W=e=>((0,i.dD)("data-v-f154a1e4"),e=e(),(0,i.Cn)(),e),B={class:"home"},O=W((()=>(0,i._)("div",{class:"headSpace"},null,-1))),V={class:"homeFrame"},R={class:"mainFunctions",id:"mainFunctions"},j={class:"main"},A={class:"postListFrame"},P={class:"sideBar"};function Z(e,t,n,a,r,s){const c=(0,i.up)("main-function-entrance"),u=(0,i.up)("post-entrance"),l=(0,i.up)("top-section-list"),d=(0,i.up)("cookie-window");return(0,i.wg)(),(0,i.iD)("div",B,[O,(0,i._)("div",V,[(0,i._)("div",R,[(0,i.Wm)(c)]),(0,i._)("div",j,[(0,i._)("div",A,[((0,i.wg)(!0),(0,i.iD)(i.HY,null,(0,i.Ko)(r.postData,((e,t)=>((0,i.wg)(),(0,i.iD)("div",{class:"postListLogic",key:t},[(0,i.Wm)(u,(0,D.vs)((0,i.F4)(e)),null,16)])))),128))]),(0,i._)("div",P,[(0,i.Wm)(l)])])]),(0,i.Wm)(o.uT,null,{default:(0,i.w5)((()=>[r.cookieVisibility?((0,i.wg)(),(0,i.j4)(d,{key:0,class:"cookies",onRemoveCookieWindow:s.removeCookieWindow},null,8,["onRemoveCookieWindow"])):(0,i.kq)("",!0)])),_:1})])}const $=e=>((0,i.dD)("data-v-e2098f58"),e=e(),(0,i.Cn)(),e),H={class:"cookieWindow"},z=(0,i.uE)('<div class="cookieDecoration" data-v-e2098f58></div><div class="cookieIcon" data-v-e2098f58></div><div class="cookieTexts" data-v-e2098f58><span class="cookieText" data-v-e2098f58>Cookies help us to provide better service for you. By clicking &quot;Accept&quot;, you agree to our use of cookies. Check more detail about our <a href="" class="cookieProtocol" data-v-e2098f58>cookie policy</a>. </span></div>',3),Q=$((()=>(0,i._)("span",{class:"cookieAgreeButtonText"},"Accept",-1))),q=[Q];function J(e,t,n,o,a,r){return(0,i.wg)(),(0,i.iD)("div",H,[z,(0,i._)("button",{class:"cookieAgreeButton",onClick:t[0]||(t[0]=(...e)=>r.cookieAccepted&&r.cookieAccepted(...e))},q)])}var G={name:"CookieWindow",emits:["removeCookieWindow"],methods:{cookieAccepted(){this.$emit("removeCookieWindow")}}};const K=(0,_.Z)(G,[["render",J],["__scopeId","data-v-e2098f58"]]);var Y=K;const X=e=>((0,i.dD)("data-v-1110f1b1"),e=e(),(0,i.Cn)(),e),ee={class:"entrances"},te=X((()=>(0,i._)("div",{class:"entranceText"},"Forum",-1))),ne=X((()=>(0,i._)("div",{class:"entrance",id:"courseSchedule"},[(0,i._)("div",{class:"entranceText"},[(0,i.Uk)("Course"),(0,i._)("br"),(0,i.Uk)("Schedule")])],-1))),oe=X((()=>(0,i._)("div",{class:"entrance",id:"comingSoon"},[(0,i._)("div",{class:"entranceText"},[(0,i.Uk)("Coming"),(0,i._)("br"),(0,i.Uk)("Soon")])],-1)));function ie(e,t,n,o,a,r){const s=(0,i.up)("router-link");return(0,i.wg)(),(0,i.iD)("div",ee,[(0,i.Wm)(s,{class:"entrance",id:"forum",to:"/forum"},{default:(0,i.w5)((()=>[te])),_:1}),ne,oe])}var ae={name:"MainFunctionEntrance"};const re=(0,_.Z)(ae,[["render",ie],["__scopeId","data-v-1110f1b1"]]);var se=re;const ce=e=>((0,i.dD)("data-v-08ef5df8"),e=e(),(0,i.Cn)(),e),ue={class:"postEntranceFrame"},le={class:"topBar"},de=["src"],me={class:"userName"},fe=ce((()=>(0,i._)("span",{class:"point"},"·",-1))),ve={class:"section"},pe={class:"postTitle"},he={class:"postImage"},ge={class:"postToolBar"},be={class:"toolButton",id:"comment"},ye=ce((()=>(0,i._)("div",{class:"postIcon",id:"commentIcon"},null,-1))),we={class:"toolText",id:"commentNumber"},ke=(0,i.uE)('<div class="toolButton" id="share" data-v-08ef5df8><div class="postIcon" id="shareIcon" data-v-08ef5df8></div><span class="toolText" id="shareText" data-v-08ef5df8>Share</span></div><div class="toolButton" id="favorite" data-v-08ef5df8><div class="postIcon" id="favoriteIcon" data-v-08ef5df8></div><span class="toolText" id="favoriteText" data-v-08ef5df8>Favorite</span></div>',2);function _e(e,t,n,o,a,r){return(0,i.wg)(),(0,i.iD)("div",ue,[(0,i._)("div",le,[(0,i._)("img",{src:n.userImageURL,class:"headImage"},null,8,de),(0,i._)("span",me,(0,D.zw)(n.userName),1),fe,(0,i._)("span",ve,(0,D.zw)(n.sectionName),1)]),(0,i._)("div",pe,(0,D.zw)(n.title),1),(0,i._)("div",he,(0,D.zw)(n.introduction),1),(0,i._)("div",ge,[(0,i._)("div",be,[ye,(0,i._)("span",we,(0,D.zw)(n.commentNumber)+" Comments",1)]),ke])])}var Ie={name:"PostEntrance",props:["userName","sectionName","title","introduction","commentNumber","userImageURL"]};const Ne=(0,_.Z)(Ie,[["render",_e],["__scopeId","data-v-08ef5df8"]]);var Le=Ne;const Ce=e=>((0,i.dD)("data-v-670817da"),e=e(),(0,i.Cn)(),e),Te={class:"topSectionFrame"},Me=Ce((()=>(0,i._)("div",{class:"topSectionListHead"},[(0,i._)("div",{class:"topSectionListIntro"},"Today’s Top Forum Sections")],-1))),Fe={class:"topSectionsFrame"};function Se(e,t,n,o,a,r){const s=(0,i.up)("SectionHomeEntrance");return(0,i.wg)(),(0,i.iD)("div",Te,[Me,(0,i._)("div",Fe,[((0,i.wg)(!0),(0,i.iD)(i.HY,null,(0,i.Ko)(a.sectionData,((e,t)=>((0,i.wg)(),(0,i.iD)("div",{class:"topSectionsLogic",key:t},[(0,i.Wm)(s,(0,D.vs)((0,i.F4)(e)),null,16)])))),128))])])}const Ue={class:"sectionCard"},Ee={class:"sectionRank"},xe=["src"],De={class:"sectionName"},We={class:"newComments"};function Be(e,t,n,o,a,r){return(0,i.wg)(),(0,i.iD)("div",Ue,[(0,i._)("div",Ee,(0,D.zw)(n.rank),1),(0,i._)("img",{src:n.sectionCoverImageURL,class:"sectionImage"},null,8,xe),(0,i._)("div",De,(0,D.zw)(n.sectionTitle),1),(0,i._)("div",We,(0,D.zw)(n.commentNumber)+" Comments",1)])}var Oe={name:"SectionEntrance",props:["sectionTitle","commentNumber","rank","sectionCoverImageURL"]};const Ve=(0,_.Z)(Oe,[["render",Be],["__scopeId","data-v-5dd04dbc"]]);var Re=Ve,je={name:"TopSectionList",components:{SectionHomeEntrance:Re},data(){return{sectionData:[{sectionTitle:"Lecture Question",commentNumber:26,rank:1,sectionCoverImageURL:n(504)},{sectionTitle:"Lost and Found",commentNumber:14,rank:2,sectionCoverImageURL:n(649)},{sectionTitle:"Transaction",commentNumber:8,rank:3,sectionCoverImageURL:n(906)}]}}};const Ae=(0,_.Z)(je,[["render",Se],["__scopeId","data-v-670817da"]]);var Pe=Ae,Ze={components:{TopSectionList:Pe,PostEntrance:Le,MainFunctionEntrance:se,CookieWindow:Y},data(){return{cookieVisibility:!0,postData:[{userName:"Jerry",sectionName:"Lecture Question",title:"The problem about binary tree",introduction:"What is the difference between a binary search tree and a binary tree?",commentNumber:6,userImageURL:n(193)},{userName:"Jerry",sectionName:"Lecture Question",title:"About AVL tree",introduction:"After inserting in the AVL tree, why will one restructuring (if necessary) be enough to rebalance the whole tree? While for deletion, we must continue checking for balance until the root of T is reached.",commentNumber:4,userImageURL:n(193)},{userName:"Jerry",sectionName:"Lecture Question",title:"Heap exercise",introduction:"When restructuring a tree, what if the children of y have the same height, and either one can be x?",commentNumber:4,userImageURL:n(193)},{userName:"Jerry",sectionName:"Lecture Question",title:"Movement of an external node in Splay Tree",introduction:"In these slides, if I switch between the right(external) and left(8) child of node x(10), would it get a different result after Zig-Zig?",commentNumber:3,userImageURL:n(193)},{userName:"Winfred",sectionName:"Lecture Question",title:"remove operation of binary tree",introduction:"after we have removed 3, can we continue to remove 6 (the root), which will change the root of the tree to 2?",commentNumber:3,userImageURL:n(603)},{userName:"Winfred",sectionName:"Lost and Found",title:"Black Watch",introduction:"I lost a watch apple at the entry to the teaching building 4. If anyone finds it, please contact me. I will really appreciate it if you could help.",commentNumber:2,userImageURL:n(603)},{userName:"Grey",sectionName:"Lost and Found",title:"Black Watch",introduction:"I lost a wallet with a student card (203721) in it. I will really appreciate it if you could help",commentNumber:2,userImageURL:n(351)},{userName:"Grey",sectionName:"Transaction",title:"MacBook Pro",introduction:"If you want to buy a second-hand MacBook Pro 2021 16 inches, please contact me.",commentNumber:1,userImageURL:n(351)},{userName:"Grey",sectionName:"Transaction",title:"iPhone 8",introduction:"Anyone who would like to buy a second-hand iPhone 8 could email me directly.",commentNumber:1,userImageURL:n(351)},{userName:"Grey",sectionName:"Transaction",title:"Java Learning Material",introduction:"If you want some java learning material, please contact me. I could sell them in a low price. Don’t hesitate!!!",commentNumber:1,userImageURL:n(351)}]}},methods:{removeCookieWindow(){this.$data.cookieVisibility=!1},checkMainFunctionsPosition(){const e=document.getElementById("mainFunctions");e.getBoundingClientRect().bottom>0?this.$store.commit("changeMainFunctionsVisible"):this.$store.commit("changeMainFunctionsInvisible")}},mounted(){window.addEventListener("scroll",this.checkMainFunctionsPosition,!0)},unmounted(){window.removeEventListener("scroll",this.checkMainFunctionsPosition,!0)}};const $e=(0,_.Z)(Ze,[["render",Z],["__scopeId","data-v-f154a1e4"]]);var He=$e;const ze=[{path:"/",name:"home",component:He},{path:"/profile",name:"profile",component:()=>n.e(845).then(n.bind(n,0)),children:[{path:"posts",name:"posts",component:()=>n.e(287).then(n.bind(n,853))},{path:"favourite",name:"favourite",component:()=>n.e(962).then(n.bind(n,155))}]},{path:"/forum",name:"forum",component:()=>n.e(315).then(n.bind(n,865))}],Qe=(0,U.p7)({history:(0,U.r5)(),routes:ze});Qe.afterEach(((e,t)=>{"/"===e.path?x.commit("changeMainFunctionsVisible"):x.commit("changeMainFunctionsInvisible"),t.path}));var qe=Qe;(0,o.ri)(S).use(x).use(qe).mount("#app")},193:function(e,t,n){e.exports=n.p+"img/Jerry.bb8f6f4c.jpg"},649:function(e,t,n){e.exports=n.p+"img/Lost&Found.ae9188b7.jpeg"},504:function(e,t,n){e.exports=n.p+"img/R&Q.acfb88f2.jpeg"},351:function(e,t,n){e.exports=n.p+"img/grey.00bd7ae7.jpg"},906:function(e,t,n){e.exports=n.p+"img/transaction.9586dac9.jpeg"},603:function(e,t,n){e.exports=n.p+"img/winfred.42a13cc2.jpg"}},t={};function n(o){var i=t[o];if(void 0!==i)return i.exports;var a=t[o]={exports:{}};return e[o](a,a.exports,n),a.exports}n.m=e,function(){var e=[];n.O=function(t,o,i,a){if(!o){var r=1/0;for(l=0;l<e.length;l++){o=e[l][0],i=e[l][1],a=e[l][2];for(var s=!0,c=0;c<o.length;c++)(!1&a||r>=a)&&Object.keys(n.O).every((function(e){return n.O[e](o[c])}))?o.splice(c--,1):(s=!1,a<r&&(r=a));if(s){e.splice(l--,1);var u=i();void 0!==u&&(t=u)}}return t}a=a||0;for(var l=e.length;l>0&&e[l-1][2]>a;l--)e[l]=e[l-1];e[l]=[o,i,a]}}(),function(){n.d=function(e,t){for(var o in t)n.o(t,o)&&!n.o(e,o)&&Object.defineProperty(e,o,{enumerable:!0,get:t[o]})}}(),function(){n.f={},n.e=function(e){return Promise.all(Object.keys(n.f).reduce((function(t,o){return n.f[o](e,t),t}),[]))}}(),function(){n.u=function(e){return"js/"+{287:"posts",315:"forum",845:"profile",962:"favourite"}[e]+"."+{287:"dde170bd",315:"3d6638eb",845:"a78c68d3",962:"f0f5c79e"}[e]+".js"}}(),function(){n.miniCssF=function(e){return"css/"+{315:"forum",845:"profile"}[e]+"."+{315:"d8696d1b",845:"af32eba7"}[e]+".css"}}(),function(){n.g=function(){if("object"===typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(e){if("object"===typeof window)return window}}()}(),function(){n.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)}}(),function(){var e={},t="framework:";n.l=function(o,i,a,r){if(e[o])e[o].push(i);else{var s,c;if(void 0!==a)for(var u=document.getElementsByTagName("script"),l=0;l<u.length;l++){var d=u[l];if(d.getAttribute("src")==o||d.getAttribute("data-webpack")==t+a){s=d;break}}s||(c=!0,s=document.createElement("script"),s.charset="utf-8",s.timeout=120,n.nc&&s.setAttribute("nonce",n.nc),s.setAttribute("data-webpack",t+a),s.src=o),e[o]=[i];var m=function(t,n){s.onerror=s.onload=null,clearTimeout(f);var i=e[o];if(delete e[o],s.parentNode&&s.parentNode.removeChild(s),i&&i.forEach((function(e){return e(n)})),t)return t(n)},f=setTimeout(m.bind(null,void 0,{type:"timeout",target:s}),12e4);s.onerror=m.bind(null,s.onerror),s.onload=m.bind(null,s.onload),c&&document.head.appendChild(s)}}}(),function(){n.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})}}(),function(){n.p=""}(),function(){var e=function(e,t,n,o){var i=document.createElement("link");i.rel="stylesheet",i.type="text/css";var a=function(a){if(i.onerror=i.onload=null,"load"===a.type)n();else{var r=a&&("load"===a.type?"missing":a.type),s=a&&a.target&&a.target.href||t,c=new Error("Loading CSS chunk "+e+" failed.\n("+s+")");c.code="CSS_CHUNK_LOAD_FAILED",c.type=r,c.request=s,i.parentNode.removeChild(i),o(c)}};return i.onerror=i.onload=a,i.href=t,document.head.appendChild(i),i},t=function(e,t){for(var n=document.getElementsByTagName("link"),o=0;o<n.length;o++){var i=n[o],a=i.getAttribute("data-href")||i.getAttribute("href");if("stylesheet"===i.rel&&(a===e||a===t))return i}var r=document.getElementsByTagName("style");for(o=0;o<r.length;o++){i=r[o],a=i.getAttribute("data-href");if(a===e||a===t)return i}},o=function(o){return new Promise((function(i,a){var r=n.miniCssF(o),s=n.p+r;if(t(r,s))return i();e(o,s,i,a)}))},i={143:0};n.f.miniCss=function(e,t){var n={315:1,845:1};i[e]?t.push(i[e]):0!==i[e]&&n[e]&&t.push(i[e]=o(e).then((function(){i[e]=0}),(function(t){throw delete i[e],t})))}}(),function(){var e={143:0};n.f.j=function(t,o){var i=n.o(e,t)?e[t]:void 0;if(0!==i)if(i)o.push(i[2]);else{var a=new Promise((function(n,o){i=e[t]=[n,o]}));o.push(i[2]=a);var r=n.p+n.u(t),s=new Error,c=function(o){if(n.o(e,t)&&(i=e[t],0!==i&&(e[t]=void 0),i)){var a=o&&("load"===o.type?"missing":o.type),r=o&&o.target&&o.target.src;s.message="Loading chunk "+t+" failed.\n("+a+": "+r+")",s.name="ChunkLoadError",s.type=a,s.request=r,i[1](s)}};n.l(r,c,"chunk-"+t,t)}},n.O.j=function(t){return 0===e[t]};var t=function(t,o){var i,a,r=o[0],s=o[1],c=o[2],u=0;if(r.some((function(t){return 0!==e[t]}))){for(i in s)n.o(s,i)&&(n.m[i]=s[i]);if(c)var l=c(n)}for(t&&t(o);u<r.length;u++)a=r[u],n.o(e,a)&&e[a]&&e[a][0](),e[a]=0;return n.O(l)},o=self["webpackChunkframework"]=self["webpackChunkframework"]||[];o.forEach(t.bind(null,0)),o.push=t.bind(null,o.push.bind(o))}();var o=n.O(void 0,[998],(function(){return n(498)}));o=n.O(o)})();
//# sourceMappingURL=app.b62eb766.js.map