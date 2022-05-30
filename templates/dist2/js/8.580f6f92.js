"use strict";(self["webpackChunkframework"]=self["webpackChunkframework"]||[]).push([[8],{6008:function(e,t,i){i.r(t),i.d(t,{revo_dropdown:function(){return h},revo_list:function(){return m}});var o=i(3520),r=function(e,t,i,o){function r(e){return e instanceof i?e:new i((function(t){t(e)}))}return new(i||(i=Promise))((function(i,n){function s(e){try{a(o.next(e))}catch(e){n(e)}}function l(e){try{a(o["throw"](e))}catch(e){n(e)}}function a(e){e.done?i(e.value):r(e.value).then(s,l)}a((o=o.apply(e,t||[])).next())}))},n=function(e,t){var i,o,r,n,s={label:0,sent:function(){if(1&r[0])throw r[1];return r[1]},trys:[],ops:[]};return n={next:l(0),throw:l(1),return:l(2)},"function"===typeof Symbol&&(n[Symbol.iterator]=function(){return this}),n;function l(e){return function(t){return a([e,t])}}function a(n){if(i)throw new TypeError("Generator is already executing.");while(s)try{if(i=1,o&&(r=2&n[0]?o["return"]:n[0]?o["throw"]||((r=o["return"])&&r.call(o),0):o.next)&&!(r=r.call(o,n[1])).done)return r;switch(o=0,r&&(n=[2&n[0],r.value]),n[0]){case 0:case 1:r=n;break;case 4:return s.label++,{value:n[1],done:!1};case 5:s.label++,o=n[1],n=[0];continue;case 7:n=s.ops.pop(),s.trys.pop();continue;default:if(r=s.trys,!(r=r.length>0&&r[r.length-1])&&(6===n[0]||2===n[0])){s=0;continue}if(3===n[0]&&(!r||n[1]>r[0]&&n[1]<r[3])){s.label=n[1];break}if(6===n[0]&&s.label<r[1]){s.label=r[1],r=n;break}if(r&&s.label<r[2]){s.label=r[2],s.ops.push(n);break}r[2]&&s.ops.pop(),s.trys.pop();continue}n=t.call(e,s)}catch(e){n=[6,e],o=0}finally{i=r=0}if(5&n[0])throw n[1];return{value:n[0]?n[1]:void 0,done:!0}}};(function(){Element.prototype.matches||(Element.prototype.matches=Element.prototype.msMatchesSelector||Element.prototype.webkitMatchesSelector),Element.prototype.closest||(Element.prototype.closest=function(e){var t=this;do{if(Element.prototype.matches.call(t,e))return t;t=t.parentElement||t.parentNode}while(null!==t&&1===t.nodeType);return null})})();var s="uuid";function l(e,t){return e?t?e[t]:e:""}function a(e,t){return t?e[t]:e}function c(e,t){var i,o=[],r=null===(i=null===t||void 0===t?void 0:t.trim())||void 0===i?void 0:i.toLocaleLowerCase();if(r)for(var n=0,s=e.source;n<s.length;n++){var a=s[n],c=l(a,e.dataLabel);if("string"===typeof c)switch(c=c.toLocaleLowerCase(),e.filter){case"start":0===c.indexOf(r)&&o.push(a);break;default:c.indexOf(r)>-1&&o.push(a);break}}else o=e.source;return o}var u=function(e){var t=function(t){var i=c(e,t);e.onFilterChange({value:t,items:i})};return e.filter||(e.filter="contains"),t(e.filterValue),e.autocomplete&&(e.value=e.filterValue),(0,o.h)("input",Object.assign({class:{"filter-box":!0},type:"text"},e,{onClick:function(t){t.preventDefault(),e.onClick&&e.onClick(t)},onInput:function(i){var o;e.onInput&&e.onInput();var r=null===(o=i.currentTarget)||void 0===o?void 0:o.value;t(r)}}))},d=function(){return(0,o.h)("span",{class:"arrow-wrapper"},(0,o.h)("svg",{class:"arrow","aria-hidden":"true",focusable:"false",role:"img",xmlns:"http://www.w3.org/2000/svg",viewBox:"0 0 320 512"},(0,o.h)("path",{fill:"currentColor",d:"M41 288h238c21.4 0 32.1 25.9 17 41L177 448c-9.4 9.4-24.6 9.4-33.9 0L24 329c-15.1-15.1-4.4-41 17-41z"})))},p='revo-dropdown{font-size:1em;font-family:"Roboto", "Helvetica", "Arial", sans-serif;font-weight:400;line-height:2em;letter-spacing:0.01em;display:-ms-inline-flexbox;display:inline-flex;-ms-flex-direction:column;flex-direction:column;vertical-align:top;padding:0;-webkit-box-sizing:border-box;box-sizing:border-box;cursor:pointer;position:relative}revo-dropdown .rv-dr-root{padding:5px 9px;padding-right:35px;-ms-flex-wrap:wrap;flex-wrap:wrap;position:relative;border-radius:4px;cursor:text;display:-ms-inline-flexbox;display:inline-flex;position:relative;font-size:1rem;-webkit-box-sizing:border-box;box-sizing:border-box;-ms-flex-align:center;align-items:center}revo-dropdown input.filter-box{padding-left:6px;padding:9.5px 4px;width:0;min-width:30px;-ms-flex-positive:1;flex-grow:1;text-overflow:ellipsis;border:0;height:1.1876em;margin:0;display:block;background:none;-webkit-box-sizing:content-box;box-sizing:content-box;letter-spacing:inherit;-webkit-animation-duration:10ms;animation-duration:10ms}revo-dropdown input.filter-box:focus{outline:none}revo-dropdown .actions{right:9px;top:calc(50% - $font-size);position:absolute}revo-dropdown label{font-size:1rem;z-index:100;top:0;left:0;position:absolute;display:block;-webkit-transform-origin:top left;transform-origin:top left;line-height:1;-webkit-transition:color 200ms cubic-bezier(0, 0, 0.2, 1) 0ms, -webkit-transform 200ms cubic-bezier(0, 0, 0.2, 1) 0ms;transition:color 200ms cubic-bezier(0, 0, 0.2, 1) 0ms, -webkit-transform 200ms cubic-bezier(0, 0, 0.2, 1) 0ms;transition:color 200ms cubic-bezier(0, 0, 0.2, 1) 0ms, transform 200ms cubic-bezier(0, 0, 0.2, 1) 0ms;transition:color 200ms cubic-bezier(0, 0, 0.2, 1) 0ms, transform 200ms cubic-bezier(0, 0, 0.2, 1) 0ms, -webkit-transform 200ms cubic-bezier(0, 0, 0.2, 1) 0ms;-webkit-transform:translate(14px, 14px) scale(1);transform:translate(14px, 14px) scale(1);pointer-events:none}revo-dropdown fieldset{border-color:#ececec;top:-5px;left:0;right:0;bottom:0;margin:0;padding:0 8px;overflow:hidden;position:absolute;z-index:0;border-style:solid;border-width:1px;border-radius:inherit;pointer-events:none}revo-dropdown fieldset legend{width:auto;height:11px;display:block;padding:0;font-size:0.75em;max-width:0.01px;text-align:left;-webkit-transition:max-width 50ms cubic-bezier(0, 0, 0.2, 1) 0ms;transition:max-width 50ms cubic-bezier(0, 0, 0.2, 1) 0ms;visibility:hidden}revo-dropdown fieldset legend>span{display:inline-block;padding-left:5px;padding-right:5px}revo-dropdown.shrink label{-webkit-transform:translate(14px, -6px) scale(0.75);transform:translate(14px, -6px) scale(0.75)}revo-dropdown.shrink legend{max-width:1000px;-webkit-transition:max-width 100ms cubic-bezier(0, 0, 0.2, 1) 50ms;transition:max-width 100ms cubic-bezier(0, 0, 0.2, 1) 50ms}revo-dropdown .arrow{width:9px;margin-top:5px;margin-left:5px;opacity:0.4}revo-dropdown .arrow-wrapper{width:15px;text-align:center}revo-dropdown.active label{color:#0089ff}revo-dropdown.active fieldset{border-color:#0089ff}.revo-dropdown-list{font-size:1em;font-family:"Roboto", "Helvetica", "Arial", sans-serif;font-weight:400;line-height:2em;letter-spacing:0.01em;position:absolute;-webkit-transition:opacity 250ms cubic-bezier(0.4, 0, 0.2, 1) 0ms, -webkit-transform 160ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;transition:opacity 250ms cubic-bezier(0.4, 0, 0.2, 1) 0ms, -webkit-transform 160ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;transition:opacity 250ms cubic-bezier(0.4, 0, 0.2, 1) 0ms, transform 160ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;transition:opacity 250ms cubic-bezier(0.4, 0, 0.2, 1) 0ms, transform 160ms cubic-bezier(0.4, 0, 0.2, 1) 0ms, -webkit-transform 160ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;z-index:999;display:none;opacity:0}.revo-dropdown-list.top .dropdown-inner{bottom:2px;-ms-flex-direction:column-reverse;flex-direction:column-reverse}.revo-dropdown-list.top .dropdown-inner .filter-box{margin-bottom:0}.revo-dropdown-list:not(.top) .dropdown-inner{top:2px;-ms-flex-direction:column;flex-direction:column}.revo-dropdown-list:not(.top) .dropdown-inner .filter-box{margin-top:0}.revo-dropdown-list .dropdown-inner{display:-ms-flexbox;display:flex;max-height:100%;position:absolute;padding:8px 0;-webkit-box-sizing:border-box;box-sizing:border-box;min-height:16px;min-width:16px;-webkit-box-shadow:0 0 14px 0 rgba(53, 64, 82, 0.05);box-shadow:0 0 14px 0 rgba(53, 64, 82, 0.05);border:1px solid rgba(0, 0, 0, 0.05);border-radius:4px;color:rgba(0, 0, 0, 0.87);overflow:hidden;background-color:#fff}.revo-dropdown-list .dropdown-inner .filter-box{border:1px solid #ececec;min-height:30px;line-height:30px;margin:10px;border-radius:6px}.revo-dropdown-list .dropdown-inner .filter-box:focus{outline:none;border-color:#0089ff}',h=function(){function e(e){(0,o.r)(this,e),this.changeValue=(0,o.c)(this,"changed",7),this.close=(0,o.c)(this,"close",7),this.open=(0,o.c)(this,"open",7),this.uuid="",this.isClosing=!1,this.currentItem=null,this.isVisible=!1,this.autoClose=!0,this.source=[],this.placeholder="Select",this.appendTo="body",this.hasFilter=!0,this.autocomplete=!1,this.autoFocus=!1}return e.prototype.doClose=function(e){return void 0===e&&(e=!1),r(this,void 0,void 0,(function(){var t;return n(this,(function(i){return!e&&(t=this.close.emit(),t.defaultPrevented)||(this.isClosing=!0,this.isVisible=!1),[2]}))}))},e.prototype.doOpen=function(){return r(this,void 0,void 0,(function(){var e;return n(this,(function(t){return e=this.open.emit(),e.defaultPrevented||(this.isVisible=!0),[2]}))}))},e.prototype.doChange=function(e,t){return r(this,void 0,void 0,(function(){return n(this,(function(i){return this.value=a(e,this.dataId),this.changeValue.emit({val:this.value,originalEvent:t}),this.autocompleteInput&&(this.autocompleteInput.value=l(this.currentItem,this.dataLabel)),this.autoClose&&this.isVisible&&this.doClose(),[2]}))}))},e.prototype.onMouseUp=function(e){var t;if(this.isVisible&&!e.defaultPrevented){var i=!(null===(t=e.target)||void 0===t?void 0:t.closest("["+s+'="'+this.uuid+'"]'));i&&this.doClose()}},e.prototype.onKey=function(e){switch(e.code){case"Escape":e.preventDefault(),this.doClose();break}},e.prototype.onValueChanged=function(e){this.currentItem=this.getValue(e)},e.prototype.componentWillLoad=function(){this.value&&(this.currentItem=this.value)},e.prototype.connectedCallback=function(){this.uuid=this.uuidv4((new Date).getTime())+"-rvdropdown","undefined"!==typeof this.value&&this.onValueChanged(this.value)},e.prototype.disconnectedCallback=function(){this.doClose(!0)},e.prototype.componentDidRender=function(){var e=this;this.dropdown&&"body"===this.appendTo&&document.body.appendChild(this.dropdown),this.isVisible&&this.updateStyles(),this.dropdownInput&&this.dropdownInput.focus(),this.autoFocus&&this.autocomplete&&setTimeout((function(){var t;return null===(t=e.autocompleteInput)||void 0===t?void 0:t.focus()}),0)},e.prototype.renderDropdown=function(){var e,t=this;return(0,o.h)("div",{class:"revo-dropdown-list",ref:function(e){return t.dropdown=e}},(0,o.h)("div",Object.assign({},(e={},e[s]=this.uuid,e),{class:"dropdown-inner",ref:function(e){return t.dropdownInner=e}}),this.hasFilter&&!this.autocomplete?(0,o.h)(u,{ref:function(e){return t.dropdownInput=e},source:this.source,filter:this.filter,dataLabel:this.dataLabel,value:this.currentFilter||"",filterValue:this.currentFilter||"",onFilterChange:function(e){var i;t.currentFilter=e.value,t.currentSource=e.items,null===(i=t.revoList)||void 0===i||i.refresh(t.currentSource)}}):void 0,(0,o.h)("revo-list",{ref:function(e){return t.revoList=e},isFocused:!0,sourceItems:this.currentSource,dataLabel:this.dataLabel,onChanged:function(e){return t.doChange(e.detail.item,e.detail.e)}})))},e.prototype.renderSelect=function(){var e=this.currentItem&&l(this.currentItem,this.dataLabel)||"";return(0,o.h)("input",{type:"text",disabled:!0,class:"filter-box",value:e})},e.prototype.renderAutocomplete=function(){var e=this,t=this.currentItem?l(this.currentItem,this.dataLabel):"";return(0,o.h)(u,{ref:function(t){return e.autocompleteInput=t},autocomplete:"true",source:this.source,filter:this.filter,dataLabel:this.dataLabel,value:t,filterValue:this.currentFilter,onKeyDown:function(t){if(!e.isVisible)switch(t.code){case"ArrowUp":case"ArrowDown":t.preventDefault(),e.showAutoComplete();break}},onInput:function(){return e.showAutoComplete()},onFocus:function(){return e.showAutoComplete()},onClick:function(){return e.showAutoComplete()},onFilterChange:function(t){var i;e.currentFilter=t.value,e.currentSource=t.items,null===(i=e.revoList)||void 0===i||i.refresh(e.currentSource)}})},e.prototype.render=function(){var e,t,i,r=this;this.isVisible&&(i=this.renderDropdown());var n=(e={},e[s]=this.uuid,e.class={active:this.isVisible,shrink:this.isVisible||!!this.currentItem||!!(null===(t=this.autocompleteInput)||void 0===t?void 0:t.value)},e.ref=function(e){return r.element=e},e.onClick=function(e){return r.selectClick(e)},e);return this.autocomplete&&(n["autocomplete"]=!0),(0,o.h)(o.H,Object.assign({},n),(0,o.h)("label",null,this.placeholder),(0,o.h)("div",{class:"rv-dr-root"},this.autocomplete?this.renderAutocomplete():this.renderSelect(),(0,o.h)("span",{class:"actions"},(0,o.h)(d,null)),(0,o.h)("fieldset",null,(0,o.h)("legend",null,(0,o.h)("span",null,this.placeholder)))),i)},e.prototype.showAutoComplete=function(){this.isVisible||this.isClosing||(this.isVisible=!0),this.isClosing=!1},e.prototype.getValue=function(e){for(var t in this.source){var i=this.source[t];if(e==a(i,this.dataId))return i}return null},e.prototype.selectClick=function(e){e.defaultPrevented||(this.isVisible?this.doClose():this.doOpen())},e.prototype.updateStyles=function(){if(this.dropdown){var e=this.element.getBoundingClientRect(),t=e.top,i=e.left,o=e.height,r=this.clientRectangle(),n=t+o+r.top,s={opacity:1,display:"block"};n>r.centerY?(s.top=n-o+"px",s.maxHeight=n-o-r.top-50,this.dropdown.classList.add("top")):(s.top=n+"px",s.maxHeight=r.bottom-n-50,this.dropdown.classList.remove("top"));var l=i+r.left,a=r.right-(l+this.dropdown.clientWidth);for(var c in a<0&&(l+=a),s.left=l+"px",this.dropdownInner.style.maxHeight=Math.min(s.maxHeight,this.maxHeight||s.maxHeight)+"px",this.dropdownInner.style.maxWidth=s.maxWidth,s)this.dropdown.style[c]=s[c]}},e.prototype.clientRectangle=function(){var e={top:window.pageYOffset||document.documentElement.scrollTop||document.body.scrollTop,bottom:0,centerY:0,height:document.body.clientHeight,left:window.pageXOffset||document.documentElement.scrollLeft||document.body.scrollLeft,right:0,width:document.body.clientWidth,centerX:0};return e.bottom=e.top+e.height,e.right=e.left+e.width,e.centerY=e.top+e.height/2,e.centerX=e.left+e.width/2,e},e.prototype.uuidv4=function(e){return(e+"-xx-y").replace(/[xy]/g,(function(e){var t=16*Math.random()|0,i="x"==e?t:3&t|8;return i.toString(16)}))},Object.defineProperty(e,"watchers",{get:function(){return{value:["onValueChanged"]}},enumerable:!1,configurable:!0}),e}();h.style=p;var f="revo-list{overflow-x:hidden;overflow-y:auto;max-height:100%;display:block}revo-list ul{margin:0;padding:0;outline:0;list-style:none}revo-list ul>li{width:auto;overflow:hidden;font-size:14px;-webkit-box-sizing:border-box;box-sizing:border-box;min-height:48px;font-weight:400;line-height:1.5;padding-top:6px;white-space:nowrap;padding-bottom:6px;padding-left:16px;padding-right:16px;display:-ms-flexbox;display:flex;position:relative;text-align:left;-ms-flex-align:center;align-items:center;-ms-flex-pack:start;justify-content:flex-start;text-decoration:none;cursor:pointer}revo-list ul>li.selected{background-color:rgba(0, 0, 0, 0.04)}revo-list ul>li:hover{background-color:rgba(0, 0, 0, 0.04)}",m=function(){function e(e){(0,o.r)(this,e),this.changed=(0,o.c)(this,"changed",3),this.currentItem=0,this.sourceItems=[],this.isFocused=!1}return e.prototype.onKey=function(e){var t;if(this.isFocused)switch(e.code){case"ArrowUp":if(e.preventDefault(),this.currentItem<=0)return;this.currentItem--;break;case"ArrowDown":e.preventDefault(),this.sourceItems[this.currentItem+1]&&this.currentItem++;break;case"Tab":e.preventDefault(),t=this.sourceItems[this.currentItem],t&&this.changed.emit({item:t,e:e});break;case"Enter":e.preventDefault(),t=this.sourceItems[this.currentItem],t&&this.changed.emit({item:t,e:e});break}},e.prototype.refresh=function(e){return r(this,void 0,void 0,(function(){return n(this,(function(t){return this.sourceItems=e,[2]}))}))},e.prototype.componentDidRender=function(){var e;null===(e=this.selectedEl)||void 0===e||e.scrollIntoView({block:"nearest",inline:"nearest"})},e.prototype.render=function(){var e=this;this.selectedEl=void 0;var t=[],i=function(i){var n=r.sourceItems[i],s=parseInt(i)===r.currentItem,a={class:{selected:s},ref:function(t){s&&(e.selectedEl=t)},onClick:function(t){return e.changed.emit({item:n,e:t})}},c=(0,o.h)("li",Object.assign({},a),l(n,r.dataLabel));t.push(c)},r=this;for(var n in this.sourceItems)i(n);return(0,o.h)("ul",null,t)},e}();m.style=f}}]);
//# sourceMappingURL=8.580f6f92.js.map