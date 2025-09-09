<html data-loomi-loaded="true"><head><script formula-runtime="">function e(e){for(var r=1;r<arguments.length;r++){var t=null!=arguments[r]?arguments[r]:{},n=Object.keys(t);"function"==typeof Object.getOwnPropertySymbols&&(n=n.concat(Object.getOwnPropertySymbols(t).filter(function(e){return Object.getOwnPropertyDescriptor(t,e).enumerable}))),n.forEach(function(r){var n;n=t[r],r in e?Object.defineProperty(e,r,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[r]=n})}return e}function r(e,r){return r=null!=r?r:{},Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):(function(e,r){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t.push.apply(t,n)}return t})(Object(r)).forEach(function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}),e}var t,n,a,o=function(t){var n="4.0.16",a="xhs-pc-web",o="4.79.0";return r(e({},t),{context_artifactName:"formula",context_artifactVersion:n||"unknown",measurement_data:r(e({},t.measurement_data),{packageName:a||"unknown",packageVersion:o||"unknown"})})},i=function(){if("undefined"!=typeof window){var e,r,t=null===(e=window.eaglet)||void 0===e?void 0:e.push;return t||(t=null===(r=window.insight)||void 0===r?void 0:r.push),t?function(e){return t(o(e),"ApmXrayTracker")}:void 0}},c="FORMULA_ASSETS_LOAD_ERROR",u=function(){var e=localStorage.getItem(c);return e?JSON.parse(e):[]};function s(e){try{var r=i();if(r)r(e);else{var t=u();if(t.length>=1e3)return;t.push(e),localStorage.setItem(c,JSON.stringify(t))}}catch(r){console.error({error:r,errorData:e})}}try{t=function(e,r,t){var a,o=function(e){if(e){var r="//fe-static.xhscdn.com";return -1!==e.indexOf(r)?"".concat(e.replace(r,"//cdn.xiaohongshu.com"),"?business=fe&scene=feplatform"):void 0}}(e);if(!o){s({measurement_name:"reload_resource_error",measurement_data:n(t,{retryErrorType:"newUrlError",timestamp:String(Date.now())})});return}"js"===r?(a=document.createElement("script")).src=o:"css"===r&&((a=document.createElement("link")).rel="stylesheet",a.href=o),a&&(a.dataset.formulaAssetRetry="1",document.head.appendChild(a),a.addEventListener("load",function(){s({measurement_name:"reload_resource_duration",measurement_data:n(t,{duration:Date.now()-new Date(Number(t.timestamp)).getTime(),retryResourceUrl:a.src||a.href})})}),a.addEventListener("error",function(){s({measurement_name:"reload_resource_error",measurement_data:n(t,{timestamp:String(Date.now()),retryErrorType:"retryOnloadError",retryResourceUrl:a.src||a.href})})}))},n=Object.assign,a=["resource/js/bundler-runtime.5d1b11a9.js","resource/js/vendor-dynamic.77f9fe85.js","resource/js/library-polyfill.46cc9284.js","resource/js/vendor.04bda7f0.js","resource/css/index.441c4d3c.css","resource/js/index.4a7dae10.js","resource/css/async/Note.12c00534.css","resource/css/async/Notification.aa311d0c.css","resource/css/async/42.1b2bf9e1.css","resource/css/async/FeedToNote.a47e232f.css","resource/css/async/minor.a7f732ec.css","resource/css/async/355.1a9a769f.css","resource/css/async/937.de1aa713.css","resource/css/async/Explore.30c1e8ce.css","resource/css/async/NPS.0fee7ba1.css","resource/css/async/User.3830129f.css","resource/css/async/953.272459c1.css","resource/css/async/75.693a9a9c.css","resource/css/async/772.db47c221.css","resource/css/async/Login.c2772494.css","resource/css/async/Board.c56ea05c.css","resource/css/async/Search.84e03d37.css"],window.addEventListener("error",function(e){var r,n,o=e.target;if(o){var i=o.href||o.src;if(i){if(!(null===(r=o.dataset)||void 0===r?void 0:r.formulaCdnRetry)&&!a.some(function(e){return i.includes(e)}))return;var c=null===(n=o.dataset)||void 0===n?void 0:n.formulaAssetRetry,u="LINK"===o.tagName?"css":"js",l={measurement_name:"biz_load_error_count",measurement_data:{path:window.location.href,resourceType:u,resourceUrl:o.href||o.src||"-",timestamp:String(Date.now())}};c||(s(l),t(i,u,l.measurement_data))}}},!0),window.addEventListener("load",function(){try{var e=i();if(!e)return;var r=u();if(r.length>0){var t=!0,n=!1,a=void 0;try{for(var o,s=r[Symbol.iterator]();!(t=(o=s.next()).done);t=!0){var l=o.value;e(l)}}catch(e){n=!0,a=e}finally{try{t||null==s.return||s.return()}finally{if(n)throw a}}}localStorage.removeItem(c)}catch(e){console.error(e)}})}catch(e){console.error("formula assets retry error: ",e)}</script><script data-apm-fmp-pre-module="">!function(e,r){try{var n="__FST__",t=["HTML","HEAD","META","LINK","SCRIPT","STYLE","NOSCRIPT"];e[n]=e[n]||{runned:!1,observer:null,mutaRecords:[],imgObserver:null,imgRecords:[],run:function(n){try{!n.runned&&(n.runned=!0,e.MutationObserver&&e.performance&&e.performance.now&&(n.observer=new e.MutationObserver((function(r){try{n.mutaRecords.push({mutations:r,startTime:e.performance.now()}),r.filter((function(e){var r=(e.target.nodeName||"").toUpperCase();return"childList"===e.type&&r&&-1===t.indexOf(r)&&e.addedNodes&&e.addedNodes.length})).forEach((function(r){[].slice.call(r.addedNodes,0).filter((function(e){var r=(e.nodeName||"").toUpperCase();return 1===e.nodeType&&"IMG"===r&&e.isConnected&&!e.closest("[fmp-ignore]")&&!e.hasAttribute("fmp-ignore")})).forEach((function(r){r.addEventListener("load",(function(){try{var t=e.performance.now(),o=r.getAttribute("src")||"";e.requestAnimationFrame((function i(a){try{r&&r.naturalWidth&&r.naturalHeight?n.imgRecords.push({name:o.split(":")[1]||o,responseEnd:a,loadTime:t,startTime:0,duration:0,type:"loaded"}):e.requestAnimationFrame(i)}catch(e){}}))}catch(e){}}))}))}))}catch(e){}})),n.observer.observe(r,{childList:!0,subtree:!0}),e.PerformanceObserver&&(n.imgObserver=new e.PerformanceObserver((function(e){try{e.getEntries().filter((function(e){return"img"===e.initiatorType||"css"===e.initiatorType||"link"===e.initiatorType})).forEach((function(e){n.imgRecords.push({name:e.name.split(":")[1]||e.name,responseEnd:e.responseEnd,startTime:e.startTime,duration:e.duration,type:"entry"})}))}catch(e){}})),n.imgObserver.observe({entryTypes:["resource"]}))))}catch(e){}}},e[n].runned||e[n].run(e[n])}catch(e){}}(window,document)</script><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,minimum-scale=1,maximum-scale=1,user-scalable=no,viewport-fit=cover"><meta name="format-detection" content="telephone=no,address=no,email=no"><meta name="mobileOptimized" content="width"><meta name="HandheldFriendly" content="true"><meta name="applicable-device" content="pc,mobile"><meta http-equiv="X-UA-Compatible" content="IE=Edge,chrome=1"><meta http-equiv="Cache-Control" content="no-transform"><meta http-equiv="Cache-Control" content="no-siteapp"><meta name="mobile-web-app-capable" content="yes"><meta name="apple-mobile-web-app-status-bar-style" content="black"><meta name="shenma-site-verification" content="3abbfaac4345ca4daaa5ad2282115298_1476771175"><meta name="360-site-verification" content="86dcc68a445e2ed8034e85f0ba88a83a"><meta name="sogou-site-verification" content="tJLhUJDcki"><meta name="google-site-verification" content="-wdhMjIAPXapbEjwFVejIM-GCtl1fc9nUdOA32eFqpM"><meta name="baidu-site-verification" content="code-IDjrix2R0M"><meta><script src="https://fe-static.xhscdn.com/as/v1/3e44/public/04b29480233f4def5c875875b6bdc3b1.js" defer="defer"></script><script src="https://fe-static.xhscdn.com/as/v1/3e44/public/a9ef723c54cfdb63556bffe75cf06ae7.js?s=sdt_source_init" defer="defer"></script><link rel="shortcut icon" href="https://fe-video-qc.xhscdn.com/fe-platform/ed8fe781ce9e16c1bfac2cd962f0721edabe2e49.ico"><script formula-runtime=""></script><script defer="defer" src="https://fe-static.xhscdn.com/formula-static/xhs-pc-web/public/resource/js/bundler-runtime.5d1b11a9.js"></script><script defer="defer" src="https://fe-static.xhscdn.com/formula-static/xhs-pc-web/public/resource/js/vendor-dynamic.77f9fe85.js"></script><script defer="defer" src="https://fe-static.xhscdn.com/formula-static/xhs-pc-web/public/resource/js/library-polyfill.46cc9284.js"></script><script defer="defer" src="https://fe-static.xhscdn.com/formula-static/xhs-pc-web/public/resource/js/vendor.04bda7f0.js"></script><script defer="defer" src="https://fe-static.xhscdn.com/formula-static/xhs-pc-web/public/resource/js/index.4a7dae10.js"></script><style type="text/css">.reds-icon[data-v-55b36ac6]{display:inline-block;vertical-align:middle;fill:currentColor}
.reds-mask[data-v-54eb1bb4]{position:absolute;top:0;left:0;width:100%;height:100%;background-color:var(--mask-backdrop);z-index:-1}
.reds-lock-scroll,.reds-lock-scroll body,.reds-lock-scroll #app{overflow:hidden !important}
.reds-modal[data-v-f9867710]{display:flex;align-items:center;justify-content:center;position:fixed;top:0;left:0;width:100%;height:100%;z-index:1000002;box-sizing:border-box}.reds-modal[data-v-f9867710]{visibility:hidden;opacity:0;transition:opacity 200ms,visibility 200ms}.reds-modal-open[data-v-f9867710]{visibility:visible;opacity:1}
.reds-dialog-paper[data-v-fa27eb18]{box-sizing:border-box;background-color:var(--elevation-high-background)}.reds-dialog-paper[data-v-fa27eb18]:focus{outline:none}.reds-dialog-paper-bottom[data-v-fa27eb18]{position:absolute;left:0;right:0;bottom:0;margin-left:auto;margin-right:auto;width:100%;border-radius:12px 12px 0 0}.reds-dialog-paper-middle[data-v-fa27eb18]{border-radius:12px;width:270px;position:relative}.reds-dialog-paper-right[data-v-fa27eb18]{position:absolute;top:0;right:0;bottom:0;width:80%;max-width:450px}.reds-dialog-paper-middle[data-v-fa27eb18]{transition:transform 200ms cubic-bezier(.42,0,.58,1);transform:translate3d(0,16px,0)}.reds-modal-open .reds-dialog-paper-middle[data-v-fa27eb18]{transform:translate3d(0,0,0)}.reds-dialog-paper-bottom[data-v-fa27eb18]{transition:transform 200ms cubic-bezier(.42,0,.58,1);transform:translate3d(0,100%,0)}.reds-modal-open .reds-dialog-paper-bottom[data-v-fa27eb18]{transform:translate3d(0,0,0)}.reds-dialog-paper-right[data-v-fa27eb18]{transition:transform 200ms cubic-bezier(.42,0,.58,1);transform:translate3d(100%,0,0)}.reds-modal-open .reds-dialog-paper-right[data-v-fa27eb18]{transform:translate3d(0,0,0)}
.reds-text.left[data-v-a847e398]{text-align:left}.reds-text.center[data-v-a847e398]{text-align:center}.reds-text.right[data-v-a847e398]{text-align:right}.reds-text.line-clamp-1[data-v-a847e398]{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}.reds-text.line-clamp-2[data-v-a847e398],.reds-text.line-clamp-3[data-v-a847e398],.reds-text.line-clamp-4[data-v-a847e398]{word-break:break-all;display:-webkit-box;-webkit-box-orient:vertical;overflow:hidden}.reds-text.line-clamp-2[data-v-a847e398]{-webkit-line-clamp:2}.reds-text.line-clamp-3[data-v-a847e398]{-webkit-line-clamp:3}.reds-text.line-clamp-4[data-v-a847e398]{-webkit-line-clamp:4}.reds-text.fs10[data-v-a847e398]{font-size:12PX;transform-origin:0 50%;transform:scale(.8333333333333334)}.reds-text.fs10.center[data-v-a847e398]{transform-origin:50% 50%}.reds-text.fs10.right[data-v-a847e398]{transform-origin:100% 50%}.fw400[data-v-a847e398]{font-weight:400}.fw600[data-v-a847e398]{font-weight:600}.ff_number[data-v-a847e398]{font-family:vars('RED Number')}.ff_number_medium[data-v-a847e398]{font-family:vars('RED Number Medium')}.ff_number_bold[data-v-a847e398]{font-family:vars('RED Number Bold')}.fs10[data-v-a847e398]{font-size:10px}.fs12[data-v-a847e398]{font-size:12px}.fs14[data-v-a847e398]{font-size:14px}.fs16[data-v-a847e398]{font-size:16px}.fs18[data-v-a847e398]{font-size:18px}.fs20[data-v-a847e398]{font-size:20px}.fs24[data-v-a847e398]{font-size:24px}.fs32[data-v-a847e398]{font-size:32px}.lh12[data-v-a847e398]{line-height:12px}.lh16[data-v-a847e398]{line-height:16px}.lh18[data-v-a847e398]{line-height:18px}.lh20[data-v-a847e398]{line-height:20px}.lh22[data-v-a847e398]{line-height:22px}.lh24[data-v-a847e398]{line-height:24px}.lh26[data-v-a847e398]{line-height:26px}.lh28[data-v-a847e398]{line-height:28px}.lh30[data-v-a847e398]{line-height:30px}.lh32[data-v-a847e398]{line-height:32px}.lh38[data-v-a847e398]{line-height:38px}.lh40[data-v-a847e398]{line-height:40px}.lh52[data-v-a847e398]{line-height:52px}
.reds-dialog-button[data-v-93fd2b7e]{position:relative;height:48px;width:100%;white-space:nowrap;padding:8px 16px;display:flex;box-sizing:border-box;align-items:center;justify-content:center;background-color:transparent;border:none;cursor:pointer}.reds-dialog-button[data-v-93fd2b7e]:active{background-color:var(--color-tertiary-label)}.reds-dialog-button.primary[data-v-93fd2b7e]{color:var(--color-red)}.reds-dialog-button.secondary[data-v-93fd2b7e]{color:var(--color-tertiary-label)}
.reds-dialog-button-group[data-v-f6941e10]{margin-top:20px;display:flex;position:relative}.reds-dialog-button-group.row[data-v-f6941e10]{flex-direction:row}.reds-dialog-button-group.row[data-v-f6941e10] .reds-dialog-button{flex:1}.reds-dialog-button-group.column[data-v-f6941e10]{flex-direction:column}.reds-dialog-button-group.row[data-v-f6941e10] .reds-dialog-button + .reds-dialog-button::before{content:"";position:absolute;background-color:var(--color-primary-label);opacity:.1;top:0;left:0;width:1PX;height:100%;transform:translateX(-.5PX) scaleX(.5)}.reds-dialog-button-group[data-v-f6941e10]::before,.reds-dialog-button-group.column[data-v-f6941e10] .reds-dialog-button + .reds-dialog-button::before{content:"";position:absolute;background-color:var(--color-primary-label);opacity:.1;left:0;top:0;width:100%;height:1PX;transform:translateY(-.5PX) scaleY(.5)}
.reds-dialog-title{padding-left:20px;padding-right:20px;margin-bottom:4px}
.reds-dialog-content{margin-top:20px;margin-bottom:20px;padding-left:20px;padding-right:20px}
.reds-image-container{position:relative;display:inline-block;vertical-align:middle}.reds-image-container.white{background-color:#fff}.reds-image-container.gray{background-color:#f5f5f5}.reds-image-container.transparent{background:transparent}.reds-image-container .loading{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%)}.reds-image-container.responsive,.reds-img-placeholder{display:block}.reds-img-box,.reds-img{position:absolute;top:0;left:0;width:100%;height:100%;border-radius:inherit}.reds-img{object-fit:cover}.reds-img:not([data-load-status='loaded']){visibility:hidden}.reds-img.animated{opacity:0;transition-duration:150ms;transition-timing-function:ease-out}.reds-img.animated[data-load-status='loaded']{opacity:1}
.reds-progress-indicator{display:inline-block}.reds-progress-indicator__media-box{position:relative;width:40px;height:40px}.reds-progress-indicator__media-box__text{color:#333;width:25px;height:16px;position:absolute;font-size:$FontSizeT3;line-height:16px;-webkit-user-select:none;user-select:none;top:16px;left:12px}.reds-progress-indicator__media-box-circle{transform:rotate(-90deg)}.reds-progress-indicator__media-box-circle--inactive{stroke:var(--color-border)}.reds-progress-indicator__media-spinner{display:flex;justify-content:center;align-items:center;width:24px;height:24px}.reds-progress-indicator__media-spinner__icon path{transform-origin:50% 50%;animation:reds-progress-indicator-spinner-rotate 1.5s linear infinite;fill:#333}.reds-progress-indicator__activity-indicator{width:24px;height:24px}.reds-progress-indicator__page-loading{z-index:999;width:22px;height:22px}.reds-progress-indicator__page-loading.has-background{width:44px;height:44px;background-color:var(--color-active-background);border-radius:8px}@keyframes reds-progress-indicator-spinner-rotate{from{transform:rotate(0deg)}to{transform:rotate(360deg)}}
.reds-avatar-live{position:absolute;left:50%;bottom:0;font-style:normal;white-space:nowrap;border-radius:60PX;transform:translate(-50%,50%) scale(.5);color:rgba(255,255,255,0.99);background-color:#ff2e4d;overflow:hidden}.reds-avatar-live-animation::before{content:"";border-radius:60PX;position:absolute;width:10px;height:50px;left:-100px;background-image:linear-gradient(to right,transparent,rgba(255,255,255,0.5),transparent);animation:searchLights .6s ease-in .1s 2}.reds-avatar.size-s .reds-avatar-live{font-size:14px;line-height:20px;padding:0 6px;margin-bottom:2px}.reds-avatar.size-m .reds-avatar-live{font-size:16px;line-height:24px;padding:0 8px;margin-bottom:2px}.reds-avatar.size-l .reds-avatar-live{font-size:20px;line-height:32px;padding:0 12px;margin-bottom:2px}.reds-avatar.size-auto .reds-avatar-live,.reds-avatar.size-xl .reds-avatar-live{font-size:24px;line-height:40px;padding:0 16px;margin-bottom:3px}.reds-avatar .animated{animation:waveInSide 1.8s cubic-bezier(.4,.05,.6,.95) infinite}.reds-avatar .animated-outside{opacity:0;animation:waveOutSide 1.8s cubic-bezier(.5,.05,.95,.75) infinite}@keyframes searchLights{0%{left:-20px;top:0}100%{left:100%;top:0}}@keyframes waveInSide{0%{transform:scale(1)}50%{transform:scale(1.1)}100%{transform:scale(1)}}@keyframes waveOutSide{0%{transform:scale(1.1);opacity:0}50%{transform:scale(1.1);opacity:0}51%{transform:scale(1.1);opacity:1}75%{border-width:1px;opacity:1}100%{transform:scale(1.2);border-width:0;box-shadow:inset 0 0 0 .5px currentColor;opacity:0}}
.reds-avatar{position:relative;border-radius:1000PX;color:#fff;background-color:currentColor;box-shadow:0 0 1PX rgba(204,204,204,0.1);display:inline-block;vertical-align:middle}.reds-avatar-img-box{position:absolute;top:0;left:0;width:100%;height:100%;display:flex;border-radius:inherit;align-items:center;justify-content:center;overflow:hidden}.reds-avatar-img-box img{object-fit:cover;display:block;height:100%;width:100%}.reds-avatar.responsive{display:inline-block}.reds-avatar.size-auto{display:block;flex:1;min-width:0}.reds-avatar-border::before{content:"";display:block;padding-top:100%}.reds-avatar-border{position:absolute;top:-50%;left:-50%;width:200%;transform:scale(.5);border-radius:inherit;box-sizing:border-box}.reds-avatar-outline{position:absolute;border-radius:inherit;top:0;left:0;width:100%;box-sizing:border-box}.reds-avatar-outline::before{content:"";display:block;padding-top:100%}.reds-avatar-outline.red{color:#ff2e4d}.reds-avatar-outline.yellow{color:#ffe900}.reds-avatar-outline.white{color:#fff}.reds-avatar.size-s .reds-avatar-outline,.reds-avatar-outline.s{top:-1px;left:-1px;width:calc(100% + 2px);border:1PX solid currentColor}.reds-avatar.size-m .reds-avatar-outline,.reds-avatar-outline.m{top:-2px;left:-2px;width:calc(100% + 4px);border:1PX solid currentColor}.reds-avatar.size-l .reds-avatar-outline,.reds-avatar-outline.l{top:-3px;left:-3px;width:calc(100% + 6px);box-shadow:inset 0 0 0 1.5PX currentColor}.reds-avatar.size-auto .reds-avatar-outline,.reds-avatar.size-xl .reds-avatar-outline,.reds-avatar-outline.xl{box-shadow:inset 0 0 0 1.5PX currentColor;top:-3px;left:-3px;width:calc(100% + 6px)}
.reds-dialog-avatar[data-v-077434fe]{margin:0 auto 16px}.reds-dialog-avatar.responsive.reds-avatar[data-v-077434fe]{display:block}
.reds-button-new{position:relative;cursor:pointer;-webkit-user-select:none;user-select:none;white-space:nowrap;outline:none;background:none;border:none;vertical-align:middle;text-align:center;display:inline-block;padding:0;border-radius:100px;font-weight:500}.reds-button-new-box{display:flex;align-items:center;justify-content:center;position:relative;font-weight:500}.reds-button-new.primary{background-color:#ff2e4d;color:#fff}.reds-button-new.primary.active{color:#000;background-color:rgba(0,0,0,0.04)}.reds-button-new.outlined{background-color:#fff;color:#ff2e4d;border:1px solid #ff2e4d}.reds-button-new.outlined.active{color:#000;border-color:rgba(0,0,0,0.1)}.reds-button-new.outlined.disabled{color:var(--color-quaternary-label);border:1px solid var(--color-quaternary-label)}.reds-button-new.text{border:none;background:var(--elevation-high-background);color:#ff2e4d}.reds-button-new.text.active{background-color:#000;color:$White;border:1px solid var(--color-border)}.reds-button-new.text.disabled{color:var(--color-quaternary-label)}.reds-button-new.dark{background-color:rgba(37,37,42,0.99);color:var(--color-inverted-label)}.reds-button-new.filledGray{background-color:var(--color-active-background)}.reds-button-new.filledGray.disabled{color:var(--color-quaternary-label)}.reds-button-new.outlinedGray{border:1px solid var(--color-border)}.reds-button-new.outlinedGray.disabled{color:var(--color-quaternary-label)}.reds-button-new.mini{font-size:$FontSizeT3;line-height:$LineHeightT3Label;padding:0 12px;height:24px}.reds-button-new.mini .reds-icon,.reds-button-new.mini img{width:16px;height:16px;margin-right:4px;font-size:$FontSizeT3}.reds-button-new.small{font-size:$FontSizeT3;line-height:$LineHeightT3Label;padding:0 14px;height:28px}.reds-button-new.small.text{height:$LineHeightT3Label}.reds-button-new.small .reds-icon,.reds-button-new.small img{width:16px;height:16px;margin-right:4px;font-size:$FontSizeT3}.reds-button-new.medium{font-size:$FontSizeT2;line-height:18px;padding:0 20px;height:36px}.reds-button-new.medium .reds-icon,.reds-button-new.medium img{width:20px;height:20px;margin-right:6px;font-size:$FontSizeT2}.reds-button-new.large{font-size:16px;font-weight:600;line-height:16px;padding:0 24px;height:40px}.reds-button-new.large.text{height:18px}.reds-button-new.large .reds-icon,.reds-button-new.large img{width:20px;height:20px;margin-right:8px;font-size:$FontSizeT2}.reds-button-new.extraLarge{font-size:16px;line-height:20px;padding:0 32px;height:48px}.reds-button-new.extraLarge.text{height:20px}.reds-button-new.extraLarge .reds-icon,.reds-button-new.extraLarge img{width:24px;height:24px;margin-right:10px;font-size:16px}.reds-button-new.mini.has-icon{padding-left:8px}.reds-button-new.small.has-icon{padding-left:10px}.reds-button-new.medium.has-icon{padding-left:12px}.reds-button-new.large.has-icon{padding-left:16px}.reds-button-new.extraLarge.has-icon{padding-left:20px}.reds-button-new.has-icon.pure-icon{border-radius:50%}.reds-button-new.has-icon.pure-icon .reds-button-new-box{padding:0}.reds-button-new.has-icon.pure-icon .reds-button__icon{margin-right:0}.reds-button-new.has-icon.pure-icon.mini{padding:0 4px}.reds-button-new.has-icon.pure-icon.small{padding:0 6px}.reds-button-new.has-icon.pure-icon.medium{padding:0 8px}.reds-button-new.has-icon.pure-icon.large{padding:0 10px}.reds-button-new.has-icon.pure-icon.extraLarge{padding:0 12px}.reds-button-new.block{display:block;width:100%}.dark-mode .reds-button-new.outlined{background-color:inherit}.dark-mode .reds-button-new.outlined.disabled{color:var(--color-quaternary-label);border-color:var(--color-quaternary-label)}.dark-mode .reds-button-new.filledGray,.dark-mode .reds-button-new.outlinedGray{color:#fff}.dark-mode .reds-button-new.text{background-color:#fff}.dark-mode .reds-button-new.disabled.filledGray,.dark-mode .reds-button-new.disabled.outlinedGray{color:var(--color-quaternary-label)}.reds-button-new.disabled{cursor:not-allowed}.reds-button-new.primary.disabled,.reds-button-new.dark.disabled{opacity:.6}.reds-button-new.text{padding:0}
.reds-alert-mask-slide-fade-enter-active,.reds-alert-mask-slide-fade-leave-active{transition:opacity .1s ease}.reds-alert-mask-slide-fade-enter-from,.reds-alert-mask-slide-fade-leave-to{opacity:0}.reds-alert-mask-fade-enter-active,.reds-alert-mask-fade-leave-active{transition:opacity .2s ease}.reds-alert-slide-fade-enter-from,.reds-alert-slide-fade-leave-to{opacity:0}.reds-alert{position:relative}.reds-alert .reds-alert-mask{position:fixed;top:0;left:0;z-index:99;width:100%;height:100%;background-color:var(--mask-backdrop)}.reds-alert .reds-alert-wrapper{position:fixed;z-index:999;top:50%;left:0;right:0;margin:0 auto;transform:translateY(-50%);width:270px;min-height:114px;overflow:hidden;border-radius:12px;max-width:calc(100vw - 16 * 2);background-color:var(--elevation-high-background);box-shadow:var(--elevation-high-shadow);-webkit-backface-visibility:hidden;backface-visibility:hidden}.reds-alert .reds-alert-wrapper.has-content .reds-alert-title{padding-bottom:4px}.reds-alert .reds-alert-wrapper.slot-content .reds-alert-title{padding-bottom:16px}.reds-alert .reds-alert-wrapper.has-media .reds-alert-title{padding-bottom:20px}.reds-alert .reds-alert-wrapper .reds-alert-title{color:var(--color-primary-label);padding-top:20px;padding-bottom:26px;font-weight:500;font-size:16px;line-height:26px;text-align:center}.reds-alert .reds-alert-wrapper .reds-alert-content{position:relative}.reds-alert .reds-alert-wrapper .reds-alert-content .reds-dialog__message__overlay{position:fixed;left:0;bottom:70px;width:100%;height:40px;background:linear-gradient(180deg,rgba(255,255,255,0) 0%,var(--color-primary-label) 100%)}.reds-alert .reds-alert-wrapper .reds-alert-content .reds-dialog__message{padding-top:8px;color:var(--color-tertiary-label);flex:1;max-height:120px;padding:0 20px 0 20px;overflow-y:auto;font-size:14px;line-height:20px;white-space:pre-wrap;text-align:center;word-wrap:break-word;margin-bottom:20px;text-wrap:balance}.reds-alert .reds-alert-wrapper .reds-alert-content .reds-dialog__message.left{text-align:left}.reds-alert .reds-alert-wrapper .reds-alert-footer{background:var(--elevation-high-background);border-top:1px solid var(--color-border);display:flex;align-items:center}.reds-alert .reds-alert-wrapper .reds-alert-footer.reds-alert-footer__round-button{border:none;padding:0 20px 20px 20px}.reds-alert .reds-alert-wrapper .reds-alert-footer.reds-alert-footer__round-button.vertical{padding-bottom:16px}.reds-alert .reds-alert-wrapper .reds-alert-footer.vertical.reds-alert-footer__round-button .reds-alert-footer__left.reds-button-new.text{height:16px;margin-top:12px}.reds-alert .reds-alert-wrapper .reds-alert-footer.vertical{flex-direction:column-reverse}.reds-alert .reds-alert-wrapper .reds-alert-footer.vertical .reds-alert-footer__left,.reds-alert .reds-alert-wrapper .reds-alert-footer.vertical .reds-alert-footer__right{width:100%}.reds-alert .reds-alert-wrapper .reds-alert-footer.vertical .reds-alert-footer__right::before{border-left:none;width:100%;height:1px;top:100%;transform:translateY(0);background-color:rgba(0,0,0,0.08)}.reds-alert .reds-alert-wrapper .reds-alert-footer.mono .reds-button-new.text .reds-button-new-text{color:var(--color-secondary-label);font-weight:400}.reds-alert .reds-alert-wrapper .reds-alert-footer .reds-alert-footer__left{width:50%}.reds-alert .reds-alert-wrapper .reds-alert-footer .reds-alert-footer__left.reds-button-new.text{height:48px}.reds-alert .reds-alert-wrapper .reds-alert-footer .reds-alert-footer__left .reds-button-new-text{color:var(--color-tertiary-label);font-weight:400}.reds-alert .reds-alert-wrapper .reds-alert-footer .reds-alert-footer__right{width:50%}.reds-alert .reds-alert-wrapper .reds-alert-footer .reds-alert-footer__right.reds-button-new.text{height:48px}.reds-alert .reds-alert-wrapper .reds-alert-footer .reds-alert-footer__right.block{width:100%}.reds-alert .reds-alert-wrapper .reds-alert-footer .reds-alert-footer__right::before{position:absolute;top:50%;left:0;width:1px;height:28px;border-left:1px solid rgba(0,0,0,0.08);transform:translateY(-50%);content:" "}.reds-alert .reds-alert-wrapper .reds-alert-footer .reds-alert-footer__right.rounded::before{opacity:0}.reds-alert .reds-alert-wrapper__media__asset{display:flex;justify-content:center;padding-top:20px}
[data-v-76bb4847] .reds-alert-mask{background-color:var(--mask-backdrop)}[data-v-76bb4847] .reds-alert-footer{border-top:1px solid var(--color-border);width:calc(100% - 12px);margin:0 auto;padding:6px 0 6px 0}[data-v-76bb4847] .reds-alert-title{color:var(--color-primary-label) !important;line-height:120%;padding-top:24px !important;font-weight:600 !important;line-height:normal !important}[data-v-76bb4847] .reds-alert-content{line-height:120%;font-size:16px}.foot-btns[data-v-76bb4847]{width:100%;display:flex;align-items:center;justify-content:center;flex-direction:column}.foot-btns .foot-btn[data-v-76bb4847]{width:100%;display:flex;align-items:center;justify-content:center;height:40px;font-weight:600;font-size:16px;cursor:pointer;color:var(--color-secondary-label)}.foot-btns .foot-btn.strong[data-v-76bb4847]{color:var(--color-red)}.foot-btns .foot-btn.strong[data-v-76bb4847]:hover{background:var(--color-tinted-red);color:var(--color-red)}.foot-btns .foot-btn[data-v-76bb4847]:hover{background-color:var(--color-active-background);border-radius:8px;color:var(--color-primary-label)}
.icon-btn-wrapper{width:var(--54fadfd9);height:var(--30922174);border-radius:999px;display:flex;align-items:center;justify-content:center;cursor:pointer;color:var(--color-secondary-label)}.icon-btn-wrapper:hover{border-radius:999px;color:var(--color-primary-label);background:var(--color-active-background)}
.reds-toast-container[data-v-16e62945]{transition:opacity 400ms}.fade-enter-active[data-v-16e62945]{opacity:1}.fade-leave-active[data-v-16e62945]{opacity:0}.reds-toast[data-v-16e62945]{font-size:16px;line-height:120%;font-weight:600;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;position:fixed;z-index:1001000;max-width:300px;pointer-events:none;border-radius:1000PX;padding:12px 16px;margin-top:4px;margin-bottom:4px;color:var(--color-inverted-label);background:var(--material-inverted-background);-webkit-backdrop-filter:var(--material-filter);backdrop-filter:var(--material-filter)}.top-left[data-v-16e62945]{top:5%;left:0}.top-center[data-v-16e62945]{top:5%;left:50%;transform:translateX(-50%)}.top-right[data-v-16e62945]{top:5%;right:0}.center[data-v-16e62945]{top:50%;left:50%;transform:translate(-50%,-50%)}.bottom-left[data-v-16e62945]{bottom:5%;left:0}.bottom-center[data-v-16e62945]{bottom:5%;left:50%;transform:translateX(-50%)}.bottom-right[data-v-16e62945]{bottom:5%;right:0}
.reds-sticky[data-v-73916935]{z-index:5 !important;background:var(--mask-paper)}.reds-sticky-box.sticky .reds-sticky[data-v-73916935]{position:fixed;z-index:10010;top:0;width:100%;box-sizing:border-box}
.reds-uploader__upload{position:relative;display:flex;flex-direction:column;align-items:center;justify-content:center;box-sizing:border-box;width:72px;height:72px;border-radius:8px;border:1px solid var(--color-border);color:var(--color-tertiary-label);font-size:12px;font-weight:400;line-height:120%}.reds-uploader__upload:hover{background:var(--color-active-background);color:var(--color-secondary-label)}.reds-uploader__upload.four{width:78px;height:78px}.reds-uploader__upload.three{width:109px;height:109px}.reds-uploader__upload.two{width:166px;height:94px}.reds-uploader__upload .reds-uploader__input{position:absolute;top:0;left:0;width:100%;height:100%;cursor:pointer;opacity:0;overflow:hidden}.reds-uploader__upload .reds-uploader__input.reds-uploader__input_disabled{cursor:not-allowed}.reds-uploader__upload .reds-uploader__desc{margin:0}.reds-uploader__upload .reds-uploader_input_desc{display:flex;align-items:center;justify-content:center;flex-direction:column;gap:6px;position:absolute;top:0;left:0;width:100%;height:100%}.reds-uploader__upload .reds-uploader_input_desc:hover{color:var(--color-secondary-label)}.reds-uploader__upload__add-icon path{fill:$ThemeDescription;fill-opacity:1}.reds-uploader__upload--disabled{opacity:.5;cursor:not-allowed}.reds-uploader__upload--disabled:hover{background:transparent;color:var(--color-tertiary-label);opacity:.5}.reds-uploader__upload--disabled .reds-uploader__desc{color:$ThemeDisabled}.reds-uploader__upload--disabled .reds-uploader__upload__add-icon path{fill:$ThemeDisabled}.reds-uploader__wrapper{display:flex;align-items:center;flex-wrap:wrap;gap:12px}.reds-uploader__wrapper .reds-uploader__preview{position:relative;border-radius:8px;border:1px solid var(--color-border)}.reds-uploader__wrapper .reds-uploader__preview.four:nth-of-type(4n){margin-right:0}.reds-uploader__wrapper .reds-uploader__preview.three:nth-of-type(3n){margin-right:0}.reds-uploader__wrapper .reds-uploader__preview.two{margin-right:0}.reds-uploader__wrapper .reds-uploader__preview.two:nth-of-type(2n){margin-right:0}.reds-uploader__wrapper .reds-uploader__preview.two:nth-of-type(2n)--narrowMargin{margin-bottom:0}.reds-uploader__wrapper .reds-uploader__preview__image{width:100%;height:100%}.reds-uploader__wrapper .reds-uploader__preview__image__content{border-radius:7px;width:100%;height:100%;visibility:visible}.reds-uploader__wrapper .reds-uploader__preview__delete{display:flex;align-items:center;justify-content:center;position:absolute;top:4px;right:4px;background:var(--material-background);padding:2px;cursor:pointer;color:var(--color-white);border-radius:4px;-webkit-backdrop-filter:var(--material-filter);backdrop-filter:var(--material-filter);width:20px;height:20px}.reds-uploader__wrapper .reds-uploader__preview__delete__icon path:first-of-type{fill:$ThemeFill4}.reds-uploader__wrapper .reds-uploader__preview__mask{position:absolute;top:0;right:0;bottom:0;left:0;display:flex;flex-direction:column;align-items:center;justify-content:center;background:$AlwaysDarkFill4;border-radius:6px;width:72px;height:72px;color:var(--color-tertiary-label);font-size:12px;font-weight:400;line-height:120%}.reds-uploader__wrapper .reds-uploader__preview__mask.four{width:100%;height:100%}.reds-uploader__wrapper .reds-uploader__preview__mask.three{width:100%;height:100%}.reds-uploader__wrapper .reds-uploader__preview__mask.two{width:100%;height:100%}.reds-uploader__wrapper .reds-uploader__preview__mask .reds-progress-indicator__media-spinner path{fill:$AlwaysLightFill5}.reds-uploader__wrapper .reds-uploader__preview__mask__msg{margin:0;margin-top:6px}.reds-uploader__wrapper .image_loading{color:var(--color-tertiary-label);width:100%;height:100%;font-size:12px;font-weight:400;line-height:120%;display:flex;align-items:center;justify-content:center;flex-direction:column;gap:6px}.reds-uploader__wrapper .image_loading .msg{margin:0}
.reds-tab-pane-list{display:flex;overflow-x:auto;overflow-y:hidden}.reds-tab-pane-list:empty{height:0}.reds-tab-pane-list::-webkit-scrollbar{display:none}.reds-tabs-list{display:flex;flex-wrap:nowrap;position:relative;font-size:16px}.reds-tabs-list::-webkit-scrollbar{display:none}.reds-tabs-list > .active-tag{position:absolute;height:40px;bottom:0;background-color:var(--color-active-background);border-radius:999px;pointer-events:none}.reds-tabs-list > .active-bar{position:absolute;bottom:.5em;height:2px;background-color:#ff2e4d;border-radius:2px;pointer-events:none}.reds-tabs-list > .reds-tab-item{display:flex;align-items:center;box-sizing:border-box;height:40px;cursor:pointer;color:var(--color-secondary-label);white-space:nowrap;transition:transform .3s cubic-bezier(.2,0,.25,1);z-index:1}.reds-tabs-list > .reds-tab-item.active{font-weight:600;color:var(--color-primary-label)}.reds-tabs-list.text > .reds-tab-item.active{transform:scale(1.28)}.reds-tabs-list.left{justify-content:flex-start}.reds-tabs-list.right{justify-content:flex-end}.reds-tabs-list.center{justify-content:center}.reds-tab-item{display:flex;align-items:center}
.divider[data-v-39ecb380]{margin:4px 8px;list-style:none;height:0;border-color:var(--color-border);border-style:solid;border-width:1px 0 0}
.badge-container[data-v-0755b6ef]{position:relative}.count[data-v-0755b6ef]{position:absolute;right:0;top:0;display:flex;align-items:center;justify-content:center;padding:0 4px;min-width:16px;height:16px;border-radius:999px;color:var(--color-white);background-color:var(--color-red);font-size:12px;font-weight:500;transform:translate(calc(100% - 4px),calc(-100% + 4px));z-index:1}
.dropdown-container[data-v-1b03e45c]{position:absolute;left:0;right:0;top:0;height:0;-webkit-user-select:none;user-select:none}.dropdown-items[data-v-1b03e45c]{padding:4px;background:var(--elevation-high-background);box-shadow:var(--elevation-high-shadow);border-radius:12px;min-width:192px;overflow:scroll;z-index:10;position:relative}
.title[data-v-6a50ee07]{height:32px;font-weight:400;font-size:12px;line-height:120%;display:flex;color:var(--color-tertiary-label);padding:9px 12px}
.dropdown-container[data-v-141cfafe]{position:fixed;z-index:10;left:0;right:0;top:0;height:0}.dropdown-items[data-v-141cfafe]{padding:4px;background:var(--elevation-high-background);box-shadow:var(--elevation-high-shadow);border-radius:12px;min-width:192px;overflow:scroll;z-index:10;position:relative}.right-icon[data-v-141cfafe]{visibility:hidden;opacity:0;transition:opacity .5s;color:var(--color-quaternary-label)}.text[data-v-141cfafe]{flex-grow:1;height:100%;display:flex;align-items:center;color:var(--color-secondary-label)}li[data-v-141cfafe]{list-style:none;height:40px;padding:0 12px;display:flex;align-items:center;width:100%;font-size:16px;cursor:pointer}li[data-v-141cfafe]:hover{background:var(--color-active-background);border-radius:8px;color:var(--color-primary-label)}li:hover .right-icon[data-v-141cfafe]{visibility:visible;opacity:1}li:hover .text[data-v-141cfafe]{color:var(--color-primary-label)}.done[data-v-141cfafe]{color:var(--color-primary-label)}.selected[data-v-141cfafe]{color:var(--color-primary-label);font-weight:600}.left-icon[data-v-141cfafe]{margin-right:4px;color:var(--color-tertiary-label)}
.msg-container[data-v-2a210922]{width:100%;padding:0 16px;height:56px;justify-content:space-between;align-items:center;border-radius:16px;background:var(--elevation-high-background);box-shadow:var(--elevation-high-shadow);display:flex;justify-content:space-between;font-size:16px;overflow:hidden;cursor:pointer}.msg-container:hover .right-area[data-v-2a210922]{color:var(--color-secondary-label)}.msg-container.fade-in[data-v-2a210922]{animation:fadeIn-2a210922 .15s linear}@keyframes fadeIn-2a210922{0%{opacity:0;transform:translateY(16px)}100%{opacity:1;transform:translateY(0)}}.msg-container.fade-out[data-v-2a210922]{animation:fadeOut-2a210922 .15s linear}@keyframes fadeOut-2a210922{0%{opacity:1;transform:translateY(0)}100%{opacity:0;transform:translateY(16px)}}.msg-container .left-area[data-v-2a210922]{display:flex;align-items:center;color:var(--color-primary-label)}.msg-container .left-area .text[data-v-2a210922]{margin-left:8px;font-weight:600}.msg-container .right-area[data-v-2a210922]{color:var(--color-tertiary-label);display:flex;align-items:center}
.text-limit[data-v-09155e13]{color:var(--color-tertiary-label)}.over-limit[data-v-09155e13]{color:var(--color-red)}
.input-basic[data-v-8da5899a]{display:flex;flex-direction:column}.input-basic.input-direction[data-v-8da5899a]{flex-direction:row}.input-label[data-v-8da5899a]{padding:0 4px;margin-bottom:8px;color:var(--color-secondary-label);font-size:14px;line-height:120%;font-weight:500;display:flex;justify-content:space-between}.input-wrapper[data-v-8da5899a]{background:var(--color-active-background);flex:1;border-radius:12px;min-height:40px;overflow:hidden}.input-wrapper-row[data-v-8da5899a]{background:transparent}.input-content[data-v-8da5899a]{width:100%;height:40px;padding:0 12px;caret-color:var(--color-red);color:var(--color-primary-label);font-size:16px}.input-contentplaceholder[data-v-8da5899a]{color:var(--color-quaternary-label);font-size:16px}.textarea-content[data-v-8da5899a]{caret-color:var(--color-red);width:100%;border:none;background:transparent;color:var(--color-primary-label);font-size:16px;padding:12px;resize:none;outline:none}.textarea-contentplaceholder[data-v-8da5899a]{color:var(--color-quaternary-label);font-size:16px}.limit-wrapper[data-v-8da5899a]{flex:0 0 auto;display:flex;align-items:center}
.dot-container[data-v-147b1aa0]{display:inline-flex;align-items:center;position:relative;cursor:pointer;border:1px solid var(--color-shadow-border);border-radius:999px;width:32px;height:20px;transition:all .15s;background-color:var(--color-active-background);justify-content:center}.dot-container .dot[data-v-147b1aa0]{fill:var(--color-white);filter:drop-shadow(0 4px 32px rgba(0,0,0,0.08)) drop-shadow(0 1px 4px rgba(0,0,0,0.04));transform:translateX(calc(-50% + 2px));transition:transform .15s}.dot-container.turn-on[data-v-147b1aa0]{background-color:var(--color-red)}.dot-container.turn-on .dot[data-v-147b1aa0]{transform:translateX(calc(50% - 2px))}.dot-container.disabled[data-v-147b1aa0]{opacity:.4;cursor:not-allowed}
.back-icon-tip-container[data-v-d33abd98]{position:absolute;width:73px;height:28px;padding:2px 4px 2px 8px;border:1px solid var(--color-border);box-shadow:var(--elevation-low-shadow);background:var(--elevation-low-background);font-size:12px;color:var(--color-secondary-label);display:flex;align-items:center;border-radius:8px;top:46px}@media screen and (max-width:959px){.back-icon-tip-container[data-v-d33abd98]{left:-4px}}.esc[data-v-d33abd98]{height:20px;color:var(--color-tertiary-label);padding:0 4px;display:flex;align-items:center;background:var(--color-active-background);border-radius:4px;margin-left:4px}
.close-box[data-v-6c30aded]{width:40px;height:40px;cursor:pointer;display:none;display:flex;justify-content:center;align-items:center;border-radius:100%;background:var(--color-background);color:var(--color-secondary-label);display:none;position:absolute;left:0;top:0;margin:12px;z-index:5}.close-box[data-v-6c30aded]:hover{background:var(--color-active-background);color:var(--color-primary-label)}@media screen and (min-width:696px) and (max-width:959px){.close-box[data-v-6c30aded]{display:flex}}@media screen and (max-width:695px){.close-box[data-v-6c30aded]{display:flex}}.close-circle[data-v-6c30aded]{position:fixed;display:flex;z-index:100;cursor:pointer}@media screen and (min-width:1728px){.close-circle[data-v-6c30aded]{left:32px;top:32px}}@media screen and (min-width:1424px) and (max-width:1727px){.close-circle[data-v-6c30aded]{left:32px;top:32px}}@media screen and (min-width:1192px) and (max-width:1423px){.close-circle[data-v-6c30aded]{left:24px;top:24px}}@media screen and (min-width:960px) and (max-width:1191px){.close-circle[data-v-6c30aded]{left:24px;top:24px}}@media screen and (min-width:696px) and (max-width:959px){.close-circle[data-v-6c30aded]{display:none}}@media screen and (max-width:695px){.close-circle[data-v-6c30aded]{display:none}}.close[data-v-6c30aded]{display:flex;align-items:center;justify-content:center;display:flex;justify-content:center;align-items:center;border-radius:100%;background:var(--color-background);color:var(--color-secondary-label);width:40px;height:40px;border-radius:40px;cursor:pointer;transition:all .3s}.close-mask-dark[data-v-6c30aded]{color:var(--color-white);background:var(--material-background);-webkit-backdrop-filter:var(--material-filter);backdrop-filter:var(--material-filter)}.explore-more[data-v-6c30aded]{background-color:var(--elevation-high-background);padding:0 12px 0 8px;display:flex;justify-content:center;align-items:center;border-radius:12px;box-shadow:var(--elevation-high-shadow);white-space:nowrap;height:40px}.triangle[data-v-6c30aded]{margin-top:8px;margin-left:2px;width:6px;z-index:5;color:var(--color-background);box-shadow:var(--elevation-high-shadow)}.text[data-v-6c30aded]{color:var(--color-primary-label);font-size:16px;font-weight:600;margin-left:8px}.mild.close-circle[data-v-6c30aded]{transition:none}@media screen and (min-width:1728px){.mild.close-circle[data-v-6c30aded]{top:calc(56px + 32px)}}@media screen and (min-width:1424px) and (max-width:1727px){.mild.close-circle[data-v-6c30aded]{top:calc(56px + 32px)}}@media screen and (min-width:1192px) and (max-width:1423px){.mild.close-circle[data-v-6c30aded]{top:calc(56px + 24px)}}@media screen and (min-width:960px) and (max-width:1191px){.mild.close-circle[data-v-6c30aded]{top:calc(56px + 24px)}}@media screen and (min-width:696px) and (max-width:959px){.mild.close-circle[data-v-6c30aded]{display:none}}@media screen and (max-width:695px){.mild.close-circle[data-v-6c30aded]{display:none}}.force-hidden[data-v-6c30aded]{display:none}.force-visible[data-v-6c30aded]{display:flex}
.course-video[data-v-23ff9ac6]{overflow:hidden}.course-video .animate[data-v-23ff9ac6]{width:100%;height:100%;object-fit:cover}.flex-center[data-v-23ff9ac6]{display:flex;align-items:center;justify-content:center}.course-trigger[data-v-23ff9ac6]{height:32px;display:flex;align-items:center;justify-content:center;border-radius:999px;padding-left:10px;padding-right:10px;font-size:14px;color:var(--color-secondary-label);cursor:pointer}.course-trigger .play[data-v-23ff9ac6]{margin-right:7px;color:var(--color-quaternary-label)}.course-trigger[data-v-23ff9ac6]:hover{color:var(--color-primary-label)}.tutorial[data-v-23ff9ac6]{background-color:var(--color-active-background)}
.access-container[data-v-7aee5252],.access-wrapper[data-v-7aee5252]{display:flex;align-items:center;justify-content:center;flex-direction:column}.title[data-v-7aee5252]{margin-bottom:32px;font-size:20px;font-weight:600;color:var(--color-primary-label)}.flex-center[data-v-7aee5252]{display:flex;align-items:center;justify-content:center}.tip-text[data-v-7aee5252]{display:flex;align-items:center;justify-content:center;font-weight:600;margin-top:16px;margin-bottom:18px;font-size:16px;color:var(--color-secondary-label)}.qrcode-box[data-v-7aee5252]{display:flex;align-items:center;justify-content:center;flex-direction:column}.qrcode-img-box[data-v-7aee5252]{position:relative;display:flex;align-items:center;justify-content:center;width:160px;height:160px;border:2px solid var(--color-shadow-border);border-radius:12px;box-shadow:var(--elevation-high-shadow);background:var(--color-white)}.qrcode-img-box .qrcode-img[data-v-7aee5252]{width:128px;height:128px}.bottom-btn-group[data-v-7aee5252]{display:flex;align-items:center;margin-top:16px}.feedback-btn[data-v-7aee5252]{padding:11px 17px;margin-right:16px;font-size:16px;text-align:center;cursor:pointer;color:var(--color-secondary-label)}.btn-close[data-v-7aee5252]{cursor:pointer;padding:10px 16px;border-radius:20px;font-size:16px;border:1px solid var(--color-border);color:var(--color-secondary-label)}
[data-v-5f656e39] .full-page .reds-mask{background:transparent}[data-v-5f656e39] .access-modal.gray{filter:grayscale(0.95)}.fade-enter-active[data-v-5f656e39],.fade-leave-active[data-v-5f656e39]{transition:all .2s}.fade-enter-from[data-v-5f656e39],.fade-leave-to[data-v-5f656e39]{opacity:0}.fade-enter-from .access-modal-content[data-v-5f656e39],.fade-leave-to .access-modal-content[data-v-5f656e39]{transform:translateY(5px)}.access-modal-content[data-v-5f656e39]{display:flex;justify-content:center;position:relative;background:var(--elevation-high-background);border-radius:20px;box-shadow:var(--elevation-high-shadow);transition:transform .2s;transition:height .6s}@media screen and (min-width:1728px){.access-modal-content[data-v-5f656e39]{height:calc(100% - 2 * 32px)}}@media screen and (min-width:1424px) and (max-width:1727px){.access-modal-content[data-v-5f656e39]{height:calc(100% - 2 * 32px)}}@media screen and (min-width:1192px) and (max-width:1423px){.access-modal-content[data-v-5f656e39]{height:calc(100% - 2 * 24px)}}@media screen and (min-width:960px) and (max-width:1191px){.access-modal-content[data-v-5f656e39]{height:calc(100% - 2 * 24px)}}@media screen and (min-width:696px) and (max-width:959px){.access-modal-content[data-v-5f656e39]{height:100%;width:100%;border:0;flex-direction:column;overflow:scroll;box-shadow:none;border-radius:0;transition:none}}@media screen and (max-width:695px){.access-modal-content[data-v-5f656e39]{box-shadow:none;height:100%;width:100%;border-radius:0;border:0;flex-direction:column;overflow:scroll;transition:none}}.access-modal-content .button[data-v-5f656e39]{position:absolute;top:8px;cursor:pointer;color:var(--color-secondary-label)}.access-modal-content .button[data-v-5f656e39]:hover{color:var(--color-primary-label);border-radius:999px;background:var(--color-active-background)}.access-modal-content .button.close[data-v-5f656e39]{right:8px}.access-modal-content .button.back[data-v-5f656e39]{left:8px}
.multistage-toggle[data-v-f17b9244]{position:relative;background:var(--color-active-background);display:flex();padding:2px;border-radius:999px;cursor:pointer}.toggle-item[data-v-f17b9244]{border-radius:999px;background:transparent;color:var(--color-tertiary-label)}.toggle-item[data-v-f17b9244]:hover{color:var(--color-primary-label)}.toggle-item.active[data-v-f17b9244]{background:var(--elevation-low-background);box-shadow:var(--elevation-low-shadow);color:var(--color-primary-label)}.icon-wrapper[data-v-f17b9244]{width:24px;height:24px;display:flex;align-items:center;justify-content:center;cursor:pointer}.method-desc[data-v-f17b9244]{bottom:32px;white-space:nowrap;position:absolute;border:1px solid var(--color-border);box-shadow:var(--elevation-low-shadow);border-radius:6px;font-size:12px;padding:5.5px 8px 5.5px 8px;background:var(--elevation-high-background);line-height:140%;color:var(--color-secondary-label)}
li[data-v-13c4f3b9]{list-style:none}ul[data-v-13c4f3b9]{margin:0;padding:0}.text-active[data-v-13c4f3b9]{color:var(--color-tertiary-label)}@media screen and (min-width:960px){.text-active[data-v-13c4f3b9]{color:var(--color-primary-label)}.text-active.active[data-v-13c4f3b9]{color:var(--color-primary-label)}}.bg-active[data-v-13c4f3b9]{color:var(--color-primary-label)}@media screen and (min-width:960px){.bg-active[data-v-13c4f3b9]{background-color:var(--color-active-background);border-radius:999px}}.tertiary-label[data-v-13c4f3b9]{color:var(--color-tertiary-label) !important}.initial-bg[data-v-13c4f3b9]{background:var(--color-background)}
li[data-v-a93a7d02]{list-style:none}ul[data-v-a93a7d02]{margin:0;padding:0}.channel[data-v-a93a7d02]{font-size:16px;font-weight:600;margin-left:14px;color:var(--color-primary-label)}.user[data-v-a93a7d02]{position:relative}.login-btn[data-v-a93a7d02]{font-size:16px;height:48px;width:100%;font-weight:600;margin-bottom:8px}.side-bar-component[data-v-a93a7d02]{display:flex}@media screen and (min-width:696px) and (max-width:959px){.side-bar-component[data-v-a93a7d02]{display:none}}@media screen and (max-width:695px){.side-bar-component[data-v-a93a7d02]{display:none}}.bottom-menu-component[data-v-a93a7d02]{display:none}@media screen and (min-width:696px) and (max-width:959px){.bottom-menu-component[data-v-a93a7d02]{display:flex}}@media screen and (max-width:695px){.bottom-menu-component[data-v-a93a7d02]{display:flex}}
.banned-title[data-v-7a413e2c]{font-weight:500}[data-v-7a413e2c] .reds-alert-title{padding-bottom:4px !important}.text[data-v-7a413e2c]{font-weight:400;font-size:12px;line-height:20px;color:var(--color-tertiary-label);padding:0 20px 20px}.reason[data-v-7a413e2c]{font-weight:500;color:var(--color-primary-label)}.link[data-v-7a413e2c]{color:var(--color-link);font-weight:500}.center[data-v-7a413e2c]{text-align:center}
.anchor[data-v-5cde0260]{position:relative}.anchor .share-icon[data-v-5cde0260]{color:var(--color-secondary-label)}.anchor .share-icon[data-v-5cde0260]:hover{color:var(--color-primary-label)}.share-container[data-v-5cde0260]{position:absolute;bottom:36px;left:50%;transform:translateX(-50%)}.share-container.bottom[data-v-5cde0260]{top:41px}.share-wrapper[data-v-5cde0260]{display:flex;flex-direction:column;align-items:center;padding-top:16px;width:240px;background:var(--elevation-high-background);box-shadow:var(--elevation-high-shadow);border-radius:12px}.share-wrapper .share-wrapper-header[data-v-5cde0260]{color:var(--color-primary-label);font-weight:600;font-size:16px;line-height:120%}.share-wrapper .text[data-v-5cde0260]{margin:8px 0;font-size:14px;line-height:120%;color:var(--color-tertiary-label);text-align:center}.qrcode-wrapper[data-v-5cde0260]{margin-top:8px;display:flex;align-items:center;justify-content:center;padding:16px;background-color:var(--color-white);border-radius:8px;box-shadow:0 2px 8px 0 rgba(0,0,0,0.04),0 1px 2px 0 rgba(0,0,0,0.02)}.qrcode-wrapper .Qr-code[data-v-5cde0260]{width:128px;height:128px}.qrcode-wrapper .Qr-code img[data-v-5cde0260]{width:100%;height:100%}.share-tools[data-v-5cde0260]{padding:6px;width:100%;height:56px;border-top:1px solid var(--color-border);display:flex;align-items:center;justify-content:center;margin-top:8px}.share-tools .reds-button-new[data-v-5cde0260]{cursor:pointer;color:var(--color-secondary-label)}
[data-v-fc1041fa] .reds-button-new:hover{background:var(--color-active-background)}[data-v-fc1041fa] .reds-button-new:active{background:var(--color-active-background);color:var(--color-primary-label)}.container[data-v-fc1041fa]{display:flex;flex-direction:column;position:fixed;top:0;background:var(--color-background);z-index:15}.container iframe[data-v-fc1041fa]{width:100%;flex-grow:1;outline:none;border:0;margin:0}.container svg[data-v-fc1041fa]{cursor:pointer;opacity:.8;color:var(--color-secondary-label)}.container .header[data-v-fc1041fa]{display:flex;align-items:center;-webkit-user-select:none;user-select:none;flex-shrink:0;height:40px;margin-bottom:8px}.container .header .title[data-v-fc1041fa]{flex:1;text-align:center;color:var(--color-primary-label);font-size:16px;font-weight:600}.container .header .left[data-v-fc1041fa],.container .header .right[data-v-fc1041fa]{flex:1;display:flex;align-items:center}.container .header .left .close-icon[data-v-fc1041fa],.container .header .right .close-icon[data-v-fc1041fa]{color:var(--color-secondary-label)}.container .header .left .close-icon[data-v-fc1041fa]:hover,.container .header .right .close-icon[data-v-fc1041fa]:hover{color:var(--color-primary-label)}.container .header .right[data-v-fc1041fa]{justify-content:flex-end}.container .header .dragger[data-v-fc1041fa]{color:var(--color-quaternary-label)}.container .header .dragger[data-v-fc1041fa]:hover{color:var(--color-tertiary-label);cursor:grab}.container .header .dragger.dragging[data-v-fc1041fa]{color:var(--color-tertiary-label);cursor:grabbing}@media screen and (min-width:960px){.container[data-v-fc1041fa]{width:440px;height:calc(100vh - 64px);margin:32px 0;padding:8px;border-radius:20px;box-shadow:var(--elevation-high-shadow);left:calc(100% - 440px);transform:translateX(-32px);transition:left .3s ease,transform .3s ease,box-shadow .3s ease}.container.out[data-v-fc1041fa]{transform:translateX(100%);box-shadow:none}.container.left[data-v-fc1041fa]{left:0;transform:translateX(32px)}.container.left.out[data-v-fc1041fa]{transform:translateX(-100%);box-shadow:none}.container iframe[data-v-fc1041fa]{border-radius:12px}.container .fullscreen-header[data-v-fc1041fa]{display:none}}@media screen and (max-width:959px){.container[data-v-fc1041fa]{width:100%;height:100%;margin:0;padding:0;border-radius:0;left:0}.container.out[data-v-fc1041fa]{display:none}.container .panel-header[data-v-fc1041fa]{display:none}}
.ad-wrap[data-v-50d98839]{position:fixed;width:0;height:0;z-index:-1}.title[data-v-50d98839]{font-weight:500}[data-v-50d98839] .reds-alert-title{padding-bottom:4px !important}.text[data-v-50d98839]{font-weight:400;font-size:12px;line-height:20px;color:var(--color-tertiary-label);padding:0 20px 20px}
.center-modal-container[data-v-7cccb6db]{background:var(--elevation-high-background);border-radius:16px;-webkit-user-select:none;user-select:none}@media screen and (min-width:1424px){.center-modal-container[data-v-7cccb6db]{width:440px}}@media screen and (min-width:1192px) and (max-width:1423px){.center-modal-container[data-v-7cccb6db]{width:400px}}@media screen and (min-width:696px) and (max-width:1191px){.center-modal-container[data-v-7cccb6db]{width:360px}}@media screen and (max-width:695px){.center-modal-container[data-v-7cccb6db]{width:320px}}.header[data-v-7cccb6db]{height:56px;padding:8px;display:flex;flex-wrap:nowrap;position:relative;justify-content:center}.text[data-v-7cccb6db]{color:var(--color-primary-label);font-weight:600;font-size:16px;display:flex;align-items:center}.close-container[data-v-7cccb6db]{right:8px;width:40px;height:40px;position:absolute;display:flex;justify-content:center;align-items:center;color:var(--color-secondary-label);cursor:pointer}.close-container[data-v-7cccb6db]:hover{background:var(--color-active-background);border-radius:999px;color:var(--color-primary-label)}
.content[data-v-4492decc]{display:flex;flex-direction:column}.desc-container[data-v-4492decc]{padding:24px}.title[data-v-4492decc]{text-align:center;color:var(--color-primary-label);font-size:18px;font-weight:600;margin-bottom:12px;-webkit-user-select:text;user-select:text}.text[data-v-4492decc]{text-align:center;color:var(--color-secondary-label);font-size:14px;-webkit-user-select:text;user-select:text}.btn-container[data-v-4492decc]{padding:0 48px 48px 48px;display:flex;justify-content:center}.btn[data-v-4492decc]{color:var(--color-secondary-label);font-size:16px;height:48px;padding:0 24px;border-radius:999px;border:1px solid var(--color-border);display:inline-flex;justify-content:center;align-items:center;font-weight:600;cursor:pointer;white-space:nowrap}.btn[data-v-4492decc]:hover{color:var(--color-primary-label);background:var(--color-active-background)}.video[data-v-4492decc]{border-bottom:1px solid var(--color-shadow-border)}
.content[data-v-402e9182]{display:flex;flex-direction:column}.desc-container[data-v-402e9182]{padding:24px}.title[data-v-402e9182]{text-align:center;color:var(--color-primary-label);font-size:18px;font-weight:600;margin-bottom:12px;-webkit-user-select:text;user-select:text}.text[data-v-402e9182]{text-align:center;color:var(--color-secondary-label);font-size:14px;-webkit-user-select:text;user-select:text}.btn-container[data-v-402e9182]{padding:0 48px 48px 48px;display:flex;justify-content:center}.btn[data-v-402e9182]{color:var(--color-secondary-label);font-size:16px;height:48px;padding:0 24px;border-radius:999px;border:1px solid var(--color-border);display:flex;justify-content:center;align-items:center;font-weight:600;white-space:nowrap;cursor:pointer}.btn[data-v-402e9182]:hover{color:var(--color-primary-label);background:var(--color-active-background)}.video[data-v-402e9182]{border-bottom:1px solid var(--color-shadow-border)}
.keyboard[data-v-c42b1888]{background-color:var(--color-primary-label);color:var(--color-inverted-label);height:24px;min-width:24px;line-height:24px;display:inline-block;padding:0 8px;border-radius:4px;font-size:12px;font-weight:500}.icon-container[data-v-c42b1888]{height:24px;width:24px;display:inline-flex;justify-content:center;align-items:center}.inverted[data-v-c42b1888]{background-color:transparent;color:var(--color-secondary-label)}.square[data-v-c42b1888]{width:24px;display:flex;padding:0;justify-content:center}
.desc[data-v-667f1520]{display:flex;align-items:center;font-size:16px;color:var(--color-secondary-label)}.content[data-v-667f1520]{height:440px;padding:24px}.keyboard-container[data-v-667f1520]{display:flex;justify-content:space-between;margin-bottom:12px}.keyboard-container.not-first[data-v-667f1520]{margin-top:12px}.keys-container[data-v-667f1520]{display:flex}
.guide[data-v-20b84cf1]{width:200px;height:200px}.container[data-v-20b84cf1]{display:flex;align-items:center;justify-content:center;flex-direction:column}.desc[data-v-20b84cf1]{font-size:18px;font-weight:600;color:var(--color-white);margin-top:24px}
.container[data-v-0eb6247e]{padding-bottom:100%;background-position:center;background-size:contain;background-repeat:no-repeat;border-radius:16px;position:relative;cursor:pointer}.container[data-v-0eb6247e]::after{content:'';position:absolute;top:0;left:0;width:100%;height:100%;transition:background-color .2s;background-color:transparent;-webkit-transform:translate3d(0,0,0);border-radius:16px}.container[data-v-0eb6247e]:hover::after{background-color:var(--mask-note-card)}.container.higher[data-v-0eb6247e]{padding-bottom:133%}.container.wider[data-v-0eb6247e]{padding-bottom:75%}.container .content[data-v-0eb6247e]{position:absolute;bottom:0;left:0;width:100%;padding:12px;display:flex;align-items:flex-end}.container .content .title[data-v-0eb6247e]{flex-grow:1;margin-right:8px;font-size:14px;color:var(--color-white)}.container .content .tag[data-v-0eb6247e]{width:40px;height:24px;font-size:12px;line-height:24px;color:var(--color-white);background:var(--material-background);-webkit-backdrop-filter:var(--material-filter);backdrop-filter:var(--material-filter);border-radius:12px;text-align:center}
[data-v-c1dba808] .reds-mask{background:var(--mask-backdrop)}.activity-modal[data-v-c1dba808]{z-index:100011}.acrivity-container[data-v-c1dba808]{cursor:pointer;position:relative;display:flex;align-items:center;justify-content:center;flex-direction:column;width:50%;border-radius:20px}@media screen and (min-width:960px) and (max-width:1191px){.acrivity-container[data-v-c1dba808]{width:60%}}@media screen and (min-width:696px) and (max-width:959px){.acrivity-container[data-v-c1dba808]{width:70%}}@media screen and (max-width:695px){.acrivity-container[data-v-c1dba808]{width:100%}}.acrivity-container .image[data-v-c1dba808]{border-radius:20px;width:100%;height:100%;object-fit:cover}.acrivity-container .open-area[data-v-c1dba808]{position:absolute;bottom:0;transform:translate(0,50%)}.acrivity-container .open-area .open-button[data-v-c1dba808]{padding:0 20px;display:flex;align-items:center;justify-content:center;font-weight:600;background:var(--elevation-high-background);font-size:16px;color:var(--color-secondary-label);border-radius:999px;height:48px}.acrivity-container .open-area .open-button .icon[data-v-c1dba808]{margin-left:8px;opacity:.3}.acrivity-container .open-area .cta-image[data-v-c1dba808]{min-height:44px;max-height:52px;object-fit:cover}.close-button[data-v-c1dba808]{position:absolute;cursor:pointer;display:flex;align-items:center;justify-content:center;top:16px;right:var(--25d9dc56);height:40px;width:88px;background:var(--elevation-high-background);border-radius:999px;font-weight:400;font-size:16px;color:var(--color-secondary-label)}.close-button.hoverable[data-v-c1dba808]{color:var(--color-primary-label)}.close-button .countdown[data-v-c1dba808]{display:flex;align-items:center;justify-content:center;width:28px;height:28px;margin-left:6px;border-radius:999px;background:var(--color-active-background);white-space:nowrap}.close-button .countdown.hoverable[data-v-c1dba808]{background:transparent;color:var(--color-secondary-label)}
.onebox[data-v-70ee96be]{display:flex;align-items:center;width:100%;height:104px;padding-left:12px}.onebox .image[data-v-70ee96be]{border:1px solid var(--color-shadow-border);border-radius:8px;object-fit:cover}.onebox .title-wrapper[data-v-70ee96be]{margin-left:16px;font-weight:600;font-size:18px;line-height:120%;color:var(--color-primary-label)}.onebox .title-wrapper .sub-title[data-v-70ee96be]{margin-top:9px;font-weight:400;font-size:14px;line-height:120%;color:var(--color-tertiary-label)}.onebox .button[data-v-70ee96be]{display:flex;align-items:center;justify-content:center;height:40px;padding:0 16px;border:1px solid var(--color-border);border-radius:999px;font-weight:400;font-size:16px;line-height:120%;color:var(--color-secondary-label);margin:0 24px 0 auto}.onebox .button[data-v-70ee96be]:hover{color:var(--color-primary-label)}
.spinner[data-v-1c901116]{animation:spin-1c901116 .6s ease-in-out infinite;width:24px;height:24px;margin-top:-16px;opacity:var(--c989fa5a);transition:opacity .45s ease-in-out}.loading-container[data-v-1c901116]{width:100%;transition:height .45s ease-in-out;display:flex;align-items:center;justify-content:center;flex-direction:column;color:var(--color-secondary-label)}@keyframes spin-1c901116{0%{transform:rotate(0deg)}100%{transform:rotate(360deg)}}
.error[data-v-22d432c2]{display:flex;align-items:center;justify-content:center;width:100vw;max-width:100%;height:calc(100vh - 88px);background:var(--color-background)}.error section[data-v-22d432c2]{display:flex;flex-direction:column;align-items:center}.error img[data-v-22d432c2]{width:160px}.error .message[data-v-22d432c2]{margin-top:40px;font-size:14px;line-height:18px;color:var(--color-tertiary-label)}.error .button[data-v-22d432c2]{display:flex;align-items:center;justify-content:center;margin-top:16px;width:96px;height:36px;border:1px solid var(--color-red);border-radius:20px;font-weight:500;font-size:14px;color:var(--color-red);cursor:pointer}
.content-container[data-v-da963056]{display:flex;overflow-x:scroll;overflow-y:hidden;white-space:nowrap;color:var(--color-secondary-label)}
.channel-scroll-container[data-v-c69fb658]{overflow:hidden;display:flex;user-select:none;-webkit-user-select:none;align-items:center;font-size:16px;color:var(--color-secondary-label);height:40px;white-space:nowrap;height:72px}.channel-scroll-container.gray[data-v-c69fb658]{filter:grayscale(0.95)}.channel[data-v-c69fb658]{height:40px;display:flex;justify-content:center;align-items:center;padding:0 16px;cursor:pointer;-webkit-user-select:none;user-select:none}.channel[data-v-c69fb658]:hover{background:var(--color-active-background);border-radius:999px;color:var(--color-primary-label)}.active[data-v-c69fb658]{background:var(--color-active-background);border-radius:999px;color:var(--color-primary-label);font-weight:600}.vertical-channel-bg[data-v-c69fb658]:hover{background:var(--color-vertical-channel)}.vertical-channel-bg[data-v-c69fb658]{padding:0 16px 0 12px}[data-v-c69fb658] .vertical-channel-bg.active{background:var(--color-vertical-channel) !important}
.wrapper[data-v-56cede88]{width:var(--columnWidth)}.wrapper .cover[data-v-56cede88]{background:var(--color-active-background);width:100%;height:var(--d49b5fbe);border-radius:var(--note-card-corner-radius)}.wrapper .interact[data-v-56cede88]{width:100%;padding:12px}.wrapper .interact .title[data-v-56cede88]{background:var(--color-active-background);width:75%;height:14px;margin-bottom:12px;border-radius:var(--note-card-corner-radius)}.wrapper .interact .author[data-v-56cede88]{background:var(--color-active-background);width:35%;height:14px;border-radius:var(--note-card-corner-radius)}
.skeleton-container[data-v-2001e7e1]{column-count:var(--feeds-columns);column-gap:calc(var(--horizontal) * 1px);grid-auto-flow:dense;margin:0 auto}.skeleton-container .skeleton-item[data-v-2001e7e1]{margin-bottom:calc(var(--vertical) * 1px);display:block;width:100%;break-inside:avoid}
.back-top[data-v-4559bcd4]{pointer-events:none;display:flex;align-items:center;justify-content:center;width:40px;height:40px;border:1px solid var(--color-border);box-shadow:var(--elevation-low-shadow);border-radius:44px;cursor:pointer;opacity:0;color:var(--color-secondary-label);z-index:10;background:var(--elevation-low-background)}.back-top.active[data-v-4559bcd4]{pointer-events:auto;visibility:visible;opacity:1}.back-top .btn-wrapper[data-v-4559bcd4]{width:100%;height:100%;border-radius:44px;display:flex;align-items:center;justify-content:center;background:var(--color-background)}.back-top .btn-wrapper[data-v-4559bcd4]:hover{background:var(--color-active-background);color:var(--color-primary-label)}.tip-container[data-v-4559bcd4]{position:absolute;height:28px;padding:0 8px;border:1px solid var(--color-border);box-shadow:var(--elevation-low-shadow);background:var(--elevation-low-background);font-size:12px;color:var(--color-secondary-label);display:flex;align-items:center;justify-content:center;border-radius:6px;right:48px;visibility:hidden}.tip-container .tip-text[data-v-4559bcd4]{width:100%;white-space:nowrap;line-height:140%}.back-top:hover .tip-container[data-v-4559bcd4]{visibility:visible}
.floating-btn-sets[data-v-2ed9bdf4]{position:fixed;display:flex;flex-direction:column;width:40px;gap:8px;right:var(--horizontalGapPx);bottom:var(--horizontalGapPx)}@media screen and (max-width:959px){.floating-btn-sets[data-v-2ed9bdf4]{bottom:calc(48px + var(--horizontal) * 1px)}}.nio-btn-sets[data-v-2ed9bdf4]{left:24px !important;bottom:72px !important}
.reload[data-v-173cc1c4]{width:40px;height:40px;background:var(--elevation-low-background);border:1px solid var(--color-border);box-shadow:var(--elevation-low-shadow);border-radius:100px;color:var(--color-secondary-label);display:flex;align-items:center;justify-content:center;transition:background .2s;cursor:pointer}.reload .btn-wrapper[data-v-173cc1c4]{width:100%;height:100%;border-radius:44px;display:flex;align-items:center;justify-content:center;background:var(--color-background)}.reload .btn-wrapper[data-v-173cc1c4]:hover{background:var(--color-active-background);color:var(--color-primary-label)}.tip-container[data-v-173cc1c4]{position:absolute;height:28px;padding:0 8px;border:1px solid var(--color-border);box-shadow:var(--elevation-low-shadow);background:var(--elevation-low-background);font-size:12px;color:var(--color-secondary-label);display:flex;align-items:center;justify-content:center;border-radius:6px;right:48px;visibility:hidden}.tip-container .tip-text[data-v-173cc1c4]{width:100%;white-space:nowrap;line-height:140%}.reload:hover .tip-container[data-v-173cc1c4]{visibility:visible}
.graphic-filter[data-v-a4fa5cbc]{display:flex;align-items:center;justify-content:center;width:40px;height:40px;border:1px solid var(--color-border);box-shadow:var(--elevation-low-shadow);border-radius:44px;cursor:pointer;z-index:10;background:var(--elevation-low-background)}.graphic-filter.checked-border[data-v-a4fa5cbc]{border:1px solid var(--color-secondary-label)}.graphic-filter.checked-border[data-v-a4fa5cbc]:hover{border:1px solid var(--color-primary-label)}.graphic-filter .btn-wrapper[data-v-a4fa5cbc]{width:100%;height:100%;border-radius:44px;display:flex;align-items:center;justify-content:center;color:var(--color-secondary-label)}.graphic-filter .btn-wrapper[data-v-a4fa5cbc]:hover{background:var(--color-active-background);color:var(--color-primary-label)}.tip-container[data-v-a4fa5cbc]{position:absolute;height:28px;padding:0 8px;border:1px solid var(--color-border);box-shadow:var(--elevation-low-shadow);background:var(--elevation-low-background);font-size:12px;color:var(--color-secondary-label);display:flex;align-items:center;justify-content:center;border-radius:6px;right:48px;visibility:hidden}.tip-container .tip-text[data-v-a4fa5cbc]{width:100%;white-space:nowrap;line-height:140%}.graphic-filter:hover .tip-container[data-v-a4fa5cbc]{visibility:visible}.spinner[data-v-a4fa5cbc]{animation:spin-a4fa5cbc .6s ease-in-out infinite;transition:opacity .45s ease-in-out}@keyframes spin-a4fa5cbc{0%{transform:rotate(0deg)}100%{transform:rotate(360deg)}}
.feeds-loading[data-v-820f2ae6]{display:flex;align-items:center;justify-content:center;width:100%;height:64px;font-size:12px;color:var(--color-tertiary-label);visibility:hidden}.feeds-loading.active[data-v-820f2ae6]{visibility:visible}
.like-wrapper[data-v-dc3a3972]{position:relative;cursor:pointer;display:flex;align-items:center}.like-wrapper .count[data-v-dc3a3972]{text-wrap:nowrap}.like-active[data-v-dc3a3972]:hover{color:var(--color-primary-label)}.like-icon.active[data-v-dc3a3972]{visibility:hidden}.like-lottie[data-v-dc3a3972]{position:absolute;left:0;top:0;transform:scale(1.7)}
span[data-v-51ec0135] img{height:14px;transform:translate(0,1px)}
.item-wrapper[data-v-7d549413]{display:flex;align-items:center;padding:8px;font-size:14px;font-weight:500;line-height:120%;min-height:40px}.item-wrapper.rec-query[data-v-7d549413]{padding:8px 12px}.item-wrapper .item-cover[data-v-7d549413]{flex-shrink:0;width:40px;height:40px;border-radius:6px;margin-right:8px;object-fit:cover}.query-note-item[data-v-7d549413]{width:100%;color:var(--13e39d34);cursor:pointer;border-radius:12px}.query-note-item.hotspot[data-v-7d549413]{display:flex;align-items:center;padding:8px 12px 8px 12px;font-weight:400;color:var(--13e39d34)}.query-note-item.hotspot[data-v-7d549413]:nth-child(1){color:#ff2442}.query-note-item.hotspot[data-v-7d549413]:nth-child(2){color:#ff3e33}.query-note-item.hotspot[data-v-7d549413]:nth-child(3){color:#ff5226}.query-note-item.hotspot .hotspot-index[data-v-7d549413]{display:flex;align-items:center;justify-content:center;font-size:12px;line-height:120%;font-weight:500;width:16px;height:16px}.query-note-item.hotspot .hotspot-title[data-v-7d549413]{color:var(--13e39d34);margin-left:8px}.query-note-item[data-v-7d549413]:hover{background-color:var(--630dd4eb)}.query-note-item:hover > .hotspot-title[data-v-7d549413]{color:var(--f1078352)}.query-note-wrapper[data-v-7d549413]{border-radius:16px;background:var(--00604742)}.query-note-wrapper .query-note-list[data-v-7d549413]{padding:0 4px 4px 4px}.query-note-wrapper .query-note-list.hotspot[data-v-7d549413]{padding:0 4px;position:relative}.query-note-wrapper .query-note-header[data-v-7d549413]{width:100%;padding:0 12px;height:60px;display:flex;align-items:center;color:var(--0773c501);font-size:16px;font-weight:600;line-height:120%}.query-note-wrapper .query-note-header .icon-warpper[data-v-7d549413]{width:40px;height:40px;border-radius:999px;background:var(--630dd4eb);margin-right:8px;display:flex;align-items:center;justify-content:center}.query-note-wrapper .query-note-header .icon-warpper.modify[data-v-7d549413]{margin-right:0;width:28px;height:28px;background:transparent;cursor:pointer;color:var(--13e39d34);margin-left:auto}.query-note-wrapper .query-note-header .icon-warpper.modify[data-v-7d549413]:hover{background-color:var(--630dd4eb);color:var(--f1078352)}.footer[data-v-7d549413]{padding:4px 0}.footer .more-hotspot[data-v-7d549413]{color:var(--color-secondary-label);cursor:pointer;background:var(--630dd4eb);border-radius:12px;display:flex;align-items:center;justify-content:center;height:32px;color:var(--13e39d34)}.footer .more-hotspot[data-v-7d549413]:hover{color:var(--f1078352)}.modify-dropdown[data-v-7d549413]{padding:0}.modify-dropdown .dropdown-items[data-v-7d549413]{min-width:90px}.modify-dropdown .menu-wrapper[data-v-7d549413]{border-radius:12px;width:100%}.modify-dropdown .menu-wrapper .menu-item[data-v-7d549413]{display:flex;align-items:center;justify-content:center;height:100%;width:100%;height:40px;cursor:pointer;color:var(--color-primary-label);border-radius:8px}.modify-dropdown .menu-wrapper .menu-item[data-v-7d549413]:hover{background:var(--color-active-background)}.modify-pad[data-v-7d549413]{position:absolute;top:0;bottom:44px;width:calc(100% - 8px);height:calc(100% - 40px);background:var(--00604742);display:flex;align-items:center;justify-content:center;flex-direction:column}.modify-pad.hide[data-v-7d549413]{height:calc(100% - 4px)}.modify-pad .modify-wrapper[data-v-7d549413]{color:var(--13e39d34);border-radius:12px;height:40px;font-size:14px;font-weight:$font-weight-normal;line-height:120%;cursor:pointer;display:flex;align-items:center;justify-content:center;width:100%}.modify-pad .modify-wrapper[data-v-7d549413]:hover{background-color:var(--630dd4eb);color:var(--f1078352)}.modify-pad .hide-text[data-v-7d549413]{font-size:16px;font-weight:600;line-height:120%;margin-bottom:6px;color:var(--f1078352)}.modify-pad .hide-text.hint[data-v-7d549413]{color:var(--13e39d34);font-size:14px;font-weight:400;line-height:140%}
.modify-dropdown .dropdown-items{min-width:90px}
.note-item[data-v-a264b01a]{position:absolute;left:0;top:0;width:var(--1bd4d75c)}.note-item.static-layout[data-v-a264b01a]{position:static}.note-item.gray[data-v-a264b01a]{filter:grayscale(0.95)}.cover[data-v-a264b01a]{position:relative;width:var(--1bd4d75c);display:flex;border-radius:var(--68479076);overflow:hidden;outline:1px solid var(--color-border);outline-offset:-1px;transition:background .2s;transform:translateZ(0)}.cover[data-v-a264b01a]::before{content:'';position:absolute;top:0;left:0;width:100%;height:100%;background:var(--color-active-background);-webkit-backdrop-filter:var(--1e4add76);backdrop-filter:var(--1e4add76);z-index:1;transition:all 400ms}.cover.ld[data-v-a264b01a]::before{background:transparent;-webkit-backdrop-filter:blur(0);backdrop-filter:blur(0)}.cover[data-v-a264b01a]::after{content:'';position:absolute;top:0;left:0;width:100%;height:100%;transition:background-color .2s;background-color:transparent;-webkit-transform:translate3d(0,0,0)}.cover:hover .loading[data-v-a264b01a]{background-color:var(--mask-backdrop);animation:fadeInOut-a264b01a 1s ease-in-out infinite}.cover img[data-v-a264b01a]{width:100%}.cover .play-icon[data-v-a264b01a]{display:flex;align-items:center;justify-content:center;position:absolute;right:14px;top:14px;width:20px;height:20px;color:var(--color-white);background:var(--material-background);-webkit-backdrop-filter:var(--material-filter);backdrop-filter:var(--material-filter);border-radius:20px}.cover .top-tag-area[data-v-a264b01a]{position:absolute;left:12px;top:12px;z-index:4}.cover .top-tag-area .top-wrapper[data-v-a264b01a]{background:var(--color-red);border-radius:999px;font-weight:500;color:var(--color-white);line-height:120%;font-size:12px;padding:5px 8px 5px 8px;display:flex;align-items:center;justify-content:center}.cover .bottom-tag-area[data-v-a264b01a]{position:absolute;left:12px;bottom:12px;z-index:4}.cover .bottom-tag-area .bottom-wrapper[data-v-a264b01a]{display:flex;align-items:center;justify-content:center;border-radius:50px;color:var(--color-white);background:var(--material-background);-webkit-backdrop-filter:var(--material-filter);backdrop-filter:var(--material-filter);padding:4px 8px 4px 8px;font-size:12px;line-height:120%;font-weight:400}.cover .bottom-tag-area .bottom-wrapper .bottom-tag-icon[data-v-a264b01a]{margin-right:2px;width:12px;height:12px}.footer[data-v-a264b01a]{padding:12px}.footer .recommend-reason[data-v-a264b01a]{margin-bottom:6px}.footer .recommend-reason .recommend-reason-icon[data-v-a264b01a]{margin-right:2px}.footer .recommend-reason .recommend-reason-text[data-v-a264b01a]{color:var(--color-tertiary-label);font-size:12px;line-height:16px;vertical-align:middle}.title[data-v-a264b01a]{margin-bottom:8px;word-break:break-all;display:-webkit-box;-webkit-box-orient:vertical;-webkit-line-clamp:2;overflow:hidden;font-weight:500;font-size:14px;line-height:140%;color:var(--color-primary-label)}.author-wrapper[data-v-a264b01a]{display:flex;align-items:center;justify-content:space-between;height:20px;color:var(--color-secondary-label);font-size:12px;transition:color 1s}.author-wrapper .author[data-v-a264b01a]{display:flex;align-items:center;color:inherit;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;margin-right:12px}.author-wrapper .author[data-v-a264b01a]:hover{color:var(--color-primary-label)}.author-wrapper .author-avatar[data-v-a264b01a]{margin-right:6px;width:20px;height:20px;border-radius:20px;border:1px solid var(--color-border);flex-shrink:0}.author-wrapper .author-avatar.no-avatar[data-v-a264b01a]{display:inline-block;background-color:var(--color-active-background)}.author-wrapper .name[data-v-a264b01a]{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}[data-v-a264b01a] .like-wrapper .count{margin-left:2px}[data-v-a264b01a] .like-wrapper:hover{color:var(--color-primary-label)}.mask[data-v-a264b01a]:hover::after{background-color:var(--mask-note-card);position:absolute;top:0;left:0;width:100%;height:100%;-webkit-transform:translate3d(0,0,0)}@keyframes fadeInOut-a264b01a{0%,100%{opacity:1}50%{opacity:0}}
.collect-wrapper[data-v-16bec73d]{position:relative;cursor:pointer;display:flex;align-items:center;color:var(--color-tertiary-label)}.count[data-v-16bec73d]{margin-left:2px;color:var(--color-primary-label)}.collect-icon[data-v-16bec73d]{color:var(--color-primary-label)}.collect-icon.active[data-v-16bec73d]{visibility:hidden}.message-container[data-v-16bec73d]{position:relative;padding:16px}
.comment-wrapper[data-v-ff8cd160]{position:relative;cursor:pointer;display:flex;align-items:center;flex-shrink:0;color:var(--color-secondary-label)}.comment-wrapper[data-v-ff8cd160]:hover{color:var(--color-primary-label)}.comment-wrapper .count[data-v-ff8cd160]{text-wrap:nowrap;margin-left:2px}
.card-bottom-wrapper[data-v-11fd8d4e]{display:flex;align-items:center;justify-content:space-between;height:32px;color:var(--color-secondary-label);font-size:12px;transition:color 1s}.card-bottom-wrapper .author[data-v-11fd8d4e]{flex-shrink:1;display:flex;align-items:center;color:inherit;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;margin-right:12px}.card-bottom-wrapper .author[data-v-11fd8d4e]:hover{color:var(--color-primary-label)}.card-bottom-wrapper .author-avatar[data-v-11fd8d4e]{margin-right:6px;border-radius:20px;border:1px solid var(--color-shadow-border);flex-shrink:0}.card-bottom-wrapper .author-avatar.no-avatar[data-v-11fd8d4e]{display:inline-block;background-color:var(--color-active-background)}.card-bottom-wrapper .name[data-v-11fd8d4e]{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}.card-bottom-wrapper .time[data-v-11fd8d4e]{overflow:hidden;text-overflow:ellipsis;white-space:nowrap;margin-top:4px;color:var(--color-tertiary-label)}
.poi-info-wrapper[data-v-15bd02fa]{max-width:calc(100% - 24px);height:24px;position:absolute;left:12px;bottom:12px;padding-left:8px;padding-right:8px;background-color:var(--material-background);border-radius:999px;-webkit-backdrop-filter:blur(10px);backdrop-filter:blur(10px);color:var(--color-white);display:flex;align-items:center}.poi-info-wrapper .poi-info-address[data-v-15bd02fa]{margin-left:2px;margin-right:4px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}.poi-info-wrapper .poi-info-divider[data-v-15bd02fa]{height:10px;stroke-width:1px}.poi-info-wrapper .poi-info-distance[data-v-15bd02fa]{margin-left:4px}.shrink-0[data-v-15bd02fa]{flex-shrink:0}
.feeds-container[data-v-330d9cca]{position:relative;margin:0 auto}.feeds-container.static-layout[data-v-330d9cca]{display:flex;justify-content:center;gap:var(--horizontalGapPx)}
.feeds-page[data-v-811a7fa6]{flex:1;padding:0 var(--horizontalGapPx);overflow-y:scroll;padding-top:72px}.feeds-page .channel-container[data-v-811a7fa6]{display:flex;justify-content:space-between;align-items:center;user-select:none;-webkit-user-select:none}.feeds-page .channel-container[data-v-811a7fa6] .channel-list{flex:1;margin-bottom:0}.feeds-page .channel-container[data-v-811a7fa6] .channel-scroll-container{background-color:transparent;width:var(--feeds-width)}.channel-icon[data-v-811a7fa6]{width:28px;height:28px;margin-right:4px}
.bottom-menu[data-v-3661fbb1]{position:fixed;bottom:0;width:100%;background:var(--color-background);display:none;padding-bottom:env(safe-area-inset-bottom)}@media screen and (min-width:696px) and (max-width:959px){.bottom-menu[data-v-3661fbb1]{display:block}}@media screen and (max-width:695px){.bottom-menu[data-v-3661fbb1]{display:block}}[data-v-3661fbb1] .channel-list{display:flex;color:var(--color-tertiary-label)}[data-v-3661fbb1] .bottom-channel{flex-grow:1;height:48px;display:flex;justify-content:center;align-items:center;color:var(--color-tertiary-label);cursor:pointer}[data-v-3661fbb1] .text{font-size:16px;margin-left:12px}@media screen and (max-width:695px){[data-v-3661fbb1] .text{display:none}}[data-v-3661fbb1] .active{color:var(--color-primary-label)}.force-visible[data-v-3661fbb1]{display:block}
.container[data-v-657d976e]{width:100%;background:var(--elevation-high-background);box-shadow:var(--elevation-high-shadow);border-radius:12px}.container .group-wrapper[data-v-657d976e]{padding:4px}.container .group-wrapper.allow-overflow[data-v-657d976e]{max-height:440px;overflow-y:scroll}.back[data-v-657d976e]{display:flex;align-items:center;justify-content:center;position:absolute;width:28px;height:28px;margin:10px 0 0 8px;color:var(--color-secondary-label);cursor:pointer;border-radius:999px}.back[data-v-657d976e]:hover{color:var(--color-primary-label);background:var(--color-active-background)}.group-navi[data-v-657d976e]{display:flex;align-items:center;color:var(--color-primary-label);height:48px;padding:4px 8px;font-size:16px;font-weight:600;justify-content:center;border-bottom:1px solid var(--color-border)}.group-header[data-v-657d976e]{display:flex;align-items:center;padding:0 12px;height:32px;color:var(--color-tertiary-label);font-size:12px;font-weight:400}.menu-item[data-v-657d976e]{display:flex;align-items:center;height:40px;padding:0 12px;color:var(--color-secondary-label);font-size:16px;font-weight:400;border-radius:8px}.menu-item .link[data-v-657d976e]{display:flex;align-items:center;height:100%;width:100%;color:inherit;font-size:inherit;font-weight:inherit}.menu-item.hover-effect[data-v-657d976e]{cursor:pointer}.menu-item.hover-effect[data-v-657d976e]:hover{color:var(--color-primary-label);background:var(--color-active-background)}.menu-item .icon[data-v-657d976e]{color:var(--color-quaternary-label);margin-left:auto}.menu-item .icon.hover-effect[data-v-657d976e]{display:none}.menu-item .icon.icon-visible[data-v-657d976e]{display:block}.menu-item .component[data-v-657d976e]{margin-left:auto}.divider[data-v-657d976e]{margin:0 8px}
.information-container[data-v-0370e1e6]{display:inline-block;width:100%;color:var(--color-primary-label);font-size:16px;position:absolute;bottom:0}.information-wrapper[data-v-0370e1e6]{-webkit-user-select:none;user-select:none;cursor:pointer;position:relative;margin-bottom:20px;height:48px;width:100%;display:flex;font-weight:600;align-items:center;border-radius:999px}.information-wrapper[data-v-0370e1e6]:hover{background:var(--color-active-background)}.information-wrapper .information-icon[data-v-0370e1e6]{margin:0 12px 0 16px}.information-pad[data-v-0370e1e6]{z-index:16;width:100%;position:absolute;bottom:72px}.app-info[data-v-0370e1e6]{padding:12px;color:var(--color-tertiary-label)}.app-info a[data-v-0370e1e6]{color:var(--color-tertiary-label)}.app-info.outside[data-v-0370e1e6]{position:absolute}.icp-info[data-v-0370e1e6]{word-break:break-word;margin:0;font-size:12px;line-height:140%}.icp-info .icp-text[data-v-0370e1e6]{font-weight:400}.corp-info[data-v-0370e1e6]{font-size:12px;line-height:140%;margin-top:4px}.corp-info p[data-v-0370e1e6]{margin:0}.vertical-center[data-v-0370e1e6]{display:inline-flex;align-items:center}.vertical-center:hover .icon-wrapper[data-v-0370e1e6]{color:var(--color-secondary-label)}.icon-wrapper color $color-tertiary-label[data-v-0370e1e6]:hover{color:var(--color-secondary-label)}.about-us[data-v-0370e1e6]{margin-bottom:8px}.about-us a[data-v-0370e1e6]{font-weight:500}.icon-gap[data-v-0370e1e6]{margin-left:2px}.dot[data-v-0370e1e6]{color:var(--color-quaternary-label)}.help[data-v-0370e1e6]{cursor:pointer}
li[data-v-6a8c8289]{list-style:none}ul[data-v-6a8c8289]{margin:0;padding:0}.icon-wrapper[data-v-6a8c8289]{color:var(--color-primary-label)}.side-bar[data-v-6a8c8289]{height:calc(100vh - 72px);overflow-y:scroll;background-color:var(--color-background);display:flex;flex-direction:column;flex-shrink:0;padding-top:16px;margin-top:72px;position:fixed;overflow:visible}@media screen and (min-width:1728px){.side-bar[data-v-6a8c8289]{width:calc(16px + calc((1728px - 7 * 32px) / 6 * 1));margin-left:16px}}@media screen and (min-width:1424px) and (max-width:1727px){.side-bar[data-v-6a8c8289]{width:calc(16px + calc((100vw - 7 * 32px) / 6 * 1));margin-left:16px}}@media screen and (min-width:1192px) and (max-width:1423px){.side-bar[data-v-6a8c8289]{width:calc(12px + calc((100vw - 6 * 24px) / 5 * 1));margin-left:12px}}@media screen and (min-width:960px) and (max-width:1191px){.side-bar[data-v-6a8c8289]{width:calc(12px + calc((100vw - 5 * 24px) / 4 * 1));margin-left:12px}}@media screen and (min-width:696px) and (max-width:959px){.side-bar[data-v-6a8c8289]{display:none}}@media screen and (max-width:695px){.side-bar[data-v-6a8c8289]{display:none}}.side-bar.gray[data-v-6a8c8289]{filter:grayscale(0.95)}[data-v-6a8c8289] .link-wrapper{display:flex;width:100%;height:48px;align-items:center}.channel-list[data-v-6a8c8289]{height:calc(100vh - 68px - 16px - 72px);-webkit-user-select:none;user-select:none;overflow-y:scroll}.channel-list .channel-list-content[data-v-6a8c8289]{height:calc(100vh - 68px - 16px - 72px)}.channel-list[data-v-6a8c8289] li{padding-left:16px;min-height:48px;display:flex;align-items:center;cursor:pointer;margin-bottom:8px;color:var(--color-tertiary-label)}.channel-list[data-v-6a8c8289] li:hover{background-color:var(--color-active-background);border-radius:999px}.channel-list[data-v-6a8c8289] li:last-child{margin-bottom:0}[data-v-6a8c8289] .channel{font-size:16px;font-weight:600;margin-left:12px;color:var(--color-primary-label)}[data-v-6a8c8289] a{color:var(--color-tertiary-label);font-size:12px;font-weight:600}[data-v-6a8c8289] .active-channel{background-color:var(--color-active-background);border-radius:999px;color:var(--color-primary-label)}.img-wrapper[data-v-6a8c8289]{width:24px;height:24px;justify-content:center;align-items:center;display:inline-flex}[data-v-6a8c8289] .link-wrapper{display:flex;width:100%;height:48px;align-items:center}.app-info[data-v-6a8c8289]{padding:12px;color:var(--color-quaternary-label);font-size:12px}.app-info a[data-v-6a8c8289]{color:var(--color-quaternary-label)}.app-info.outside[data-v-6a8c8289]{position:absolute}.icp-info[data-v-6a8c8289]{word-break:break-word;margin:0;font-size:12px;line-height:140%}.icp-info .icp-text[data-v-6a8c8289]{font-weight:400}.corp-info[data-v-6a8c8289]{font-size:12px;line-height:140%;margin-top:4px}.corp-info p[data-v-6a8c8289]{margin:0}
.reds-button-new[data-v-d957886a]{height:40px !important;color:var(--color-secondary-label);font-size:16px;line-height:120%;padding:0 16px;background:transparent}.reds-button-new[data-v-d957886a]:hover{background:var(--color-active-background);border-radius:999px;color:var(--color-primary-label)}.reds-button-new[data-v-d957886a] .reds-button-new-box{font-weight:400}.transparent .menu button[data-v-d957886a],.transparent .menu .menu-icon-btn[data-v-d957886a]{color:rgba(255,255,255,0.8)}.transparent button[data-v-d957886a]:hover .reds-button-new-box{color:var(--color-primary-label)}.menu[data-v-d957886a]{display:flex}.link[data-v-d957886a]{display:inline-flex;flex-grow:1;color:inherit;height:100%;align-items:center;width:100%}.channel-btn[data-v-d957886a]{color:var(--color-secondary-label)}.channel-btn[data-v-d957886a]:hover{color:var(--color-primary-label)}.icon[data-v-d957886a]{color:var(--color-quaternary-label)}.dropdown-nav[data-v-d957886a]{display:flex}@media screen and (max-width:959px){.dropdown-nav[data-v-d957886a]{display:none}}.menu-icon-dropdown-nav[data-v-d957886a]{position:relative;display:none}@media screen and (max-width:959px){.menu-icon-dropdown-nav[data-v-d957886a]{display:block}}.menu-icon-dropdown-nav .information-pad[data-v-d957886a]{z-index:16;width:223px;margin-top:4px;position:absolute;right:0}.force-visible[data-v-d957886a]{display:block}
.user-item-box[data-v-f7c244c6]{display:flex;align-items:center;padding:20px}@media screen and (min-width:696px) and (max-width:959px){.user-item-box[data-v-f7c244c6]{padding:16px}}@media screen and (max-width:695px){.user-item-box[data-v-f7c244c6]{padding:12px 16px}}.user-item-box.sug[data-v-f7c244c6]{padding:0}.avatar[data-v-f7c244c6]{display:flex}.avatar .user-image[data-v-f7c244c6]{width:72px;height:72px;border-radius:72px;border:1px solid var(--color-border);object-fit:cover;background:var(--color-active-background)}.avatar .user-image.sug[data-v-f7c244c6]{width:40px;height:40px}@media screen and (min-width:960px) and (max-width:1191px){.avatar .user-image[data-v-f7c244c6]{width:64px;height:64px}}@media screen and (min-width:696px) and (max-width:959px){.avatar .user-image[data-v-f7c244c6]{width:56px;height:56px}}@media screen and (max-width:695px){.avatar .user-image[data-v-f7c244c6]{width:40px;height:40px}}.user-info[data-v-f7c244c6]{display:flex;flex-direction:column;color:var(--color-tertiary-label);font-size:14px;font-weight:400;line-height:120%;margin:0 20px;width:100%}.user-info.sug[data-v-f7c244c6]{font-size:12px;margin:0 12px}@media screen and (min-width:696px) and (max-width:959px){.user-info[data-v-f7c244c6]{margin:0 16px}}@media screen and (max-width:695px){.user-info[data-v-f7c244c6]{font-size:12px;margin:0 12px;width:calc(100vw - 200px)}}.user-info .user-name-box[data-v-f7c244c6]{display:flex;align-items:center}.user-info .user-name-box .user-name[data-v-f7c244c6]{display:flex;align-items:center;justify-content:center;color:var(--color-primary-label);font-size:18px;font-weight:600;line-height:120%;margin-right:6px;white-space:nowrap}.user-info .user-name-box .user-name.sug[data-v-f7c244c6]{font-size:16px}@media screen and (max-width:959px){.user-info .user-name-box .user-name[data-v-f7c244c6]{font-size:16px}}.user-info .user-name-box .verify-icon[data-v-f7c244c6]{display:flex;margin-left:2px}.user-info .user-name-box .user-tag[data-v-f7c244c6]{overflow:hidden;text-overflow:ellipsis;white-space:nowrap;height:20px;margin-right:4px;font-size:12px;font-weight:400;line-height:120%;padding:3px 4px;color:var(--color-tertiary-label);border-radius:4px;background:var(--color-active-background);white-space:nowrap}.user-info .user-desc[data-v-f7c244c6]{display:flex;margin-top:6px;white-space:nowrap}@media screen and (max-width:695px){.user-info .user-desc[data-v-f7c244c6]{margin-top:4px}}.user-info .user-desc .user-desc-box[data-v-f7c244c6]{display:flex;align-items:center}.divider[data-v-f7c244c6]{margin:0 8px;display:inline-block;height:12px;border:.5px solid var(--color-border)}.divider.sug[data-v-f7c244c6]{margin:0 6px}@media screen and (max-width:695px){.divider[data-v-f7c244c6]{margin:0 6px}}.btn[data-v-f7c244c6]{margin-left:auto}
.history[data-v-ac555648]{padding:4px}.history-list[data-v-ac555648]{display:flex;align-items:center;padding:0 8px 8px 8px;flex-wrap:wrap;position:relative;gap:8px}.history-list .history-item[data-v-ac555648]{display:flex;align-items:center;justify-content:center;height:32px;color:var(--color-secondary-label);font-size:14px;font-weight:400;line-height:120%;padding:0 12px;white-space:nowrap;background:var(--color-active-background);border-radius:999px;border:1px solid transparent;cursor:pointer}.history-list .history-item.enableDelete[data-v-ac555648]{background:transparent;border:1px solid var(--color-border);height:32px;padding:0 6px 0 12px;cursor:auto}.history-list .history-item.enableDelete[data-v-ac555648]:hover{color:var(--color-secondary-label)}.history-list .history-item[data-v-ac555648]:hover{color:var(--color-primary-label)}.history-list .history-item .close-box[data-v-ac555648]{display:flex;align-items:center;justify-content:center;height:20px;width:20px;flex:0 0 20px;margin-left:6px;cursor:pointer}.history-list .history-item .close-box[data-v-ac555648]:hover{border-radius:999px;background:var(--color-active-background);color:var(--color-primary-label)}.history-list .chevron-icon[data-v-ac555648]{display:flex;align-items:center;justify-content:center;width:32px;height:32px;border:1px solid var(--color-border);transform:rotateX(180deg);border-radius:999px;cursor:pointer;color:var(--color-secondary-label)}.history-list .chevron-icon[data-v-ac555648]:hover{background:var(--color-active-background);color:var(--color-primary-label)}.history-list .chevron-icon.canSpand[data-v-ac555648]{transform:revert}.header[data-v-ac555648]{display:flex;padding:0 4px 0 12px;align-items:center;height:32px;font-style:normal;font-weight:400;font-size:12px;line-height:120%;color:var(--color-tertiary-label)}.header .icon-group[data-v-ac555648]{display:flex;margin-left:auto;font-size:12px;font-weight:400;line-height:$line-height-default;color:var(--color-secondary-label);gap:4px}.header .icon-group .icon-box[data-v-ac555648]{display:flex;align-items:center;justify-content:center;height:24px;width:24px;gap:4px;padding:0 4px;cursor:pointer}.header .icon-group .icon-box.enableDelete[data-v-ac555648]{width:auto}.header .icon-group .icon-box[data-v-ac555648]:hover{color:var(--color-primary-label)}
.hotspots[data-v-119fe976]{padding:4px}.header[data-v-119fe976]{padding:8px 12px;height:32px}.header .header-img[data-v-119fe976]{height:14px}.hotspot-item[data-v-119fe976]{padding:0 12px;display:flex;align-items:center;height:40px;cursor:pointer;color:var(--color-tertiary-label)}.hotspot-item[data-v-119fe976]:nth-child(1){color:#ff2442}.hotspot-item[data-v-119fe976]:nth-child(2){color:#ff3e33}.hotspot-item[data-v-119fe976]:nth-child(3){color:#ff5226}.hotspot-item[data-v-119fe976]:hover{background:var(--color-active-background);border-radius:8px}.hotspot-item:hover > .hotspot-title[data-v-119fe976]{color:var(--color-primary-label)}.hotspot-item .hotspot-index[data-v-119fe976]{display:flex;align-items:center;justify-content:center;font-weight:500;font-size:14px;line-height:120%;width:16px;height:16px}.hotspot-item .hotspot-title[data-v-119fe976]{margin:0 6px;color:var(--color-secondary-label);font-weight:400;font-size:16px;line-height:120%;display:flex;align-items:center;height:100%;flex:1}.hotspot-item .hotspot-title .text[data-v-119fe976]{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}.hotspot-item .hotspot-title img[data-v-119fe976]{margin-left:6px;height:14px}.hotspot-item .hotspot-score[data-v-119fe976]{color:var(--color-quaternary-label);margin-left:auto;font-weight:400;font-size:12px;line-height:120%}
.sug-container-wrapper[data-v-57872acf]{margin-top:8px;width:100%;background-color:var(--elevation-high-background);box-shadow:var(--elevation-high-shadow);border-radius:12px;overflow:scroll}.sug-container-wrapper.query-trending[data-v-57872acf]{position:relative;padding-top:100%}.sug-container.query-trending[data-v-57872acf]{width:100%;position:absolute;top:0}.sug-box[data-v-57872acf]{padding:4px}.header[data-v-57872acf]{display:flex;padding:10.5px 12px 10.5px 12px;align-items:center;height:32px;font-style:normal;font-weight:400;font-size:12px;line-height:120%;color:var(--color-tertiary-label)}.header .refresh[data-v-57872acf]{margin-left:auto;display:flex;align-items:center;color:var(--color-secondary-label);cursor:pointer}.header .refresh .icon[data-v-57872acf]{margin-right:5.5px;opacity:.8}.header .refresh[data-v-57872acf]:hover{color:var(--color-primary-label)}.sug-wrapper[data-v-57872acf]{display:flex;flex-wrap:wrap}.sug-wrapper .sug-item[data-v-57872acf]{width:100%;padding:0 12px;font-size:16px;height:40px;line-height:120%;font-weight:400;border-radius:8px;color:var(--color-tertiary-label);display:flex;align-items:center}.sug-wrapper .sug-item[data-v-57872acf]:hover{background-color:var(--color-active-background);cursor:pointer}.sug-wrapper .sug-item .highlight[data-v-57872acf]{color:var(--color-primary-label)}.sug-wrapper .query-trending[data-v-57872acf]{color:var(--color-secondary-label);width:100%}.sug-wrapper .query-trending[data-v-57872acf]:hover{color:var(--color-primary-label)}.sug-wrapper .query-trending .sug-text[data-v-57872acf]{overflow:hidden;text-overflow:ellipsis;white-space:nowrap;display:flex;align-items:center;justify-content:center;height:20px}.sug-wrapper .query-trending.selected[data-v-57872acf]{background-color:var(--color-active-background);color:var(--color-primary-label)}.sug-wrapper .query-trending.hotspot[data-v-57872acf]{width:calc(50% - 2px)}.sug-wrapper .query-trending.hotspot[data-v-57872acf]:nth-child(even){margin-left:2px}.sug-wrapper .query-trending.hotspot[data-v-57872acf]:nth-child(odd){margin-right:2px}.sug-wrapper .selected-sug[data-v-57872acf]{background-color:var(--color-active-background)}.sug-wrapper .sug-user[data-v-57872acf]{height:64px}.sug-style[data-v-57872acf]{display:flex;align-items:center;justify-content:center;margin-left:4px;height:100%;padding:0 3px;font-weight:500;font-size:12px;line-height:120%;border-radius:4px}.sug-style.artificial[data-v-57872acf]{background:var(--color-blue);color:var(--color-white)}
.transparent-icon[data-v-721de8bd]{color:var(--color-secondary-label) !important}.transparent-icon[data-v-721de8bd]:hover{color:var(--color-primary-label) !important}.input-box[data-v-721de8bd]{height:40px;position:fixed;left:50%;transform:translate(-50%)}@media screen and (min-width:1728px){.input-box[data-v-721de8bd]{width:calc(32px + calc((1728px - 7 * 32px) / 6 * 2))}}@media screen and (min-width:1424px) and (max-width:1727px){.input-box[data-v-721de8bd]{width:calc(32px + calc((100vw - 7 * 32px) / 6 * 2))}}@media screen and (min-width:1192px) and (max-width:1423px){.input-box[data-v-721de8bd]{width:calc(24px + calc((100vw - 6 * 24px) / 5 * 2))}}@media screen and (min-width:960px) and (max-width:1191px){.input-box[data-v-721de8bd]{width:calc(24px + calc((100vw - 5 * 24px) / 4 * 2))}}@media screen and (min-width:696px) and (max-width:959px){.input-box[data-v-721de8bd]{width:calc(24px + calc((100vw - 4 * 24px) / 3 * 2))}}@media screen and (max-width:695px){.input-box[data-v-721de8bd]{width:calc(12px + calc((100vw - 3 * 12px) / 2 * 2))}}@media screen and (max-width:695px){.input-box[data-v-721de8bd]{width:0}}.input-box.minWidthShowSearchClass[data-v-721de8bd]{position:relative;left:0;transform:translate(0);width:100%}.search-input[data-v-721de8bd]{padding:0 84px 0 16px;width:100%;height:100%;font-size:16px;line-height:120%;color:var(--color-primary-label);caret-color:var(--color-red);background:var(--color-active-background);border-radius:999px}@media screen and (max-width:695px){.search-input[data-v-721de8bd]{padding:0}}.search-input[data-v-721de8bd]::placeholder{color:var(--color-quaternary-label)}.search-input.minWidthShowSearchClass[data-v-721de8bd]{padding:0 84px 0 16px}.search-input.showSearcHotspotTag[data-v-721de8bd]{color:transparent}@media screen and (max-width:695px){.sug-pad[data-v-721de8bd]{opacity:0}}.sug-pad.minWidthShowSearchClass[data-v-721de8bd]{opacity:1}.input-button[data-v-721de8bd]{position:absolute;right:0;top:0;display:flex;align-items:center;justify-content:center;height:100%;color:var(--color-secondary-label)}@media screen and (max-width:695px){.input-button[data-v-721de8bd]{opacity:0}}.input-button .search-icon[data-v-721de8bd],.input-button .close-icon[data-v-721de8bd]{width:40px;height:100%;display:flex;align-items:center;justify-content:center;cursor:pointer;color:var(--color-secondary-label)}.input-button .search-icon[data-v-721de8bd]:hover,.input-button .close-icon[data-v-721de8bd]:hover{color:var(--color-primary-label);border-radius:999px}.input-button.minWidthShowSearchClass[data-v-721de8bd]{opacity:1}.search-icon[data-v-721de8bd]{margin-right:4px;color:var(--color-secondary-label)}.reds-button-new[data-v-721de8bd]{height:40px !important;color:var(--color-secondary-label);font-size:16px;line-height:120%;padding:0 16px;background:transparent}.reds-button-new[data-v-721de8bd]:hover{background:var(--color-active-background);border-radius:999px;color:var(--color-primary-label)}.reds-button-new[data-v-721de8bd] .reds-button-new-box{font-weight:400}.cancel-btn[data-v-721de8bd]{margin-left:12px}.min-width-search-icon[data-v-721de8bd]{cursor:pointer;padding-right:10px;display:none}@media screen and (max-width:695px){.min-width-search-icon[data-v-721de8bd]{display:block;position:fixed;right:52px}}.nio-search-input-width[data-v-721de8bd]{width:calc(100vw - 24px * 2 - 40px * 2 - 8px * 2)}.hotspot-tag[data-v-721de8bd]{position:absolute;top:4px;left:4px;height:32px;padding:0 12px;background:var(--color-background);border-radius:999px;display:flex;align-items:center;justify-content:center;font-weight:400;font-size:16px;line-height:120%;max-width:calc(100% - 88px);cursor:pointer;color:var(--color-red)}.hotspot-tag .text[data-v-721de8bd]{margin-left:4px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;flex:1;color:var(--color-primary-label)}
header[data-v-5c1b2170]{position:relative;display:flex;align-items:center;justify-content:space-between;width:100%;max-width:var(--67f219a2);height:var(--header-height);padding:0 16px 0 24px;z-index:10}@media screen and (min-width:1728px){header[data-v-5c1b2170]{padding:0 32px}}@media screen and (min-width:1424px) and (max-width:1727px){header[data-v-5c1b2170]{padding:0 32px}}@media screen and (max-width:695px){header[data-v-5c1b2170]{padding:0 12px 0 16px}}header.mask-paper[data-v-5c1b2170]{background:var(--mask-paper);-webkit-backdrop-filter:blur(20px);backdrop-filter:blur(20px)}.right[data-v-5c1b2170]{display:flex}.information-header[data-v-5c1b2170]{position:absolute;top:72px;left:0;z-index:10}.header-container[data-v-5c1b2170]{display:flex;flex-direction:column;justify-content:center;width:100vw;height:72px;position:fixed;left:0;top:0;z-index:10;align-items:center}.header-container.gray[data-v-5c1b2170]{filter:grayscale(0.95)}.header-container.transparent[data-v-5c1b2170]{position:absolute}.header-logo[data-v-5c1b2170]{width:auto;height:32px}
.layout[data-v-34b87540]{width:100%;overflow:hidden;background-color:var(--color-background);margin:0 auto;min-width:320px}.layout.limit[data-v-34b87540]{max-width:var(--40bdee49)}.main-container[data-v-34b87540]{display:flex}.main-content[data-v-34b87540]{width:100%}@media screen and (min-width:1728px){.main-content.with-side-bar[data-v-34b87540]{padding-left:calc(32px + calc((1728px - 7 * 32px) / 6 * 1))}}@media screen and (min-width:1424px) and (max-width:1727px){.main-content.with-side-bar[data-v-34b87540]{padding-left:calc(32px + calc((100vw - 7 * 32px) / 6 * 1))}}@media screen and (min-width:1192px) and (max-width:1423px){.main-content.with-side-bar[data-v-34b87540]{padding-left:calc(24px + calc((100vw - 6 * 24px) / 5 * 1))}}@media screen and (min-width:960px) and (max-width:1191px){.main-content.with-side-bar[data-v-34b87540]{padding-left:calc(24px + calc((100vw - 5 * 24px) / 4 * 1))}}
.collection-list-item-wrapper[data-v-355e9ea1]{flex-shrink:0;border-radius:16px;width:var(--987b0b72);height:var(--987b0b72);position:relative;margin-right:var(--442acb1c);cursor:pointer}.collection-list-item-wrapper .collection-list-item-title[data-v-355e9ea1]{position:absolute;bottom:12px;left:12px;color:var(--color-white);font-size:16px;font-weight:600;line-height:120%;text-shadow:0 1px 4px rgba(0,0,0,0.25)}.collection-list-item-wrapper .collection-list-item-tag[data-v-355e9ea1]{position:absolute;right:8.334px;top:8px;width:24px;height:24px;padding:6px;display:flex;align-items:center;justify-content:center;background:var(--material-background);border-radius:999px;-webkit-backdrop-filter:blur(15px);backdrop-filter:blur(15px)}.collection-list-item-wrapper .collection-list-item-decorate[data-v-355e9ea1]{width:69px;border-radius:16px;border:1px solid var(--color-shadow-border);background:var(--color-active-background)}.collection-list-item-wrapper .decorate1[data-v-355e9ea1]{position:absolute;right:-15.667px;top:12px;height:calc(var(--987b0b72) - 25px)}.collection-list-item-wrapper .decorate2[data-v-355e9ea1]{position:absolute;right:-7.667px;top:5px;height:calc(var(--987b0b72) - 10px)}
.collection-list-wrapper[data-v-8cb274da]{display:flex;width:100%;overflow:scroll;padding-right:24px}
.skeleton-container[data-v-3f370206]{position:relative;margin:0 auto;width:100%;height:calc(100vh - 88px);overflow:hidden;transition:width .5s}.img[data-v-3f370206]{position:absolute;left:0;top:0;width:var(--78cabcb1);color:var(--color-active-background)}
.feeds-page[data-v-f3020152]{flex:1;padding:0 var(--5f14e45a);overflow-y:scroll;padding-top:72px}.feeds-page .channel-container[data-v-f3020152]{display:flex;justify-content:space-between;align-items:center;user-select:none;-webkit-user-select:none}.feeds-page .channel-container[data-v-f3020152] .channel-list{flex:1;margin-bottom:0}.feeds-page .channel-container[data-v-f3020152] .channel-scroll-container{-webkit-backdrop-filter:blur(20px);backdrop-filter:blur(20px);background-color:transparent}.rec-title[data-v-f3020152]{color:var(--color-primary-label);font-size:16px;font-weight:600;line-height:120%;margin-bottom:16px}
.nio-header[data-v-1721c56b]{position:fixed;width:100vw;height:64px;display:flex;align-items:center;justify-content:center;padding:24px 36px;color:var(--color-primary-label);font-size:16px;font-weight:600;line-height:120%;border-bottom:1px solid var(--color-border);z-index:10;background:var(--color-background)}.close-box[data-v-1721c56b]{width:40px;height:40px;cursor:pointer;position:absolute;left:0;top:calc(50% - 20px);margin-left:24px;z-index:5;border-radius:999px;display:flex;align-items:center;justify-content:center}.close-box[data-v-1721c56b]:hover{background:var(--color-active-background);color:var(--color-primary-label)}
header[data-v-5da00110]{position:relative;display:flex;align-items:center;justify-content:space-between;width:100%;max-width:var(--20c4f496);height:72px;padding:0 16px 0 24px;z-index:10;border-bottom:1px solid var(--color-border)}@media screen and (min-width:1728px){header[data-v-5da00110]{padding:0 32px}}@media screen and (min-width:1424px) and (max-width:1727px){header[data-v-5da00110]{padding:0 32px}}@media screen and (max-width:695px){header[data-v-5da00110]{padding:0 12px 0 16px}}header.mask-paper[data-v-5da00110]{background:var(--mask-paper);-webkit-backdrop-filter:blur(20px);backdrop-filter:blur(20px)}.right[data-v-5da00110]{display:flex}.information-header[data-v-5da00110]{position:absolute;top:72px;left:0;z-index:10}.header-container[data-v-5da00110]{display:flex;flex-direction:column;justify-content:center;width:100vw;height:72px;position:fixed;left:0;top:0;z-index:10;align-items:center}.header-container.gray[data-v-5da00110]{filter:grayscale(0.95)}.header-container.transparent[data-v-5da00110]{position:absolute}.close-box[data-v-5da00110]{width:40px;height:40px;cursor:pointer;top:calc(50% - 20px);z-index:5;border-radius:999px;display:flex;align-items:center;justify-content:center}.close-box[data-v-5da00110]:hover{background:var(--color-active-background);color:var(--color-primary-label)}
.layout[data-v-4968c87e]{width:100%;overflow:hidden;background-color:var(--color-background);margin:0 auto;min-width:320px}.layout.limit[data-v-4968c87e]{max-width:var(--9c8fe97c)}.main-container[data-v-4968c87e]{display:flex}.main-content[data-v-4968c87e]{width:100%}
.iphone[data-v-0e6d046c]{width:300px;height:600px;position:relative}.iphone .iphone-mp4[data-v-0e6d046c]{position:absolute;width:260px;height:564px;margin:18px 20px}.iphone .iphone-mp4 .my-video[data-v-0e6d046c]{width:260px;height:564px}.iphone .iphone-case[data-v-0e6d046c]{position:absolute;width:300px;height:600px;background-image:url("//ci.xiaohongshu.com/3ca6607e-d4a5-4cb9-b455-a746713d8283");background-repeat:no-repeat;background-size:contain}@media screen and (min-height:900px){.iphone[data-v-0e6d046c]{zoom:1}}@media screen and (min-height:820px) and (max-height:900px){.iphone[data-v-0e6d046c]{zoom:.9}}@media screen and (max-height:820px){.iphone[data-v-0e6d046c]{zoom:.8}}@media screen and (max-height:720px){.iphone[data-v-0e6d046c]{zoom:.7}}@media screen and (max-height:540px){.iphone[data-v-0e6d046c]{zoom:.6}}
.container[data-v-1cdf7708]{top:0;left:0;right:0;bottom:0;position:fixed}.video-bg[data-v-1cdf7708]{position:absolute;right:0;bottom:0;left:0;top:0}.video-bg[data-v-1cdf7708]:before{content:'';position:absolute;width:100%;height:100%;background:rgba(0,0,0,0)}.video-bg .my-video[data-v-1cdf7708]{min-width:100%;min-height:100%}.content[data-v-1cdf7708]{position:relative;left:0;top:0;right:0;bottom:0;width:100%;height:100%}.content .middle[data-v-1cdf7708]{top:0;left:0;right:0;bottom:0;position:absolute;width:100%;height:100%}.content .middle .middle-wrapper[data-v-1cdf7708]{top:50%;left:50%;transform:translate(-60%,-60%);display:flex;flex-direction:row;justify-content:center;align-items:center;position:absolute}.content .middle .middle-wrapper .iphone-wrapper[data-v-1cdf7708]{margin-right:60px}.content .middle .middle-wrapper .description[data-v-1cdf7708]{display:flex;flex-direction:column;justify-content:center;align-items:flex-start}.content .middle .middle-wrapper .description .logo-big[data-v-1cdf7708]{width:143px;height:50px;background-image:url("//ci.xiaohongshu.com/83074709-0d05-4d1c-9d38-24a8e910d914");background-size:contain;background-repeat:no-repeat;background-position:center center}.content .middle .middle-wrapper .description .lifestyle[data-v-1cdf7708]{white-space:nowrap;color:#fff;font-size:48px;font-weight:500;margin:0;margin-top:13px}.content .middle .middle-wrapper .description .lifestyle-english[data-v-1cdf7708]{white-space:nowrap;color:#fff;font-size:14px;font-family:Helvetica,Arial,sans-serif;font-style:oblique;font-weight:400;margin:0;margin-top:20px}.content .middle .middle-wrapper .description .qrcodes[data-v-1cdf7708]{margin-top:36px;display:flex;flex-direction:row;justify-content:flex-start;align-items:center;color:#333}.content .middle .middle-wrapper .description .qrcodes div[data-v-1cdf7708]{display:flex;flex-direction:row;justify-content:center;align-items:center;width:150px;height:40px;border-radius:20px;background-color:#fff;margin-right:15px;cursor:pointer;position:relative}.content .middle .middle-wrapper .description .qrcodes div[data-v-1cdf7708]:before{content:'';position:absolute;top:35px;left:0;width:100%;height:142px;border-radius:0 0 20px 20px;background-color:#fff;opacity:0;visibility:hidden}.content .middle .middle-wrapper .description .qrcodes div[data-v-1cdf7708]:after{content:'';position:absolute;top:40px;left:8px;width:134px;height:134px;border-radius:12px 12px 12px 12px;background-image:url("//ci.xiaohongshu.com/0b84da4e-3984-4603-a2f2-72a806e5494d");background-repeat:no-repeat;background-size:contain;opacity:0;visibility:hidden}.content .middle .middle-wrapper .description .qrcodes div[data-v-1cdf7708]:hover{border-radius:20px 20px 0 0}.content .middle .middle-wrapper .description .qrcodes div[data-v-1cdf7708]:hover:before{top:40px;opacity:1;visibility:visible}.content .middle .middle-wrapper .description .qrcodes div[data-v-1cdf7708]:hover:after{top:40px;opacity:1;visibility:visible}.content .middle .middle-wrapper .description .qrcodes div span[data-v-1cdf7708]{display:inline-block;width:24px;height:24px;margin-right:6px}.content .middle .middle-wrapper .description .qrcodes .android[data-v-1cdf7708]:after{background-image:url("//ci.xiaohongshu.com/8aa9236a-43ef-44f0-97d3-3167847de82a")}@media screen and (min-height:900px){.middle-wrapper[data-v-1cdf7708]{zoom:1}}@media screen and (min-height:820px) and (max-height:900px){.middle-wrapper[data-v-1cdf7708]{zoom:.9}}@media screen and (max-height:820px){.middle-wrapper[data-v-1cdf7708]{zoom:.8}}@media screen and (max-height:720px){.middle-wrapper[data-v-1cdf7708]{zoom:.7}}@media screen and (max-height:540px){.middle-wrapper[data-v-1cdf7708]{zoom:.6}}@media screen and (min-width:1250px) and (max-width:1400px){.footer[data-v-1cdf7708]{zoom:.9}}@media screen and (max-width:1250px) and (min-width:1101px){.header[data-v-1cdf7708]{zoom:.9}.footer[data-v-1cdf7708]{zoom:.8}}@media screen and (max-width:1101px) and (min-width:1030px){.header[data-v-1cdf7708]{zoom:.8}.footer[data-v-1cdf7708]{zoom:.7}}@media screen and (max-width:1030px) and (min-width:1024px){.header[data-v-1cdf7708]{zoom:.8}.footer[data-v-1cdf7708]{zoom:.6}}@media screen and (max-width:1024px){.header[data-v-1cdf7708]{zoom:.8}.footer[data-v-1cdf7708]{zoom:.6}}
/*! normalize.css v8.0.1 | MIT License | github.com/necolas/normalize.css */

/* Document
   ========================================================================== */

/**
 * 1. Correct the line height in all browsers.
 * 2. Prevent adjustments of font size after orientation changes in iOS.
 */

html {
  line-height: 1.15; /* 1 */
  -webkit-text-size-adjust: 100%; /* 2 */
}

/* Sections
   ========================================================================== */

/**
 * Remove the margin in all browsers.
 */

body {
  margin: 0;
}

/**
 * Render the `main` element consistently in IE.
 */

main {
  display: block;
}

/**
 * Correct the font size and margin on `h1` elements within `section` and
 * `article` contexts in Chrome, Firefox, and Safari.
 */

h1 {
  font-size: 2em;
  margin: 0.67em 0;
}

/* Grouping content
   ========================================================================== */

/**
 * 1. Add the correct box sizing in Firefox.
 * 2. Show the overflow in Edge and IE.
 */

hr {
  box-sizing: content-box; /* 1 */
  height: 0; /* 1 */
  overflow: visible; /* 2 */
}

/**
 * 1. Correct the inheritance and scaling of font size in all browsers.
 * 2. Correct the odd `em` font sizing in all browsers.
 */

pre {
  font-family: monospace, monospace; /* 1 */
  font-size: 1em; /* 2 */
}

/* Text-level semantics
   ========================================================================== */

/**
 * Remove the gray background on active links in IE 10.
 */

a {
  background-color: transparent;
}

/**
 * 1. Remove the bottom border in Chrome 57-
 * 2. Add the correct text decoration in Chrome, Edge, IE, Opera, and Safari.
 */

abbr[title] {
  border-bottom: none; /* 1 */
  text-decoration: underline; /* 2 */
  -webkit-text-decoration: underline dotted;
          text-decoration: underline dotted; /* 2 */
}

/**
 * Add the correct font weight in Chrome, Edge, and Safari.
 */

b,
strong {
  font-weight: bolder;
}

/**
 * 1. Correct the inheritance and scaling of font size in all browsers.
 * 2. Correct the odd `em` font sizing in all browsers.
 */

code,
kbd,
samp {
  font-family: monospace, monospace; /* 1 */
  font-size: 1em; /* 2 */
}

/**
 * Add the correct font size in all browsers.
 */

small {
  font-size: 80%;
}

/**
 * Prevent `sub` and `sup` elements from affecting the line height in
 * all browsers.
 */

sub,
sup {
  font-size: 75%;
  line-height: 0;
  position: relative;
  vertical-align: baseline;
}

sub {
  bottom: -0.25em;
}

sup {
  top: -0.5em;
}

/* Embedded content
   ========================================================================== */

/**
 * Remove the border on images inside links in IE 10.
 */

img {
  border-style: none;
}

/* Forms
   ========================================================================== */

/**
 * 1. Change the font styles in all browsers.
 * 2. Remove the margin in Firefox and Safari.
 */

button,
input,
optgroup,
select,
textarea {
  font-family: inherit; /* 1 */
  font-size: 100%; /* 1 */
  line-height: 1.15; /* 1 */
  margin: 0; /* 2 */
}

/**
 * Show the overflow in IE.
 * 1. Show the overflow in Edge.
 */

button,
input { /* 1 */
  overflow: visible;
}

/**
 * Remove the inheritance of text transform in Edge, Firefox, and IE.
 * 1. Remove the inheritance of text transform in Firefox.
 */

button,
select { /* 1 */
  text-transform: none;
}

/**
 * Correct the inability to style clickable types in iOS and Safari.
 */

button,
[type="button"],
[type="reset"],
[type="submit"] {
  -webkit-appearance: button;
}

/**
 * Remove the inner border and padding in Firefox.
 */

button::-moz-focus-inner,
[type="button"]::-moz-focus-inner,
[type="reset"]::-moz-focus-inner,
[type="submit"]::-moz-focus-inner {
  border-style: none;
  padding: 0;
}

/**
 * Restore the focus styles unset by the previous rule.
 */

button:-moz-focusring,
[type="button"]:-moz-focusring,
[type="reset"]:-moz-focusring,
[type="submit"]:-moz-focusring {
  outline: 1px dotted ButtonText;
}

/**
 * Correct the padding in Firefox.
 */

fieldset {
  padding: 0.35em 0.75em 0.625em;
}

/**
 * 1. Correct the text wrapping in Edge and IE.
 * 2. Correct the color inheritance from `fieldset` elements in IE.
 * 3. Remove the padding so developers are not caught out when they zero out
 *    `fieldset` elements in all browsers.
 */

legend {
  box-sizing: border-box; /* 1 */
  color: inherit; /* 2 */
  display: table; /* 1 */
  max-width: 100%; /* 1 */
  padding: 0; /* 3 */
  white-space: normal; /* 1 */
}

/**
 * Add the correct vertical alignment in Chrome, Firefox, and Opera.
 */

progress {
  vertical-align: baseline;
}

/**
 * Remove the default vertical scrollbar in IE 10+.
 */

textarea {
  overflow: auto;
}

/**
 * 1. Add the correct box sizing in IE 10.
 * 2. Remove the padding in IE 10.
 */

[type="checkbox"],
[type="radio"] {
  box-sizing: border-box; /* 1 */
  padding: 0; /* 2 */
}

/**
 * Correct the cursor style of increment and decrement buttons in Chrome.
 */

[type="number"]::-webkit-inner-spin-button,
[type="number"]::-webkit-outer-spin-button {
  height: auto;
}

/**
 * 1. Correct the odd appearance in Chrome and Safari.
 * 2. Correct the outline style in Safari.
 */

[type="search"] {
  -webkit-appearance: textfield; /* 1 */
  outline-offset: -2px; /* 2 */
}

/**
 * Remove the inner padding in Chrome and Safari on macOS.
 */

[type="search"]::-webkit-search-decoration {
  -webkit-appearance: none;
}

/**
 * 1. Correct the inability to style clickable types in iOS and Safari.
 * 2. Change font properties to `inherit` in Safari.
 */

::-webkit-file-upload-button {
  -webkit-appearance: button; /* 1 */
  font: inherit; /* 2 */
}

/* Interactive
   ========================================================================== */

/*
 * Add the correct display in Edge, IE 10+, and Firefox.
 */

details {
  display: block;
}

/*
 * Add the correct display in all browsers.
 */

summary {
  display: list-item;
}

/* Misc
   ========================================================================== */

/**
 * Add the correct display in IE 10+.
 */

template {
  display: none;
}

/**
 * Add the correct display in IE 10.
 */

[hidden] {
  display: none;
}

:root,.force-light{--color-primary-label:#333;--color-secondary-label:rgba(51,51,51,0.8);--color-tertiary-label:rgba(51,51,51,0.6);--color-quaternary-label:rgba(51,51,51,0.3);--color-link:#13386c;--color-inverted-label:#fff;--color-background:#fff;--color-active-background:rgba(0,0,0,0.03);--color-border:rgba(0,0,0,0.08);--color-shadow-border:rgba(0,0,0,0.02);--elevation-low-background:#fff;--elevation-high-background:#fff;--elevation-note-background:#fff;--elevation-low-shadow:0 2px 8px 0 rgba(0,0,0,0.04),0 1px 2px 0 rgba(0,0,0,0.02);--elevation-high-shadow:0 4px 32px 0 rgba(0,0,0,0.08),0 1px 4px 0 rgba(0,0,0,0.04);--elevation-note-shadow:0 8px 64px 0 rgba(0,0,0,0.04),0 1px 4px 0 rgba(0,0,0,0.02);--elevation-low-shadow-filter:drop-shadow(0 2px 8px rgba(0,0,0,0.04)) drop-shadow(0 1px 2px rgba(0,0,0,0.02));--elevation-high-shadow-filter:drop-shadow(0 4px 32px rgba(0,0,0,0.08)) drop-shadow(0 1px 4px rgba(0,0,0,0.04));--material-filter:saturate(150%) blur(10px);--material-background:rgba(64,64,64,0.25);--material-inverted-background:rgba(51,51,51,0.9);--mask-backdrop:rgba(0,0,0,0.25);--mask-note-card:rgba(0,0,0,0.25);--mask-paper:rgba(255,255,255,0.98);--color-white:#fff;--color-red:#ff2442;--color-tinted-red:rgba(255,36,66,0.06);--color-blue:#3d8af5;--color-tinted-blue:rgba(61,138,245,0.1);--mask-video-player-mask:linear-gradient(180deg,rgba(0,0,0,0.25) 0%,rgba(0,0,0,0) 24.48%,rgba(0,0,0,0) 50%,rgba(0,0,0,0.75) 100%);--search-hotspot-hint:linear-gradient(90deg,#ff2543 0%,#ff5225 100%);--color-vertical-channel:#fff9d5}:root[dark],.force-dark{--color-primary-label:#fff;--color-secondary-label:rgba(255,255,255,0.8);--color-tertiary-label:rgba(255,255,255,0.6);--color-quaternary-label:rgba(255,255,255,0.3);--color-link:#c7daef;--color-inverted-label:#0a0a0a;--color-background:#0a0a0a;--color-active-background:rgba(255,255,255,0.04);--color-border:rgba(255,255,255,0.08);--color-shadow-border:rgba(255,255,255,0.02);--elevation-low-background:#121212;--elevation-high-background:#181818;--elevation-note-background:#121212;--elevation-low-shadow:0 2px 8px 0 rgba(0,0,0,0.04),0 1px 2px 0 rgba(0,0,0,0.02),0 0 0 1px rgba(255,255,255,0.04) inset;--elevation-high-shadow:0 4px 32px 0 rgba(0,0,0,0.08),0 1px 4px 0 rgba(0,0,0,0.04),0 0 0 1px rgba(255,255,255,0.06) inset;--elevation-note-shadow:0 8px 64px 0 rgba(0,0,0,0.04),0 1px 4px 0 rgba(0,0,0,0.02);--elevation-low-shadow-filter:drop-shadow(0 2px 8px rgba(0,0,0,0.04)) drop-shadow(0 1px 2px rgba(0,0,0,0.02)) drop-shadow(0 0 1px rgba(255,255,255,0.04));--elevation-high-shadow-filter:drop-shadow(0 4px 32px rgba(0,0,0,0.08)) drop-shadow(0 1px 4px rgba(0,0,0,0.04)) drop-shadow(0 0 1px rgba(255,255,255,0.06));--material-filter:saturate(150%) blur(10px);--material-background:rgba(64,64,64,0.25);--material-inverted-background:rgba(255,255,255,0.9);--mask-backdrop:rgba(0,0,0,0.5);--mask-note-card:rgba(0,0,0,0.25);--mask-paper:rgba(10,10,10,0.98);--color-white:#fff;--color-red:#ff2e4d;--color-tinted-red:rgba(255,46,77,0.06);--color-blue:#3d8af5;--color-tinted-blue:rgba(61,138,245,0.1);--mask-video-player-mask:linear-gradient(180deg,rgba(0,0,0,0.25) 0%,rgba(0,0,0,0) 24.48%,rgba(0,0,0,0) 50%,rgba(0,0,0,0.75) 100%);--search-hotspot-hint:linear-gradient(90deg,#ff2543 0%,#ff5225 100%);--color-vertical-channel:#181714}html,body{font-size:14px;color:var(--color-primary-label);width:100vw !important;max-width:100%;font-family:system-ui,Apple Color Emoji,Segoe UI Emoji,Segoe UI Symbol,Noto Color Emoji,-apple-system,Segoe UI,Roboto,Ubuntu,Cantarell,Noto Sans,sans-serif,BlinkMacSystemFont,Helvetica Neue,Arial,PingFang SC,PingFang TC,PingFang HK,Microsoft Yahei,Microsoft JhengHei;margin:0;background-color:var(--color-background);-webkit-font-smoothing:antialiased}::-webkit-scrollbar{background-color:var(--color-background);width:0;height:0}*{box-sizing:border-box;-webkit-user-select:auto;user-select:auto;scrollbar-width:none;-webkit-tap-highlight-color:transparent}h1{font-size:48px}h2{font-size:36px}h3{font-size:26px}h4{font-size:20px}a{text-decoration:none;background-color:transparent}input,button{-webkit-appearance:none;appearance:none;outline:none;border:none;background:none;padding:0}input:-webkit-autofill,input:-webkit-autofill:hover,input:-webkit-autofill:focus,input:-webkit-autofill:active{-webkit-box-shadow:0 0 0 1000px var(--elevation-high-background) inset;-webkit-text-fill-color:var(--color-primary-label)}input[type=number]{-moz-appearance:textfield}input[type=number]::-webkit-inner-spin-button,input[type=number]::-webkit-outer-spin-button{-webkit-appearance:none;margin:0}button{padding:0}.reds-toast{max-width:initial !important}input::-webkit-credentials-auto-fill-button{display:none !important;visibility:hidden;pointer-events:none;position:absolute;right:0}@media screen and (min-width:1728px){:root{--vertical:16;--horizontal:32;--interaction-width:440px;--horizontalGapPx:32px;--verticalGapPx:16px;--feeds-width:calc(1728px - 96px - calc((1728px - 7 * 32px) / 6 * 1));--feeds-columns:5;--columnWidth:calc((1728px - 32px * 7) / 6);--note-card-corner-radius:16px;--modal-width:440px}}@media screen and (min-width:1424px) and (max-width:1727px){:root{--vertical:16;--horizontal:32;--interaction-width:440px;--horizontalGapPx:32px;--verticalGapPx:16px;--feeds-width:calc(100vw - 96px - calc((100vw - 7 * 32px) / 6 * 1));--feeds-columns:5;--columnWidth:calc((100vw - 32px * 7) / 6);--note-card-corner-radius:16px;--modal-width:440px}}@media screen and (min-width:1192px) and (max-width:1423px){:root{--vertical:12;--horizontal:24;--interaction-width:400px;--horizontalGapPx:24px;--verticalGapPx:12px;--feeds-width:calc(100vw - 72px - calc((100vw - 6 * 24px) / 5 * 1));--feeds-columns:4;--columnWidth:calc((100vw - 24px * 6) / 5);--note-card-corner-radius:16px;--modal-width:400px}}@media screen and (min-width:960px) and (max-width:1191px){:root{--vertical:12;--horizontal:24;--interaction-width:360px;--horizontalGapPx:24px;--verticalGapPx:12px;--feeds-width:calc(100vw - 72px - calc((100vw - 5 * 24px) / 4 * 1));--feeds-columns:3;--columnWidth:calc((100vw - 24px * 5) / 4);--note-card-corner-radius:16px;--modal-width:360px}}@media screen and (min-width:696px) and (max-width:959px){:root{--vertical:12;--horizontal:24;--interaction-width:100vw;--horizontalGapPx:24px;--verticalGapPx:12px;--feeds-width:calc(100vw - 48px);--feeds-columns:3;--columnWidth:calc((100vw - 24px * 4) / 3);--note-card-corner-radius:16px;--modal-width:360px}}@media screen and (max-width:695px){:root{--vertical:6;--horizontal:12;--interaction-width:100vw;--horizontalGapPx:12px;--verticalGapPx:6px;--feeds-width:calc(100vw - 24px);--feeds-columns:2;--columnWidth:calc((100vw - 12px * 3) / 2);--note-card-corner-radius:12px;--modal-width:360px}}:root{--header-height:72px}

/*# sourceMappingURL=https://picasso-private-1251524319.cos.ap-shanghai.myqcloud.com/data/formula-static/formula/xhs-pc-web/index.441c4d3c.css.map*/</style><title>大厂电报 - 小红书</title>
<link rel="dns-prefetch" href="https://sns-webpic-qc.xhscdn.com">
<link rel="dns-prefetch" href="https://sns-avatar-qc.xhscdn.com">
<link rel="dns-prefetch" href="https://picasso-static.xiaohongshu.com">
<link rel="dns-prefetch" href="https://sns-video-qc.xhscdn.com">
<link rel="dns-prefetch" href="https://sns-video-hw.xhscdn.com">
<link rel="dns-prefetch" href="https://sns-video-bd.xhscdn.com">
<link rel="dns-prefetch" href="https://sns-video-qn.xhscdn.com">
<link rel="dns-prefetch" href="https://sns-video-hw.xhscdn.net">
<link rel="manifest" href="//fe-video-qc.xhscdn.com/fe-platform/ebf234fe97561cc2242114a0c5ba836eaf0848f8.json?attname=fe-platform/ebf234fe97561cc2242114a0c5ba836eaf0848f8.json.json">
<link rel="apple-touch-icon-precomposed" href="//picasso-static.xiaohongshu.com/fe-platform/f43dc4a8baf03678996c62d8db6ebc01a82256ff.png">
<link rel="apple-touch-icon" href="//picasso-static.xiaohongshu.com/fe-platform/f43dc4a8baf03678996c62d8db6ebc01a82256ff.png">
<meta name="og:image" content="//picasso-static.xiaohongshu.com/fe-platform/e6214e4fbfae2cf14d634d4296916e8a5eaefdf4.png">
<meta itemprop="image" content="//picasso-static.xiaohongshu.com/fe-platform/f43dc4a8baf03678996c62d8db6ebc01a82256ff.png">
<style>true</style>
<meta name="theme-color" content="rgb(255, 255, 255)">
<script type="text/javascript">(e=>{const t=localStorage.getItem("xhs-pc-theme")||"",o=null===(e=window.matchMedia("(prefers-color-scheme: dark)"))||void 0===e?void 0:e.matches;var r;(t&&"system"!==t?"dark"===t:o)&&(null===(r=document)||void 0===r||null===(r=r.querySelector("meta[name='theme-color']"))||void 0===r||r.setAttribute("content","rgb(10, 10, 10)"),document.documentElement.setAttribute("dark",""))})();</script>
<meta name="server-rendered" content="">
<meta name="keywords" content="小红书,小红书购物笔记,福利社,red,RED,little red book,xiaohongshu">
<meta name="description" content="大厂电报在「小红书」上有25383位粉丝，已关注39人，来「小红书」查看更多大厂电报分享的视频和笔记">
<meta name="og:site_name" content="小红书">
<meta name="og:title" content="大厂电报 - 小红书">
<meta name="og:url" content="https://xiaohongshu.com/user/profile/67f8fd81000000000e010b43">
<meta http-equiv="Content-Security-Policy" content="upgrade-insecure-requests">
<link rel="preload" as="image" href="https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo31lvmkfehl80g5pvovm0ji2q3r980kf0?imageView2/2/w/540/format/webp|imageMogr2/strip2">
<link rel="preload" as="image" href="https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo31lvmkfehl80g5pvovm0ji2q3r980kf0?imageView2/2/w/540/format/webp|imageMogr2/strip2">
<link rel="preload" as="image" href="https://sns-webpic-qc.xhscdn.com/202509081416/88049fbe310fb6d9042ff342757a4287/1040g2sg31m38d73llmt05pvovm0ji2q3egnrdso!nc_n_webp_mw_1">
<link rel="preload" as="image">
<link rel="preload" as="image" href="https://sns-webpic-qc.xhscdn.com/202509081416/7bdeab8ced93c345e6bdb7cd2cead218/1040g2sg31m2rmme64qhg5nv613509bs8upnjnlg!nc_n_webp_mw_1">
<link rel="preload" as="image">
<link rel="preload" as="image" href="https://sns-webpic-qc.xhscdn.com/202509081416/b62ba595501960a0b6b16a8617711c31/1040g2sg31m4qr2knm8e05pvovm0ji2q3o5pp998!nc_n_webp_mw_1">
<link rel="preload" as="image">
<link rel="preload" as="image" href="https://sns-webpic-qc.xhscdn.com/202509081416/02e3f53435c14f28f4c05978d81c0801/1040g00831m4mkmdim64g5pvovm0ji2q314cbf4g!nc_n_webp_mw_1">
<link rel="preload" as="image">
<link rel="preload" as="image" href="https://sns-webpic-qc.xhscdn.com/202509081416/94895e8807e1f0ce100ccd43ceda838d/1040g00831m4m9op15i1g5pvovm0ji2q3e6ekos8!nc_n_webp_mw_1">
<link rel="preload" as="image"><style type="text/css" data-href="https://fe-static.xhscdn.com/formula-static/xhs-pc-web/public/resource/css/async/User.3830129f.css" data-inject="resource/css/async/User.3830129f.css">.modal[data-v-57e93c10]{width:440px;background-color:var(--elevation-high-background);box-shadow:var(--elevation-high-shadow);border-radius:16px}@media screen and (min-width:1192px) and (max-width:1423px){.modal[data-v-57e93c10]{width:400px}}@media screen and (max-width:1191px){.modal[data-v-57e93c10]{max-width:360px;min-width:320px;margin:0 var(--horizontalGapPx)}}.header[data-v-57e93c10]{display:flex;justify-content:space-around;align-items:center;height:56px;padding:8px;border-bottom:1px solid var(--color-border);font-size:16px;font-weight:600;line-height:120%;position:relative;color:var(--color-primary-label)}.header .header-right[data-v-57e93c10]{position:absolute;right:8px}.content[data-v-57e93c10]{display:flex;justify-content:center;padding:24px;flex-direction:column;gap:20px}.content-part[data-v-57e93c10]{display:flex;justify-content:center;flex-direction:column;gap:8px}.content-part.switch[data-v-57e93c10]{flex-direction:row;justify-content:space-between;align-items:center;gap:4px;padding-right:4px}.content-part .board-input[data-v-57e93c10]{background:var(--color-active-background);border-radius:12px}.content-part .form-title[data-v-57e93c10]{height:17px;margin-left:4px;color:var(--color-secondary-label);font-size:14px;font-weight:400;line-height:140%;margin-bottom:8px}.content-part .form-title.switch[data-v-57e93c10]{margin-bottom:4px;font-weight:500}.content-part .form-desc[data-v-57e93c10]{color:var(--color-tertiary-label);font-size:12px;font-weight:400;margin-left:4px}.delete-btn[data-v-57e93c10]{color:var(--color-red);font-size:16px;font-weight:600;line-height:120%;height:40px;padding:0 16px;border-radius:999px;display:flex;align-items:center;justify-content:center;margin:0 auto;cursor:pointer}.delete-btn[data-v-57e93c10]:hover{background:var(--color-tinted-red)}.footer[data-v-57e93c10]{display:flex;align-items:center;justify-content:center;gap:8px;padding:16px;height:72px;border-top:1px solid var(--color-border)}.footer .btn[data-v-57e93c10]{border-radius:999px;padding:0 16px;font-size:16px;display:flex;align-items:center;justify-content:center;height:40px;cursor:pointer;border:1px solid var(--color-border);color:var(--color-secondary-label)}.footer .btn[data-v-57e93c10]:hover{background:var(--color-active-background);color:var(--color-primary-label)}.footer .btn.done[data-v-57e93c10]{font-size:16px;font-weight:600;line-height:120%;color:var(--color-white);background:var(--color-red)}.footer .btn.done.loading[data-v-57e93c10]{opacity:.5}
.create-board[data-v-52f35ca2]{position:fixed;background:var(--color-primary-label);color:var(--color-inverted-label);right:calc(var(--feeds-width) / 2 + var(--horizontalGapPx));transform:translateX(50%);height:40px;gap:4px;padding:0 16px;border-radius:999px;bottom:var(--horizontalGapPx);cursor:pointer;font-size:16px;font-weight:600;line-height:120%;display:flex;align-items:center;justify-content:center}@media screen and (max-width:959px){.create-board[data-v-52f35ca2]{bottom:calc(var(--horizontalGapPx) + 48px)}}@media screen and (min-width:1728px){.create-board[data-v-52f35ca2]{right:calc(var(--feeds-width) / 2 + var(--horizontalGapPx) + 50vw - 864px)}}
.loading[data-v-5a8e0ee8]{margin-top:72px}
.board-card[data-v-5946ffba]{width:calc((100% - 2 * var(--horizontalGapPx)) / 2);margin-bottom:24px;margin-right:var(--horizontalGapPx);display:flex;flex-direction:column;align-items:flex-start;border-radius:16px;border:1px solid var(--color-border);padding:20px}@media screen and (min-width:1424px){.board-card[data-v-5946ffba]{width:calc((100% - 3 * var(--horizontalGapPx)) / 3)}}@media screen and (max-width:695px){.board-card[data-v-5946ffba]{width:calc(100% - var(--horizontalGapPx))}}.board-card .board-info[data-v-5946ffba]{display:flex;align-items:center;width:100%}.board-card .board-info .board-name[data-v-5946ffba]{font-size:18px;font-weight:600;line-height:120%;color:var(--color-primary-label)}.board-card .board-info .board-name .title[data-v-5946ffba]{display:flex;align-items:center}.board-card .board-info .board-name .title .lock[data-v-5946ffba]{margin-left:4px}.board-card .board-info .board-name .desc[data-v-5946ffba]{display:flex;color:var(--color-tertiary-label);font-size:12px;line-height:120%;font-weight:400;margin-top:8px}.board-card .board-info .board-name .desc .fans[data-v-5946ffba]{margin-left:16px}.board-card .image-wrapper[data-v-5946ffba]{display:flex;width:100%;gap:12px;margin-top:20px}.board-card .image-wrapper .image-item[data-v-5946ffba]{width:calc((100% - 36px) / 4);background:var(--color-active-background);padding-top:calc((100% - 36px) / 4);height:0;position:relative;border-radius:4px;border:1px solid var(--color-shadow-border)}.board-card .image-wrapper .image-item .image[data-v-5946ffba]{height:100%;width:100%;position:absolute;border-radius:3px;object-fit:cover;top:0}.follow[data-v-5946ffba]{margin-left:auto}
.board-wrapper[data-v-23fc5846]{display:flex;flex-wrap:wrap}
.static-layout[data-v-64126f47]{gap:16px;justify-content:center}.tab-content-item[data-v-64126f47]{padding-top:1px;flex-shrink:0}.sub-tab-list[data-v-64126f47]{padding:16px 0}.collection-icon[data-v-64126f47]{margin-right:4px}
.user-page-sticky .reds-sticky{padding:16px 0}
.reds-tab-item[data-v-bb2dbd52]{font-size:16px}.reds-tab-item[data-v-bb2dbd52]:hover{color:var(--color-primary-label)}@media screen and (min-width:1728px){.reds-tabs-list[data-v-bb2dbd52]{width:calc(1728px - 32px - calc((1728px - 7 * 32px) / 6 * 1))}}@media screen and (min-width:1424px) and (max-width:1727px){.reds-tabs-list[data-v-bb2dbd52]{width:calc(100vw - 32px - calc((100vw - 7 * 32px) / 6 * 1))}}@media screen and (min-width:1192px) and (max-width:1423px){.reds-tabs-list[data-v-bb2dbd52]{width:calc(100vw - 24px - calc((100vw - 6 * 24px) / 5 * 1))}}@media screen and (min-width:960px) and (max-width:1191px){.reds-tabs-list[data-v-bb2dbd52]{width:calc(100vw - 24px - calc((100vw - 5 * 24px) / 4 * 1))}}.collection-icon[data-v-bb2dbd52]{margin-right:4px}.feeds-tab-container[data-v-bb2dbd52]{padding-left:var(--horizontalGapPx)}.transform-container[data-v-bb2dbd52]{display:flex;will-change:transform;transform:translate(0,0);transition:var(--4e45219e);gap:var(--horizontalGapPx)}.lock-icon[data-v-bb2dbd52]{color:var(--color-secondary-label)}[data-v-bb2dbd52] .empty-note-container{width:100%;display:flex;justify-content:center;display:flex;align-items:center;justify-content:center}[data-v-bb2dbd52] .empty{display:flex;align-items:center;justify-content:center;flex-direction:column}[data-v-bb2dbd52] .empty-icon{color:var(--color-quaternary-label);border-radius:999px;border:1px solid var(--color-border)}[data-v-bb2dbd52] .empty-text{font-size:14px;line-height:18px;text-align:center;color:var(--color-tertiary-label);margin-top:16px}.width-auto[data-v-bb2dbd52]{width:auto}.sub-tab-list[data-v-bb2dbd52]{justify-content:flex-start}.divider[data-v-bb2dbd52]{width:100%;height:1px;background:var(--color-border);width:var(--feeds-width);margin:0 var(--horizontalGapPx)}[data-v-bb2dbd52] .empty-container{margin-top:72px}
.ban[data-v-21077154]{width:100%;margin-top:57px;display:flex;align-items:center;justify-content:center}.line[data-v-21077154]{margin:0 33px 0 33px;border-top:1px solid var(--color-border)}.content[data-v-21077154]{width:220px;height:100%;display:flex;align-items:center;justify-content:center;flex-direction:column;font-size:13px;line-height:20px;text-align:center;color:var(--color-tertiary-label)}.content .icon[data-v-21077154]{color:var(--color-quaternary-label);border-radius:999px;border:1px solid var(--color-border)}div[data-v-21077154]{margin-top:15px}
.ban[data-v-a800c388]{width:100%;margin-top:57px;display:flex;align-items:center;justify-content:center}.line[data-v-a800c388]{margin:0 33px 0 33px;border-top:1px solid var(--color-border)}.content[data-v-a800c388]{width:220px;height:100%;display:flex;align-items:center;justify-content:center;flex-direction:column;font-size:13px;line-height:20px;text-align:center;color:var(--color-tertiary-label)}.content .icon[data-v-a800c388]{color:var(--color-quaternary-label);border-radius:999px;border:1px solid var(--color-border)}div[data-v-a800c388]{margin-top:15px}
.silence[data-v-be825c32]{height:32px;background:var(--color-active-background);border-radius:999px;padding:0 12px;display:inline-block;font-size:14px;color:var(--color-tertiary-label);margin-top:24px}.silence .info[data-v-be825c32]{height:100%;display:flex;align-items:center;justify-content:center}.waring-icon[data-v-be825c32]{margin-right:6px}
.avatar-wrapper[data-v-86ee68bc]{text-align:center;width:calc((1728px - 7 * 32px) / 6 * 1);height:calc(0.7 * calc((1728px - 7 * 32px) / 6 * 1))}@media screen and (min-width:1424px) and (max-width:1727px){.avatar-wrapper[data-v-86ee68bc]{width:calc((100vw - 7 * 32px) / 6 * 1);height:calc(0.7 * calc((100vw - 7 * 32px) / 6 * 1))}}@media screen and (min-width:1192px) and (max-width:1423px){.avatar-wrapper[data-v-86ee68bc]{width:calc((100vw - 6 * 24px) / 5 * 1);height:calc(0.7 * calc((100vw - 6 * 24px) / 5 * 1))}}@media screen and (min-width:960px) and (max-width:1191px){.avatar-wrapper[data-v-86ee68bc]{width:calc((100vw - 5 * 24px) / 4 * 1);height:calc(0.7 * calc((100vw - 5 * 24px) / 4 * 1))}}@media screen and (min-width:696px) and (max-width:959px){.avatar-wrapper[data-v-86ee68bc]{width:calc((100vw - 4 * 24px) / 3 * 1);height:calc(0.7 * calc((100vw - 4 * 24px) / 3 * 1))}}@media screen and (max-width:695px){.avatar-wrapper[data-v-86ee68bc]{width:72px;height:72px}}.user-image[data-v-86ee68bc]{border-radius:50%;margin:0 auto;width:70%;height:100%;object-fit:cover}.user-image.no-avatar[data-v-86ee68bc]{display:inline-block;background-color:var(--color-active-background)}@media screen and (max-width:695px){.user-image[data-v-86ee68bc]{width:100%}}
.basic-info[data-v-1d90bc98]{display:flex;align-items:center}.user-basic[data-v-1d90bc98]{width:100%}@media screen and (max-width:695px){.user-basic[data-v-1d90bc98]{margin-left:16px}}.avatar[data-v-1d90bc98]{display:none}@media screen and (max-width:695px){.avatar[data-v-1d90bc98]{display:block}}.user-nickname[data-v-1d90bc98]{width:100%;display:flex;align-items:center;max-width:calc(100% - 144px)}@media screen and (max-width:695px){.user-nickname[data-v-1d90bc98]{max-width:100%}}.user-nickname .user-name[data-v-1d90bc98]{font-weight:600;font-size:24px;line-height:120%;color:var(--color-primary-label);word-wrap:break-word;width:100%}@media screen and (max-width:695px){.user-nickname .user-name[data-v-1d90bc98]{font-size:18px}}.verify-icon[data-v-1d90bc98]{display:inline-flex;margin-left:6px}.verify-icon .icon[data-v-1d90bc98]{height:20px;width:20px}@media screen and (max-width:695px){.verify-icon .icon[data-v-1d90bc98]{height:16px;width:16px}}.user-content[data-v-1d90bc98]{width:100%;font-size:12px;line-height:120%;color:var(--color-tertiary-label);display:flex;margin-top:8px}@media screen and (max-width:695px){.user-content[data-v-1d90bc98]{line-height:120%}}.user-redId[data-v-1d90bc98]{padding-right:12px}.user-IP[data-v-1d90bc98]{position:relative}.user-IP[data-v-1d90bc98]::before{content:'';display:block;height:12px;border-right:1px solid var(--color-border);position:absolute;left:-6px;top:2px}
.user-desc[data-v-4947d265]{width:100%;font-size:14px;line-height:140%;color:var(--color-primary-label);margin-top:16px;white-space:pre-line}.user-tags[data-v-4947d265]{margin-top:16px;display:flex;align-items:center;font-size:12px;color:var(--color-primary-label);text-align:center;font-weight:400;line-height:120%;flex-wrap:wrap;row-gap:var(--verticalGapPx)}.user-tags .tag-item[data-v-4947d265]{display:flex;align-items:center;justify-content:center;padding:4px 8px;gap:4px;height:18px;border-radius:41px;background:var(--color-active-background);height:24px;line-height:24px;margin-right:6px;color:var(--color-tertiary-label)}.user-tags .tag-item[data-v-4947d265]:first-child{padding:3px 6px}.user-tags .tag-item[data-v-4947d265]:last-child{margin-right:0}.user-tags .tag-item .gender[data-v-4947d265]{display:flex;align-items:center;justify-content:center}.user-tags .tag-item .gender .gender-text[data-v-4947d265]{margin-left:2px}
.data-info[data-v-18b45ae8]{display:flex;align-items:center;justify-content:center;margin-top:20px}.user-interactions[data-v-18b45ae8]{width:100%;display:flex;align-items:center}.user-interactions>div[data-v-18b45ae8]{height:100%;display:flex;align-items:center;justify-content:center;text-align:center;margin-right:16px}@media screen and (max-width:695px){.user-interactions>div[data-v-18b45ae8]{flex-direction:column}}.user-interactions>div[data-v-18b45ae8]:last-child{margin-right:0}.user-interactions .shows[data-v-18b45ae8]{color:var(--color-tertiary-label);font-size:14px;line-height:120%}@media screen and (max-width:695px){.user-interactions .shows[data-v-18b45ae8]{margin-top:4px}}.user-interactions .count[data-v-18b45ae8]{font-weight:500;font-size:14px;margin-right:4px}
.user[data-v-6be60601]{padding-top:72px;display:flex;align-items:center;justify-content:center}.user-info[data-v-6be60601]{display:flex;justify-content:center;padding:48px 0 48px 0}@media screen and (min-width:1192px) and (max-width:1423px){.user-info[data-v-6be60601]{padding:32px 0 32px 0}}@media screen and (min-width:960px) and (max-width:1191px){.user-info[data-v-6be60601]{padding:24px 0 24px 0}}@media screen and (min-width:696px) and (max-width:959px){.user-info[data-v-6be60601]{padding:24px 0 24px 0}}@media screen and (max-width:695px){.user-info[data-v-6be60601]{padding:16px;margin-right:auto;width:100vw}}@media screen and (max-width:695px){.avatar[data-v-6be60601]{display:none}}.info[data-v-6be60601]{margin-left:32px}@media screen and (min-width:1728px){.info[data-v-6be60601]{width:calc(32px + calc((1728px - 7 * 32px) / 6 * 2))}}@media screen and (min-width:1424px) and (max-width:1727px){.info[data-v-6be60601]{width:calc(32px + calc((100vw - 7 * 32px) / 6 * 2))}}@media screen and (min-width:1192px) and (max-width:1423px){.info[data-v-6be60601]{width:calc(24px + calc((100vw - 6 * 24px) / 5 * 2))}}@media screen and (min-width:960px) and (max-width:1191px){.info[data-v-6be60601]{width:calc(24px + calc((100vw - 5 * 24px) / 4 * 2))}}@media screen and (min-width:696px) and (max-width:959px){.info[data-v-6be60601]{width:calc(24px + calc((100vw - 4 * 24px) / 3 * 2))}}@media screen and (max-width:695px){.info[data-v-6be60601]{width:calc(12px + calc((100vw - 3 * 12px) / 2 * 2))}}@media screen and (min-width:696px) and (max-width:1191px){.info[data-v-6be60601]{margin-left:24px}}@media screen and (max-width:695px){.info[data-v-6be60601]{margin-left:0;width:auto}}.info-part[data-v-6be60601]{position:relative;width:100%}.info-right-area[data-v-6be60601]{position:absolute;margin-left:auto;display:flex;right:0;top:0}@media screen and (max-width:695px){.info-right-area[data-v-6be60601]{bottom:0;top:auto}}.info-right-area .info-right-area-more-container[data-v-6be60601]{margin-left:8px;z-index:5}
.user-page-skeleton[data-v-2f9164cc]{padding-top:72px}.user-info-wrapper[data-v-2f9164cc]{display:flex;justify-content:center;padding:48px 0 48px 0}@media screen and (min-width:1192px) and (max-width:1423px){.user-info-wrapper[data-v-2f9164cc]{padding:32px 0 32px 0}}@media screen and (min-width:960px) and (max-width:1191px){.user-info-wrapper[data-v-2f9164cc]{padding:24px 0 24px 0}}@media screen and (min-width:696px) and (max-width:959px){.user-info-wrapper[data-v-2f9164cc]{padding:24px 0 24px 0}}@media screen and (max-width:695px){.user-info-wrapper[data-v-2f9164cc]{padding:16px;margin-right:auto;width:100vw}}.user-info-skeleton-small[data-v-2f9164cc]{width:100%;height:100%;display:none}@media screen and (max-width:695px){.user-info-skeleton-small[data-v-2f9164cc]{display:block}}.user-info-skeleton-small .info-skeleton-small[data-v-2f9164cc]{width:auto;color:var(--color-active-background)}.info[data-v-2f9164cc]{margin-left:32px}@media screen and (min-width:1728px){.info[data-v-2f9164cc]{width:calc(32px + calc((1728px - 7 * 32px) / 6 * 2))}}@media screen and (min-width:1424px) and (max-width:1727px){.info[data-v-2f9164cc]{width:calc(32px + calc((100vw - 7 * 32px) / 6 * 2))}}@media screen and (min-width:1192px) and (max-width:1423px){.info[data-v-2f9164cc]{width:calc(24px + calc((100vw - 6 * 24px) / 5 * 2))}}@media screen and (min-width:960px) and (max-width:1191px){.info[data-v-2f9164cc]{width:calc(24px + calc((100vw - 5 * 24px) / 4 * 2))}}@media screen and (min-width:696px) and (max-width:959px){.info[data-v-2f9164cc]{width:calc(24px + calc((100vw - 4 * 24px) / 3 * 2))}}@media screen and (max-width:695px){.info[data-v-2f9164cc]{width:calc(12px + calc((100vw - 3 * 12px) / 2 * 2))}}@media screen and (min-width:696px) and (max-width:1191px){.info[data-v-2f9164cc]{margin-left:24px}}@media screen and (max-width:695px){.info[data-v-2f9164cc]{display:none}}.info-skeleton[data-v-2f9164cc]{height:100%;width:100%;color:var(--color-active-background)}.avatar-skeleton-wrapper[data-v-2f9164cc]{text-align:center;width:calc((1728px - 7 * 32px) / 6 * 1);height:calc(0.7 * calc((1728px - 7 * 32px) / 6 * 1))}@media screen and (min-width:1424px) and (max-width:1727px){.avatar-skeleton-wrapper[data-v-2f9164cc]{width:calc((100vw - 7 * 32px) / 6 * 1);height:calc(0.7 * calc((100vw - 7 * 32px) / 6 * 1))}}@media screen and (min-width:1192px) and (max-width:1423px){.avatar-skeleton-wrapper[data-v-2f9164cc]{width:calc((100vw - 6 * 24px) / 5 * 1);height:calc(0.7 * calc((100vw - 6 * 24px) / 5 * 1))}}@media screen and (min-width:960px) and (max-width:1191px){.avatar-skeleton-wrapper[data-v-2f9164cc]{width:calc((100vw - 5 * 24px) / 4 * 1);height:calc(0.7 * calc((100vw - 5 * 24px) / 4 * 1))}}@media screen and (min-width:696px) and (max-width:959px){.avatar-skeleton-wrapper[data-v-2f9164cc]{width:calc((100vw - 4 * 24px) / 3 * 1);height:calc(0.7 * calc((100vw - 4 * 24px) / 3 * 1))}}@media screen and (max-width:695px){.avatar-skeleton-wrapper[data-v-2f9164cc]{display:none}}.avatar-skeleton[data-v-2f9164cc]{border-radius:50%;height:100%;color:var(--color-active-background)}.tab[data-v-2f9164cc]{height:72px}.note-skeleton[data-v-2f9164cc]{margin-left:var(--504beeb6)}
.user-page[data-v-8069da68]{background:var(--color-background);overflow-y:scroll;overflow-x:hidden;flex:1}.show-tabs[data-v-8069da68]{width:100%;height:44px;font-size:16px;line-height:20px;display:flex;align-items:center;justify-content:center;cursor:pointer}.show-tabs .note[data-v-8069da68]{height:100%;padding:12px 16px;font-weight:500;color:var(--color-primary-label)}.show-tabs .note .number[data-v-8069da68]{color:var(--color-tertiary-label);font-size:14px}.show-tabs .note .line[data-v-8069da68]{padding:0 3px}

</style><script src="https://fe-video-qc.xhscdn.com/fe-platform/abf6e0874371419fa6fffa7540610e2013588fe6/html2canvas.min.js"></script><link rel="stylesheet" type="text/css" href="https://fe-static.xhscdn.com/formula-static/xhs-pc-web/public/resource/css/async/772.db47c221.css"><link rel="stylesheet" type="text/css" href="https://fe-static.xhscdn.com/formula-static/xhs-pc-web/public/resource/css/async/75.693a9a9c.css"><style>:root .heshen_B_Blue_light{--color-primary: rgba(35, 114, 251, 1);--color-info: rgba(35, 114, 251, 1);--color-success: rgba(0, 171, 71, 1);--color-success-hover: rgba(0, 143, 60, 1);--color-success-pressing: rgba(0, 110, 48, 1);--color-success-disabled: rgba(140, 232, 170, 1);--color-success-light: rgba(225, 250, 235, 1);--color-success-light-hover: rgba(194, 243, 214, 1);--color-success-light-pressing: rgba(140, 232, 170, 1);--color-info-hover: rgba(26, 95, 213, 1);--color-info-pressing: rgba(19, 76, 178, 1);--color-info-disabled: rgba(185, 212, 254, 1);--color-info-light: rgba(235, 243, 255, 1);--color-info-light-hover: rgba(214, 230, 255, 1);--color-info-light-pressing: rgba(185, 212, 254, 1);--color-primary-hover: rgba(26, 95, 213, 1);--color-primary-pressing: rgba(19, 76, 178, 1);--color-primary-disabled: rgba(185, 212, 254, 1);--color-primary-light: rgba(235, 243, 255, 1);--color-primary-light-hover: rgba(214, 230, 255, 1);--color-primary-light-pressing: rgba(185, 212, 254, 1);--color-danger: rgba(251, 51, 103, 1);--color-danger-hover: rgba(214, 33, 77, 1);--color-danger-pressing: rgba(172, 18, 58, 1);--color-danger-disabled: rgba(254, 177, 195, 1);--color-danger-light: rgba(255, 236, 242, 1);--color-danger-light-hover: rgba(255, 216, 228, 1);--color-danger-light-pressing: rgba(254, 177, 195, 1);--color-warning: rgba(253, 99, 33, 1);--color-warning-hover: rgba(228, 84, 16, 1);--color-warning-pressing: rgba(189, 64, 0, 1);--color-warning-disabled: rgba(255, 193, 160, 1);--color-warning-light: rgba(255, 238, 229, 1);--color-warning-light-hover: rgba(254, 223, 206, 1);--color-warning-light-pressing: rgba(255, 193, 160, 1);--color-text-title: rgba(0, 0, 0, .85);--color-text-paragraph: rgba(0, 0, 0, .7);--color-text-description: rgba(0, 0, 0, .53);--color-text-placeholder: rgba(0, 0, 0, .42);--color-text-disabled: rgba(0, 0, 0, .2);--color-bg: rgba(255, 255, 255, 1);--color-bg-: rgba(245, 245, 245, 1);--color-bg-1: rgba(250, 250, 250, 1);--color-bg-2: rgba(255, 255, 255, 1);--color-fill: rgba(0, 0, 0, .03);--color-fill-hover: rgba(0, 0, 0, .05);--color-fill-pressing: rgba(0, 0, 0, .08);--color-fill-disabled: rgba(0, 0, 0, .02);--color-fill-light: rgba(0, 0, 0, 0);--color-line-divider: rgba(0, 0, 0, .08);--color-line-stroke: rgba(0, 0, 0, .1);--color-fill-mask: rgba(0, 0, 0, .8);--color-mask-light: rgba(0, 0, 0, .65);--color-mask-loading: rgba(255, 255, 255, .7);--color-brand-0: rgba(255, 247, 246, 1);--color-brand-1: rgba(255, 237, 235, 1);--color-brand-2: rgba(255, 216, 213, 1);--color-brand-3: rgba(255, 183, 180, 1);--color-brand-4: rgba(255, 141, 142, 1);--color-brand-5: rgba(255, 89, 99, 1);--color-brand-6: rgba(255, 36, 66, 1);--color-brand-7: rgba(219, 0, 49, 1);--color-brand-8: rgba(160, 0, 32, 1);--color-brand-9: rgba(130, 0, 21, 1);--color-brand-10: rgba(72, 0, 9, 1);--color-white: rgba(255, 255, 255, 1);--color-grey-0: rgba(250, 250, 250, 1);--color-grey-1: rgba(243, 243, 243, 1);--color-grey-2: rgba(226, 226, 226, 1);--color-grey-3: rgba(204, 204, 204, 1);--color-grey-4: rgba(180, 180, 180, 1);--color-grey-5: rgba(157, 157, 157, 1);--color-grey-6: rgba(136, 136, 136, 1);--color-grey-7: rgba(116, 116, 116, 1);--color-grey-8: rgba(97, 97, 97, 1);--color-grey-9: rgba(78, 78, 78, 1);--color-grey-10: rgba(61, 61, 61, 1);--color-black: rgba(0, 0, 0, 1);--color-red-0: rgba(255, 248, 250, 1);--color-red-1: rgba(255, 236, 242, 1);--color-red-2: rgba(255, 216, 228, 1);--color-red-3: rgba(254, 177, 195, 1);--color-red-4: rgba(255, 139, 161, 1);--color-red-5: rgba(253, 100, 128, 1);--color-red-6: rgba(251, 51, 103, 1);--color-red-7: rgba(214, 33, 77, 1);--color-red-8: rgba(172, 18, 58, 1);--color-red-9: rgba(120, 15, 39, 1);--color-red-10: rgba(83, 0, 27, 1);--color-orange-0: rgba(255, 247, 243, 1);--color-orange-1: rgba(255, 238, 229, 1);--color-orange-2: rgba(254, 223, 206, 1);--color-orange-3: rgba(255, 193, 160, 1);--color-orange-4: rgba(255, 162, 117, 1);--color-orange-5: rgba(255, 131, 79, 1);--color-orange-6: rgba(253, 99, 33, 1);--color-orange-7: rgba(228, 84, 16, 1);--color-orange-8: rgba(189, 64, 0, 1);--color-orange-9: rgba(137, 44, 0, 1);--color-orange-10: rgba(95, 32, 0, 1);--color-yellow-0: rgba(255, 250, 222, 1);--color-yellow-1: rgba(252, 244, 207, 1);--color-yellow-2: rgba(253, 239, 171, 1);--color-yellow-3: rgba(255, 232, 140, 1);--color-yellow-4: rgba(252, 222, 108, 1);--color-yellow-5: rgba(255, 211, 47, 1);--color-yellow-6: rgba(247, 198, 0, 1);--color-yellow-7: rgba(222, 178, 0, 1);--color-yellow-8: rgba(188, 144, 0, 1);--color-yellow-9: rgba(154, 118, 0, 1);--color-yellow-10: rgba(122, 93, 0, 1);--color-green-0: rgba(239, 253, 245, 1);--color-green-1: rgba(225, 250, 235, 1);--color-green-2: rgba(194, 243, 214, 1);--color-green-3: rgba(140, 232, 170, 1);--color-green-4: rgba(80, 211, 127, 1);--color-green-5: rgba(33, 196, 99, 1);--color-green-6: rgba(0, 171, 71, 1);--color-green-7: rgba(0, 143, 60, 1);--color-green-8: rgba(0, 110, 48, 1);--color-green-9: rgba(0, 79, 33, 1);--color-green-10: rgba(4, 49, 22, 1);--color-teal-0: rgba(245, 251, 251, 1);--color-teal-1: rgba(232, 247, 246, 1);--color-teal-2: rgba(208, 238, 235, 1);--color-teal-3: rgba(157, 222, 217, 1);--color-teal-4: rgba(115, 203, 196, 1);--color-teal-5: rgba(0, 183, 169, 1);--color-teal-6: rgba(0, 154, 141, 1);--color-teal-7: rgba(0, 126, 116, 1);--color-teal-8: rgba(0, 99, 91, 1);--color-teal-9: rgba(0, 73, 67, 1);--color-teal-10: rgba(8, 55, 51, 1);--color-cyan-0: rgba(242, 251, 254, 1);--color-cyan-1: rgba(231, 246, 254, 1);--color-cyan-2: rgba(207, 237, 253, 1);--color-cyan-3: rgba(155, 218, 251, 1);--color-cyan-4: rgba(104, 195, 243, 1);--color-cyan-5: rgba(38, 175, 231, 1);--color-cyan-6: rgba(10, 143, 201, 1);--color-cyan-7: rgba(9, 108, 156, 1);--color-cyan-8: rgba(13, 83, 120, 1);--color-cyan-9: rgba(3, 58, 86, 1);--color-cyan-10: rgba(3, 39, 57, 1);--color-blue-0: rgba(250, 252, 255, 1);--color-blue-1: rgba(235, 243, 255, 1);--color-blue-2: rgba(214, 230, 255, 1);--color-blue-3: rgba(185, 212, 254, 1);--color-blue-4: rgba(126, 176, 251, 1);--color-blue-5: rgba(75, 140, 251, 1);--color-blue-6: rgba(35, 114, 251, 1);--color-blue-7: rgba(26, 95, 213, 1);--color-blue-8: rgba(19, 76, 178, 1);--color-blue-9: rgba(15, 58, 133, 1);--color-blue-10: rgba(18, 38, 74, 1);--color-purple-0: rgba(250, 248, 255, 1);--color-purple-1: rgba(243, 238, 255, 1);--color-purple-2: rgba(232, 220, 255, 1);--color-purple-3: rgba(210, 187, 255, 1);--color-purple-4: rgba(187, 153, 255, 1);--color-purple-5: rgba(162, 120, 254, 1);--color-purple-6: rgba(135, 89, 236, 1);--color-purple-7: rgba(108, 65, 200, 1);--color-purple-8: rgba(82, 47, 157, 1);--color-purple-9: rgba(56, 32, 108, 1);--color-purple-10: rgba(39, 16, 81, 1);--color-violet-0: rgba(252, 248, 253, 1);--color-violet-1: rgba(249, 238, 251, 1);--color-violet-2: rgba(242, 218, 248, 1);--color-violet-3: rgba(230, 180, 243, 1);--color-violet-4: rgba(217, 144, 235, 1);--color-violet-5: rgba(200, 108, 222, 1);--color-violet-6: rgba(175, 74, 200, 1);--color-violet-7: rgba(144, 52, 167, 1);--color-violet-8: rgba(111, 37, 129, 1);--color-violet-9: rgba(76, 24, 89, 1);--color-violet-10: rgba(59, 8, 72, 1);--color-pink-0: rgba(254, 246, 251, 1);--color-pink-1: rgba(253, 237, 248, 1);--color-pink-2: rgba(253, 215, 240, 1);--color-pink-3: rgba(251, 174, 226, 1);--color-pink-4: rgba(250, 134, 212, 1);--color-pink-5: rgba(241, 93, 192, 1);--color-pink-6: rgba(213, 61, 162, 1);--color-pink-7: rgba(177, 41, 130, 1);--color-pink-8: rgba(137, 29, 100, 1);--color-pink-9: rgba(96, 21, 71, 1);--color-pink-10: rgba(73, 1, 55, 1);--contrast-0: rgba(255, 255, 255, 1);--color-fill-opaque: rgba(255, 255, 255, 1);--color-fill-hover-opaque: rgba(242, 242, 242, 1);--color-fill-pressing-opaque: rgba(235, 235, 235, 1);--color-fill-disabled-opaque: rgba(250, 250, 250, 1);--contrast-12: rgba(0, 0, 0, .08);--contrast-15: rgba(0, 0, 0, .18);--contrast-18: rgba(0, 0, 0, .24);--contrast-21: rgba(0, 0, 0, .3);--contrast-full: rgba(0, 0, 0, 1);--color-dark-bg: rgba(61, 61, 61, 1);--padding-size-radius-component: 4px;--padding-size-space-container: 5px;--padding-size-radius-container: 6px;--color-bg-Button-Primary-default: rgba(35, 114, 251, 1);--color-bg-Button-Primary-hover: rgba(26, 95, 213, 1);--color-bg-Button-Primary-pressing: rgba(19, 76, 178, 1);--color-bg-Button-Primary-disabled: rgba(185, 212, 254, 1)}:root .heshen_B_Red_light{--color-primary: rgba(255, 36, 66, 1);--color-info: rgba(35, 114, 251, 1);--color-success: rgba(0, 171, 71, 1);--color-success-hover: rgba(0, 143, 60, 1);--color-success-pressing: rgba(0, 110, 48, 1);--color-success-disabled: rgba(140, 232, 170, 1);--color-success-light: rgba(225, 250, 235, 1);--color-success-light-hover: rgba(194, 243, 214, 1);--color-success-light-pressing: rgba(140, 232, 170, 1);--color-info-hover: rgba(26, 95, 213, 1);--color-info-pressing: rgba(19, 76, 178, 1);--color-info-disabled: rgba(185, 212, 254, 1);--color-info-light: rgba(235, 243, 255, 1);--color-info-light-hover: rgba(214, 230, 255, 1);--color-info-light-pressing: rgba(185, 212, 254, 1);--color-primary-hover: rgba(219, 0, 49, 1);--color-primary-pressing: rgba(160, 0, 32, 1);--color-primary-disabled: rgba(255, 183, 180, 1);--color-primary-light: rgba(255, 237, 235, 1);--color-primary-light-hover: rgba(255, 216, 213, 1);--color-primary-light-pressing: rgba(255, 183, 180, 1);--color-danger: rgba(251, 51, 103, 1);--color-danger-hover: rgba(214, 33, 77, 1);--color-danger-pressing: rgba(172, 18, 58, 1);--color-danger-disabled: rgba(254, 177, 195, 1);--color-danger-light: rgba(255, 236, 242, 1);--color-danger-light-hover: rgba(255, 216, 228, 1);--color-danger-light-pressing: rgba(254, 177, 195, 1);--color-warning: rgba(253, 99, 33, 1);--color-warning-hover: rgba(228, 84, 16, 1);--color-warning-pressing: rgba(189, 64, 0, 1);--color-warning-disabled: rgba(255, 193, 160, 1);--color-warning-light: rgba(255, 238, 229, 1);--color-warning-light-hover: rgba(254, 223, 206, 1);--color-warning-light-pressing: rgba(255, 193, 160, 1);--color-text-title: rgba(0, 0, 0, .85);--color-text-paragraph: rgba(0, 0, 0, .7);--color-text-description: rgba(0, 0, 0, .53);--color-text-placeholder: rgba(0, 0, 0, .42);--color-text-disabled: rgba(0, 0, 0, .2);--color-bg: rgba(255, 255, 255, 1);--color-bg-: rgba(245, 245, 245, 1);--color-bg-1: rgba(250, 250, 250, 1);--color-bg-2: rgba(255, 255, 255, 1);--color-fill: rgba(0, 0, 0, .03);--color-fill-hover: rgba(0, 0, 0, .05);--color-fill-pressing: rgba(0, 0, 0, .08);--color-fill-disabled: rgba(0, 0, 0, .02);--color-fill-light: rgba(0, 0, 0, 0);--color-line-divider: rgba(0, 0, 0, .08);--color-line-stroke: rgba(0, 0, 0, .1);--color-fill-mask: rgba(0, 0, 0, .8);--color-mask-light: rgba(0, 0, 0, .65);--color-mask-loading: rgba(255, 255, 255, .7);--color-brand-0: rgba(255, 247, 246, 1);--color-brand-1: rgba(255, 237, 235, 1);--color-brand-2: rgba(255, 216, 213, 1);--color-brand-3: rgba(255, 183, 180, 1);--color-brand-4: rgba(255, 141, 142, 1);--color-brand-5: rgba(255, 89, 99, 1);--color-brand-6: rgba(255, 36, 66, 1);--color-brand-7: rgba(219, 0, 49, 1);--color-brand-8: rgba(160, 0, 32, 1);--color-brand-9: rgba(130, 0, 21, 1);--color-brand-10: rgba(72, 0, 9, 1);--color-white: rgba(255, 255, 255, 1);--color-grey-0: rgba(250, 250, 250, 1);--color-grey-1: rgba(243, 243, 243, 1);--color-grey-2: rgba(226, 226, 226, 1);--color-grey-3: rgba(204, 204, 204, 1);--color-grey-4: rgba(180, 180, 180, 1);--color-grey-5: rgba(157, 157, 157, 1);--color-grey-6: rgba(136, 136, 136, 1);--color-grey-7: rgba(116, 116, 116, 1);--color-grey-8: rgba(97, 97, 97, 1);--color-grey-9: rgba(78, 78, 78, 1);--color-grey-10: rgba(61, 61, 61, 1);--color-black: rgba(0, 0, 0, 1);--color-red-0: rgba(255, 248, 250, 1);--color-red-1: rgba(255, 236, 242, 1);--color-red-2: rgba(255, 216, 228, 1);--color-red-3: rgba(254, 177, 195, 1);--color-red-4: rgba(255, 139, 161, 1);--color-red-5: rgba(253, 100, 128, 1);--color-red-6: rgba(251, 51, 103, 1);--color-red-7: rgba(214, 33, 77, 1);--color-red-8: rgba(172, 18, 58, 1);--color-red-9: rgba(120, 15, 39, 1);--color-red-10: rgba(83, 0, 27, 1);--color-orange-0: rgba(255, 247, 243, 1);--color-orange-1: rgba(255, 238, 229, 1);--color-orange-2: rgba(254, 223, 206, 1);--color-orange-3: rgba(255, 193, 160, 1);--color-orange-4: rgba(255, 162, 117, 1);--color-orange-5: rgba(255, 131, 79, 1);--color-orange-6: rgba(253, 99, 33, 1);--color-orange-7: rgba(228, 84, 16, 1);--color-orange-8: rgba(189, 64, 0, 1);--color-orange-9: rgba(137, 44, 0, 1);--color-orange-10: rgba(95, 32, 0, 1);--color-yellow-0: rgba(255, 250, 222, 1);--color-yellow-1: rgba(252, 244, 207, 1);--color-yellow-2: rgba(253, 239, 171, 1);--color-yellow-3: rgba(255, 232, 140, 1);--color-yellow-4: rgba(252, 222, 108, 1);--color-yellow-5: rgba(255, 211, 47, 1);--color-yellow-6: rgba(247, 198, 0, 1);--color-yellow-7: rgba(222, 178, 0, 1);--color-yellow-8: rgba(188, 144, 0, 1);--color-yellow-9: rgba(154, 118, 0, 1);--color-yellow-10: rgba(122, 93, 0, 1);--color-green-0: rgba(239, 253, 245, 1);--color-green-1: rgba(225, 250, 235, 1);--color-green-2: rgba(194, 243, 214, 1);--color-green-3: rgba(140, 232, 170, 1);--color-green-4: rgba(80, 211, 127, 1);--color-green-5: rgba(33, 196, 99, 1);--color-green-6: rgba(0, 171, 71, 1);--color-green-7: rgba(0, 143, 60, 1);--color-green-8: rgba(0, 110, 48, 1);--color-green-9: rgba(0, 79, 33, 1);--color-green-10: rgba(4, 49, 22, 1);--color-teal-0: rgba(245, 251, 251, 1);--color-teal-1: rgba(232, 247, 246, 1);--color-teal-2: rgba(208, 238, 235, 1);--color-teal-3: rgba(157, 222, 217, 1);--color-teal-4: rgba(115, 203, 196, 1);--color-teal-5: rgba(0, 183, 169, 1);--color-teal-6: rgba(0, 154, 141, 1);--color-teal-7: rgba(0, 126, 116, 1);--color-teal-8: rgba(0, 99, 91, 1);--color-teal-9: rgba(0, 73, 67, 1);--color-teal-10: rgba(8, 55, 51, 1);--color-cyan-0: rgba(242, 251, 254, 1);--color-cyan-1: rgba(231, 246, 254, 1);--color-cyan-2: rgba(207, 237, 253, 1);--color-cyan-3: rgba(155, 218, 251, 1);--color-cyan-4: rgba(104, 195, 243, 1);--color-cyan-5: rgba(38, 175, 231, 1);--color-cyan-6: rgba(10, 143, 201, 1);--color-cyan-7: rgba(9, 108, 156, 1);--color-cyan-8: rgba(13, 83, 120, 1);--color-cyan-9: rgba(3, 58, 86, 1);--color-cyan-10: rgba(3, 39, 57, 1);--color-blue-0: rgba(250, 252, 255, 1);--color-blue-1: rgba(235, 243, 255, 1);--color-blue-2: rgba(214, 230, 255, 1);--color-blue-3: rgba(185, 212, 254, 1);--color-blue-4: rgba(126, 176, 251, 1);--color-blue-5: rgba(75, 140, 251, 1);--color-blue-6: rgba(35, 114, 251, 1);--color-blue-7: rgba(26, 95, 213, 1);--color-blue-8: rgba(19, 76, 178, 1);--color-blue-9: rgba(15, 58, 133, 1);--color-blue-10: rgba(18, 38, 74, 1);--color-purple-0: rgba(250, 248, 255, 1);--color-purple-1: rgba(243, 238, 255, 1);--color-purple-2: rgba(232, 220, 255, 1);--color-purple-3: rgba(210, 187, 255, 1);--color-purple-4: rgba(187, 153, 255, 1);--color-purple-5: rgba(162, 120, 254, 1);--color-purple-6: rgba(135, 89, 236, 1);--color-purple-7: rgba(108, 65, 200, 1);--color-purple-8: rgba(82, 47, 157, 1);--color-purple-9: rgba(56, 32, 108, 1);--color-purple-10: rgba(39, 16, 81, 1);--color-violet-0: rgba(252, 248, 253, 1);--color-violet-1: rgba(249, 238, 251, 1);--color-violet-2: rgba(242, 218, 248, 1);--color-violet-3: rgba(230, 180, 243, 1);--color-violet-4: rgba(217, 144, 235, 1);--color-violet-5: rgba(200, 108, 222, 1);--color-violet-6: rgba(175, 74, 200, 1);--color-violet-7: rgba(144, 52, 167, 1);--color-violet-8: rgba(111, 37, 129, 1);--color-violet-9: rgba(76, 24, 89, 1);--color-violet-10: rgba(59, 8, 72, 1);--color-pink-0: rgba(254, 246, 251, 1);--color-pink-1: rgba(253, 237, 248, 1);--color-pink-2: rgba(253, 215, 240, 1);--color-pink-3: rgba(251, 174, 226, 1);--color-pink-4: rgba(250, 134, 212, 1);--color-pink-5: rgba(241, 93, 192, 1);--color-pink-6: rgba(213, 61, 162, 1);--color-pink-7: rgba(177, 41, 130, 1);--color-pink-8: rgba(137, 29, 100, 1);--color-pink-9: rgba(96, 21, 71, 1);--color-pink-10: rgba(73, 1, 55, 1);--contrast-0: rgba(255, 255, 255, 1);--color-fill-opaque: rgba(255, 255, 255, 1);--color-fill-hover-opaque: rgba(242, 242, 242, 1);--color-fill-pressing-opaque: rgba(235, 235, 235, 1);--color-fill-disabled-opaque: rgba(250, 250, 250, 1);--contrast-12: rgba(0, 0, 0, .08);--contrast-15: rgba(0, 0, 0, .18);--contrast-18: rgba(0, 0, 0, .24);--contrast-21: rgba(0, 0, 0, .3);--contrast-full: rgba(0, 0, 0, 1);--color-dark-bg: rgba(61, 61, 61, 1);--padding-size-radius-component: 4px;--padding-size-space-container: 5px;--padding-size-radius-container: 6px;--color-bg-Button-Primary-default: rgba(255, 36, 66, 1);--color-bg-Button-Primary-hover: rgba(219, 0, 49, 1);--color-bg-Button-Primary-pressing: rgba(160, 0, 32, 1);--color-bg-Button-Primary-disabled: rgba(255, 183, 180, 1)}:root .heshen_C_Red_light{--color-primary: rgba(255, 36, 66, 1);--color-info: rgba(35, 114, 251, 1);--color-success: rgba(0, 171, 71, 1);--color-success-hover: rgba(0, 143, 60, 1);--color-success-pressing: rgba(0, 110, 48, 1);--color-success-disabled: rgba(140, 232, 170, 1);--color-success-light: rgba(225, 250, 235, 1);--color-success-light-hover: rgba(194, 243, 214, 1);--color-success-light-pressing: rgba(140, 232, 170, 1);--color-info-hover: rgba(26, 95, 213, 1);--color-info-pressing: rgba(19, 76, 178, 1);--color-info-disabled: rgba(185, 212, 254, 1);--color-info-light: rgba(235, 243, 255, 1);--color-info-light-hover: rgba(214, 230, 255, 1);--color-info-light-pressing: rgba(185, 212, 254, 1);--color-primary-hover: rgba(219, 0, 49, 1);--color-primary-pressing: rgba(160, 0, 32, 1);--color-primary-disabled: rgba(255, 183, 180, 1);--color-primary-light: rgba(255, 237, 235, 1);--color-primary-light-hover: rgba(255, 216, 213, 1);--color-primary-light-pressing: rgba(255, 183, 180, 1);--color-danger: rgba(251, 51, 103, 1);--color-danger-hover: rgba(214, 33, 77, 1);--color-danger-pressing: rgba(172, 18, 58, 1);--color-danger-disabled: rgba(254, 177, 195, 1);--color-danger-light: rgba(255, 236, 242, 1);--color-danger-light-hover: rgba(255, 216, 228, 1);--color-danger-light-pressing: rgba(254, 177, 195, 1);--color-warning: rgba(253, 99, 33, 1);--color-warning-hover: rgba(228, 84, 16, 1);--color-warning-pressing: rgba(189, 64, 0, 1);--color-warning-disabled: rgba(255, 193, 160, 1);--color-warning-light: rgba(255, 238, 229, 1);--color-warning-light-hover: rgba(254, 223, 206, 1);--color-warning-light-pressing: rgba(255, 193, 160, 1);--color-text-title: rgba(0, 0, 0, .85);--color-text-paragraph: rgba(0, 0, 0, .7);--color-text-description: rgba(0, 0, 0, .53);--color-text-placeholder: rgba(0, 0, 0, .42);--color-text-disabled: rgba(0, 0, 0, .2);--color-bg: rgba(255, 255, 255, 1);--color-bg-: rgba(245, 245, 245, 1);--color-bg-1: rgba(250, 250, 250, 1);--color-bg-2: rgba(255, 255, 255, 1);--color-fill: rgba(0, 0, 0, .03);--color-fill-hover: rgba(0, 0, 0, .05);--color-fill-pressing: rgba(0, 0, 0, .08);--color-fill-disabled: rgba(0, 0, 0, .02);--color-fill-light: rgba(0, 0, 0, 0);--color-line-divider: rgba(0, 0, 0, .08);--color-line-stroke: rgba(0, 0, 0, .1);--color-fill-mask: rgba(0, 0, 0, .8);--color-mask-light: rgba(0, 0, 0, .65);--color-mask-loading: rgba(255, 255, 255, .7);--color-brand-0: rgba(255, 247, 246, 1);--color-brand-1: rgba(255, 237, 235, 1);--color-brand-2: rgba(255, 216, 213, 1);--color-brand-3: rgba(255, 183, 180, 1);--color-brand-4: rgba(255, 141, 142, 1);--color-brand-5: rgba(255, 89, 99, 1);--color-brand-6: rgba(255, 36, 66, 1);--color-brand-7: rgba(219, 0, 49, 1);--color-brand-8: rgba(160, 0, 32, 1);--color-brand-9: rgba(130, 0, 21, 1);--color-brand-10: rgba(72, 0, 9, 1);--color-white: rgba(255, 255, 255, 1);--color-grey-0: rgba(250, 250, 250, 1);--color-grey-1: rgba(243, 243, 243, 1);--color-grey-2: rgba(226, 226, 226, 1);--color-grey-3: rgba(204, 204, 204, 1);--color-grey-4: rgba(180, 180, 180, 1);--color-grey-5: rgba(157, 157, 157, 1);--color-grey-6: rgba(136, 136, 136, 1);--color-grey-7: rgba(116, 116, 116, 1);--color-grey-8: rgba(97, 97, 97, 1);--color-grey-9: rgba(78, 78, 78, 1);--color-grey-10: rgba(61, 61, 61, 1);--color-black: rgba(0, 0, 0, 1);--color-red-0: rgba(255, 248, 250, 1);--color-red-1: rgba(255, 236, 242, 1);--color-red-2: rgba(255, 216, 228, 1);--color-red-3: rgba(254, 177, 195, 1);--color-red-4: rgba(255, 139, 161, 1);--color-red-5: rgba(253, 100, 128, 1);--color-red-6: rgba(251, 51, 103, 1);--color-red-7: rgba(214, 33, 77, 1);--color-red-8: rgba(172, 18, 58, 1);--color-red-9: rgba(120, 15, 39, 1);--color-red-10: rgba(83, 0, 27, 1);--color-orange-0: rgba(255, 247, 243, 1);--color-orange-1: rgba(255, 238, 229, 1);--color-orange-2: rgba(254, 223, 206, 1);--color-orange-3: rgba(255, 193, 160, 1);--color-orange-4: rgba(255, 162, 117, 1);--color-orange-5: rgba(255, 131, 79, 1);--color-orange-6: rgba(253, 99, 33, 1);--color-orange-7: rgba(228, 84, 16, 1);--color-orange-8: rgba(189, 64, 0, 1);--color-orange-9: rgba(137, 44, 0, 1);--color-orange-10: rgba(95, 32, 0, 1);--color-yellow-0: rgba(255, 250, 222, 1);--color-yellow-1: rgba(252, 244, 207, 1);--color-yellow-2: rgba(253, 239, 171, 1);--color-yellow-3: rgba(255, 232, 140, 1);--color-yellow-4: rgba(252, 222, 108, 1);--color-yellow-5: rgba(255, 211, 47, 1);--color-yellow-6: rgba(247, 198, 0, 1);--color-yellow-7: rgba(222, 178, 0, 1);--color-yellow-8: rgba(188, 144, 0, 1);--color-yellow-9: rgba(154, 118, 0, 1);--color-yellow-10: rgba(122, 93, 0, 1);--color-green-0: rgba(239, 253, 245, 1);--color-green-1: rgba(225, 250, 235, 1);--color-green-2: rgba(194, 243, 214, 1);--color-green-3: rgba(140, 232, 170, 1);--color-green-4: rgba(80, 211, 127, 1);--color-green-5: rgba(33, 196, 99, 1);--color-green-6: rgba(0, 171, 71, 1);--color-green-7: rgba(0, 143, 60, 1);--color-green-8: rgba(0, 110, 48, 1);--color-green-9: rgba(0, 79, 33, 1);--color-green-10: rgba(4, 49, 22, 1);--color-teal-0: rgba(245, 251, 251, 1);--color-teal-1: rgba(232, 247, 246, 1);--color-teal-2: rgba(208, 238, 235, 1);--color-teal-3: rgba(157, 222, 217, 1);--color-teal-4: rgba(115, 203, 196, 1);--color-teal-5: rgba(0, 183, 169, 1);--color-teal-6: rgba(0, 154, 141, 1);--color-teal-7: rgba(0, 126, 116, 1);--color-teal-8: rgba(0, 99, 91, 1);--color-teal-9: rgba(0, 73, 67, 1);--color-teal-10: rgba(8, 55, 51, 1);--color-cyan-0: rgba(242, 251, 254, 1);--color-cyan-1: rgba(231, 246, 254, 1);--color-cyan-2: rgba(207, 237, 253, 1);--color-cyan-3: rgba(155, 218, 251, 1);--color-cyan-4: rgba(104, 195, 243, 1);--color-cyan-5: rgba(38, 175, 231, 1);--color-cyan-6: rgba(10, 143, 201, 1);--color-cyan-7: rgba(9, 108, 156, 1);--color-cyan-8: rgba(13, 83, 120, 1);--color-cyan-9: rgba(3, 58, 86, 1);--color-cyan-10: rgba(3, 39, 57, 1);--color-blue-0: rgba(250, 252, 255, 1);--color-blue-1: rgba(235, 243, 255, 1);--color-blue-2: rgba(214, 230, 255, 1);--color-blue-3: rgba(185, 212, 254, 1);--color-blue-4: rgba(126, 176, 251, 1);--color-blue-5: rgba(75, 140, 251, 1);--color-blue-6: rgba(35, 114, 251, 1);--color-blue-7: rgba(26, 95, 213, 1);--color-blue-8: rgba(19, 76, 178, 1);--color-blue-9: rgba(15, 58, 133, 1);--color-blue-10: rgba(18, 38, 74, 1);--color-purple-0: rgba(250, 248, 255, 1);--color-purple-1: rgba(243, 238, 255, 1);--color-purple-2: rgba(232, 220, 255, 1);--color-purple-3: rgba(210, 187, 255, 1);--color-purple-4: rgba(187, 153, 255, 1);--color-purple-5: rgba(162, 120, 254, 1);--color-purple-6: rgba(135, 89, 236, 1);--color-purple-7: rgba(108, 65, 200, 1);--color-purple-8: rgba(82, 47, 157, 1);--color-purple-9: rgba(56, 32, 108, 1);--color-purple-10: rgba(39, 16, 81, 1);--color-violet-0: rgba(252, 248, 253, 1);--color-violet-1: rgba(249, 238, 251, 1);--color-violet-2: rgba(242, 218, 248, 1);--color-violet-3: rgba(230, 180, 243, 1);--color-violet-4: rgba(217, 144, 235, 1);--color-violet-5: rgba(200, 108, 222, 1);--color-violet-6: rgba(175, 74, 200, 1);--color-violet-7: rgba(144, 52, 167, 1);--color-violet-8: rgba(111, 37, 129, 1);--color-violet-9: rgba(76, 24, 89, 1);--color-violet-10: rgba(59, 8, 72, 1);--color-pink-0: rgba(254, 246, 251, 1);--color-pink-1: rgba(253, 237, 248, 1);--color-pink-2: rgba(253, 215, 240, 1);--color-pink-3: rgba(251, 174, 226, 1);--color-pink-4: rgba(250, 134, 212, 1);--color-pink-5: rgba(241, 93, 192, 1);--color-pink-6: rgba(213, 61, 162, 1);--color-pink-7: rgba(177, 41, 130, 1);--color-pink-8: rgba(137, 29, 100, 1);--color-pink-9: rgba(96, 21, 71, 1);--color-pink-10: rgba(73, 1, 55, 1);--contrast-0: rgba(255, 255, 255, 1);--color-fill-opaque: rgba(255, 255, 255, 1);--color-fill-hover-opaque: rgba(242, 242, 242, 1);--color-fill-pressing-opaque: rgba(235, 235, 235, 1);--color-fill-disabled-opaque: rgba(250, 250, 250, 1);--contrast-12: rgba(0, 0, 0, .08);--contrast-15: rgba(0, 0, 0, .18);--contrast-18: rgba(0, 0, 0, .24);--contrast-21: rgba(0, 0, 0, .3);--contrast-full: rgba(0, 0, 0, 1);--color-dark-bg: rgba(61, 61, 61, 1);--padding-size-radius-component: 999px;--padding-size-space-container: 11px;--padding-size-radius-container: 16px;--color-bg-Button-Primary-default: rgba(255, 36, 66, 1);--color-bg-Button-Primary-hover: rgba(255, 36, 66, 1);--color-bg-Button-Primary-pressing: rgba(255, 36, 66, 1);--color-bg-Button-Primary-disabled: rgba(48, 48, 52, .15)}:root .heshen_C_Red_dark{--color-primary: rgba(231, 34, 61, 1);--color-info: rgba(35, 114, 251, 1);--color-success: rgba(2, 156, 66, 1);--color-success-hover: rgba(32, 187, 95, 1);--color-success-pressing: rgba(78, 203, 123, 1);--color-success-disabled: rgba(11, 80, 40, 1);--color-success-light: rgba(16, 42, 28, 1);--color-success-light-hover: rgba(14, 57, 33, 1);--color-success-light-pressing: rgba(11, 80, 40, 1);--color-info-hover: rgba(71, 137, 250, 1);--color-info-pressing: rgba(119, 166, 248, 1);--color-info-disabled: rgba(24, 57, 114, 1);--color-info-light: rgba(28, 39, 59, 1);--color-info-light-hover: rgba(29, 49, 83, 1);--color-info-light-pressing: rgba(24, 57, 114, 1);--color-primary-hover: rgba(243, 86, 95, 1);--color-primary-pressing: rgba(246, 136, 137, 1);--color-primary-disabled: rgba(113, 26, 38, 1);--color-primary-light: rgba(54, 22, 27, 1);--color-primary-light-hover: rgba(78, 23, 32, 1);--color-primary-light-pressing: rgba(113, 26, 38, 1);--color-danger: rgba(228, 48, 95, 1);--color-danger-hover: rgba(241, 96, 123, 1);--color-danger-pressing: rgba(246, 134, 155, 1);--color-danger-disabled: rgba(112, 32, 53, 1);--color-danger-light: rgba(54, 24, 32, 1);--color-danger-light-hover: rgba(77, 27, 41, 1);--color-danger-light-pressing: rgba(112, 32, 53, 1);--color-warning: rgba(229, 91, 32, 1);--color-warning-hover: rgba(243, 125, 76, 1);--color-warning-pressing: rgba(246, 156, 113, 1);--color-warning-disabled: rgba(113, 51, 25, 1);--color-warning-light: rgba(54, 31, 22, 1);--color-warning-light-hover: rgba(77, 39, 23, 1);--color-warning-light-pressing: rgba(113, 51, 25, 1);--color-text-title: rgba(249, 249, 253, .89);--color-text-paragraph: rgba(248, 248, 252, .69);--color-text-description: rgba(243, 243, 252, .53);--color-text-placeholder: rgba(239, 239, 250, .32);--color-text-disabled: rgba(247, 247, 253, .19);--color-bg: rgba(19, 19, 20, 1);--color-bg-: rgba(10, 10, 10, 1);--color-bg-1: rgba(29, 29, 31, 1);--color-bg-2: rgba(34, 34, 36, 1);--color-fill: rgba(219, 219, 240, .07);--color-fill-hover: rgba(219, 219, 240, .09);--color-fill-pressing: rgba(219, 219, 240, .12);--color-fill-disabled: rgba(219, 219, 240, .05);--color-fill-light: rgba(0, 0, 0, 0);--color-line-divider: rgba(219, 219, 240, .09);--color-line-stroke: rgba(219, 219, 240, .12);--color-fill-mask: rgba(22, 22, 23, .8);--color-mask-light: rgba(22, 22, 23, .65);--color-mask-loading: rgba(19, 19, 20, .7);--color-brand-0: rgba(43, 21, 25, 1);--color-brand-1: rgba(54, 22, 27, 1);--color-brand-2: rgba(78, 23, 32, 1);--color-brand-3: rgba(113, 26, 38, 1);--color-brand-4: rgba(172, 30, 50, 1);--color-brand-5: rgba(208, 33, 57, 1);--color-brand-6: rgba(231, 34, 61, 1);--color-brand-7: rgba(243, 86, 95, 1);--color-brand-8: rgba(246, 136, 137, 1);--color-brand-9: rgba(248, 178, 175, 1);--color-brand-10: rgba(250, 212, 209, 1);--color-white: rgba(249, 249, 253, .89);--color-grey-0: rgba(29, 29, 31, 1);--color-grey-1: rgba(34, 34, 36, 1);--color-grey-2: rgba(45, 45, 47, 1);--color-grey-3: rgba(60, 60, 62, 1);--color-grey-4: rgba(85, 85, 89, 1);--color-grey-5: rgba(101, 101, 105, 1);--color-grey-6: rgba(111, 111, 115, 1);--color-grey-7: rgba(141, 141, 145, 1);--color-grey-8: rgba(177, 177, 180, 1);--color-grey-9: rgba(203, 203, 206, 1);--color-grey-10: rgba(224, 224, 227, 1);--color-black: rgba(0, 0, 0, 1);--color-red-0: rgba(42, 22, 28, 1);--color-red-1: rgba(54, 24, 32, 1);--color-red-2: rgba(77, 27, 41, 1);--color-red-3: rgba(112, 32, 53, 1);--color-red-4: rgba(170, 40, 74, 1);--color-red-5: rgba(205, 45, 86, 1);--color-red-6: rgba(228, 48, 95, 1);--color-red-7: rgba(241, 96, 123, 1);--color-red-8: rgba(246, 134, 155, 1);--color-red-9: rgba(247, 172, 190, 1);--color-red-10: rgba(255, 222, 229, 1);--color-orange-0: rgba(42, 27, 21, 1);--color-orange-1: rgba(54, 31, 22, 1);--color-orange-2: rgba(77, 39, 23, 1);--color-orange-3: rgba(113, 51, 25, 1);--color-orange-4: rgba(171, 71, 28, 1);--color-orange-5: rgba(206, 83, 30, 1);--color-orange-6: rgba(229, 91, 32, 1);--color-orange-7: rgba(243, 125, 76, 1);--color-orange-8: rgba(246, 156, 113, 1);--color-orange-9: rgba(248, 188, 156, 1);--color-orange-10: rgba(255, 247, 242, 1);--color-yellow-0: rgba(42, 37, 18, 1);--color-yellow-1: rgba(53, 46, 17, 1);--color-yellow-2: rgba(76, 64, 15, 1);--color-yellow-3: rgba(110, 91, 12, 1);--color-yellow-4: rgba(167, 135, 7, 1);--color-yellow-5: rgba(201, 162, 4, 1);--color-yellow-6: rgba(224, 180, 2, 1);--color-yellow-7: rgba(243, 201, 46, 1);--color-yellow-8: rgba(243, 214, 104, 1);--color-yellow-9: rgba(248, 226, 136, 1);--color-yellow-10: rgba(248, 235, 168, 1);--color-green-0: rgba(17, 34, 25, 1);--color-green-1: rgba(16, 42, 28, 1);--color-green-2: rgba(14, 57, 33, 1);--color-green-3: rgba(11, 80, 40, 1);--color-green-4: rgba(7, 118, 53, 1);--color-green-5: rgba(4, 141, 61, 1);--color-green-6: rgba(2, 156, 66, 1);--color-green-7: rgba(32, 187, 95, 1);--color-green-8: rgba(78, 203, 123, 1);--color-green-9: rgba(136, 226, 166, 1);--color-green-10: rgba(190, 239, 210, 1);--color-teal-0: rgba(17, 33, 32, 1);--color-teal-1: rgba(16, 39, 38, 1);--color-teal-2: rgba(14, 53, 50, 1);--color-teal-3: rgba(11, 73, 68, 1);--color-teal-4: rgba(7, 107, 99, 1);--color-teal-5: rgba(4, 127, 117, 1);--color-teal-6: rgba(2, 140, 129, 1);--color-teal-7: rgba(1, 175, 162, 1);--color-teal-8: rgba(111, 196, 189, 1);--color-teal-9: rgba(153, 216, 211, 1);--color-teal-10: rgba(204, 234, 231, 1);--color-cyan-0: rgba(18, 31, 38, 1);--color-cyan-1: rgba(18, 38, 47, 1);--color-cyan-2: rgba(17, 50, 65, 1);--color-cyan-3: rgba(15, 69, 92, 1);--color-cyan-4: rgba(13, 100, 138, 1);--color-cyan-5: rgba(12, 118, 165, 1);--color-cyan-6: rgba(11, 131, 183, 1);--color-cyan-7: rgba(37, 167, 220, 1);--color-cyan-8: rgba(101, 188, 234, 1);--color-cyan-9: rgba(151, 212, 244, 1);--color-cyan-10: rgba(232, 248, 255, 1);--color-blue-0: rgba(25, 33, 47, 1);--color-blue-1: rgba(28, 39, 59, 1);--color-blue-2: rgba(29, 49, 83, 1);--color-blue-3: rgba(24, 57, 114, 1);--color-blue-4: rgba(32, 80, 162, 1);--color-blue-5: rgba(25, 98, 225, 1);--color-blue-6: rgba(35, 114, 251, 1);--color-blue-7: rgba(71, 137, 250, 1);--color-blue-8: rgba(119, 166, 248, 1);--color-blue-9: rgba(165, 194, 248, 1);--color-blue-10: rgba(213, 227, 251, 1);--color-purple-0: rgba(31, 26, 42, 1);--color-purple-1: rgba(36, 30, 52, 1);--color-purple-2: rgba(48, 37, 74, 1);--color-purple-3: rgba(65, 47, 106, 1);--color-purple-4: rgba(94, 65, 160, 1);--color-purple-5: rgba(112, 75, 193, 1);--color-purple-6: rgba(123, 82, 214, 1);--color-purple-7: rgba(155, 115, 242, 1);--color-purple-8: rgba(180, 148, 246, 1);--color-purple-9: rgba(204, 182, 248, 1);--color-purple-10: rgba(230, 217, 255, 1);--color-violet-0: rgba(35, 25, 38, 1);--color-violet-1: rgba(42, 27, 47, 1);--color-violet-2: rgba(58, 33, 65, 1);--color-violet-3: rgba(81, 41, 92, 1);--color-violet-4: rgba(120, 55, 137, 1);--color-violet-5: rgba(144, 63, 164, 1);--color-violet-6: rgba(159, 68, 182, 1);--color-violet-7: rgba(191, 104, 212, 1);--color-violet-8: rgba(209, 139, 226, 1);--color-violet-9: rgba(224, 175, 236, 1);--color-violet-10: rgba(248, 224, 255, 1);--color-pink-0: rgba(38, 23, 34, 1);--color-pink-1: rgba(48, 25, 41, 1);--color-pink-2: rgba(68, 30, 56, 1);--color-pink-3: rgba(97, 36, 77, 1);--color-pink-4: rgba(145, 46, 112, 1);--color-pink-5: rgba(174, 53, 134, 1);--color-pink-6: rgba(194, 57, 148, 1);--color-pink-7: rgba(230, 89, 183, 1);--color-pink-8: rgba(241, 129, 204, 1);--color-pink-9: rgba(244, 169, 220, 1);--color-pink-10: rgba(248, 211, 236, 1);--contrast-0: rgba(19, 19, 20, 1);--color-fill-opaque: rgba(19, 19, 20, 1);--color-fill-hover-opaque: rgba(37, 37, 40, 1);--color-fill-pressing-opaque: rgba(43, 43, 46, 1);--color-fill-disabled-opaque: rgba(29, 29, 31, 1);--contrast-12: rgba(233, 233, 249, .1);--contrast-15: rgba(236, 236, 245, .18);--contrast-18: rgba(255, 255, 255, .2);--contrast-21: rgba(239, 239, 250, .3);--contrast-full: rgba(255, 255, 255, 1);--color-dark-bg: rgba(34, 34, 36, 1);--padding-size-radius-component: 999px;--padding-size-space-container: 11px;--padding-size-radius-container: 16px;--color-bg-Button-Primary-default: rgba(231, 34, 61, 1);--color-bg-Button-Primary-hover: rgba(231, 34, 61, 1);--color-bg-Button-Primary-pressing: rgba(231, 34, 61, 1);--color-bg-Button-Primary-disabled: rgba(255, 255, 255, .08)}:root{--background-color: white;--text-color: #000000D9;--label-color: #000000B2;--border-color: #eee;--btn-text-color: #000000D9;--input-color: #00000008;--modal-mask-color: #00000080;--toast-bg-color: #000000b3;--toast-text-color: #fff;--bg-primary: #ff2e4d;--Title: rgba(0, 0, 0, .8);--Description: rgba(0, 0, 0, .45);--PlaceHolder: rgba(0, 0, 0, .27);--Disabled: rgba(0, 0, 0, .27);--Paragraph: rgba(0, 0, 0, .62);--Primary: rgba(255, 36, 66, 1);--PrimaryHover: rgba(255, 36, 66, .6);--Fill1: rgba(48, 48, 52, .05);--Bg: rgba(255, 255, 255, 1);--Separator: rgba(0, 0, 0, .08);--Separator2: rgba(0, 0, 0, .2);--Label: rgba(51, 51, 51, 1);--Background: rgba(255, 255, 255, 1);--Info2: rgba(236, 244, 254, 1);--Primary2: rgba(255, 237, 240, 1);--Warnning: rgba(255, 125, 3, 1);--White: #ffffff;--PrimaryBgDisabled: rgba(48, 48, 52, .15);--PrimaryLabelFillDisabled: rgba(255, 255, 255, 1);--Fill5: rgba(48, 48, 52, .99);--NeutralWhite: rgba(255, 255, 255, 1)}:root .theme-dark{--background-color: #181818;--text-color: white;--label-color: #f8f8fcb0;--border-color: #DBDBF01F;--btn-text-color: #F9F9FDE3;--input-color: #fff;--toast-bg-color: #F9F9FDE3;--toast-text-color: #181818;--Title: rgba(255, 255, 255, .84);--Description: rgba(255, 255, 255, .36);--PlaceHolder: rgba(255, 255, 255, .21);--Disabled: rgba(255, 255, 255, .21);--Paragraph: rgba(255, 255, 255, .56);--Primary: rgba(255, 46, 77, 1);--Fill1: rgba(255, 255, 255, .04);--Bg: rgba(25, 25, 30, 1);--Separator: rgba(255, 255, 255, .07);--Separator2: rgba(255, 255, 255, .16);--Label: rgba(245, 245, 245, 1);--Background: rgba(5, 5, 10, 1);--Info2: rgba(29, 38, 51, 1);--Primary2: rgba(48, 28, 31, 1);--PrimaryBgDisabled: rgba(255, 255, 255, .08);--PrimaryLabelFillDisabled: rgba(255, 255, 255, .21);--Fill5: rgba(255, 255, 255, .99);--NeutralWhite: rgba(0, 0, 0, 1)}:root .theme-light{--background-color: white;--text-color: #000000D9;--label-color: #000000B2;--border-color: #eee;--btn-text-color: #000000D9;--input-color: #00000008;--toast-bg-color: #000000b3;--toast-text-color: #fff;--Title: rgba(0, 0, 0, .8);--Description: rgba(0, 0, 0, .45);--PlaceHolder: rgba(0, 0, 0, .3);--Disabled: rgba(0, 0, 0, .27);--Paragraph: rgba(0, 0, 0, .62);--Primary: rgba(255, 36, 66, 1);--Fill1: rgba(48, 48, 52, .05);--Bg: rgba(255, 255, 255, 1);--Separator: rgba(0, 0, 0, .08);--Label: rgba(51, 51, 51, 1);--Info2: rgba(236, 244, 254, 1);--Primary2: rgba(255, 237, 240, 1);--Warnning: rgba(255, 125, 3, 1)}.captcha-flex{display:flex;align-items:center}.text-h2{font-size:24px;font-weight:600;line-height:32px;color:var(--Title)}.text-b2-desc{font-size:14px;font-weight:400;line-height:22px;color:var(--Description)}.text-b1-disabled{font-size:14px;font-weight:400;line-height:22px;color:var(--Disabled)}.m-8{margin:8px}.m-12{margin:12px}.mt-12{margin-top:12px}.m-16{margin:16px}.mt-16{margin-top:16px}.mt-36{margin-top:36px}.mb-12{margin-bottom:12px}.mb-16{margin-bottom:16px}.mb-36{margin-bottom:36px}.visually-hidden{position:absolute;width:1px;height:1px;margin:-1px;padding:0;overflow:hidden;clip:rect(0,0,0,0);border:0}:root{--font-family-default: "PingFang SC";--size-text-small: 12px;--size-text-default: 14px;--size-text-paragraph: 14px;--size-text-h6: 16px;--size-text-h5: 18px;--size-text-h4: 20px;--size-text-h3: 24px;--size-text-h2: 28px;--size-text-h1: 32px;--size-text-line-height-small: 20px;--size-text-line-height-default: 22px;--size-text-line-height-paragraph: 22px;--size-text-line-height-h6: 24px;--size-text-line-height-h5: 26px;--size-text-line-height-h4: 28px;--size-text-line-height-h3: 36px;--size-text-line-height-h2: 40px;--size-text-line-height-h1: 44px;--size-text-font-weight-default: 400;--size-text-font-weight-bold: 500}.text-default{font-size:var(--size-text-default);font-weight:var(--size-text-font-weight-default);line-height:var(--size-text-line-height-default)}.text-default-bold{font-size:var(--size-text-default);font-weight:var(--size-text-font-weight-bold);line-height:var(--size-text-line-height-default)}.text-h6-default{font-size:var(--size-text-h6);font-weight:var(--size-text-font-weight-default);line-height:var(--size-text-line-height-h6)}.text-h6-bold{font-size:var(--size-text-h6);font-weight:var(--size-text-font-weight-bold);line-height:var(--size-text-line-height-h6)}.text-small{font-size:var(--size-text-small);font-weight:var(--size-text-font-weight-default);line-height:var(--size-text-line-height-small)}.text-paragraph{font-size:var(--size-text-paragraph);font-weight:var(--size-text-font-weight-default);line-height:var(--size-text-line-height-paragraph)}.text-paragraph-bold{font-size:var(--size-text-paragraph);font-weight:var(--size-text-font-weight-bold);line-height:var(--size-text-line-height-paragraph)}.text-b2-loose{font-size:var(--size-text-default);font-weight:var(--size-text-font-weight-default);line-height:var(--size-text-line-height-default)}.color-description{color:var(--color-text-description)}.color-warning{color:var(--color-warning)}.color-text-paragraph{color:var(--color-text-paragraph)}.color-title,.text-title{color:var(--color-text-title)}.text-placeholder{color:var(--color-text-placeholder)}.loading-spinner[data-v-d5003260]{border:4px solid transparent;border-radius:50%;border-top-color:currentColor;animation:spin-d5003260 1s linear infinite}@keyframes spin-d5003260{to{transform:rotate(360deg)}}.captcha-modal[data-v-e847acf9]{position:fixed;display:flex;justify-content:center;align-items:center;width:100vw;height:100vh;z-index:10000000;left:0;right:0;top:0;bottom:0;background-color:#00000080}.captcha-modal-delight[data-v-e847acf9]{box-shadow:0 8px 20px #0000001f}.captcha-modal-content[data-v-e847acf9]{width:400px;padding:20px 24px;border-radius:16px;background-color:var(--background-color)}.captcha-modal-delight .captcha-modal-content[data-v-e847acf9]{padding:16px 24px;border-radius:4px}.captcha-modal__header[data-v-e847acf9]{display:flex;justify-content:space-between;align-items:center}.captcha-modal-title[data-v-e847acf9]{flex:1;padding-left:24px;text-align:center;font-weight:500;font-size:16px;color:var(--Title)}.captcha-modal-delight .captcha-modal-title[data-v-e847acf9]{text-align:left;padding-left:0}.captcha-modal-title-no-padding[data-v-e847acf9]{padding-left:0}.captcha-modal__close[data-v-e847acf9],.captcha-modal__header-back[data-v-e847acf9]{cursor:pointer;font-size:16px}.captcha-form-item[data-v-1da80264]{margin-bottom:16px;padding:0 16px}.captcha-form-header[data-v-1da80264]{display:flex;align-items:center;justify-content:space-between;margin-bottom:12px}.captcha-control[data-v-1da80264]{position:relative;display:flex;flex-direction:column}.captcha-form-title[data-v-1da80264]{font-size:14px;line-height:18px;font-weight:500;color:var(--Title)}.captcha-required[data-v-1da80264]{color:#ff2442;margin-left:4px}.captcha-error-message[data-v-1da80264]{margin-top:12px;color:var(--Warnning);font-size:14px}.captcha-form-error-item[data-v-1da80264] textarea,.captcha-form-error-item[data-v-1da80264] input{background:var(--Primary2)}.v-enter-active,.v-leave-active{transition:opacity .3s ease}.v-enter-from,.v-leave-to{opacity:0}.popover-container{position:relative;display:inline-block}.popover-content{position:absolute;background-color:var(--color-bg);border:.5px solid var(--color-line-divider);border-radius:4px;box-shadow:0 2px 5px #0000001a;padding:8px;z-index:1000}.toast[data-v-2511de6e]{position:fixed;top:50%;left:50%;transform:translate(-50%,-50%);padding:12px 16px;color:var(--toast-text-color);background-color:var(--toast-bg-color);border-radius:18px;box-shadow:0 2px 5px #0003;transition:opacity .3s ease;opacity:1;font-size:12px;z-index:10000010}@keyframes fadeInOut-2511de6e{0%,to{opacity:0}10%,90%{opacity:1}}.toast[data-v-134ae11f]{position:fixed;top:15%;left:50%;transform:translate(-50%,-50%);display:flex;align-items:center;justify-content:center;padding:12px 16px;box-sizing:border-box;border:1px solid var(--color-success-light-pressing);background-color:var(--color-success-light);color:var(--color-text-title);border-radius:4px;box-shadow:0 5px 20px #0000001f;transition:opacity .3s ease;font-size:14px;z-index:10000010}.toast-success[data-v-134ae11f]{border:1px solid var(--color-success-light-pressing);background-color:var(--color-success-light)}.toast-error[data-v-134ae11f]{border:1px solid var(--color-warning-light-pressing);background-color:var(--color-warning-light)}.toast-msg[data-v-134ae11f]{margin-left:8px;text-align:center}@keyframes fadeInOut-134ae11f{0%,to{opacity:0}10%,90%{opacity:1}}.r-input-box[data-v-0c73fc29]{display:flex;align-items:center;position:relative;border:1px solid transparent;overflow:hidden;padding:var(--padding-size-space-container) 12px;box-sizing:border-box;border-radius:var(--padding-size-radius-component);background-color:var(--color-fill);transition:all .3s ease}.r-input-box--focus[data-v-0c73fc29]{border:1px solid var(--color-primary)}.r-input-box--readonly[data-v-0c73fc29]{border:1px solid var(--color-line-stroke)}.r-input-box--error[data-v-0c73fc29]{background-color:var(--color-danger-light)}.r-input-inner[data-v-0c73fc29]{height:22px;box-sizing:border-box;flex:1;border:none;color:var(--color-text-title);background-color:transparent;transition:all .3s ease}.r-input-inner[data-v-0c73fc29]:focus{outline:none}.r-input-clearable[data-v-0c73fc29]{cursor:pointer;color:var(--color-text-description)}.region-list-box[data-v-b0f170e6]{max-height:320px;overflow:auto}.region-item[data-v-b0f170e6]{display:flex;justify-content:space-between;padding:5px 12px;cursor:pointer}.item[data-v-b0f170e6]:hover{opacity:.6}.region-text[data-v-b0f170e6],.region-code[data-v-b0f170e6]{color:var(--color-text-paragraph)}.textarea[data-v-8a5d8d59]{flex:1;height:48px;line-height:48px;padding:0 16px;background:var(--Fill1);outline:none;border:none;box-sizing:border-box;resize:none;border-radius:8px;border:1px solid transparent;color:var(--Title);caret-color:var(--Primary)}.theme-light .textarea[data-v-8a5d8d59]::placeholder{color:#00000045}.theme-dark .textarea[data-v-8a5d8d59]::placeholder{color:#ffffff36}.input-item-box[data-v-8a5d8d59]{display:flex;align-items:center}.input-box[data-v-8a5d8d59]{position:relative}.text-right[data-v-8a5d8d59]{position:absolute;font-size:12px;top:16px;right:16px;bottom:12px;color:var(--Disabled)}.region-code[data-v-8a5d8d59]{cursor:pointer;padding-right:8px;font-size:18px;font-weight:400;color:var(--Description)}.region-code-text[data-v-8a5d8d59]{padding-right:0}.textarea[data-v-74a58b74]{width:100%;background-color:var(--Fill1);outline:none;border:none;padding:9px 12px;box-sizing:border-box;resize:none;height:100px;border-radius:8px;border:1px solid transparent;color:var(--Title);caret-color:var(--Primary)}.theme-light .textarea[data-v-74a58b74]::placeholder{color:#00000045}.theme-dark .textarea[data-v-74a58b74]::placeholder{color:#ffffff36}.text-count[data-v-74a58b74]{position:absolute;right:12px;top:72px;z-index:111;font-size:12px;color:var(--Disabled)}.tag-container[data-v-487da69e]{display:flex;justify-content:space-between;flex-wrap:wrap}.tag-item[data-v-487da69e]{width:calc(50% - 6px);background:var(--Fill1);height:36px;display:flex;margin-bottom:12px;border-radius:6px;justify-content:center;align-items:center;-webkit-user-select:none;user-select:none;font-size:14px;color:var(--Paragraph);cursor:pointer}.last-row[data-v-487da69e]{margin-bottom:0}.tag-active[data-v-487da69e]{background:var(--Primary2);color:var(--Primary)}.content[data-v-fd3a9e66]{padding:9px 16px;font-size:14px;line-height:22px;font-weight:400;color:var(--Title);background-color:var(--Info2)}.upload-btn[data-v-064ec0ec]{width:calc((100% - 32px)/3);border-radius:6px;background-color:var(--Fill1);display:flex;cursor:pointer}.input-file[data-v-064ec0ec]{display:none}.upload-content[data-v-064ec0ec]{display:flex;flex-direction:column;align-items:center;justify-content:center;height:100%;width:100%;color:var(--Description)}.upload-plus[data-v-064ec0ec]{font-size:30px}.upload-desc[data-v-064ec0ec]{font-size:12px}.upload-item[data-v-064ec0ec]{border-radius:4px;overflow:hidden;margin-right:16px;margin-bottom:12px;position:relative}.last-right-item[data-v-064ec0ec]{margin-right:0}.upload-img[data-v-064ec0ec]{width:100%;height:100%}.upload-container[data-v-064ec0ec]{display:flex;flex-wrap:wrap}.upload-layer[data-v-064ec0ec]{position:absolute;width:100%;height:100%;display:flex;justify-content:center;align-items:center;background:#0009;top:0;left:0;opacity:0}.upload-layer[data-v-064ec0ec]:hover{opacity:1}.delete-btn[data-v-064ec0ec]{width:30px;height:30px;display:flex;justify-content:center;align-items:center;border-radius:4px;cursor:pointer}.delete-btn[data-v-064ec0ec]:hover{background:#ffffff4d}.error-tip-icon[data-v-064ec0ec]{position:absolute;right:0;bottom:0}.loading-container[data-v-064ec0ec]{position:absolute;top:0;left:0;z-index:20;display:flex;justify-content:center;align-items:center;width:100%;height:100%;background:#ffffff80}.upload-btn[data-v-07eb156e]{width:100px;height:100px;border-radius:4px;background-color:#00000008;display:flex;cursor:pointer}.input-file[data-v-07eb156e]{display:none}.upload-content[data-v-07eb156e]{display:flex;flex-direction:column;align-items:center;height:100%;padding-top:8px;width:100%}.upload-plus[data-v-07eb156e]{font-size:30px;color:#00000087}.upload-desc[data-v-07eb156e]{font-size:14px;color:#00000087}.upload-item[data-v-07eb156e]{width:100px;height:100px;border-radius:4px;overflow:hidden;margin-right:16px;margin-bottom:10px;position:relative}.upload-img[data-v-07eb156e]{width:100%;height:100%}.upload-container[data-v-07eb156e]{display:flex;flex-wrap:wrap}.upload-layer[data-v-07eb156e]{position:absolute;width:100%;height:100%;display:flex;justify-content:center;align-items:center;background:#0009;top:0;left:0;opacity:0}.upload-layer[data-v-07eb156e]:hover{opacity:1}.delete-btn[data-v-07eb156e]{width:30px;height:30px;display:flex;justify-content:center;align-items:center;border-radius:4px;cursor:pointer}.delete-btn[data-v-07eb156e]:hover{background:#ffffff4d}.error-tip-icon[data-v-07eb156e]{position:absolute;right:0;bottom:0}.loading-container[data-v-07eb156e]{position:absolute;top:0;left:0;z-index:20;display:flex;justify-content:center;align-items:center;width:100%;height:100%;background:#ffffff80}.captcha-report-form[data-v-65bcb70a]{margin-top:16px;min-height:400px;display:flex;flex-direction:column}.report-form-native[data-v-65bcb70a]{min-height:unset}.form-list-box[data-v-65bcb70a]{flex:1;max-height:70vh;overflow:auto}.pb-24[data-v-65bcb70a]{padding-bottom:24px}.form-title[data-v-65bcb70a]{color:var(--label-color);font-size:14px;font-weight:700;height:32px;line-height:22px}.form-item[data-v-65bcb70a]{margin-bottom:20px}.w-full[data-v-65bcb70a]{width:100%}.important-w-full[data-v-65bcb70a]{width:100%!important}.bottom-box[data-v-65bcb70a]{padding:0 16px}.submit-btn[data-v-65bcb70a]{width:100%;height:40px;background:#ff2442;color:#fff;display:flex;justify-content:center;align-items:center;border-radius:20px;font-size:14px;font-weight:500;cursor:pointer}.report-success[data-v-f403f441]{display:flex;flex-direction:column;justify-content:center;align-items:center;padding:40px 0}.success-img[data-v-f403f441]{width:160px}.success-desc[data-v-f403f441]{font-size:16px;color:var(--text-color);font-weight:500;margin-top:20px}.back-btn[data-v-f403f441]{width:60px;height:32px;background:#ff2442;display:flex;justify-content:center;align-items:center;border-radius:20px;color:#fff;font-size:14px;font-weight:500;-webkit-user-select:none;user-select:none;cursor:pointer;margin-top:20px}[data-v-cc090901] .captcha-modal-content{padding-left:0;padding-right:0}[data-v-cc090901] .captcha-modal__header{padding:0 16px}.captcha-modal-native[data-v-cc090901]{background-color:transparent}@media (max-width: 400px){[data-v-cc090901] .captcha-modal-content{width:380px}}.loading-container[data-v-cc090901]{display:flex;flex-direction:column;justify-content:center;align-items:center;height:70vh}.loading-desc[data-v-cc090901]{margin-top:20px}.r-captcha-modal[data-v-552c280a]{position:fixed;display:flex;justify-content:center;align-items:center;width:100vw;height:100vh;z-index:10000000;left:0;right:0;top:0;bottom:0;background-color:var(--color-fill-mask)}.captcha-modal-content[data-v-552c280a]{width:400px;padding:16px 24px 24px;border-radius:var(--padding-size-radius-container);background-color:var(--color-bg-2)}.captcha-modal__header[data-v-552c280a]{display:flex;justify-content:space-between;align-items:center}.captcha-modal-title[data-v-552c280a]{flex:1;color:var(--color-text-title)}.captcha-modal-title-no-padding[data-v-552c280a]{padding-left:0}.captcha-modal__close[data-v-552c280a],.captcha-modal__header-back[data-v-552c280a]{cursor:pointer;font-size:16px}.qrcode-img[data-v-2a17fead]{width:100%;height:100%}.qrcode-container[data-v-2a17fead]{width:200px;height:200px;padding:12px;box-sizing:border-box;background-color:#fff;border-radius:12px;border:.5px solid var(--color-line-stroke);overflow:hidden;display:flex;justify-content:center;align-items:center;margin:auto;position:relative}.qr-scan[data-v-2a17fead]{position:absolute;top:0;left:0;width:100%;height:100%;background-color:#fffffff5;display:flex;justify-content:center;align-items:center;flex-direction:column}.qr-scan-desc[data-v-2a17fead]{color:var(--color-text-paragraph);margin-top:12px;text-align:center}.expire-desc[data-v-2a17fead]{color:#ff2442;font-family:PingFang SC;font-size:12px;font-style:normal;font-weight:500;line-height:20px}.refresh-btn[data-v-2a17fead]{font-size:12px;color:#00000087;cursor:pointer;font-family:PingFang SC;font-style:normal;font-weight:400;line-height:20px}.cursor-pointer[data-v-2a17fead]{cursor:pointer}.color-warning[data-v-2a17fead]{color:var(--color-warning)}.animate-spin[data-v-2a17fead]{animation:spin-2a17fead 1s linear infinite}@keyframes spin-2a17fead{to{transform:rotate(-360deg)}}.qrcode-desc[data-v-9920d5a1]{margin-top:20px;margin-bottom:18px;color:var(--color-text-paragraph)}.xhs-text[data-v-9920d5a1]{font-weight:500;color:var(--color-primary)}.avatar[data-v-9920d5a1]{width:72px;height:72px;border-radius:72px}.nickname[data-v-9920d5a1]{color:var(--color-text-title);margin-top:16px}.qrcode-user[data-v-9920d5a1]{display:flex;justify-content:center;align-items:center;flex-direction:column;margin-top:20px;margin-bottom:20px}.icon-spinning[data-v-60f8f322]{animation:spin-60f8f322 1s linear infinite}@keyframes spin-60f8f322{0%{transform:rotate(0)}to{transform:rotate(360deg)}}.btn[data-v-ec00e89a]{display:inline-flex;align-items:center;justify-content:center;padding:var(--padding-size-space-container) 16px;border-radius:var(--padding-size-radius-component);cursor:pointer;transition:all .3s;outline:none;box-sizing:border-box}.btn-block[data-v-ec00e89a]{display:flex}.btn-default[data-v-ec00e89a]{background:var(--color-bg-Button-Primary-default);color:var(--color-white)}.btn-default[data-v-ec00e89a]:hover{background:var(--color-bg-Button-Primary-hover)}.btn-default[data-v-ec00e89a]:active{background:var(--color-bg-Button-Primary-pressing)}.btn-stroke[data-v-ec00e89a]{border:none;color:var(--color-text-title);background-color:var(--color-fill)}.btn-stroke[data-v-ec00e89a]:hover{background:var(--color-fill-hover)}.btn-stroke[data-v-ec00e89a]:active{background:var(--color-fill-pressing)}.btn-lg[data-v-ec00e89a]{padding:12px 20px;font-size:16px}.btn-sm[data-v-ec00e89a]{padding:6px 12px;font-size:12px}.btn-disabled[data-v-ec00e89a]{background-color:var(--color-bg-Button-Primary-disabled);color:var(--color-white);cursor:not-allowed}.refresh-container[data-v-4bd378c1]{display:flex;justify-content:center;align-items:center;flex-direction:column;padding-top:48px}.error-png[data-v-4bd378c1]{width:60px;height:60px}.confirm-text[data-v-4bd378c1]{color:var(--color-text-title);margin-top:16px;margin-bottom:8px}.cancel-text[data-v-4bd378c1]{margin-bottom:24px;color:var(--color-text-description)}.loading-container[data-v-032d635c]{height:220px;display:flex;justify-content:center;align-items:center}.qrcode-foot[data-v-032d635c]{display:flex;justify-content:center;margin-top:32px;margin-bottom:10px}.feedback-btn[data-v-032d635c]{color:var(--color-text-paragraph);cursor:pointer;-webkit-user-select:none;user-select:none}.qrcode-img[data-v-52594c88]{width:100%;height:100%}.qrcode-container[data-v-52594c88]{width:200px;height:200px;padding:12px;box-sizing:border-box;background-color:#fff;border-radius:12px;border:.5px solid var(--color-line-stroke);overflow:hidden;display:flex;justify-content:center;align-items:center;margin:auto;position:relative}.qr-scan[data-v-52594c88]{position:absolute;top:0;left:0;width:100%;height:100%;background-color:#fffffff5;display:flex;justify-content:center;align-items:center;flex-direction:column}.qr-scan-desc[data-v-52594c88]{color:var(--color-text-paragraph);margin-top:12px;text-align:center}.expire-desc[data-v-52594c88]{color:#ff2442;font-family:PingFang SC;font-size:12px;font-style:normal;font-weight:500;line-height:20px}.refresh-btn[data-v-52594c88]{font-size:12px;color:#00000087;cursor:pointer;font-family:PingFang SC;font-style:normal;font-weight:400;line-height:20px}.cursor-pointer[data-v-52594c88]{cursor:pointer}.color-warning[data-v-52594c88]{color:var(--color-warning)}.animate-spin[data-v-52594c88]{animation:spin-52594c88 1s linear infinite}@keyframes spin-52594c88{to{transform:rotate(-360deg)}}.qrcode-desc[data-v-b065280a]{margin-top:20px;margin-bottom:18px;text-align:center;color:var(--color-text-paragraph)}.xhs-text[data-v-b065280a]{font-weight:500;color:var(--color-primary)}.avatar[data-v-b065280a]{width:80px;height:80px;border-radius:80px}.nickname[data-v-b065280a]{color:var(--color-text-title);margin-top:16px}.qrcode-user[data-v-b065280a]{display:flex;justify-content:center;align-items:center;flex-direction:column;margin-top:20px;margin-bottom:20px}.qrcode-foot[data-v-b065280a]{display:flex;justify-content:center;margin-top:40px;margin-bottom:10px}.feedback-btn[data-v-b065280a]{color:var(--color-text-paragraph);cursor:pointer;-webkit-user-select:none;user-select:none}[data-v-121e136f] .captcha-modal-content{width:336px;padding:24px}@media (max-width: 696px){[data-v-121e136f] .captcha-modal-content{width:296px;padding:12px}}.loading-container[data-v-121e136f]{height:220px;display:flex;justify-content:center;align-items:center}.static-content[data-v-121e136f]{max-width:400px;min-width:280px;padding:24px;border-radius:16px;background-color:var(--color-bg-2);box-shadow:0 1px 4px #00000006,0 4px 32px #0000000d}.static-content-native[data-v-121e136f]{box-shadow:none}.title[data-v-121e136f]{color:var(--color-text-title)}.qrcode-foot[data-v-121e136f]{display:flex;justify-content:center;margin-top:32px;margin-bottom:10px}.feedback-btn[data-v-121e136f]{color:var(--color-text-paragraph);cursor:pointer;-webkit-user-select:none;user-select:none}.feedback-btn[data-v-c5a12bea]{display:flex;align-items:center;cursor:pointer;padding:4px 12px;border-radius:20px;transition:all .3s}.feedback-text[data-v-c5a12bea]{color:var(--color-text-paragraph)}.feedback-text[data-v-c5a12bea]:hover{color:var(--color-text-title)}.combine-list[data-v-6e5d9215]{max-height:360px;overflow-y:auto}.combine-item[data-v-6e5d9215]{display:flex;align-items:center;justify-content:space-between;cursor:pointer;padding:8px 0;border-bottom:1px solid var(--color-line-divider)}.combine-item[data-v-6e5d9215]:hover{opacity:.8}.icon-left[data-v-6e5d9215]{width:24px;height:24px}.combine-item-content[data-v-6e5d9215]{flex:1;margin-left:16px}.icon-right[data-v-6e5d9215]{width:16px;height:16px}.icon-spinning[data-v-4c868c51]{animation:spin-4c868c51 1s linear infinite}@keyframes spin-4c868c51{0%{transform:rotate(0)}to{transform:rotate(360deg)}}.empty-state[data-v-336f571b]{display:flex;flex-direction:column;align-items:center;justify-content:center;height:100%;margin-top:64px;color:var(--color-text-paragraph)}.empty-state__description[data-v-336f571b]{margin-top:16px;margin-bottom:24px;text-align:center;color:var(--color-text-title)}.user-info[data-v-05d3fc3e]{display:flex;flex-direction:column;align-items:center}.avatar[data-v-05d3fc3e]{width:72px;height:72px;border-radius:50%;object-fit:cover}.nickname[data-v-05d3fc3e]{margin-top:8px}.capptch-modal-content-inner[data-v-3ac513a8]{margin-top:16px}.static-capptch-modal-content[data-v-3ac513a8]{width:336px;margin-top:16px;box-shadow:none}@media (max-width: 696px){.static-capptch-modal-content[data-v-3ac513a8]{width:296px}}.static-content[data-v-3ac513a8]{padding:12px;border-radius:16px;background-color:var(--color-bg-2);box-shadow:0 1px 4px #00000006,0 4px 32px #0000000d}.static-content-native[data-v-3ac513a8]{box-shadow:none}.static-close[data-v-3ac513a8]{position:absolute;top:0;right:0;width:22px;height:22px;cursor:pointer}.bottom-box[data-v-3ac513a8]{display:flex;align-items:center;justify-content:center;margin-top:12px}.feedback-btn[data-v-3ac513a8]{display:flex;align-items:center;cursor:pointer;padding:4px 12px;border-radius:20px;transition:all .3s}.feedback-text[data-v-3ac513a8]{color:var(--color-text-paragraph)}.feedback-text[data-v-3ac513a8]:hover{color:var(--color-text-title)}.title[data-v-3ac513a8]{position:relative;text-align:center}.api-sec-desc[data-v-3ac513a8]{margin-bottom:24px;color:var(--color-text-paragraph)}.resend-box[data-v-3ac513a8]{margin-top:24px;margin-bottom:36px;font-size:14px;color:var(--color-text-paragraph)}.error-box[data-v-3ac513a8]{margin-top:4px;display:flex;align-items:center;color:var(--color-danger)}input[data-v-3ac513a8]{caret-color:var(--bg-primary)}input[data-v-3ac513a8]::placeholder{font-size:16px;color:#00000045}.theme-light input[data-v-3ac513a8]::placeholder{font-size:16px;color:#00000045}.theme-dark input[data-v-3ac513a8]::placeholder{font-size:16px;color:#ffffff36}.disable[data-v-3ac513a8]{opacity:.6}.region-select-box[data-v-3ac513a8]{display:flex;align-items:center;justify-content:center;cursor:pointer;color:var(--color-text-title);padding-right:8px;margin-right:8px;border-right:1px solid var(--color-line-divider)}.sms-code-get-text-counting[data-v-3ac513a8]{color:var(--color-info-disabled)}.sms-code-get-text[data-v-3ac513a8]{cursor:pointer;color:var(--color-info)}.text-disable[data-v-3ac513a8]{color:var(--color-info-disabled)}.sms-code-get-text[data-v-3ac513a8]:hover{color:var(--color-info-hover)}.sms-code-get-text[data-v-3ac513a8]:active{color:var(--color-info-pressing)}.region-select-popover[data-v-3ac513a8]{width:382px;left:-12px;top:28px}.capptch-modal-content-inner[data-v-82da9e8f]{margin-top:16px}.static-capptch-modal-content[data-v-82da9e8f]{width:336px;margin-top:16px;box-shadow:none}@media (max-width: 696px){.static-capptch-modal-content[data-v-82da9e8f]{width:296px}}.static-content[data-v-82da9e8f]{padding:12px;border-radius:16px;background-color:var(--color-bg-2);box-shadow:0 1px 4px #00000006,0 4px 32px #0000000d}.static-content-native[data-v-82da9e8f]{box-shadow:none}.static-close[data-v-82da9e8f]{position:absolute;top:0;right:0;width:22px;height:22px;cursor:pointer}.bottom-box[data-v-82da9e8f]{display:flex;align-items:center;justify-content:center;margin-top:12px}.feedback-btn[data-v-82da9e8f]{display:flex;align-items:center;cursor:pointer;padding:4px 12px;border-radius:20px;transition:all .3s}.feedback-text[data-v-82da9e8f]{color:var(--color-text-paragraph)}.feedback-text[data-v-82da9e8f]:hover{color:var(--color-text-title)}.title[data-v-82da9e8f]{position:relative;text-align:center}.receive-number[data-v-82da9e8f]{margin-top:16px;margin-bottom:24px;cursor:default;white-space:nowrap;color:var(--color-text-paragraph)}.resend-box[data-v-82da9e8f]{margin-top:24px;margin-bottom:36px;font-size:14px;color:var(--color-text-paragraph)}.error-box[data-v-82da9e8f]{margin-top:4px;display:flex;align-items:center;color:var(--color-danger)}input[data-v-82da9e8f]{caret-color:var(--bg-primary)}input[data-v-82da9e8f]::placeholder{font-size:16px;color:#00000045}.theme-light input[data-v-82da9e8f]::placeholder{font-size:16px;color:#00000045}.theme-dark input[data-v-82da9e8f]::placeholder{font-size:16px;color:#ffffff36}.disable[data-v-82da9e8f]{opacity:.6}.sms-code-get-text-counting[data-v-82da9e8f]{color:var(--color-info-disabled)}.sms-code-get-text[data-v-82da9e8f]{cursor:pointer;color:var(--color-info)}.text-disable[data-v-82da9e8f]{color:var(--color-info-disabled)}.sms-code-get-text[data-v-82da9e8f]:hover{color:var(--color-info-hover)}.sms-code-get-text[data-v-82da9e8f]:active{color:var(--color-info-pressing)}.error-box[data-v-1422e356]{display:flex;flex-direction:column;justify-content:center;align-items:center}.error-text[data-v-1422e356]{margin-top:12px;font-size:12px;color:var(--color-text-paragraph)}.red-captcha-loading[data-v-6afa8e3a]{display:flex;width:fit-content;height:fit-content;flex-direction:column;align-items:center;font-style:normal;font-weight:400;font-size:14px;line-height:120%;color:#00000045}.red-captcha-center[data-v-6afa8e3a]{display:flex;justify-content:center;align-items:center;height:100%;width:100%}.red-captcha-circle[data-v-6afa8e3a]{animation:spin-6afa8e3a 1s linear infinite}@keyframes spin-6afa8e3a{0%{transform:rotate(0)}to{transform:rotate(360deg)}}.img-box[data-v-8bb49914]{display:flex;flex-direction:column}.question-box[data-v-8bb49914]{display:flex;align-items:center;justify-content:center;margin-bottom:8px}.question-text[data-v-8bb49914]{font-size:14px;font-weight:400;color:#0000009e;line-height:22px}.question-img-box[data-v-8bb49914]{width:174px;background-color:#f8f8f8}.question-img[data-v-8bb49914]{height:32px;margin-left:12px;border-radius:4px;overflow:hidden}.img-bg-box[data-v-8bb49914]{position:relative;width:100%;min-height:222px;border-radius:8px;overflow:hidden;cursor:pointer;-webkit-tap-highlight-color:transparent}.img-bg[data-v-8bb49914]{position:absolute;border-radius:4px;width:100%;height:100%;display:flex}.exception-box[data-v-8bb49914]{height:315px;display:flex;justify-content:center;align-items:center;border-radius:8px;background-color:#f8f8f8}@media (max-width: 696px){.exception-box[data-v-8bb49914]{height:285px}}.point-mark[data-v-8bb49914]{position:absolute;width:24px;height:24px;margin:-12px 0 0 -12px;border-radius:50%;color:#fff;font-size:14px;font-weight:500;line-height:24px;text-align:center;background:#303034fc;box-shadow:0 0 2px #0003}.scale-up[data-v-8bb49914]{animation:scaleUp-8bb49914 .3s forwards}@keyframes scaleUp-8bb49914{0%{transform:scale(0)}to{transform:scale(1)}}.check-status-mask[data-v-8bb49914]{position:absolute;top:0;left:0;width:100%;height:100%;display:flex;align-items:center;justify-content:center;background-color:#303034e6;color:#fff;z-index:1}.checking-text[data-v-8bb49914]{margin-top:12px;color:#fff;font-size:16px}.check-status-content[data-v-8bb49914]{display:flex;flex-direction:column;align-items:center}.red-captcha-slider-bar[data-v-f347cfbf]{margin-top:12px;width:100%;height:40px;border-radius:20px;position:relative;background-color:#f8f8f8}@media (max-width: 696px){.red-captcha-slider-bar[data-v-f347cfbf]{margin-top:8px}}.red-captcha-track[data-v-f347cfbf]{width:100%;height:40px;display:flex;justify-content:center;align-items:center;border-radius:20px;position:relative;background-color:#f8f8f8}.track-tip-content[data-v-f347cfbf]{height:100%;width:100%;border-radius:20px;display:flex;align-items:center;justify-content:center}.track-placeholder[data-v-f347cfbf]{padding-left:20px;color:#3333334d}.track-success[data-v-f347cfbf]{color:#3d8af5;background-color:#3d8af512}.track-fail[data-v-f347cfbf]{color:red;background-color:#ff000012}.red-captcha-slider[data-v-f347cfbf]{display:flex;justify-content:center;align-items:center;box-sizing:border-box;position:absolute;width:52px;height:40px;left:0;top:0;background:#fff;border:1px solid rgba(0,0,0,.08);box-shadow:0 1px 2px #00000006,0 2px 8px #00000006;border-radius:999px;cursor:pointer}.active-slider-track[data-v-f347cfbf]{position:absolute;left:0;height:100%;border-radius:999px;background-color:#3d8af5}.img-box[data-v-5b003c4d]{min-height:258px;display:flex;flex-direction:column;border-radius:8px;overflow:hidden}.img-question[data-v-5b003c4d]{width:100%}.img-mask[data-v-5b003c4d]{width:100%;display:flex}.img-mask-box[data-v-5b003c4d]{position:relative}.opacity-mask[data-v-5b003c4d]{position:absolute;top:0;bottom:0;right:0;left:0;border-left:1px solid rgba(255,36,66,1);background-color:#e9e9e9f2}.exception-box[data-v-5b003c4d]{height:293px;display:flex;justify-content:center;align-items:center;border-radius:8px;background-color:#f8f8f8}@media (max-width: 696px){.exception-box[data-v-5b003c4d]{height:258px}}.rotate-captcha[data-v-02afcaa9]{width:100%}.exception-box[data-v-02afcaa9]{height:224px;display:flex;justify-content:center;align-items:center;border-radius:8px;background-color:#f8f8f8}@media (max-width: 696px){.exception-box[data-v-02afcaa9]{height:213px}}.img-box[data-v-02afcaa9]{position:relative;width:100%;height:224px;border-radius:8px;overflow:hidden}@media (max-width: 696px){.img-box[data-v-02afcaa9]{height:213px}}.img-bg[data-v-02afcaa9]{position:absolute;top:0;bottom:0;width:100%;height:100%}.rotate-img-box[data-v-02afcaa9]{position:absolute;width:100%;height:100%;display:flex;align-items:center;justify-content:center}.img-center[data-v-02afcaa9]{height:100%}.bottom-box[data-v-02afcaa9]{display:flex;justify-content:center;align-items:center;margin-top:20px}.feedback[data-v-02afcaa9]{margin-left:20px}.bottom-box[data-v-e56d226b]{margin-top:12px;display:flex;align-items:center;justify-content:center;color:#333c}@media (max-width: 696px){.bottom-box[data-v-e56d226b]{margin-top:8px}}.refresh-btn[data-v-e56d226b]{display:flex;align-items:center;margin-right:24px;cursor:pointer;padding:4px 8px;border-radius:20px}.refresh-btn[data-v-e56d226b]:hover{background-color:#f8f8f8}.refresh-text[data-v-e56d226b]{margin-left:4px}.feedback-btn[data-v-e56d226b]{display:flex;align-items:center;cursor:pointer;padding:4px 8px;border-radius:20px}.feedback-btn[data-v-e56d226b]:hover{background-color:#f8f8f8}.feedback-text[data-v-e56d226b]{margin-left:4px}[data-v-cf46c32a] .captcha-modal-content{width:336px;padding:24px}@media (max-width: 696px){[data-v-cf46c32a] .captcha-modal-content{width:296px;padding:12px}}.capptch-modal-content-inner[data-v-cf46c32a]{margin-top:12px;width:100%}.static-capptch-modal-content[data-v-cf46c32a]{width:336px;margin-top:12px;box-shadow:none}@media (max-width: 696px){.static-capptch-modal-content[data-v-cf46c32a]{width:296px}}.static-content[data-v-cf46c32a]{padding:12px;border-radius:16px;background-color:var(--color-bg-2);box-shadow:0 1px 4px #00000006,0 4px 32px #0000000d}.static-content-native[data-v-cf46c32a]{box-shadow:none}.title[data-v-cf46c32a]{position:relative;text-align:center;font-size:16px;font-weight:600;color:var(--color-text-title)}.static-close[data-v-cf46c32a]{position:absolute;top:0;right:0;width:22px;height:22px}.loading-box[data-v-cf46c32a]{height:240px;display:flex;justify-content:center;align-items:center}.outer-error-box[data-v-cf46c32a]{height:240px;border-radius:8px;background-color:var(--color-bg-2)}.exception-box[data-v-cf46c32a]{height:240px;display:flex;justify-content:center;align-items:center;border-radius:8px;background-color:var(--color-bg-2)}.feedback-entry-container[data-v-85761ed5]{display:flex;justify-content:center;margin-top:12px}.back-btn[data-v-85761ed5]{display:flex;align-items:center;cursor:pointer;padding:4px 12px;border-radius:20px;transition:all .3s;color:var(--color-text-paragraph)}.back-btn[data-v-85761ed5]:hover{color:var(--color-text-title);background-color:var(--color-bg)}.loading-container[data-v-c5007f43]{display:flex;flex-direction:column;justify-content:center;align-items:center;height:70vh}.loading-desc[data-v-c5007f43]{margin-top:20px}.restricted-content[data-v-e46194cb]{display:flex;flex-direction:column;align-items:center;justify-content:center}.msg[data-v-e46194cb]{margin-top:24px;margin-bottom:16px;font-size:16px;font-weight:500;color:var(--color-text-title);text-align:center}.code[data-v-e46194cb]{margin-bottom:24px;font-size:14px;color:var(--color-text-description);text-align:center}.feedback-entry[data-v-e46194cb]{display:flex;align-items:center;justify-content:center}[data-v-e46194cb] .feedback-text{color:var(--color-text-description)}</style><style data-id="immersive-translate-input-injected-css">.immersive-translate-input {
  position: absolute;
  top: 0;
  right: 0;
  left: 0;
  bottom: 0;
  z-index: 2147483647;
  display: flex;
  justify-content: center;
  align-items: center;
}
.immersive-translate-attach-loading::after {
  content: " ";

  --loading-color: #f78fb6;
  width: 6px;
  height: 6px;
  border-radius: 50%;
  display: block;
  margin: 12px auto;
  position: relative;
  color: white;
  left: -100px;
  box-sizing: border-box;
  animation: immersiveTranslateShadowRolling 1.5s linear infinite;

  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-2000%, -50%);
  z-index: 100;
}

.immersive-translate-loading-spinner {
  vertical-align: middle !important;
  width: 10px !important;
  height: 10px !important;
  display: inline-block !important;
  margin: 0 4px !important;
  border: 2px rgba(221, 244, 255, 0.6) solid !important;
  border-top: 2px rgba(0, 0, 0, 0.375) solid !important;
  border-left: 2px rgba(0, 0, 0, 0.375) solid !important;
  border-radius: 50% !important;
  padding: 0 !important;
  -webkit-animation: immersive-translate-loading-animation 0.6s infinite linear !important;
  animation: immersive-translate-loading-animation 0.6s infinite linear !important;
}

@-webkit-keyframes immersive-translate-loading-animation {
  from {
    -webkit-transform: rotate(0deg);
  }

  to {
    -webkit-transform: rotate(359deg);
  }
}

@keyframes immersive-translate-loading-animation {
  from {
    transform: rotate(0deg);
  }

  to {
    transform: rotate(359deg);
  }
}

.immersive-translate-input-loading {
  --loading-color: #f78fb6;
  width: 6px;
  height: 6px;
  border-radius: 50%;
  display: block;
  margin: 12px auto;
  position: relative;
  color: white;
  left: -100px;
  box-sizing: border-box;
  animation: immersiveTranslateShadowRolling 1.5s linear infinite;
}

@keyframes immersiveTranslateShadowRolling {
  0% {
    box-shadow: 0px 0 rgba(255, 255, 255, 0), 0px 0 rgba(255, 255, 255, 0),
      0px 0 rgba(255, 255, 255, 0), 0px 0 rgba(255, 255, 255, 0);
  }

  12% {
    box-shadow: 100px 0 var(--loading-color), 0px 0 rgba(255, 255, 255, 0),
      0px 0 rgba(255, 255, 255, 0), 0px 0 rgba(255, 255, 255, 0);
  }

  25% {
    box-shadow: 110px 0 var(--loading-color), 100px 0 var(--loading-color),
      0px 0 rgba(255, 255, 255, 0), 0px 0 rgba(255, 255, 255, 0);
  }

  36% {
    box-shadow: 120px 0 var(--loading-color), 110px 0 var(--loading-color),
      100px 0 var(--loading-color), 0px 0 rgba(255, 255, 255, 0);
  }

  50% {
    box-shadow: 130px 0 var(--loading-color), 120px 0 var(--loading-color),
      110px 0 var(--loading-color), 100px 0 var(--loading-color);
  }

  62% {
    box-shadow: 200px 0 rgba(255, 255, 255, 0), 130px 0 var(--loading-color),
      120px 0 var(--loading-color), 110px 0 var(--loading-color);
  }

  75% {
    box-shadow: 200px 0 rgba(255, 255, 255, 0), 200px 0 rgba(255, 255, 255, 0),
      130px 0 var(--loading-color), 120px 0 var(--loading-color);
  }

  87% {
    box-shadow: 200px 0 rgba(255, 255, 255, 0), 200px 0 rgba(255, 255, 255, 0),
      200px 0 rgba(255, 255, 255, 0), 130px 0 var(--loading-color);
  }

  100% {
    box-shadow: 200px 0 rgba(255, 255, 255, 0), 200px 0 rgba(255, 255, 255, 0),
      200px 0 rgba(255, 255, 255, 0), 200px 0 rgba(255, 255, 255, 0);
  }
}

.immersive-translate-toast {
  display: flex;
  position: fixed;
  z-index: 2147483647;
  left: 0;
  right: 0;
  top: 1%;
  width: fit-content;
  padding: 12px 20px;
  margin: auto;
  overflow: auto;
  background: #fef6f9;
  box-shadow: 0px 4px 10px 0px rgba(0, 10, 30, 0.06);
  font-size: 15px;
  border-radius: 8px;
  color: #333;
}

.immersive-translate-toast-content {
  display: flex;
  flex-direction: row;
  align-items: center;
}

.immersive-translate-toast-hidden {
  margin: 0 20px 0 72px;
  text-decoration: underline;
  cursor: pointer;
}

.immersive-translate-toast-close {
  color: #666666;
  font-size: 20px;
  font-weight: bold;
  padding: 0 10px;
  cursor: pointer;
}

@media screen and (max-width: 768px) {
  .immersive-translate-toast {
    top: 0;
    padding: 12px 0px 0 10px;
  }
  .immersive-translate-toast-content {
    flex-direction: column;
    text-align: center;
  }
  .immersive-translate-toast-hidden {
    margin: 10px auto;
  }
}

.immersive-translate-dialog {
  position: fixed;
  z-index: 2147483647;
  left: 0;
  top: 0;
  display: flex;
  width: 300px;
  flex-direction: column;
  align-items: center;
  font-size: 15px;
  left: 0;
  right: 0;
  top: 0;
  bottom: 0;
  margin: auto;
  height: fit-content;
  border-radius: 20px;
  background-color: #fff;
}

.immersive-translate-modal {
  display: none;
  position: fixed;
  z-index: 2147483647;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  overflow: auto;
  background-color: rgb(0, 0, 0);
  background-color: rgba(0, 0, 0, 0.4);
  font-size: 15px;
}

.immersive-translate-modal-content {
  background-color: #fefefe;
  margin: 10% auto;
  padding: 40px 24px 24px;
  border-radius: 12px;
  width: 350px;
  font-family: system-ui, -apple-system, "Segoe UI", "Roboto", "Ubuntu",
    "Cantarell", "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji",
    "Segoe UI Symbol", "Noto Color Emoji";
  position: relative;
}

@media screen and (max-width: 768px) {
  .immersive-translate-modal-content {
    margin: 25% auto !important;
  }
}

@media screen and (max-width: 480px) {
  .immersive-translate-modal-content {
    width: 80vw !important;
    margin: 20vh auto !important;
    padding: 20px 12px 12px !important;
  }

  .immersive-translate-modal-title {
    font-size: 14px !important;
  }

  .immersive-translate-modal-body {
    font-size: 13px !important;
    max-height: 60vh !important;
  }

  .immersive-translate-btn {
    font-size: 13px !important;
    padding: 8px 16px !important;
    margin: 0 4px !important;
  }

  .immersive-translate-modal-footer {
    gap: 6px !important;
    margin-top: 16px !important;
  }
}

.immersive-translate-modal .immersive-translate-modal-content-in-input {
  max-width: 500px;
}
.immersive-translate-modal-content-in-input .immersive-translate-modal-body {
  text-align: left;
  max-height: unset;
}

.immersive-translate-modal-title {
  text-align: center;
  font-size: 16px;
  font-weight: 700;
  color: #333333;
}

.immersive-translate-modal-body {
  text-align: center;
  font-size: 14px;
  font-weight: 400;
  color: #333333;
  margin-top: 24px;
  word-break: break-all;
}

@media screen and (max-width: 768px) {
  .immersive-translate-modal-body {
    max-height: 250px;
    overflow-y: auto;
  }
}

.immersive-translate-close {
  color: #666666;
  position: absolute;
  right: 16px;
  top: 16px;
  font-size: 20px;
  font-weight: bold;
}

.immersive-translate-close:hover,
.immersive-translate-close:focus {
  text-decoration: none;
  cursor: pointer;
}

.immersive-translate-modal-footer {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  margin-top: 24px;
}

.immersive-translate-btn {
  width: fit-content;
  color: #fff;
  background-color: #ea4c89;
  border: none;
  font-size: 14px;
  margin: 0 8px;
  padding: 9px 30px;
  border-radius: 5px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.immersive-translate-btn-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 8px;
}

.immersive-translate-btn:hover {
  background-color: #f082ac;
}
.immersive-translate-btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}
.immersive-translate-btn:disabled:hover {
  background-color: #ea4c89;
}

.immersive-translate-link-btn {
  background-color: transparent;
  color: #ea4c89;
  border: none;
  cursor: pointer;
  height: 30px;
  line-height: 30px;
}

.immersive-translate-cancel-btn {
  /* gray color */
  background-color: rgb(89, 107, 120);
}

.immersive-translate-cancel-btn:hover {
  background-color: hsl(205, 20%, 32%);
}

.immersive-translate-action-btn {
  background-color: transparent;
  color: #ea4c89;
  border: 1px solid #ea4c89;
}

.immersive-translate-btn svg {
  margin-right: 5px;
}

.immersive-translate-link {
  cursor: pointer;
  user-select: none;
  -webkit-user-drag: none;
  text-decoration: none;
  color: #ea4c89;
  -webkit-tap-highlight-color: rgba(0, 0, 0, 0.1);
}

.immersive-translate-primary-link {
  cursor: pointer;
  user-select: none;
  -webkit-user-drag: none;
  text-decoration: none;
  color: #ea4c89;
  -webkit-tap-highlight-color: rgba(0, 0, 0, 0.1);
}

.immersive-translate-modal input[type="radio"] {
  margin: 0 6px;
  cursor: pointer;
}

.immersive-translate-modal label {
  cursor: pointer;
}

.immersive-translate-close-action {
  position: absolute;
  top: 2px;
  right: 0px;
  cursor: pointer;
}

.imt-image-status {
  background-color: rgba(0, 0, 0, 0.5) !important;
  display: flex !important;
  flex-direction: column !important;
  align-items: center !important;
  justify-content: center !important;
  border-radius: 16px !important;
}
.imt-image-status img,
.imt-image-status svg,
.imt-img-loading {
  width: 28px !important;
  height: 28px !important;
  margin: 0 0 8px 0 !important;
  min-height: 28px !important;
  min-width: 28px !important;
  position: relative !important;
}
.imt-img-loading {
  background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADgAAAA4CAMAAACfWMssAAAAtFBMVEUAAAD////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////oK74hAAAAPHRSTlMABBMIDyQXHwyBfFdDMSw+OjXCb+5RG51IvV/k0rOqlGRM6KKMhdvNyZBz9MaupmxpWyj437iYd/yJVNZeuUC7AAACt0lEQVRIx53T2XKiUBCA4QYOiyCbiAsuuGBcYtxiYtT3f6/pbqoYHVFO5r+iivpo6DpAWYpqeoFfr9f90DsYAuRSWkFnPO50OgR9PwiCUFcl2GEcx+N/YBh6pvKaefHlUgZd1zVe0NbYcQjGBfzrPE8Xz8aF+71D8gG6DHFPpc4a7xFiCDuhaWgKgGIJQ3d5IMGDrpS4S5KgpIm+en9f6PlAhKby4JwEIxlYJV9h5k5nee9GoxHJ2IDSNB0dwdad1NAxDJ/uXDHYmebdk4PdbkS58CIVHdYSUHTYYRWOJblWSyu2lmy3KNFVJNBhxcuGW4YBVCbYGRZwIooipHsNqjM4FbgOQqQqSKQQU9V8xmi1QlgHqQQ6DDBvRUVCDirs+EzGDGOQTCATgtYTnbCVLgsVgRE0T1QE0qHCFAht2z6dLvJQs3Lo2FQoDxWNUiBhaP4eRgwNkI+dAjVOA/kUrIDwf3CG8NfNOE0eiFotSuo+rBiq8tD9oY4Qzc6YJw99hl1wzpQvD7ef2M8QgnOGJfJw+EltQc+oX2yn907QB22WZcvlUpd143dqQu+8pCJZuGE4xCuPXJqqcs5sNpsI93Rmzym1k4Npk+oD1SH3/a3LOK/JpUBpWfqNySxWzCfNCUITuDG5dtuphrUJ1myeIE9bIsPiKrfqTai5WZxbhtNphYx6GEIHihyGFTI69lje/rxajdh0s0msZ0zYxyPLhYCb1CyHm9Qsd2H37Y3lugVwL9kNh8Ot8cha6fUNQ8nuXi5z9/ExsAO4zQrb/ev1yrCB7lGyQzgYDGuxq1toDN/JGvN+HyWNHKB7zEoK+PX11e12G431erGYzwmytAWU56fkMHY5JJnDRR2eZji3AwtIcrEV8Cojat/BdQ7XOwGV1e1hDjGGjXbdArm8uJZtCH5MbcctVX8A1WpqumJHwckAAAAASUVORK5CYII=");
  background-size: 28px 28px;
  animation: image-loading-rotate 1s linear infinite !important;
}

.imt-image-status span {
  color: var(--bg-2, #fff) !important;
  font-size: 14px !important;
  line-height: 14px !important;
  font-weight: 500 !important;
  font-family: "PingFang SC", Arial, sans-serif !important;
}

.imt-primary-button {
  display: flex;
  padding: 12px 80px;
  justify-content: center;
  align-items: center;
  gap: 8px;
  border-radius: 8px;
  background: #ea4c89;
  color: #fff;
  font-size: 16px;
  font-style: normal;
  font-weight: 700;
  line-height: 24px;
  border: none;
  cursor: pointer;
}

.imt-retry-text {
  color: #999;
  text-align: center;
  font-size: 14px;
  font-style: normal;
  font-weight: 400;
  line-height: 21px;
  cursor: pointer;
}

.imt-action-container {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.imt-modal-content-text {
  text-align: left;
  color: #333;
  font-size: 16px;
  font-weight: 400;
  line-height: 24px;
}

@keyframes image-loading-rotate {
  from {
    transform: rotate(360deg);
  }
  to {
    transform: rotate(0deg);
  }
}

.imt-linear-gradient-text {
  background: linear-gradient(90deg, #00a6ff 0%, #c369ff 52.4%, #ff4590 100%);
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.imt-flex-center {
  display: flex;
  align-items: center;
  justify-content: center;
}

.imt-linear-black-btn {
  border-radius: 50px;
  background: linear-gradient(66deg, #222 19%, #696969 94.25%);
  height: 48px;
  width: 100%;
  color: #fff;
  font-size: 16px;
  font-weight: 700;
  display: flex;
  align-items: center;
  cursor: pointer;
  justify-content: center;
}
</style></head><body><div style="display: none;"><svg><defs><clipPath id="a"><rect width="72" height="72" rx="36"></rect></clipPath><clipPath id="a"><rect width="150" height="150" x=".5" rx="75"></rect></clipPath><clipPath id="a"><path d="M0 0h24v24H0z"></path></clipPath><clipPath id="a"><path fill="#fff" d="M3 3h14v14H3z"></path></clipPath></defs><symbol id="creator" viewBox="0 0 24 24"><path fill="currentColor" d="M16 4.8A4.2 4.2 0 0 1 20.2 9v6a4.2 4.2 0 0 1-4.2 4.2H8A4.2 4.2 0 0 1 3.8 15V9A4.2 4.2 0 0 1 8 4.8zM8 3a6 6 0 0 0-6 6v6a6 6 0 0 0 6 6h8a6 6 0 0 0 6-6V9a6 6 0 0 0-6-6z"></path><path fill="currentColor" d="M11.1 15a.9.9 0 1 0 1.8 0v-2.1H15a.9.9 0 1 0 0-1.8h-2.1V9a.9.9 0 1 0-1.8 0v2.1H9a.9.9 0 0 0 0 1.8h2.1z"></path></symbol><symbol id="tab_btn_right" viewBox="0 0 20 20"><path d="M6.91 2.744a.833.833 0 0 1 1.18 0l6.666 6.667a.833.833 0 0 1 0 1.178l-6.667 6.667a.833.833 0 1 1-1.178-1.179L12.988 10 6.911 3.923a.833.833 0 0 1 0-1.179"></path></symbol><symbol id="close" viewBox="0 0 24 24"><path d="M19.23 4.772a.92.92 0 0 1 0 1.301l-5.928 5.928 5.926 5.925a.92.92 0 0 1-1.302 1.302l-5.925-5.926-5.928 5.929a.92.92 0 0 1-1.214.076l-.087-.076a.92.92 0 0 1 0-1.302l5.928-5.928-5.93-5.93a.92.92 0 0 1 1.3-1.301l5.931 5.93 5.928-5.928a.92.92 0 0 1 1.215-.077z"></path></symbol><symbol id="scan_qr" viewBox="0 0 20 21"><path fill-opacity=".8" d="M2.5 5.042C2.5 3.914 3.414 3 4.542 3h2.583c1.128 0 2.042.914 2.042 2.042v2.583a2.04 2.04 0 0 1-2.042 2.042H4.542A2.04 2.04 0 0 1 2.5 7.625zM4.542 4.5c-.3 0-.542.243-.542.542v2.583c0 .3.243.542.542.542h2.583c.3 0 .542-.243.542-.542V5.042c0-.3-.243-.542-.542-.542zM10.833 5.042c0-1.128.914-2.042 2.042-2.042h2.583c1.128 0 2.042.914 2.042 2.042v2.583a2.04 2.04 0 0 1-2.042 2.042h-2.583a2.04 2.04 0 0 1-2.042-2.042zm2.042-.542c-.3 0-.542.243-.542.542v2.583c0 .3.243.542.542.542h2.583c.3 0 .542-.243.542-.542V5.042c0-.3-.242-.542-.542-.542zM2.5 13.375c0-1.128.914-2.042 2.042-2.042h2.583c1.128 0 2.042.914 2.042 2.042v2.583A2.04 2.04 0 0 1 7.125 18H4.542A2.04 2.04 0 0 1 2.5 15.958zm2.042-.542c-.3 0-.542.243-.542.542v2.583c0 .3.243.542.542.542h2.583c.3 0 .542-.242.542-.542v-2.583c0-.3-.243-.542-.542-.542zM12.5 12.167a.833.833 0 1 1-1.667 0 .833.833 0 0 1 1.667 0M15.833 12.167a.833.833 0 1 1-1.666 0 .833.833 0 0 1 1.666 0M14.167 13.833a.833.833 0 1 1-1.667 0 .833.833 0 0 1 1.667 0M17.5 13.833a.833.833 0 1 1-1.667 0 .833.833 0 0 1 1.667 0M12.5 15.5a.833.833 0 1 1-1.667 0 .833.833 0 0 1 1.667 0M14.167 17.167a.833.833 0 1 1-1.667 0 .833.833 0 0 1 1.667 0M15.833 15.5a.833.833 0 1 1-1.666 0 .833.833 0 0 1 1.666 0M17.5 17.167a.833.833 0 1 1-1.667 0 .833.833 0 0 1 1.667 0"></path></symbol><symbol id="change" viewBox="0 0 14 14"><path d="M7 1.682a5.318 5.318 0 0 0-3.826 9.012l.311-.31a.328.328 0 0 1 .56.232v1.505a.33.33 0 0 1-.328.329H2.212a.328.328 0 0 1-.232-.56l.359-.36a6.5 6.5 0 0 1 7.19-10.52.59.59 0 1 1-.46 1.089A5.3 5.3 0 0 0 7 1.682M11.303 4.536l.263-.264a5.318 5.318 0 0 1-5.655 7.935.59.59 0 0 0-.24 1.157q.645.135 1.33.136a6.5 6.5 0 0 0 5.422-10.085l.385-.385a.328.328 0 0 0-.232-.56h-1.505a.33.33 0 0 0-.328.328v1.505c0 .293.353.44.56.233"></path></symbol><symbol id="IOS" viewBox="0 0 24 28"><path fill="#333" fill-rule="nonzero" d="M20.54 18.423q1.152 1.633 2.644 2.112-.647 2-2.054 4.17-2.166 3.267-4.277 3.267-.787 0-2.335-.535-1.434-.536-2.504-.536-1.069 0-2.363.564Q8.3 28 7.428 28q-2.532 0-4.98-4.31Q0 19.437 0 15.324q0-3.802 1.857-6.225Q3.77 6.676 6.584 6.676q.619 0 1.378.155a6 6 0 0 1 1.576.577q.873.48 1.435.662.563.184.872.184.367 0 1.126-.17a5.2 5.2 0 0 0 1.519-.62 11.4 11.4 0 0 1 1.407-.675q.59-.226 1.21-.226 1.969 0 3.545 1.07.844.564 1.716 1.663-1.294 1.125-1.885 1.972-1.098 1.577-1.097 3.436 0 2.056 1.153 3.719M14.883 5.268q-.985.93-1.8 1.21a6 6 0 0 1-.718.156q-.436.07-1 .127.03-2.48 1.295-4.282Q13.927.676 16.825 0q.057.283.085.394v.31q0 1.014-.479 2.282-.506 1.24-1.547 2.282"></path></symbol><symbol id="comment" viewBox="0 0 16 16"><path fill="currentColor" fill-opacity=".8" d="M3.182 10.985c.175.283.221.633.113.958l-.535 1.606c.185-.036.393-.075.605-.114.308-.056.63-.113.904-.156.242-.037.535-.08.73-.08.285 0 .607.088.814.144l.054.014c.496.133 1.162.31 2.133.31A5.676 5.676 0 0 0 13.666 8a5.667 5.667 0 1 0-10.484 2.985m-.937 3.682a.667.667 0 0 1-.62-.878l.721-2.162a.14.14 0 0 0-.013-.114A6.667 6.667 0 1 1 14.667 8c0 3.682-3 6.667-6.667 6.667-1.105 0-1.873-.205-2.391-.344-.264-.07-.463-.123-.61-.123-.414 0-2.552.429-2.73.464zm8.855-6.5a.833.833 0 1 0-1.667 0 .833.833 0 0 0 1.667 0M5.733 9a.833.833 0 1 1 0-1.667.833.833 0 0 1 0 1.667"></path></symbol><symbol id="ic_arrow_left" viewBox="0 0 20 20"><path fill="currentColor" d="M1.268 9.354a.914.914 0 0 0 0 1.292l5.586 5.586a.914.914 0 0 0 1.292-1.292l-4.025-4.026h13.965a.914.914 0 0 0 0-1.828H4.12L8.146 5.06a.914.914 0 0 0-1.292-1.292z"></path></symbol><symbol id="liked" viewBox="0 0 24 24"><path fill="#FF2442" d="m20.17 13.537-7.122 7.034a1.494 1.494 0 0 1-2.096 0l-7.128-7.04a6.125 6.125 0 0 1 .006-8.728A6.25 6.25 0 0 1 8.233 3c1.36 0 2.68.436 3.767 1.253A6.26 6.26 0 0 1 15.767 3a6.25 6.25 0 0 1 4.404 1.803 6.127 6.127 0 0 1 0 8.734"></path></symbol><symbol id="qq_f" viewBox="0 0 20 20"><path fill="currentColor" fill-opacity=".8" d="M5.142 17.2a.57.57 0 0 1-.22-.443c0-.471.461-.799.924-1.009a4.1 4.1 0 0 1-.835-1.428c-.374.437-.745.707-1.012.707-.417 0-.666-.435-.666-1.165 0-1.255.699-3.064 1.284-4.36.203-.447.305-.915.305-1.39C4.922 3.969 7.658 2.5 10 2.5s5.077 1.47 5.077 5.61c0 .478.102.945.305 1.392.586 1.296 1.285 3.104 1.285 4.36 0 .73-.25 1.165-.667 1.165-.267 0-.638-.27-1.012-.706a4.05 4.05 0 0 1-.836 1.428c.463.209.925.536.925 1.008a.57.57 0 0 1-.22.442c-.76.627-4.478.069-4.515.063a2.2 2.2 0 0 0-.679 0c-.024.004-1.557.238-2.86.238-.727 0-1.383-.073-1.661-.3"></path></symbol><symbol id="illegal" viewBox="0 0 12 12"><path fill="#fff" d="m3.38 8.667-.816.47a.374.374 0 1 1-.376-.65l8.248-4.75a.374.374 0 1 1 .376.65l-.63.362q.376.443.733.972a.5.5 0 0 1 .034.5l-.034.058-.12.177C9.38 8.486 7.716 9.5 6 9.5c-.898 0-1.78-.278-2.62-.833m4.087-2.354L5.534 7.426Q5.755 7.5 6 7.5a1.5 1.5 0 0 0 1.467-1.187M6 2.5c1.08 0 2.137.401 3.125 1.205L7.031 4.91A1.5 1.5 0 0 0 4.54 6.345l-2.327 1.34q-.586-.602-1.126-1.406a.5.5 0 0 1-.034-.5l.034-.058.12-.177C2.623 3.514 4.284 2.5 6 2.5"></path></symbol><symbol id="picture" viewBox="0 0 20 20"><path d="M6.917 8.25a1.333 1.333 0 1 1 0-2.667 1.333 1.333 0 0 1 0 2.667"></path><path d="M14.583 2.083H5.417a3.333 3.333 0 0 0-3.334 3.334v9.166a3.333 3.333 0 0 0 3.334 3.334h9.166a3.333 3.333 0 0 0 3.334-3.334V5.417a3.333 3.333 0 0 0-3.334-3.334m1.834 3.334v5.651L14.38 9.01l-.009-.009a1.167 1.167 0 0 0-1.65.009L8.95 12.823 7.444 11.3l-.01-.009a1.167 1.167 0 0 0-1.649.01l-2.202 2.224v-8.11c0-1.012.821-1.833 1.834-1.833h9.166c1.013 0 1.834.821 1.834 1.834m-2.866 4.888 2.866 2.896v1.382c0 1.013-.821 1.834-1.834 1.834H5.417a1.83 1.83 0 0 1-1.62-.974l2.817-2.847 1.506 1.521a1.167 1.167 0 0 0 1.65.009l.008-.009z"></path></symbol><symbol id="user_blocked" viewBox="0 0 97 96"><path fill="#333" fill-opacity=".3" d="m36.75 44.892 14.703 14.702c-.99.265-2.032.406-3.109.406-6.627 0-12-5.373-12-12 0-1.076.142-2.118.407-3.108m-1.595-1.597a14 14 0 0 0-.81 4.705c0 7.732 6.267 14 14 14 1.65 0 3.234-.285 4.704-.81 1.008-.36 1.196-1.632.44-2.389L37.543 42.857c-.756-.757-2.029-.568-2.388.44m24.783 7.814L45.236 36.406A12 12 0 0 1 48.344 36c6.628 0 12 5.373 12 12a12 12 0 0 1-.406 3.109m-.792 2.036c.756.756 2.029.567 2.388-.44.525-1.47.81-3.054.81-4.705 0-7.732-6.267-14-14-14-1.65 0-3.234.286-4.704.81-1.008.36-1.196 1.632-.44 2.389z"></path><path fill="#333" fill-opacity=".3" d="M48.345 24c13.254 0 24 10.745 24 24 0 11.892-8.65 21.764-20 23.668V96h-2V71.918a24.3 24.3 0 0 1-4 0V96h-2V71.668c-11.351-1.904-20-11.776-20-23.668 0-13.255 10.745-24 24-24m0 46c12.15 0 22-9.85 22-22s-9.85-22-22-22-22 9.85-22 22 9.85 22 22 22"></path></symbol><symbol id="success" viewBox="0 0 48 48"><circle cx="24" cy="24" r="24"></circle><path fill="#fff" d="M38.182 14.182c.602.602.602 1.58 0 2.182L20.727 33.818a1.543 1.543 0 0 1-2.182 0l-8.727-8.727A1.543 1.543 0 1 1 12 22.909l7.636 7.636L36 14.182a1.543 1.543 0 0 1 2.182 0"></path></symbol><symbol id="loading_mini" viewBox="0 0 16 16"><path fill="currentColor" d="M8 2.4A5.6 5.6 0 1 0 13.6 8a.9.9 0 1 1 1.8 0A7.4 7.4 0 1 1 8 .6a.9.9 0 0 1 0 1.8"></path></symbol><symbol id="user_skeleton_s" viewBox="0 0 390 158"><g clip-path="url(#a)"><path d="M0 0h72v72H0z"></path></g><rect width="112" height="24" x="88" y="10" rx="12"></rect><rect width="160" height="16" x="88" y="46" rx="8"></rect><rect width="280" height="16" y="88" rx="8"></rect><rect width="120" height="16" y="114" rx="8"></rect><rect width="64" height="16" y="142" rx="8"></rect><rect width="64" height="16" x="80" y="142" rx="8"></rect><rect width="64" height="16" x="160" y="142" rx="8"></rect></symbol><symbol id="fire" viewBox="0 0 20 20"><path fill="#5E5E5E" fill-rule="evenodd" d="M13.072 6.333c-.264-1.319-.914-3.133-2.505-4.623A8.4 8.4 0 0 0 9.266.714s-.086.574-.465 1.49c-.509 1.23-1.545 3.077-3.608 4.986-4.918 4.162-3.911 10.813 1.13 11.933q.715.161 1.54.163s-.14-.687-.078-1.5q.017-.245.063-.499c.104-.563.329-1.132.775-1.54l2.367 3.539c6.083.19 8.522-7.938 5.743-12.651a6.8 6.8 0 0 0-.958-1.265s-.344.561-.905 1.23q-.096.114-.199.23c-.399.451-.886.927-1.425 1.299 0 0 .037-.74-.174-1.796m2.64 1.584a9.5 9.5 0 0 1-1.613 1.446l-2.503 1.73.152-3.032v-.124a6 6 0 0 0-.024-.464 8 8 0 0 0-.32-1.626 7 7 0 0 0-1.426-2.592l-.042.088c-.643 1.361-1.771 3.14-3.724 4.948l-.024.022-.026.022c-2.32 1.962-2.978 4.44-2.566 6.284.303 1.356 1.197 2.49 2.702 2.948.079-.86.36-2.055 1.311-2.926l1.289-1.181 2.872 4.294c2.054-.253 3.56-1.86 4.244-4.156.576-1.93.459-4.04-.302-5.681m-3.964.145V8.06" clip-rule="evenodd"></path></symbol><symbol id="exclamation_marks_b" viewBox="0 0 16 16"><g fill="currentColor"><path d="M7.4 4.884c0-.304.268-.55.6-.55s.6.246.6.55v4.232c0 .304-.269.55-.6.55-.332 0-.6-.246-.6-.55zM8 11.667a.6.6 0 1 0 0-1.2.6.6 0 0 0 0 1.2"></path><path d="M14.667 8A6.667 6.667 0 1 1 1.333 8a6.667 6.667 0 0 1 13.334 0m-1.2 0A5.467 5.467 0 1 0 2.533 8a5.467 5.467 0 0 0 10.934 0"></path></g></symbol><symbol id="arrow_top" viewBox="0 0 24 24"><path fill="currentColor" d="M12.646 3.268a.914.914 0 0 0-1.292 0L5.768 8.854a.914.914 0 1 0 1.292 1.292l4.026-4.025v13.965a.914.914 0 0 0 1.828 0V6.12l4.026 4.025a.914.914 0 1 0 1.292-1.292z"></path></symbol><symbol id="AlertCircle" viewBox="0 0 32 32"><g fill="#333"><path d="M14.8 9.768c0-.608.537-1.101 1.2-1.101s1.2.493 1.2 1.101v8.464c0 .608-.538 1.101-1.2 1.101-.663 0-1.2-.493-1.2-1.101zM15.999 23.335a1.2 1.2 0 1 0 0-2.402 1.2 1.2 0 0 0 0 2.402"></path><path d="M29.333 16c0 7.364-5.97 13.333-13.333 13.333S2.667 23.363 2.667 16 8.637 2.667 16 2.667 29.333 8.637 29.333 16m-2.4 0c0-6.038-4.895-10.933-10.933-10.933S5.067 9.962 5.067 16 9.962 26.933 16 26.933 26.933 22.038 26.933 16"></path></g></symbol><symbol id="convention_b" viewBox="0 0 24 24"><path fill="currentColor" d="M10.26 4.651c-.881-.827-2.195-1.309-3.375-1.52a8 8 0 0 0-1.767-.123c-.539.028-1.091.128-1.543.357a.94.94 0 0 0-.485.642c-.154.714-.114 1.684.15 2.674a7.16 7.16 0 0 0 1.656 3.033c1.016 1.09 2.455 1.578 3.718 1.781.702.113 1.393.145 2 .127-.584 3.615.353 6.998.699 8.245.05.18.087.317.106.402.112.508.593.824 1.075.706s.781-.626.67-1.134c-.031-.138-.082-.327-.145-.561-.367-1.367-1.143-4.256-.645-7.324.71.117 1.61.182 2.54.108 1.274-.101 2.744-.472 3.836-1.477a7.1 7.1 0 0 0 1.87-2.891c.335-.965.445-1.93.344-2.653a.95.95 0 0 0-.438-.68c-.434-.265-.978-.409-1.513-.48a8 8 0 0 0-1.77-.019c-1.193.115-2.537.49-3.475 1.244a8.1 8.1 0 0 0-1.747 1.955A8.1 8.1 0 0 0 10.26 4.65M4.962 6.17a5 5 0 0 1-.172-1.23q.178-.03.415-.043a6.2 6.2 0 0 1 1.38.099c1.02.182 1.957.574 2.483 1.068.835.784 1.739 2.08 1.808 3.656a9 9 0 0 1-1.993-.092C7.79 9.451 6.797 9.06 6.174 8.39a5.24 5.24 0 0 1-1.21-2.22M19.2 5.835a4.9 4.9 0 0 1-.261 1.212 5.2 5.2 0 0 1-1.367 2.116c-.67.618-1.688.93-2.792 1.017a9 9 0 0 1-1.994-.07c.183-1.565 1.178-2.785 2.067-3.499.56-.45 1.523-.766 2.552-.865.5-.048.98-.042 1.385.012q.234.031.41.077"></path></symbol><symbol id="ic_dragger" viewBox="0 0 20 20"><path fill="currentColor" d="M7.5 3.333a1.667 1.667 0 1 1-3.333 0 1.667 1.667 0 0 1 3.333 0M15.833 3.333a1.667 1.667 0 1 1-3.333 0 1.667 1.667 0 0 1 3.333 0M7.5 10a1.667 1.667 0 1 1-3.333 0A1.667 1.667 0 0 1 7.5 10M15.833 10a1.667 1.667 0 1 1-3.333 0 1.667 1.667 0 0 1 3.333 0M7.5 16.667a1.667 1.667 0 1 1-3.334 0 1.667 1.667 0 0 1 3.334 0M15.833 16.667a1.667 1.667 0 1 1-3.333 0 1.667 1.667 0 0 1 3.333 0"></path></symbol><symbol id="more" viewBox="0 0 20 20"><path d="M5 10a1.25 1.25 0 1 1-2.5 0A1.25 1.25 0 0 1 5 10M11.25 10a1.25 1.25 0 1 1-2.5 0 1.25 1.25 0 0 1 2.5 0M16.25 11.25a1.25 1.25 0 1 0 0-2.5 1.25 1.25 0 0 0 0 2.5"></path></symbol><symbol id="arrow_right" viewBox="0 0 20 20"><path fill="currentColor" fill-opacity=".3" fill-rule="evenodd" d="M6.91 2.744a.833.833 0 0 1 1.18 0l6.666 6.667a.833.833 0 0 1 0 1.178l-6.667 6.667a.833.833 0 1 1-1.178-1.179L12.988 10 6.911 3.923a.833.833 0 0 1 0-1.179" clip-rule="evenodd"></path></symbol><symbol id="link_c" viewBox="0 0 24 24"><path fill="currentColor" d="M19.138 3.442a4.92 4.92 0 0 0-6.96 0l-1.42 1.42a.904.904 0 0 0 1.278 1.278l1.42-1.42a3.114 3.114 0 0 1 4.404 0l1.42 1.42a3.114 3.114 0 0 1 0 4.404l-2.841 2.841a3.114 3.114 0 0 1-4.403 0l-.71-.71a.904.904 0 0 0-1.28 1.278l.711.71a4.92 4.92 0 0 0 6.96 0l2.842-2.84a4.92 4.92 0 0 0 0-6.961z"></path><path fill="currentColor" d="M4.862 20.559a4.92 4.92 0 0 0 6.96 0l1.634-1.634a.904.904 0 0 0-1.278-1.279l-1.634 1.634a3.114 3.114 0 0 1-4.404 0l-1.42-1.42a3.114 3.114 0 0 1 0-4.404l2.841-2.841a3.114 3.114 0 0 1 4.403 0l.71.71a.904.904 0 0 0 1.28-1.278l-.711-.71a4.92 4.92 0 0 0-6.96 0l-2.841 2.84a4.92 4.92 0 0 0 0 6.961z"></path></symbol><symbol id="emoji" viewBox="0 0 20 20"><g fill="currentColor" fill-rule="evenodd" clip-rule="evenodd"><path d="M8.334 9A1.167 1.167 0 1 1 6 9a1.167 1.167 0 0 1 2.334 0M14 9a1.167 1.167 0 1 1-2.333 0A1.167 1.167 0 0 1 14 9M8.022 12.379c.515.616 1.195.939 1.984.939.793 0 1.47-.326 1.975-.947a.739.739 0 0 0-1.146-.932c-.226.277-.483.401-.829.401-.348 0-.613-.126-.85-.41a.739.739 0 0 0-1.134.949"></path><path d="M1.667 10a8.333 8.333 0 1 1 16.667 0 8.333 8.333 0 0 1-16.667 0M10 16.832a6.833 6.833 0 1 0 0-13.667 6.833 6.833 0 0 0 0 13.667"></path></g></symbol><symbol id="checkmark" viewBox="0 0 16 16"><path fill="#fff" fill-rule="evenodd" d="m15.05 3.79-9.188 9.188L.95 8.066l1.273-1.273 3.64 3.64 7.914-7.915z" clip-rule="evenodd"></path></symbol><symbol id="dark_mode" viewBox="0 0 24 24"><path d="M19.904 14.202a8.2 8.2 0 1 1-9.695-10.203 10 10 0 0 0-.009.403c0 5.38 4.336 9.748 9.704 9.8m.288-1.802-.192.002a8 8 0 0 1-7.636-10.394 10 10 0 0 0-1.896.11c-4.795.74-8.466 4.883-8.466 9.884 0 5.523 4.477 10 10 10 4.825 0 8.852-3.417 9.792-7.964.127-.61.197-1.242.207-1.888-.58.15-1.186.235-1.809.25"></path></symbol><symbol id="notification" viewBox="0 0 24 24"><path fill="currentcolor" d="M20.16 13.9v-2.7c0-3.18-1.99-6.07-4.98-7.3C14.58 2.75 13.35 2 12 2s-2.58.75-3.18 1.9c-3 1.23-4.98 4.12-4.98 7.3v2.69C2.77 14.26 2 15.26 2 16.42c0 1.48 1.24 2.68 2.76 2.68H8.5c.28 1.64 1.73 2.9 3.5 2.9s3.22-1.26 3.5-2.9h3.74c1.52 0 2.76-1.2 2.76-2.68 0-1.16-.77-2.15-1.84-2.52M12 20.2c-.74 0-1.36-.46-1.6-1.1h3.19c-.23.64-.85 1.1-1.59 1.1m7.24-2.9H4.76c-.5 0-.9-.39-.9-.88 0-.48.41-.88.91-.88.51 0 .93-.4.93-.9V11.2c0-2.56 1.67-4.88 4.14-5.76.26-.09.46-.29.56-.54.24-.66.89-1.1 1.61-1.1s1.37.44 1.61 1.1c.09.25.3.45.56.54 2.48.88 4.14 3.19 4.14 5.76v3.44c0 .5.42.9.94.9.5 0 .9.39.9.88a.91.91 0 0 1-.92.88"></path></symbol><symbol id="user_empty_collect" viewBox="0 0 96 96"><path fill-rule="evenodd" d="M64.968 42.473a1.5 1.5 0 0 1-.166-.18zm0 0 .13.143a1 1 0 0 0-.13-.143M52.207 37.421c.078.02.079.017 0 0" clip-rule="evenodd"></path><path d="M16 64a1 1 0 1 0 0 2h64a1 1 0 1 0 0-2h-3a7 7 0 0 0-6.019-6.932 22.9 22.9 0 0 0-6.013-14.595 1.5 1.5 0 0 1-.166-.18c-.36-.458-.554-1.204-.617-2.081a20 20 0 0 1-.035-.694l-.003-.077c-.008-.197-.015-.4-.027-.584a4 4 0 0 0-.087-.643c-.041-.176-.144-.539-.46-.808a2.1 2.1 0 0 0-1.047-.473c.421-.502.888-.979 1.363-1.38 1.003 1.019 2.46 1.81 4.165 2.149 3.589.712 6.922-.847 7.445-3.483.5-2.52-1.75-5.11-5.084-5.956.276-2.227-.476-4.245-2.116-5.109-2.336-1.23-5.588.35-7.264 3.53-1.624 3.082-1.172 6.535.981 7.867a14.4 14.4 0 0 0-1.669 1.925l-.068-.14-.024-.05c-.232-.485-.63-1.316-1.706-1.741-.62-.245-1.25-.198-1.777-.088-.509.106-1.038.298-1.504.467l-.04.015-.007.002c-.861.312-1.712.62-2.64.515C51.102 35.157 49.57 35 48 35c-12.39 0-22.493 9.798-22.981 22.068A7 7 0 0 0 19 64zm9.026-4.905a5 5 0 0 1 2.003.01A5 5 0 0 1 31 64H21a5 5 0 0 1 4.026-4.905m1.994-2.021C27.505 45.906 36.712 37 48 37c1.44 0 2.848.145 4.207.421 1.223.251 2.477-.158 3.615-.57l.086-.032q.313-.113.576-.204c.257-.087.484-.156.696-.2.695-.145 1.001.173 1.297.788l.012.026c.622 1.296 1.914 1.608 3.23 1.646.582.018.414.581.452 1.008l.042.473c.07.956.239 2.335 1.15 3.327a20.92 20.92 0 0 1 5.617 13.39A7 7 0 0 0 63 64H33a7 7 0 0 0-5.98-6.926m41.951 2.032a5 5 0 0 1 2.003-.011A5 5 0 0 1 75 64H65a5 5 0 0 1 3.971-4.894m3.108-23.702c-.923.432-2.215.618-3.635.336-1.015-.202-1.878-.599-2.54-1.083a4.7 4.7 0 0 1-.692-.616c-.325-.355-.534-.702-.652-1.027a1.83 1.83 0 0 1-.094-.985c.108-.544.534-1.142 1.458-1.574a5.3 5.3 0 0 1 1.909-.458 6.8 6.8 0 0 1 2.09.204c1.248.317 2.24.93 2.868 1.617.689.752.854 1.468.746 2.012s-.534 1.142-1.458 1.574m-3.655-8.691c.057.387.064.818.01 1.275-2.969-.075-5.482 1.393-5.93 3.652a4 4 0 0 0-.065.52 3.1 3.1 0 0 1-.333-1.046c-.147-.982.038-2.244.698-3.497s1.597-2.119 2.49-2.553c.894-.435 1.603-.388 2.073-.14.47.247.91.805 1.056 1.789"></path><path d="M56 58a1 1 0 1 0 0 2 1 1 0 0 0 0-2m-3 1a3 3 0 1 1 6 0 3 3 0 0 1-6 0M40 58a1 1 0 1 0 0 2 1 1 0 0 0 0-2m-3 1a3 3 0 1 1 6 0 3 3 0 0 1-6 0M55.13 50.957a1 1 0 0 1-1.809-.855l.904.427-.904-.427v-.001l.003-.006.005-.009.012-.024.038-.073a4.186 4.186 0 0 1 .652-.882c.462-.477 1.237-1.029 2.322-1.029 1.086 0 1.86.552 2.323 1.03a4.2 4.2 0 0 1 .689.955l.012.024.004.01.002.003v.002s.002.001-.886.42l.888-.419a1 1 0 1 1-1.816.84 2.18 2.18 0 0 0-.33-.444c-.24-.247-.529-.42-.886-.42s-.646.173-.887.42a2.2 2.2 0 0 0-.33.445l-.01.02.002-.005zM37.904 50.957a1 1 0 0 1-1.808-.855l.904.427-.904-.427v-.001l.003-.006.005-.009.012-.024.038-.073q.047-.087.133-.224c.114-.178.285-.416.519-.657.463-.478 1.237-1.03 2.323-1.03s1.86.552 2.322 1.03a4.2 4.2 0 0 1 .689.955l.012.024.004.01.002.003v.002s.002.001-.886.42l.888-.419a1 1 0 0 1-1.806.86l-.01-.02a2.187 2.187 0 0 0-.33-.444c-.24-.247-.529-.42-.885-.42-.358 0-.647.173-.888.42a2.2 2.2 0 0 0-.34.465l.002-.005z"></path></symbol><symbol id="back" viewBox="0 0 20 20"><path fill="currentColor" d="M8.082 9.877a.17.17 0 0 0 0 .224l5.477 6.144a.76.76 0 0 1-.05 1.06.727.727 0 0 1-1.04-.05L6.44 10.492a.76.76 0 0 1 0-1.01l6.017-6.738a.727.727 0 0 1 1.04-.05.76.76 0 0 1 .049 1.06z"></path></symbol><symbol id="play-s" viewBox="0 0 12 12"><path fill="#fff" d="m4.401 2.13 5.14 3.06a.947.947 0 0 1 0 1.621L4.401 9.87a.924.924 0 0 1-1.273-.334A.95.95 0 0 1 3 9.059V2.941C3 2.42 3.416 2 3.93 2c.166 0 .328.045.471.13"></path></symbol><symbol id="delete_back" viewBox="0 0 16 16"><path d="M11.42 10.357a.6.6 0 0 1-.848 0L9.064 8.848l-1.509 1.508a.6.6 0 0 1-.848-.848l1.508-1.509-1.508-1.508a.6.6 0 0 1 .848-.849l1.509 1.509 1.508-1.509a.6.6 0 1 1 .849.849L9.912 7.999l1.509 1.509a.6.6 0 0 1 0 .849"></path><path d="M4.166 4c.508-.632 1.276-1 2.089-1h5.735a2.67 2.67 0 0 1 2.675 2.667v4.666A2.67 2.67 0 0 1 11.99 13H6.255a2.68 2.68 0 0 1-2.089-1l-2.54-3.167a1.33 1.33 0 0 1 0-1.666zm2.089.2c-.447 0-.87.203-1.15.55l-2.54 3.167a.13.13 0 0 0 0 .166l2.54 3.167c.28.348.703.55 1.15.55h5.735c.813 0 1.472-.657 1.472-1.467V5.667c0-.81-.659-1.467-1.472-1.467z"></path></symbol><symbol id="user" viewBox="0 0 24 24"><g fill="currentColor"><path d="M12 8.067a2.1 2.1 0 1 0 0 4.2 2.1 2.1 0 0 0 0-4.2m-3.9 2.1a3.9 3.9 0 1 1 7.8 0 3.9 3.9 0 0 1-7.8 0"></path><path d="M22 12c0 5.523-4.477 10-10 10S2 17.523 2 12 6.477 2 12 2s10 4.477 10 10M7.796 16.132c1.117-.721 2.606-1.138 4.204-1.138s3.087.417 4.204 1.138c.666.43 1.237.998 1.586 1.674a8.2 8.2 0 1 0-11.58 0c.349-.676.92-1.244 1.586-1.674m7.432 1.512c-.785-.507-1.924-.85-3.228-.85s-2.443.343-3.228.85c-.64.414-.98.885-1.089 1.33A8.16 8.16 0 0 0 12 20.2c1.584 0 3.063-.45 4.317-1.227-.108-.444-.449-.915-1.09-1.329"></path></g></symbol><symbol id="reply" viewBox="0 0 16 16"><path fill="currentColor" fill-rule="evenodd" d="m2.617 11.337 1.019-.633c.205.33.259.74.132 1.12l-.374 1.122a35 35 0 0 1 1.024-.178 5.5 5.5 0 0 1 .732-.079c.306 0 .646.092.837.145l.051.013c.467.125 1.074.286 1.962.286 2.823 0 5.134-2.3 5.134-5.134a5.133 5.133 0 1 0-9.498 2.705zm-.672 2.162a.633.633 0 0 0 .612.831c.168-.033 2.2-.44 2.593-.44.139 0 .328.05.579.117.493.131 1.222.326 2.271.326 3.484 0 6.334-2.836 6.334-6.334a6.333 6.333 0 1 0-11.717 3.338c.02.032.025.072.013.108z" clip-rule="evenodd"></path></symbol><symbol id="group" viewBox="0 0 24 24"><path fill="#FF2442" d="M18.803 24H5.197A5.197 5.197 0 0 1 0 18.804V5.197A5.197 5.197 0 0 1 5.197 0h13.606A5.197 5.197 0 0 1 24 5.197v13.607A5.197 5.197 0 0 1 18.803 24"></path><path fill="#fff" fill-rule="evenodd" d="M21.053 12.41c-.067-.343-.244-.598-.543-.753a1.4 1.4 0 0 0-.665-.166h-.133c-.033 0-.033 0-.033-.034v-.798c0-.1 0-.199-.022-.299a1.5 1.5 0 0 0-.111-.399 1.2 1.2 0 0 0-.51-.542 1.6 1.6 0 0 0-.753-.2h-.543c-.056 0-.056 0-.056-.044v-.377c0-.011 0-.022-.01-.022-.012-.011-.023 0-.023 0h-1.174s-.012.01-.012.022v.41c0 .011-.01.011-.022.011h-.764c-.022 0-.022.011-.022.022v1.119c0 .067 0 .067.066.067h.687c.067 0 .055.1.055.1v.875s0 .089-.044.089h-1.119c-.055 0-.044.066-.044.066v1.097s-.011.055.044.055h1.097c.066 0 .055 0 .055.056v2.448c0 .067 0 .067.067.067h1.086c.066 0 .066 0 .066-.066v-2.482c0-.023 0-.023.022-.023h1.763a.45.45 0 0 1 .21.045c.133.066.2.166.21.31v.897c0 .2-.077.277-.244.277h-.919c-.022 0-.022 0-.022.023 0 .01.354.82.42.986v.01c0 .012.023.023.034.023h.388c.11 0 .387 0 .498-.011.1-.011.21-.022.31-.056.444-.132.732-.531.732-.997V12.71c0-.11-.011-.21-.022-.299m-2.57-.942c0 .011-.012.023-.012.023h-.776c-.01 0-.01-.011-.022-.023v-.044l-.01-.942c0-.055 0-.055.055-.055h.553c.034 0 .067 0 .09.01.077.023.121.079.121.156v.875m-3.159 2.604c0-.01-.01-.01-.022-.01h-1.097c-.033 0-.033 0-.033-.034V10.47c0-.055 0-.055.055-.055h.654c.055 0 .055 0 .055-.056V9.263c0-.066 0-.055-.055-.055h-2.648c-.045 0-.056 0-.056.055v1.097c0 .067 0 .056.056.056h.642c.056 0 .056 0 .056.055v3.513c0 .066 0 .066-.067.066h-.986c-.033 0-.044.022-.044.022l-.532 1.153-.011.022c0 .01.011.01.044.01h3.956c.022 0 .022 0 .022-.021v-1.13c.011-.012.011-.023.011-.034m-8.908-5.24H5.274a.024.024 0 0 0-.022.021c0 .289-.01 3.07-.01 4.477v.709c0 .222-.2.2-.211.2h-.554c-.034 0-.034 0-.034.033s.355.809.421.953c.011.01.022.022.045.022.122 0 .576.01.709-.011a1 1 0 0 0 .332-.1c.222-.122.366-.321.454-.576.045-.133.056-.266.056-.41v-2.615c0-.831 0-2.482-.011-2.693-.011 0-.022-.01-.033-.01m5.24 3.744h-.664c-.067 0-.111-.066-.089-.133l.886-1.994c.012-.011 0-.022-.022-.022h-.997c-.077 0-.133-.089-.1-.155l.665-1.485c.011-.011 0-.022-.022-.022H10.14c-.011 0-.011 0-.023.01l-.698 1.574c-.066.144-.144.288-.2.432-.032.089-.077.178-.099.277a.3.3 0 0 0-.01.144.36.36 0 0 0 .176.289c.034.022.067.033.1.044a.7.7 0 0 0 .255.044h.443c.022 0-.443 1.008-.52 1.208-.045.1-.078.188-.111.288-.011.044-.023.089-.011.133a.36.36 0 0 0 .177.3.4.4 0 0 0 .1.044.7.7 0 0 0 .254.044h1.252c.011 0 .011 0 .023-.011l.432-.975c0-.011-.011-.034-.022-.034m-2.914.698c-.077-.166-.088-.276-.1-.465 0-.077-.01-.144-.01-.221-.011-.111-.023-.222-.023-.333-.01-.122-.022-.244-.022-.366l-.033-.354a4 4 0 0 1-.022-.344 3 3 0 0 1-.022-.332c-.011-.122-.022-.244-.022-.366 0-.022 0-.055-.011-.066 0-.011-.045-.011-.056-.011H7.302c-.022 0-.022 0-.022.022.01.077.01.144.022.221.011.167.022.322.044.488l.034.377c.01.177.022.343.044.52.011.2.033.4.044.599.011.088.011.166.022.255.023.188.056.377.111.554.067.255.144.498.266.742.078.166.166.321.277.454.011.011.022.045.033.034 0 0 0-.011.011-.011.067-.144.566-1.252.599-1.33-.022-.033-.033-.022-.045-.066M4.41 10.417H3.236c-.012 0-.012 0-.012.01 0 0 0 .045-.01.056a4 4 0 0 0-.023.366c-.01.11-.022.221-.022.332-.011.111-.022.233-.022.344l-.033.354c-.011.122-.023.244-.023.366-.01.11-.022.222-.022.332-.01.078-.01.144-.01.222-.012.177-.023.3-.1.465-.023.045-.023.034 0 .089.033.066.52 1.152.598 1.319l.01.01c.012 0 .023-.021.034-.033.111-.144.2-.299.277-.454.111-.233.2-.487.266-.742.044-.189.078-.366.11-.554.012-.078.012-.166.023-.255.011-.2.033-.399.044-.599.011-.177.023-.343.045-.52l.033-.377a7 7 0 0 1 .044-.488c.011-.077.011-.144.022-.221-.033-.011-.033-.022-.055-.022m6.759 3.634H9.895c-.189 0-.4-.033-.576-.1-.011 0-.023 0-.023.011l-.542 1.175c0 .011 0 .022.01.022a1 1 0 0 0 .377.089h1.496c.011 0 .011 0 .022-.011l.532-1.164c0-.01-.01-.022-.022-.022m8.71-3.634h.586c.045 0 .09 0 .133-.011a.61.61 0 0 0 .466-.72.603.603 0 0 0-.665-.466c-.3.044-.52.3-.52.598v.588c-.012 0 0 .01 0 .01" clip-rule="evenodd"></path></symbol><symbol id="skeleton_s" viewBox="0 0 200 204"><rect width="200" height="150" rx="16"></rect><rect width="128" height="16" x="4" y="158" rx="8"></rect><rect width="160" height="16" x="4" y="180" opacity=".5" rx="8"></rect></symbol><symbol id="like" viewBox="0 0 16 16"><path fill="currentColor" fill-opacity=".8" d="M3.256 3.913a3.083 3.083 0 0 0-.003 4.397L8 12.998l4.743-4.684a3.085 3.085 0 0 0 .001-4.4c-.6-.593-1.4-.914-2.233-.914a3.17 3.17 0 0 0-1.91.635L8 4.087l-.601-.452A3.17 3.17 0 0 0 5.489 3c-.834 0-1.634.321-2.233.913m10.19 5.111-4.748 4.69a.996.996 0 0 1-1.397 0L2.549 9.02a4.083 4.083 0 0 1 .004-5.82A4.17 4.17 0 0 1 5.488 2c.907 0 1.787.29 2.512.835A4.17 4.17 0 0 1 10.51 2c1.093 0 2.146.422 2.936 1.202a4.085 4.085 0 0 1 0 5.822"></path></symbol><symbol id="livephoto_slash" viewBox="0 0 20 20"><path fill="#fff" d="M10.012 15.608q-1.169 0-2.185-.436a5.6 5.6 0 0 1-1.778-1.19 5.7 5.7 0 0 1-1.197-1.777 5.6 5.6 0 0 1-.429-2.186q0-.705.166-1.363a5.5 5.5 0 0 1 .491-1.238l.512.519a4.7 4.7 0 0 0-.366.996Q5.1 9.46 5.1 10.02q0 1.03.374 1.923.38.885 1.051 1.563.678.672 1.563 1.052a4.9 4.9 0 0 0 1.923.373q.567 0 1.093-.124a5 5 0 0 0 1.003-.367l.505.512q-.58.313-1.238.484a5.3 5.3 0 0 1-1.363.173m0-2.746q-.795 0-1.438-.38a2.87 2.87 0 0 1-1.024-1.024 2.77 2.77 0 0 1-.38-1.439q0-.242.062-.45l3.23 3.23a1.6 1.6 0 0 1-.45.063m0-5.679q.782 0 1.425.38.65.381 1.031 1.031.387.644.387 1.425 0 .575-.214 1.086L8.933 7.391a2.8 2.8 0 0 1 1.08-.208m0-2.746q1.149 0 2.159.436a5.64 5.64 0 0 1 2.988 2.988q.436 1.01.436 2.158 0 .872-.25 1.66a5.4 5.4 0 0 1-.691 1.446l-.484-.491a4.8 4.8 0 0 0 .747-2.615 4.856 4.856 0 0 0-1.439-3.466 4.86 4.86 0 0 0-3.466-1.438q-.726 0-1.39.2-.657.195-1.224.547L6.9 5.37a5.67 5.67 0 0 1 3.112-.934M10 3.04a.36.36 0 0 1-.256-.097.36.36 0 0 1-.097-.256q0-.145.097-.25a.35.35 0 0 1 .256-.103q.152 0 .249.104a.34.34 0 0 1 .103.249.35.35 0 0 1-.103.256.34.34 0 0 1-.25.097m1.272.117a.34.34 0 0 1-.249-.104.34.34 0 0 1-.104-.249q0-.151.104-.256a.34.34 0 0 1 .25-.103q.15 0 .255.103.104.105.104.256a.34.34 0 0 1-.104.25.35.35 0 0 1-.256.103m1.232.325a.35.35 0 0 1-.25-.097.35.35 0 0 1-.103-.256q0-.152.104-.249a.34.34 0 0 1 .249-.103q.152 0 .249.103.103.097.103.25a.35.35 0 0 1-.103.255.34.34 0 0 1-.25.097m1.162.554a.35.35 0 0 1-.256-.104.34.34 0 0 1-.104-.25q0-.15.104-.255a.35.35 0 0 1 .256-.104.34.34 0 0 1 .249.104q.104.104.104.256a.34.34 0 0 1-.104.249.34.34 0 0 1-.25.104m1.044.726a.35.35 0 0 1-.256-.104.35.35 0 0 1-.097-.249q0-.151.097-.249a.35.35 0 0 1 .256-.104.34.34 0 0 1 .25.104q.102.097.103.25a.34.34 0 0 1-.104.248.34.34 0 0 1-.249.104m.906.906a.35.35 0 0 1-.255-.104.34.34 0 0 1-.104-.249q0-.151.104-.256a.35.35 0 0 1 .255-.103.34.34 0 0 1 .25.103q.103.105.103.256a.34.34 0 0 1-.104.25.34.34 0 0 1-.249.103m.734 1.052a.35.35 0 0 1-.256-.104.35.35 0 0 1-.097-.25.36.36 0 0 1 .097-.255.35.35 0 0 1 .256-.104.34.34 0 0 1 .249.104q.103.103.103.256a.34.34 0 0 1-.103.249.34.34 0 0 1-.25.104m.532 1.155a.34.34 0 0 1-.249-.104.35.35 0 0 1-.104-.256.34.34 0 0 1 .104-.249.34.34 0 0 1 .25-.104q.15 0 .255.104a.34.34 0 0 1 .104.25.35.35 0 0 1-.104.255.35.35 0 0 1-.256.104m.332 1.224a.35.35 0 0 1-.256-.104.34.34 0 0 1-.103-.249q0-.151.103-.249a.35.35 0 0 1 .256-.103.34.34 0 0 1 .25.103q.103.097.103.25a.34.34 0 0 1-.104.248.34.34 0 0 1-.249.104m.111 1.26a.35.35 0 0 1-.256-.105.34.34 0 0 1-.104-.249q0-.152.104-.249a.35.35 0 0 1 .256-.103.34.34 0 0 1 .249.103q.105.097.104.25a.34.34 0 0 1-.104.248.34.34 0 0 1-.249.104m-.11 1.258a.35.35 0 0 1-.257-.104.34.34 0 0 1-.103-.249q0-.152.103-.249a.35.35 0 0 1 .256-.104.34.34 0 0 1 .25.104q.103.097.103.25a.34.34 0 0 1-.104.248.34.34 0 0 1-.249.104m-.333 1.231a.34.34 0 0 1-.249-.104.35.35 0 0 1-.104-.255.34.34 0 0 1 .104-.25.34.34 0 0 1 .25-.103q.15 0 .255.104a.34.34 0 0 1 .104.249.35.35 0 0 1-.104.255.35.35 0 0 1-.256.104m-.532 1.149a.36.36 0 0 1-.256-.097.36.36 0 0 1-.097-.256q0-.145.097-.25a.35.35 0 0 1 .256-.103.34.34 0 0 1 .249.104.34.34 0 0 1 .103.249.35.35 0 0 1-.103.256.35.35 0 0 1-.25.097m-2.684 2.683a.35.35 0 0 1-.256-.103.33.33 0 0 1-.104-.25.34.34 0 0 1 .104-.248.35.35 0 0 1 .256-.104.34.34 0 0 1 .249.104.34.34 0 0 1 .104.249.33.33 0 0 1-.104.249.34.34 0 0 1-.25.103m-1.162.554a.34.34 0 0 1-.25-.104.34.34 0 0 1-.103-.249q0-.152.104-.256a.34.34 0 0 1 .249-.104q.152 0 .249.104.103.105.103.256a.34.34 0 0 1-.103.25.33.33 0 0 1-.25.103m-1.232.325a.34.34 0 0 1-.249-.104.34.34 0 0 1-.104-.249q0-.152.104-.256a.35.35 0 0 1 .25-.097.36.36 0 0 1 .255.097q.104.105.104.256a.34.34 0 0 1-.104.25.35.35 0 0 1-.256.103M10 17.677a.35.35 0 0 1-.256-.104.35.35 0 0 1-.097-.25.36.36 0 0 1 .097-.255.35.35 0 0 1 .256-.104q.152 0 .249.104.103.103.103.256a.34.34 0 0 1-.103.249.33.33 0 0 1-.25.104m-1.273-.118a.35.35 0 0 1-.256-.104.34.34 0 0 1-.104-.249q0-.152.104-.256a.36.36 0 0 1 .256-.097q.146 0 .249.097.104.105.104.256a.34.34 0 0 1-.104.25.34.34 0 0 1-.25.103m-1.232-.325a.35.35 0 0 1-.255-.104.35.35 0 0 1-.097-.249.36.36 0 0 1 .097-.256.35.35 0 0 1 .255-.104.34.34 0 0 1 .25.104q.103.105.103.256a.34.34 0 0 1-.104.25.34.34 0 0 1-.249.103m-1.162-.554a.34.34 0 0 1-.249-.103.33.33 0 0 1-.103-.25.34.34 0 0 1 .103-.248.34.34 0 0 1 .25-.104q.15 0 .255.104a.34.34 0 0 1 .104.249.33.33 0 0 1-.104.249.35.35 0 0 1-.256.103m-1.044-.726a.34.34 0 0 1-.25-.104.34.34 0 0 1-.103-.249q0-.151.104-.256a.34.34 0 0 1 .249-.103q.151 0 .249.103.104.105.104.256a.34.34 0 0 1-.104.25.33.33 0 0 1-.25.103m-.906-.906a.35.35 0 0 1-.25-.097.35.35 0 0 1-.103-.256.34.34 0 0 1 .104-.249.34.34 0 0 1 .249-.104q.151 0 .256.104a.34.34 0 0 1 .103.25.35.35 0 0 1-.103.255.36.36 0 0 1-.256.097m-.734-1.051A.35.35 0 0 1 3.4 13.9a.35.35 0 0 1-.103-.256.34.34 0 0 1 .103-.25.34.34 0 0 1 .25-.103q.151 0 .248.104a.34.34 0 0 1 .104.249.35.35 0 0 1-.104.256.34.34 0 0 1-.249.097m-.532-1.149a.35.35 0 0 1-.256-.104.35.35 0 0 1-.104-.255.34.34 0 0 1 .104-.25.35.35 0 0 1 .256-.103.34.34 0 0 1 .249.104.34.34 0 0 1 .104.249.35.35 0 0 1-.104.255.34.34 0 0 1-.25.104m-.332-1.231a.34.34 0 0 1-.25-.104.34.34 0 0 1-.103-.249q0-.152.104-.249a.34.34 0 0 1 .249-.104q.152 0 .256.104.103.097.103.25a.34.34 0 0 1-.103.248.35.35 0 0 1-.256.104m-.11-1.259a.34.34 0 0 1-.25-.104.34.34 0 0 1-.104-.249q0-.152.104-.249a.34.34 0 0 1 .25-.103q.15 0 .255.103.104.097.104.25a.34.34 0 0 1-.104.248.35.35 0 0 1-.256.104m.11-1.259a.34.34 0 0 1-.25-.104.34.34 0 0 1-.103-.249q0-.151.104-.249a.34.34 0 0 1 .249-.103q.152 0 .256.103.103.097.103.25a.34.34 0 0 1-.103.248.35.35 0 0 1-.256.104m.332-1.224a.35.35 0 0 1-.256-.104.35.35 0 0 1-.104-.256.34.34 0 0 1 .104-.249.35.35 0 0 1 .256-.104.34.34 0 0 1 .249.104.34.34 0 0 1 .104.25.35.35 0 0 1-.104.255.34.34 0 0 1-.25.104m.532-1.155a.34.34 0 0 1-.249-.104.34.34 0 0 1-.103-.25q0-.15.103-.255a.34.34 0 0 1 .25-.104q.151 0 .248.104.105.103.104.256a.34.34 0 0 1-.104.249.33.33 0 0 1-.249.104m2.684-2.684a.34.34 0 0 1-.249-.104.34.34 0 0 1-.103-.25q0-.15.103-.255a.34.34 0 0 1 .25-.104q.15 0 .255.104t.104.256a.34.34 0 0 1-.104.249.35.35 0 0 1-.256.104m1.162-.554a.36.36 0 0 1-.255-.097.36.36 0 0 1-.097-.256q0-.152.097-.249a.35.35 0 0 1 .255-.103.34.34 0 0 1 .25.103q.103.097.103.25a.35.35 0 0 1-.104.255.35.35 0 0 1-.249.097m1.232-.325a.35.35 0 0 1-.256-.104.34.34 0 0 1-.104-.249q0-.151.104-.256a.35.35 0 0 1 .256-.103.34.34 0 0 1 .249.103q.104.105.104.256a.34.34 0 0 1-.104.25.34.34 0 0 1-.25.103m7.284 13.634L3.233 4.021a.5.5 0 0 1-.152-.373q0-.228.152-.38a.5.5 0 0 1 .38-.152q.222 0 .381.152l12.77 12.77a.48.48 0 0 1 .152.373q0 .22-.152.38a.52.52 0 0 1-.38.152.5.5 0 0 1-.374-.152"></path></symbol><symbol id="wechat" viewBox="0 0 20 16"><path fill="#07C160" d="M15.486 9.528a.736.736 0 1 1 0-1.472.736.736 0 0 1 0 1.472m-3.681 0a.736.736 0 1 1 0-1.473.736.736 0 0 1 0 1.473m5.454 4.216c1.165-.843 1.908-2.091 1.908-3.478 0-2.54-2.472-4.601-5.526-4.601s-5.526 2.06-5.526 4.601 2.473 4.602 5.526 4.602c.61 0 1.216-.084 1.802-.252a.5.5 0 0 1 .162-.023c.104 0 .205.03.294.084l1.208.698q.05.03.107.034a.183.183 0 0 0 .183-.183.5.5 0 0 0-.028-.135l-.252-.928a.4.4 0 0 1-.02-.118.38.38 0 0 1 .155-.3"></path><path fill="#07C160" d="M9.67 5.221a.88.88 0 1 1 0-1.758.88.88 0 0 1 0 1.758m-4.417 0a.88.88 0 1 1 0-1.758.88.88 0 0 1 0 1.758M7.461.583C3.803.583.834 3.055.834 6.104c0 1.664.892 3.161 2.29 4.173a.44.44 0 0 1 .161.502l-.298 1.114a.6.6 0 0 0-.036.16.22.22 0 0 0 .221.221.24.24 0 0 0 .126-.041l1.454-.838a.662.662 0 0 1 .546-.073 7.8 7.8 0 0 0 2.163.304c.126 0 .244 0 .364-.009a4.3 4.3 0 0 1-.222-1.353c0-2.78 2.705-5.036 6.044-5.036.125 0 .24 0 .359.01C13.503 2.6 10.768.583 7.46.583"></path></symbol><symbol id="menu" viewBox="0 0 20 20"><path d="M3.25 4.167h13.5a.75.75 0 0 1 0 1.5H3.25a.75.75 0 0 1 0-1.5M3.25 9.25h13.5a.75.75 0 0 1 0 1.5H3.25a.75.75 0 0 1 0-1.5M16.75 14.333H3.25a.75.75 0 0 0 0 1.5h13.5a.75.75 0 0 0 0-1.5"></path></symbol><symbol id="ic_weibo" viewBox="0 0 20 20"><path fill="currentColor" d="M11.449 6.194c1.944-.817 3.642-.865 4.262.024.33.474.299 1.138-.006 1.908-.14.354.043.41.313.49 1.095.341 2.315 1.166 2.315 2.618 0 2.405-3.457 5.433-8.652 5.433-3.963 0-8.014-1.927-8.014-5.096 0-1.657 1.046-3.573 2.848-5.381 2.406-2.413 5.212-3.513 6.268-2.453.465.466.51 1.275.211 2.24-.156.485.455.216.455.217m-2.5 1.794c-3.162.314-5.56 2.257-5.355 4.339s2.936 3.518 6.098 3.204 5.56-2.256 5.355-4.34c-.206-2.082-2.935-3.516-6.098-3.203m-1.302 6.648c-1.52-.492-2.165-1.998-1.499-3.355.654-1.33 2.355-2.082 3.86-1.69 1.557.404 2.352 1.879 1.715 3.31-.645 1.465-2.501 2.245-4.076 1.735m.858-2.851c-.49-.206-1.123.005-1.425.481-.306.477-.162 1.047.325 1.268.493.226 1.148.012 1.454-.478.3-.495.142-1.06-.354-1.271"></path></symbol><symbol id="lock" viewBox="0 0 20 20"><path fill="currentColor" fill-opacity=".4" d="M11.25 10.833c0 .41-.196.772-.5 1v1.084a.75.75 0 0 1-1.5 0v-1.083a1.25 1.25 0 1 1 2-1"></path><path fill="currentColor" fill-opacity=".4" d="M10 1.667A4.083 4.083 0 0 0 5.918 5.75v.168a3.335 3.335 0 0 0-2.583 3.249v5A3.333 3.333 0 0 0 6.667 17.5h6.667a3.333 3.333 0 0 0 3.333-3.333v-5a3.335 3.335 0 0 0-2.583-3.249V5.75a4.083 4.083 0 0 0-4.083-4.083m2.584 4.166H7.417V5.75a2.583 2.583 0 0 1 5.167 0zm-7.75 3.334c0-1.013.82-1.834 1.833-1.834h6.667c1.013 0 1.833.821 1.833 1.834v5c0 1.012-.82 1.833-1.833 1.833H6.667a1.833 1.833 0 0 1-1.833-1.833z"></path></symbol><symbol id="search" viewBox="0 0 24 24"><path d="M11.5 3a8.5 8.5 0 0 1 6.613 13.84l3.023 3.024a.9.9 0 1 1-1.272 1.272l-3.024-3.023A8.5 8.5 0 1 1 11.5 3m0 15.2a6.7 6.7 0 1 0 0-13.4 6.7 6.7 0 0 0 0 13.4"></path></symbol><symbol id="private" viewBox="0 0 12 12"><path fill="#fff" d="M6 1a2.45 2.45 0 0 0-2.45 2.45v.1A2 2 0 0 0 2 5.5v3a2 2 0 0 0 2 2h4a2 2 0 0 0 2-2v-3a2 2 0 0 0-1.55-1.95v-.1A2.45 2.45 0 0 0 6 1m1.55 2.5h-3.1v-.05a1.55 1.55 0 0 1 3.1 0zm-1.1 3.6v.65a.45.45 0 1 1-.9 0V7.1A.749.749 0 0 1 6 5.75a.75.75 0 0 1 .45 1.35"></path></symbol><symbol id="collect_small" viewBox="0 0 16 16"><path fill="currentColor" fill-opacity=".8" d="M10.885 14.232c.395.172.852.123 1.2-.13.348-.254.536-.673.491-1.1l-.3-2.923a.33.33 0 0 1 .083-.258l1.996-2.213a1.205 1.205 0 0 0-.646-1.989l-2.936-.63a.33.33 0 0 1-.217-.156l-1.51-2.569a1.213 1.213 0 0 0-2.092 0l-1.51 2.569a.33.33 0 0 1-.218.157l-2.936.63a1.205 1.205 0 0 0-.646 1.99L3.64 9.82c.063.07.094.164.084.258l-.301 2.923c-.044.427.143.846.491 1.1.349.253.806.302 1.2.13l2.752-1.201a.33.33 0 0 1 .267 0zM2.385 6.939a.2.2 0 0 1-.043-.202.21.21 0 0 1 .157-.14l2.936-.63c.365-.078.68-.306.87-.628l1.51-2.568A.21.21 0 0 1 8 2.667c.077 0 .146.04.183.104l1.51 2.568c.19.322.505.55.87.628l2.936.63a.21.21 0 0 1 .157.14.2.2 0 0 1-.043.202l-1.996 2.213c-.253.28-.375.654-.336 1.03l.3 2.922a.21.21 0 0 1-.084.189.22.22 0 0 1-.212.022l-2.752-1.2a1.33 1.33 0 0 0-1.067 0l-2.751 1.2a.22.22 0 0 1-.213-.022.21.21 0 0 1-.084-.189l.3-2.923a1.33 1.33 0 0 0-.336-1.03z"></path></symbol><symbol id="share_new" viewBox="0 0 24 24"><path fill="currentColor" d="M14.863 1.863a.9.9 0 0 1 1.273 0l4.5 4.5a.9.9 0 0 1 0 1.273l-4.5 4.5a.9.9 0 1 1-1.273-1.273l2.9-2.9c-2.266.143-3.919.534-5.195 1.257-1.62.918-2.763 2.449-3.723 5.087a.9.9 0 1 1-1.691-.615c1.04-2.862 2.397-4.83 4.527-6.038 1.648-.934 3.678-1.362 6.2-1.501l-3.018-3.017a.9.9 0 0 1 0-1.273M7 4.9A3.1 3.1 0 0 0 3.9 8v9A3.1 3.1 0 0 0 7 20.1h9a3.1 3.1 0 0 0 3.1-3.1v-4a.9.9 0 0 1 1.8 0v4a4.9 4.9 0 0 1-4.9 4.9H7A4.9 4.9 0 0 1 2.1 17V8A4.9 4.9 0 0 1 7 3.1h4a.9.9 0 1 1 0 1.8z"></path></symbol><symbol id="female" viewBox="0 0 12 12"><path fill="#FF7084" d="M6 1.75a2.25 2.25 0 1 1 0 4.5 2.25 2.25 0 0 1 0-4.5M3 4a3 3 0 0 0 2.625 2.977v.648h-2.25a.375.375 0 1 0 0 .75h2.25v2.25a.375.375 0 0 0 .75 0v-2.25h2.25a.375.375 0 1 0 0-.75h-2.25v-.648A3 3 0 1 0 3 4"></path></symbol><symbol id="menu" viewBox="0 0 20 20"><path d="M3.25 4.167h13.5a.75.75 0 0 1 0 1.5H3.25a.75.75 0 0 1 0-1.5M3.25 9.25h13.5a.75.75 0 0 1 0 1.5H3.25a.75.75 0 0 1 0-1.5M16.75 14.333H3.25a.75.75 0 0 0 0 1.5h13.5a.75.75 0 0 0 0-1.5"></path></symbol><symbol id="chevron_down" viewBox="0 0 16 16"><path d="M2.195 5.529a.667.667 0 0 0 0 .943l5.334 5.333c.26.26.682.26.942 0l5.334-5.333a.667.667 0 1 0-.943-.943L8 10.39 3.138 5.529a.667.667 0 0 0-.943 0"></path></symbol><symbol id="search_user_info_skeleton" viewBox="0 0 160 40"><rect width="80" height="16" rx="8"></rect><rect width="160" height="16" y="24" rx="8"></rect></symbol><symbol id="alert" viewBox="0 0 20 20"><path d="M9.25 6.105c0-.38.336-.688.75-.688s.75.308.75.688v5.29c0 .38-.336.688-.75.688s-.75-.308-.75-.688zM10 14.584a.75.75 0 1 0 0-1.5.75.75 0 0 0 0 1.5"></path><path d="M18.333 10a8.333 8.333 0 1 1-16.666 0 8.333 8.333 0 0 1 16.666 0m-1.5 0a6.833 6.833 0 1 0-13.666 0 6.833 6.833 0 0 0 13.666 0"></path></symbol><symbol id="arrow_right_top" viewBox="0 0 24 24"><path fill="currentColor" fill-rule="evenodd" d="M6.664 5a1 1 0 0 1 1-1h11.314a1 1 0 0 1 1 1v11.314a1 1 0 1 1-2 0v-8.9L6.958 18.435a1 1 0 1 1-1.415-1.414L16.563 6H7.665a1 1 0 0 1-1-1" clip-rule="evenodd"></path></symbol><symbol id="speaker" viewBox="0 0 20 20"><g fill="#3D8AF5"><path d="m12.334 15.624-.957-.383a3.56 3.56 0 0 1-5.751-.955l-.326-.04a4.247 4.247 0 0 1 0-8.492s3.264-.023 5.22-.652c.726-.234 1.814-.726 1.814-.726a2.806 2.806 0 0 1 5.489.817v9.614a2.805 2.805 0 0 1-5.49.817m.28-1.504V5.88s-1.027.471-1.716.686c-1.549.482-4.121.515-4.121.515v5.838h.007q.025.284.12.54a2.061 2.061 0 0 0 3.881-.04l.113.015zm1.5 1.629a1.305 1.305 0 0 0 2.209-.941V5.192a1.305 1.305 0 1 0-2.61 0v9.614c0 .37.154.704.401.942m-10.21-8.05a2.75 2.75 0 0 0-1.248 2.3 2.745 2.745 0 0 0 2.747 2.748V7.253q-.063 0-.126.003a2.73 2.73 0 0 0-1.374.442"></path><path d="M8.828 13.64a.883.883 0 1 0 0-1.765.883.883 0 0 0 0 1.766"></path></g></symbol><symbol id="Android" viewBox="0 0 24 28"><path fill="#333" fill-rule="nonzero" d="M8.2 5.974a.62.62 0 0 0 .457-.194.64.64 0 0 0 .191-.463.64.64 0 0 0-.19-.462.62.62 0 0 0-.458-.194.6.6 0 0 0-.45.194.65.65 0 0 0-.182.462q0 .27.183.463a.6.6 0 0 0 .449.194m7.018 0a.6.6 0 0 0 .45-.194.65.65 0 0 0 .183-.463.65.65 0 0 0-.183-.462.6.6 0 0 0-.45-.194.62.62 0 0 0-.457.194.64.64 0 0 0-.191.462q0 .27.191.463a.62.62 0 0 0 .457.194M1.713 9.07q.699 0 1.198.505.498.504.499 1.211v7.236q0 .723-.491 1.228a1.62 1.62 0 0 1-1.206.505q-.715 0-1.214-.505A1.68 1.68 0 0 1 0 18.022v-7.236q0-.707.499-1.211a1.64 1.64 0 0 1 1.214-.505m17.63.32v11.206q0 .774-.532 1.313a1.74 1.74 0 0 1-1.28.538h-1.248v3.82q0 .723-.499 1.228A1.64 1.64 0 0 1 14.57 28q-.716 0-1.214-.505a1.68 1.68 0 0 1-.5-1.228v-3.82h-2.295v3.82q0 .723-.498 1.228A1.64 1.64 0 0 1 8.848 28q-.698 0-1.197-.505a1.68 1.68 0 0 1-.5-1.228l-.016-3.82h-1.23q-.765 0-1.298-.538a1.8 1.8 0 0 1-.532-1.313V9.39zm-3.858-6.815a7.34 7.34 0 0 1 2.844 2.582 6.6 6.6 0 0 1 1.064 3.627H4.008q0-1.97 1.065-3.627a7.3 7.3 0 0 1 2.86-2.582L6.754.37q-.117-.219.083-.336.216-.101.332.1l1.198 2.222a8.1 8.1 0 0 1 3.343-.707q1.763 0 3.343.707L16.25.135q.116-.203.332-.101.2.117.083.336zm7.933 8.211v7.236q0 .723-.499 1.228a1.64 1.64 0 0 1-1.214.505q-.699 0-1.197-.505a1.68 1.68 0 0 1-.5-1.228v-7.236q0-.723.5-1.22.498-.495 1.197-.496.716 0 1.214.496.5.497.5 1.22"></path></symbol><symbol id="play" viewBox="0 0 10 12"><path fill="currentColor" d="M2.002.515 9.345 4.85a1.335 1.335 0 0 1 0 2.297L2.002 11.48A1.326 1.326 0 0 1 0 10.332V1.664A1.33 1.33 0 0 1 2.002.515"></path></symbol><symbol id="right-arrow" viewBox="0 0 16 16"><path fill="#333" fill-opacity=".6" d="M6.195 2.862c.26-.26.683-.26.943 0l4.667 4.666c.26.26.26.683 0 .943l-4.667 4.667a.667.667 0 1 1-.943-.943L10.39 8 6.195 3.805a.667.667 0 0 1 0-.943"></path></symbol><symbol id="location" viewBox="0 0 12 12"><path fill="#fff" d="M2.105 7.618a4.33 4.33 0 0 1-.605-2.21C1.5 2.282 4.69.13 7.806 1.342c.916.356 1.944 1.347 2.317 2.24.582 1.39.478 2.841-.228 4.034-.475.8-1.712 1.944-3.2 3.14a1.11 1.11 0 0 1-1.39 0c-1.494-1.202-2.725-2.34-3.2-3.14M6 6.75A1.375 1.375 0 1 0 6 4a1.375 1.375 0 0 0 0 2.75"></path></symbol><symbol id="collected" viewBox="0 0 24 24"><path fill="#FDBC5F" d="M18.865 19.503a1.81 1.81 0 0 1-.737 1.649 1.82 1.82 0 0 1-1.8.196L12.2 19.546a.5.5 0 0 0-.4 0l-4.127 1.802a1.82 1.82 0 0 1-1.801-.196 1.81 1.81 0 0 1-.737-1.65l.452-4.384a.5.5 0 0 0-.127-.386l-2.994-3.32a1.81 1.81 0 0 1-.377-1.77c.2-.615.713-1.077 1.347-1.213l4.404-.945a.5.5 0 0 0 .326-.235l2.265-3.853a1.82 1.82 0 0 1 3.138 0l2.265 3.853a.5.5 0 0 0 .326.235l4.404.945a1.808 1.808 0 0 1 .97 2.984l-2.994 3.319a.5.5 0 0 0-.127.386z"></path></symbol><symbol id="user_banned" viewBox="0 0 96 96"><path d="M67.053 60c.77 1.333-.193 3-1.733 3H30.68c-1.54 0-2.502-1.667-1.733-3l17.32-30c.77-1.333 2.695-1.333 3.465 0zM51.464 29c-1.54-2.667-5.389-2.667-6.928 0l-17.32 30c-1.54 2.667.384 6 3.464 6h34.64c3.08 0 5.004-3.333 3.465-6z"></path><path d="M49 53.5a1 1 0 1 1-2 0 1 1 0 0 1 2 0M48 41.5a1.5 1.5 0 0 0-1.5 1.5l.018.232L47 49.5a1 1 0 1 0 2 0l.482-6.268L49.5 43a1.5 1.5 0 0 0-1.5-1.5"></path></symbol><symbol id="exit" viewBox="0 0 24 24"><path fill="currentColor" d="M3.268 11.354a.914.914 0 0 0 0 1.292l5.586 5.586a.914.914 0 0 0 1.292-1.292l-4.025-4.026h13.965a.914.914 0 0 0 0-1.828H6.12l4.025-4.026a.914.914 0 1 0-1.292-1.292z"></path></symbol><symbol id="reload" viewBox="0 0 24 24"><path fill="currentColor" d="M10.783 7.078a.91.91 0 0 1 .087-1.282l2.156-1.884a7.98 7.98 0 0 0-8.138 3.913 8.044 8.044 0 0 0 1.834 10.194.909.909 0 1 1-1.16 1.4 9.86 9.86 0 0 1-2.25-12.5A9.794 9.794 0 0 1 14.96 2.524c.773.264.966 1.27.354 1.803l-3.248 2.838a.91.91 0 0 1-1.283-.087M13.217 16.922a.91.91 0 0 1-.087 1.282l-2.156 1.884a7.98 7.98 0 0 0 8.138-3.913 8.044 8.044 0 0 0-1.834-10.194.909.909 0 1 1 1.16-1.4 9.86 9.86 0 0 1 2.25 12.5A9.794 9.794 0 0 1 9.04 21.476c-.772-.263-.965-1.265-.354-1.803l3.248-2.838a.91.91 0 0 1 1.283.087"></path></symbol><symbol id="done" viewBox="0 0 20 20"><path fill="currentColor" fill-opacity=".6" d="M2.656 10.212a.625.625 0 0 1 .882-.056l4.726 4.159 8.964-10.757a.625.625 0 0 1 .96.8l-9.375 11.25a.625.625 0 0 1-.893.07l-5.208-4.584a.625.625 0 0 1-.056-.882"></path></symbol><symbol id="thanks" viewBox="0 0 24 25"><rect width="24" height="24" y=".5" fill="#FF2442" rx="12"></rect><path stroke="#fff" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="m6 13 4 4 8-8"></path></symbol><symbol id="ic_close" viewBox="0 0 20 20"><path fill="currentColor" d="M16.025 3.977c.3.299.3.784 0 1.084L11.085 10l4.938 4.938a.767.767 0 0 1-1.084 1.084L10 11.085l-4.94 4.94a.77.77 0 0 1-1.012.064l-.072-.064c-.3-.299-.3-.784 0-1.084l4.94-4.94-4.942-4.942a.767.767 0 1 1 1.084-1.084l4.942 4.941 4.94-4.94a.77.77 0 0 1 1.012-.063z"></path></symbol><symbol id="skeleton_m" viewBox="0 0 200 254"><rect width="200" height="200" rx="16"></rect><rect width="128" height="16" x="4" y="208" rx="8"></rect><rect width="160" height="16" x="4" y="230" opacity=".5" rx="8"></rect></symbol><symbol id="male" viewBox="0 0 12 12"><path fill="#5B92E1" d="M5.735 1.11a.375.375 0 0 1 .53 0L8.39 3.235a.375.375 0 0 1-.53.53L6.375 2.28v2.743a3 3 0 1 1-.75 0V2.28L4.14 3.765a.375.375 0 0 1-.53-.53zM6 5.75a2.25 2.25 0 1 0 0 4.5 2.25 2.25 0 0 0 0-4.5"></path></symbol><symbol id="company" viewBox="0 0 24 24"><path fill="#5B92E1" fill-rule="evenodd" d="M12 22c5.523 0 10-4.477 10-10S17.523 2 12 2 2 6.477 2 12s4.477 10 10 10" clip-rule="evenodd"></path><path fill="#fff" d="M17.244 9.526a.894.894 0 0 0-.02-1.273.915.915 0 0 0-1.286.021l-5.415 5.543-1.972-1.953a.915.915 0 0 0-1.285 0 .894.894 0 0 0 0 1.272l2.625 2.6a.913.913 0 0 0 1.296-.01z"></path></symbol><symbol id="livephoto" viewBox="0 0 20 20"><path fill="#fff" d="M9.999 15.588q-1.17 0-2.186-.43a5.6 5.6 0 0 1-1.778-1.196 5.7 5.7 0 0 1-1.197-1.778 5.55 5.55 0 0 1-.429-2.179q0-1.161.43-2.172A5.6 5.6 0 0 1 6.041 6.05a5.57 5.57 0 0 1 3.957-1.633q1.155 0 2.165.436t1.777 1.21q.775.768 1.21 1.778.438 1.01.437 2.165 0 1.163-.436 2.172a5.7 5.7 0 0 1-1.204 1.778 5.55 5.55 0 0 1-1.784 1.197 5.4 5.4 0 0 1-2.165.436m0-.671q1.016 0 1.909-.38a4.9 4.9 0 0 0 2.621-2.623q.38-.89.38-1.909 0-1.017-.386-1.902a4.9 4.9 0 0 0-1.059-1.563 4.9 4.9 0 0 0-1.563-1.059 4.7 4.7 0 0 0-1.902-.387q-1.017 0-1.91.38a4.94 4.94 0 0 0-2.621 2.622 4.8 4.8 0 0 0-.38 1.91q0 1.023.38 1.915a4.91 4.91 0 0 0 2.614 2.615q.893.38 1.917.38m0-11.877a.36.36 0 0 1-.256-.097.36.36 0 0 1-.097-.256q0-.145.097-.25a.35.35 0 0 1 .256-.103q.152 0 .249.104a.34.34 0 0 1 .103.249.35.35 0 0 1-.103.256.34.34 0 0 1-.25.097m1.272.117a.34.34 0 0 1-.249-.104.34.34 0 0 1-.104-.249q0-.151.104-.256a.34.34 0 0 1 .25-.103q.15 0 .255.103.104.105.104.256a.34.34 0 0 1-.104.25.35.35 0 0 1-.256.103m1.232.325a.35.35 0 0 1-.25-.097.35.35 0 0 1-.103-.256q0-.152.104-.249a.34.34 0 0 1 .249-.103q.152 0 .249.103.103.097.103.25a.35.35 0 0 1-.103.255.34.34 0 0 1-.25.097m1.162.554a.35.35 0 0 1-.256-.104.34.34 0 0 1-.104-.25q0-.15.104-.255a.35.35 0 0 1 .256-.104.34.34 0 0 1 .249.104q.104.104.104.256a.34.34 0 0 1-.104.249.34.34 0 0 1-.25.104m1.044.726a.35.35 0 0 1-.256-.104.35.35 0 0 1-.097-.249q0-.151.097-.249a.35.35 0 0 1 .256-.104.34.34 0 0 1 .25.104q.102.097.103.25a.34.34 0 0 1-.104.248.34.34 0 0 1-.249.104m.906.906a.35.35 0 0 1-.255-.104.34.34 0 0 1-.104-.249q0-.151.104-.256a.35.35 0 0 1 .255-.103.34.34 0 0 1 .25.103q.103.105.103.256a.34.34 0 0 1-.104.25.34.34 0 0 1-.249.103m.734 1.052a.35.35 0 0 1-.256-.104.35.35 0 0 1-.097-.25.36.36 0 0 1 .097-.255.35.35 0 0 1 .256-.104.34.34 0 0 1 .249.104q.103.103.103.256a.34.34 0 0 1-.103.249.34.34 0 0 1-.25.104m.532 1.155a.34.34 0 0 1-.249-.104.35.35 0 0 1-.104-.256.34.34 0 0 1 .104-.249.34.34 0 0 1 .25-.104q.15 0 .255.104a.34.34 0 0 1 .104.25.35.35 0 0 1-.104.255.35.35 0 0 1-.256.104m.332 1.224a.35.35 0 0 1-.256-.104.34.34 0 0 1-.103-.249q0-.151.103-.249a.35.35 0 0 1 .256-.103.34.34 0 0 1 .25.103q.103.097.103.25a.34.34 0 0 1-.104.248.34.34 0 0 1-.249.104m.111 1.26a.35.35 0 0 1-.256-.105.34.34 0 0 1-.104-.249q0-.152.104-.249a.35.35 0 0 1 .256-.103.34.34 0 0 1 .249.103q.105.097.104.25a.34.34 0 0 1-.104.248.34.34 0 0 1-.249.104m-.11 1.258a.35.35 0 0 1-.257-.104.34.34 0 0 1-.103-.249q0-.152.103-.249a.35.35 0 0 1 .256-.104.34.34 0 0 1 .25.104q.103.097.103.25a.34.34 0 0 1-.104.248.34.34 0 0 1-.249.104m-.333 1.231a.34.34 0 0 1-.249-.104.35.35 0 0 1-.104-.255.34.34 0 0 1 .104-.25.34.34 0 0 1 .25-.103q.15 0 .255.104a.34.34 0 0 1 .104.249.35.35 0 0 1-.104.255.35.35 0 0 1-.256.104m-.532 1.149a.36.36 0 0 1-.256-.097.36.36 0 0 1-.097-.256q0-.145.097-.25a.35.35 0 0 1 .256-.103.34.34 0 0 1 .249.104.34.34 0 0 1 .103.249.35.35 0 0 1-.103.256.35.35 0 0 1-.25.097m-.734 1.051a.36.36 0 0 1-.255-.097.35.35 0 0 1-.104-.256.34.34 0 0 1 .104-.249.35.35 0 0 1 .255-.104.34.34 0 0 1 .25.104.34.34 0 0 1 .103.25.35.35 0 0 1-.104.255.35.35 0 0 1-.249.097m-.906.906a.35.35 0 0 1-.256-.104.35.35 0 0 1-.097-.249.36.36 0 0 1 .097-.256.35.35 0 0 1 .256-.103.34.34 0 0 1 .25.103q.102.105.103.256a.34.34 0 0 1-.104.25.34.34 0 0 1-.249.103m-1.044.726a.35.35 0 0 1-.256-.103.33.33 0 0 1-.104-.25.34.34 0 0 1 .104-.248.35.35 0 0 1 .256-.104.34.34 0 0 1 .249.104.34.34 0 0 1 .104.249.33.33 0 0 1-.104.249.34.34 0 0 1-.25.103m-1.162.554a.34.34 0 0 1-.25-.104.34.34 0 0 1-.103-.249q0-.152.104-.256a.34.34 0 0 1 .249-.104q.152 0 .249.104.103.105.103.256a.34.34 0 0 1-.103.25.33.33 0 0 1-.25.103m-1.232.325a.34.34 0 0 1-.249-.104.34.34 0 0 1-.104-.249q0-.152.104-.256a.35.35 0 0 1 .25-.097.36.36 0 0 1 .255.097q.104.105.104.256a.34.34 0 0 1-.104.25.35.35 0 0 1-.256.103M10 17.677a.35.35 0 0 1-.256-.104.35.35 0 0 1-.097-.25.36.36 0 0 1 .097-.255.35.35 0 0 1 .256-.104q.152 0 .249.104.103.103.103.256a.34.34 0 0 1-.103.249.33.33 0 0 1-.25.104m-1.273-.118a.35.35 0 0 1-.256-.104.34.34 0 0 1-.104-.249q0-.152.104-.256a.36.36 0 0 1 .256-.097q.146 0 .249.097.104.105.104.256a.34.34 0 0 1-.104.25.34.34 0 0 1-.25.103m-1.232-.325a.35.35 0 0 1-.255-.104.35.35 0 0 1-.097-.249.36.36 0 0 1 .097-.256.35.35 0 0 1 .255-.104.34.34 0 0 1 .25.104q.103.105.103.256a.34.34 0 0 1-.104.25.34.34 0 0 1-.249.103m-1.162-.554a.34.34 0 0 1-.249-.103.33.33 0 0 1-.103-.25.34.34 0 0 1 .103-.248.34.34 0 0 1 .25-.104q.15 0 .255.104a.34.34 0 0 1 .104.249.33.33 0 0 1-.104.249.35.35 0 0 1-.256.103m-1.044-.726a.34.34 0 0 1-.25-.104.34.34 0 0 1-.103-.249q0-.151.104-.256a.34.34 0 0 1 .249-.103q.151 0 .249.103.104.105.104.256a.34.34 0 0 1-.104.25.33.33 0 0 1-.25.103m-.906-.906a.35.35 0 0 1-.25-.097.35.35 0 0 1-.103-.256.34.34 0 0 1 .104-.249.34.34 0 0 1 .249-.104q.151 0 .256.104a.34.34 0 0 1 .103.25.35.35 0 0 1-.103.255.36.36 0 0 1-.256.097m-.734-1.051A.35.35 0 0 1 3.4 13.9a.35.35 0 0 1-.103-.256.34.34 0 0 1 .103-.25.34.34 0 0 1 .25-.103q.151 0 .248.104a.34.34 0 0 1 .104.249.35.35 0 0 1-.104.256.34.34 0 0 1-.249.097m-.532-1.149a.35.35 0 0 1-.256-.104.35.35 0 0 1-.104-.255.34.34 0 0 1 .104-.25.35.35 0 0 1 .256-.103.34.34 0 0 1 .249.104.34.34 0 0 1 .104.249.35.35 0 0 1-.104.255.34.34 0 0 1-.25.104m-.332-1.231a.34.34 0 0 1-.25-.104.34.34 0 0 1-.103-.249q0-.152.104-.249a.34.34 0 0 1 .249-.104q.152 0 .256.104.103.097.103.25a.34.34 0 0 1-.103.248.35.35 0 0 1-.256.104m-.11-1.259a.34.34 0 0 1-.25-.104.34.34 0 0 1-.104-.249q0-.152.104-.249a.34.34 0 0 1 .25-.103q.15 0 .255.103.104.097.104.25a.34.34 0 0 1-.104.248.35.35 0 0 1-.256.104m.11-1.259a.34.34 0 0 1-.25-.104.34.34 0 0 1-.103-.249q0-.151.104-.249a.34.34 0 0 1 .249-.103q.152 0 .256.103.103.097.103.25a.34.34 0 0 1-.103.248.35.35 0 0 1-.256.104m.332-1.224a.35.35 0 0 1-.256-.104.35.35 0 0 1-.104-.256.34.34 0 0 1 .104-.249.35.35 0 0 1 .256-.104.34.34 0 0 1 .249.104.34.34 0 0 1 .104.25.35.35 0 0 1-.104.255.34.34 0 0 1-.25.104m.532-1.155a.34.34 0 0 1-.249-.104.34.34 0 0 1-.103-.25q0-.15.103-.255a.34.34 0 0 1 .25-.104q.151 0 .248.104.105.103.104.256a.34.34 0 0 1-.104.249.33.33 0 0 1-.249.104m.734-1.052a.34.34 0 0 1-.25-.104.34.34 0 0 1-.103-.249q0-.151.104-.256a.34.34 0 0 1 .249-.103q.151 0 .256.103.103.105.103.256a.34.34 0 0 1-.103.25.35.35 0 0 1-.256.103m.906-.906a.34.34 0 0 1-.25-.104.34.34 0 0 1-.103-.249q0-.151.104-.249a.34.34 0 0 1 .249-.104q.151 0 .249.104.104.097.104.25a.34.34 0 0 1-.104.248.33.33 0 0 1-.25.104m1.044-.726a.34.34 0 0 1-.249-.104.34.34 0 0 1-.103-.25q0-.15.103-.255a.34.34 0 0 1 .25-.104q.15 0 .255.104t.104.256a.34.34 0 0 1-.104.249.35.35 0 0 1-.256.104m1.162-.554a.36.36 0 0 1-.255-.097.36.36 0 0 1-.097-.256q0-.152.097-.249a.35.35 0 0 1 .255-.103.34.34 0 0 1 .25.103q.103.097.103.25a.35.35 0 0 1-.104.255.35.35 0 0 1-.249.097m1.232-.325a.35.35 0 0 1-.256-.104.34.34 0 0 1-.104-.249q0-.151.104-.256a.35.35 0 0 1 .256-.103.34.34 0 0 1 .249.103q.104.105.104.256a.34.34 0 0 1-.104.25.34.34 0 0 1-.25.103m1.273 9.698a2.8 2.8 0 0 1-1.44-.38 2.87 2.87 0 0 1-1.023-1.024 2.77 2.77 0 0 1-.38-1.439q0-.78.38-1.425a2.9 2.9 0 0 1 1.03-1.03A2.76 2.76 0 0 1 10 7.177q.78 0 1.425.38.65.38 1.03 1.03.388.644.388 1.425 0 .788-.388 1.439-.38.643-1.024 1.024a2.76 2.76 0 0 1-1.431.38m0-1.3q.421 0 .767-.208.354-.207.56-.553.208-.353.208-.782 0-.422-.207-.768a1.6 1.6 0 0 0-.56-.553 1.43 1.43 0 0 0-.768-.214q-.43 0-.775.207t-.554.56q-.207.346-.207.768 0 .43.2.782.208.346.554.553.353.208.782.208"></path></symbol><symbol id="loading" viewBox="0 0 20 20"><path fill="currentColor" fill-opacity=".3" d="M10 3.182A6.818 6.818 0 1 0 16.816 10a.758.758 0 0 1 1.516 0 8.333 8.333 0 1 1-8.334-8.333.758.758 0 0 1 0 1.515"></path></symbol><symbol id="ic_link" viewBox="0 0 20 20"><path fill="currentColor" d="M15.948 2.868a4.1 4.1 0 0 0-5.8 0L8.964 4.052a.753.753 0 0 0 1.066 1.065l1.183-1.184a2.595 2.595 0 0 1 3.67 0l1.184 1.184a2.595 2.595 0 0 1 0 3.67l-2.368 2.367a2.595 2.595 0 0 1-3.67 0l-.591-.592a.753.753 0 1 0-1.066 1.066l.592.591a4.1 4.1 0 0 0 5.8 0l2.368-2.367a4.1 4.1 0 0 0 0-5.8z"></path><path fill="currentColor" d="M4.052 17.132a4.1 4.1 0 0 0 5.8 0l1.361-1.361a.753.753 0 0 0-1.065-1.066l-1.361 1.362a2.595 2.595 0 0 1-3.67 0l-1.184-1.184a2.595 2.595 0 0 1 0-3.67l2.368-2.367a2.595 2.595 0 0 1 3.67 0l.591.592a.753.753 0 0 0 1.066-1.066l-.592-.592a4.1 4.1 0 0 0-5.8 0l-2.368 2.368a4.1 4.1 0 0 0 0 5.8z"></path></symbol><symbol id="right" viewBox="0 0 16 16"><path d="M5.527 2.195c.26-.26.683-.26.943 0l5.333 5.334c.26.26.26.682 0 .942L6.47 13.805a.667.667 0 1 1-.943-.943L10.39 8 5.527 3.138a.667.667 0 0 1 0-.943"></path></symbol><symbol id="user_empty_like" viewBox="0 0 96 96"><path fill-rule="evenodd" d="M66.865 49.088 48 67.953 29.135 49.088A11.96 11.96 0 0 1 26 41c0-6.627 5.373-12 12-12 3.424 0 6.513 1.434 8.7 3.734.478.504.914 1.05 1.3 1.63q.581-.872 1.3-1.63A11.97 11.97 0 0 1 58 29c6.627 0 12 5.373 12 12 0 3.116-1.188 5.954-3.135 8.088m-36.282-1.38A9.96 9.96 0 0 1 28 41c0-5.523 4.477-10 10-10a9.99 9.99 0 0 1 8.334 4.472L48 37.977l1.666-2.505A9.99 9.99 0 0 1 58 31c5.523 0 10 4.477 10 10a9.96 9.96 0 0 1-2.583 6.707L48 65.124z" clip-rule="evenodd"></path><path d="M34 41a4 4 0 0 1 4-4 1 1 0 1 0 0-2 6 6 0 0 0-6 6 1 1 0 1 0 2 0M73.275 51.815a4.744 4.744 0 0 0-6.276 5.995l.166.402 3.87 9.342 9.341-3.87.402-.166a4.744 4.744 0 1 0-4.662-8.23 4.74 4.74 0 0 0-2.841-3.473M22.687 51.815a4.743 4.743 0 0 1 6.276 5.995l-.166.402-3.87 9.342-9.342-3.87-.402-.166a4.744 4.744 0 1 1 4.663-8.23 4.74 4.74 0 0 1 2.84-3.473" opacity=".5"></path></symbol><symbol id="ic_wechat" viewBox="0 0 20 20"><path fill="currentColor" d="M14.136 7.044c.09.163-.03.36-.22.376-2.716.26-4.842 2.383-4.842 4.96a4.7 4.7 0 0 0 .876 2.713.257.257 0 0 1-.156.395 7.25 7.25 0 0 1-3.542-.116c-.565-.165-1.101-.2-1.591-.104l-.574.11a.8.8 0 0 1-.628-.142.78.78 0 0 1-.311-.556l-.072-.792a2 2 0 0 0-.366-.971 5.53 5.53 0 0 1-1.043-3.214c0-3.283 2.952-5.953 6.582-5.953 2.574 0 4.806 1.343 5.887 3.294m-8.006.873a.892.892 0 1 0 .003-1.785.892.892 0 0 0-.003 1.785m2.68-.892a.892.892 0 1 0 1.787 0 .892.892 0 0 0-1.787 0"></path><path fill="currentColor" d="M10 12.38c0-2.133 1.869-3.868 4.166-3.868 2.299 0 4.167 1.735 4.167 3.868a3.67 3.67 0 0 1-.664 2.096 1.06 1.06 0 0 0-.188.509l-.043.492a.68.68 0 0 1-.265.477.66.66 0 0 1-.525.12l-.347-.067a1.8 1.8 0 0 0-.875.06 4.4 4.4 0 0 1-1.26.183c-2.297 0-4.166-1.735-4.166-3.87m1.786-1.487a.595.595 0 1 0 1.189.001.595.595 0 0 0-1.19-.001m3.571.595a.595.595 0 1 0 0-1.19.595.595 0 0 0 0 1.19"></path></symbol><symbol id="arrow_right_f" viewBox="0 0 24 24"><path fill="#fff" d="M2 12c0 5.523 4.477 10 10 10s10-4.477 10-10S17.523 2 12 2 2 6.477 2 12m11.53 3.78a.75.75 0 1 1-1.06-1.06l1.97-1.97H7.75a.75.75 0 0 1 0-1.5h6.69l-1.97-1.97a.75.75 0 0 1 1.06-1.06l3.25 3.25a.75.75 0 0 1 0 1.06z" opacity=".5"></path></symbol><symbol id="success" viewBox="0 0 24 24"><g fill="#333" fill-opacity=".6"><path d="M22 12c0 5.523-4.477 10-10 10S2 17.523 2 12 6.477 2 12 2s10 4.477 10 10m-1.8 0a8.2 8.2 0 1 0-16.4 0 8.2 8.2 0 0 0 16.4 0"></path><path d="M17.069 8.865a.9.9 0 0 1 .05 1.271l-4.807 5.21a1.9 1.9 0 0 1-2.785.007l-2.619-2.811a.9.9 0 1 1 1.316-1.229l2.619 2.812a.1.1 0 0 0 .146 0l4.808-5.21a.9.9 0 0 1 1.272-.05"></path></g></symbol><symbol id="thumbUp" viewBox="0 0 24 24"><path fill="currentColor" d="m11.319 5.135-.002.018q0 .014-.002.039l-.002.06c-.016.436-.134 1.727-1.04 2.858C9.264 9.373 8.25 9.721 7.38 9.983c-.307.092-.542.389-.542.813v7.537a1.1 1.1 0 0 0 1.1 1.1H17.1a2.1 2.1 0 0 0 2.007-1.484l1.499-4.877a2.1 2.1 0 0 0-2.008-2.717h-5.62l.275-1.116c.309-1.251.526-2.45.318-3.944l-.012-.088-.007-.05a1.04 1.04 0 0 0-.225-.487c-.129-.15-.403-.37-1.06-.37-.413 0-.6.153-.713.296-.143.18-.21.408-.235.539m-1.175-1.657c.43-.543 1.122-.978 2.123-.978 1.144 0 1.93.422 2.425.997a2.84 2.84 0 0 1 .662 1.55c.186 1.334.088 2.472-.107 3.508h3.351c2.624 0 4.499 2.538 3.728 5.045l-1.498 4.878a3.9 3.9 0 0 1-3.728 2.755H7.938a2.9 2.9 0 0 1-2.9-2.9v-7.537c0-1.113.66-2.187 1.824-2.537.727-.219 1.329-.428 2.006-1.274.55-.686.636-1.512.646-1.797l.001-.02c.002-.07.007-.22.036-.37.05-.262.192-.816.593-1.32M2.898 8.555a.9.9 0 0 1 .9.9v10.793a.9.9 0 1 1-1.8 0V9.455a.9.9 0 0 1 .9-.9"></path></symbol><symbol id="vector-left" viewBox="0 0 6 24"><path fill="currentColor" fill-rule="evenodd" d="M6 23.372V24v-1.895zM5.999 1.873V.011v.617q0 .622 0 1.245" clip-rule="evenodd"></path><path fill="currentColor" d="M5.994 21.377c-.008-.837-.02-1.774-.297-2.588-.3-.88-.825-1.463-1.442-2.049-.444-.421-1.392-1.25-1.85-1.654-.374-.33-1.116-.977-1.474-1.33C.48 13.312 0 12.763 0 12s.48-1.312.93-1.756c.359-.353 1.1-1 1.475-1.33.458-.403 1.405-1.232 1.85-1.654.617-.587 1.141-1.169 1.441-2.048.277-.815.29-1.752.298-2.589l.005-.75v20.232q0-.365-.005-.728"></path></symbol><symbol id="delete" viewBox="0 0 20 20"><path d="M8.125 2.5h3.75a.625.625 0 1 1 0 1.25h-3.75a.625.625 0 1 1 0-1.25M8.125 7.5a.625.625 0 0 0-.625.625v6.25a.625.625 0 1 0 1.25 0v-6.25a.625.625 0 0 0-.625-.625M11.25 8.125a.625.625 0 1 1 1.25 0v6.25a.625.625 0 1 1-1.25 0z"></path><path d="M16.875 5a.625.625 0 1 1 0 1.25h-1.042v7.917A3.333 3.333 0 0 1 12.5 17.5h-5a3.333 3.333 0 0 1-3.333-3.333V6.25H3.125a.625.625 0 1 1 0-1.25zM5.417 6.25v7.917c0 1.15.932 2.083 2.083 2.083h5c1.15 0 2.083-.933 2.083-2.083V6.25z"></path></symbol><symbol id="login_checked" viewBox="0 0 16 16"><path d="m15.05 3.79-9.188 9.188L.95 8.066l1.273-1.273 3.64 3.64 7.914-7.915z"></path></symbol><symbol id="arrow_left" viewBox="0 0 20 20"><path fill="currentColor" d="M12.27 2.705a.783.783 0 0 1 .034 1.072L6.84 9.867a.2.2 0 0 0 0 .267l5.463 6.089a.783.783 0 0 1-.033 1.072.704.704 0 0 1-1.026-.035L5.196 10.52a.783.783 0 0 1 0-1.038l6.049-6.741a.704.704 0 0 1 1.026-.035"></path></symbol><symbol id="me" viewBox="0 0 25 24"><path fill="currentColor" d="M15.95 7.5a3.7 3.7 0 1 1-7.4 0 3.7 3.7 0 0 1 7.4 0m1.8 0a5.5 5.5 0 1 0-11 0 5.5 5.5 0 0 0 11 0M2.25 21.005c0-3.4 2.756-6.155 6.155-6.155h7.69c3.4 0 6.155 2.755 6.155 6.155v.093a.9.9 0 0 1-1.8 0v-.093a4.355 4.355 0 0 0-4.355-4.355h-7.69a4.355 4.355 0 0 0-4.355 4.355v.093a.9.9 0 1 1-1.8 0v-.093"></path></symbol><symbol id="famous" viewBox="0 0 24 24"><path fill="#FF2442" fill-rule="evenodd" d="M12 22c5.523 0 10-4.477 10-10S17.523 2 12 2 2 6.477 2 12s4.477 10 10 10" clip-rule="evenodd"></path><path fill="#fff" d="M17.244 9.526a.894.894 0 0 0-.02-1.273.915.915 0 0 0-1.286.021l-5.415 5.543-1.972-1.953a.915.915 0 0 0-1.285 0 .894.894 0 0 0 0 1.272l2.625 2.6a.913.913 0 0 0 1.296-.01z"></path></symbol><symbol id="close" viewBox="0 0 24 24"><path d="M19.23 4.772a.92.92 0 0 1 0 1.301l-5.928 5.928 5.926 5.925a.92.92 0 0 1-1.302 1.302l-5.925-5.926-5.928 5.929a.92.92 0 0 1-1.214.076l-.087-.076a.92.92 0 0 1 0-1.302l5.928-5.928-5.93-5.93a.92.92 0 0 1 1.3-1.301l5.931 5.93 5.928-5.928a.92.92 0 0 1 1.215-.077z"></path></symbol><symbol id="plus" viewBox="0 0 16 16"><path d="M8.003 1.851c.339 0 .613.275.613.614v4.922h4.92a.613.613 0 1 1 0 1.227h-4.92v4.922c0 .313-.234.57-.536.609l-.077.005a.613.613 0 0 1-.613-.614V8.614H2.464a.613.613 0 1 1 0-1.227h4.924V2.465c0-.313.235-.571.537-.61z"></path></symbol><symbol id="transshipment" viewBox="0 0 16 16"><path d="M7.999 2.546a5.455 5.455 0 0 0-3.924 9.243l.319-.318a.337.337 0 0 1 .574.238v1.544c0 .186-.15.336-.336.336H3.088c-.3 0-.45-.362-.238-.574l.368-.369a6.667 6.667 0 0 1 7.374-10.79.606.606 0 0 1-.472 1.117 5.4 5.4 0 0 0-2.121-.427M12.412 5.473l.27-.27a5.454 5.454 0 0 1-5.8 8.138.606.606 0 1 0-.247 1.186q.662.139 1.364.14A6.667 6.667 0 0 0 13.56 4.324l.395-.396a.337.337 0 0 0-.238-.574h-1.544a.337.337 0 0 0-.337.336v1.544c0 .3.363.45.575.239"></path></symbol><symbol id="switch_dot" viewBox="0 0 16 16"><circle cx="8" cy="8" r="8" fill="#fff"></circle></symbol><symbol id="add_b" viewBox="0 0 12 12"><path fill="currentColor" fill-opacity=".6" d="M5.55 10.546V6.45H1.455A.45.45 0 0 1 1 6c0-.248.204-.45.455-.45H5.55V1.455C5.55 1.204 5.751 1 6 1s.45.204.45.455V5.55h4.096c.25 0 .454.202.454.45 0 .249-.203.45-.454.45H6.45v4.096A.45.45 0 0 1 6 11a.45.45 0 0 1-.45-.454"></path></symbol><symbol id="setting" viewBox="0 0 24 24"><path d="M23.002 7a5 5 0 0 1-9.92.896l-.08.004h-11a.9.9 0 0 1 0-1.8h11l.08.004a5.002 5.002 0 0 1 9.92.896m-5 3.2a3.2 3.2 0 1 0 0-6.4 3.2 3.2 0 0 0 0 6.4M1.002 17a5 5 0 0 1 9.92-.896l.08-.004h11a.9.9 0 0 1 0 1.8h-11l-.08-.003A5.001 5.001 0 0 1 1.002 17m5 3.2a3.2 3.2 0 1 0 0-6.4 3.2 3.2 0 0 0 0 6.4"></path></symbol><symbol id="user_avatar_skeleton" viewBox="0 0 151 150"><g clip-path="url(#a)"><path d="M.5 0h150v150H.5z"></path></g></symbol><symbol id="phone" viewBox="0 0 14 22"><path fill="currentColor" d="M3 .5a3 3 0 0 0-3 3v15a3 3 0 0 0 3 3h8a3 3 0 0 0 3-3v-15a3 3 0 0 0-3-3zM10 2h1a1.5 1.5 0 0 1 1.5 1.5v15A1.5 1.5 0 0 1 11 20H3a1.5 1.5 0 0 1-1.5-1.5v-15A1.5 1.5 0 0 1 3 2h1a2 2 0 0 0 2 2h2a2 2 0 0 0 2-2"></path></symbol><symbol id="close_b" viewBox="0 0 20 20"><path fill="#fff" d="M16.025 3.977c.3.299.3.784 0 1.084L11.085 10l4.938 4.938a.767.767 0 0 1-1.084 1.084L10 11.085l-4.94 4.94a.77.77 0 0 1-1.012.064l-.072-.064c-.3-.299-.3-.784 0-1.084l4.94-4.94-4.942-4.942a.767.767 0 1 1 1.084-1.084l4.942 4.941 4.94-4.94a.77.77 0 0 1 1.012-.063z"></path></symbol><symbol id="light_mode" viewBox="0 0 24 24"><g clip-path="url(#a)"><path d="M11.998 16.2a4.2 4.2 0 1 1 0-8.4 4.2 4.2 0 0 1 0 8.4m0 1.8a6 6 0 1 0 0-12 6 6 0 0 0 0 12M11.998.1a.9.9 0 0 1 .9.9v2a.9.9 0 0 1-1.8 0V1a.9.9 0 0 1 .9-.9M3.583 3.585a.9.9 0 0 1 1.273 0L6.27 4.999a.9.9 0 0 1-1.273 1.273L3.583 4.858a.9.9 0 0 1 0-1.273m16.83 0a.9.9 0 0 1 0 1.273l-1.415 1.414A.9.9 0 0 1 17.725 5l1.414-1.414a.9.9 0 0 1 1.273 0M.097 12a.9.9 0 0 1 .9-.9h2a.9.9 0 0 1 0 1.8h-2a.9.9 0 0 1-.9-.9m20 0a.9.9 0 0 1 .9-.9h2a.9.9 0 0 1 0 1.8h-2a.9.9 0 0 1-.9-.9M6.27 17.727a.9.9 0 0 1 0 1.273l-1.414 1.414a.9.9 0 1 1-1.273-1.273l1.414-1.414a.9.9 0 0 1 1.273 0m11.455 0a.9.9 0 0 1 1.273 0l1.414 1.414a.9.9 0 1 1-1.273 1.273L17.725 19a.9.9 0 0 1 0-1.273M11.998 20.1a.9.9 0 0 1 .9.9v2a.9.9 0 0 1-1.8 0v-2a.9.9 0 0 1 .9-.9"></path></g></symbol><symbol id="home" viewBox="0 0 24 24"><path fill="currentColor" d="M20.768 7.934a4 4 0 0 0-1.825-2.153l-5-2.778-.055-.03a4 4 0 0 0-3.83.03l-5 2.778A4 4 0 0 0 3 9.278v7.646q0 .1.005.2A4 4 0 0 0 7 20.924h10q.1 0 .2-.005a4 4 0 0 0 3.8-3.995V9.243a4 4 0 0 0-.232-1.309m-9.776-3.452a2 2 0 0 1 2.016 0l5.2 3.033a2 2 0 0 1 .992 1.728v7.881a2 2 0 0 1-2 2H6.8a2 2 0 0 1-2-2V9.243a2 2 0 0 1 .992-1.728z"></path><path fill="currentColor" fill-rule="evenodd" d="M9.72 14.883h-.001l-.002-.003-.003-.003-.004-.006-.007-.008-.001-.002.001.002z" clip-rule="evenodd"></path><path fill="currentColor" d="m9.703 14.863-.001-.002zl.047.045a1.7 1.7 0 0 0 .33.222c.33.176.934.394 1.92.394s1.59-.218 1.92-.394a1.7 1.7 0 0 0 .377-.268.9.9 0 0 1 1.423 1.102l-.035.044-.056.065q-.067.076-.183.18a3.5 3.5 0 0 1-.679.465c-.606.324-1.503.606-2.767.606s-2.16-.282-2.767-.606c-.301-.16-.523-.327-.679-.465a2.5 2.5 0 0 1-.24-.245l-.034-.044a.9.9 0 0 1 1.423-1.101m.016.02-.002-.003-.003-.003-.004-.006-.007-.008z"></path></symbol><symbol id="ic_share" viewBox="0 0 20 20"><path fill="currentColor" d="M5.787 4.017a1.77 1.77 0 0 0-1.77 1.77v8.427c0 .977.792 1.77 1.77 1.77h8.427a1.77 1.77 0 0 0 1.77-1.77v-1.265a.758.758 0 0 1 1.516 0v1.265a3.286 3.286 0 0 1-3.286 3.286H5.787A3.286 3.286 0 0 1 2.5 14.214V5.787A3.287 3.287 0 0 1 5.787 2.5H7.05a.758.758 0 1 1 0 1.517zm9.124 0-6.29 6.29a.758.758 0 0 0 1.073 1.072l6.29-6.29v3.647a.758.758 0 0 0 1.516 0V3.258a.76.76 0 0 0-.758-.758h-5.478a.758.758 0 0 0 0 1.517z"></path></symbol><symbol id="imgNoteSelect" viewBox="0 0 20 20"><g fill="currentColor"><path d="M7.917 6.875a1.042 1.042 0 1 0-2.084 0 1.042 1.042 0 0 0 2.084 0"></path><path fill-rule="evenodd" d="M2.5 7.833c0-1.867 0-2.8.363-3.513.32-.627.83-1.137 1.457-1.457C5.033 2.5 5.966 2.5 7.833 2.5h4.334c1.867 0 2.8 0 3.513.363.627.32 1.137.83 1.457 1.457.363.713.363 1.646.363 3.513v4.334l-.001.726h-1.5l-2.666-2.666L9.28 14.28a.75.75 0 0 1-1.06 0l-1.553-1.553-2.397 2.397c.176.288.429.522.731.676.11.056.302.122.765.16.48.039 1.11.04 2.067.04h1.334v1.5H7.833c-1.867 0-2.8 0-3.513-.363a3.33 3.33 0 0 1-1.457-1.457c-.363-.713-.363-1.646-.363-3.513zM12.167 4H7.833c-.958 0-1.586.001-2.067.04-.463.038-.655.104-.765.16A1.83 1.83 0 0 0 4.2 5c-.056.11-.122.302-.16.765-.039.48-.04 1.11-.04 2.067v4.334c0 .427 0 .79.004 1.102l2.132-2.133a.75.75 0 0 1 1.061 0L8.75 12.69l4.053-4.053a.75.75 0 0 1 1.06 0L16 10.773v-2.94c0-.958-.001-1.586-.04-2.067-.038-.463-.104-.655-.16-.765A1.83 1.83 0 0 0 15 4.2c-.11-.056-.302-.122-.765-.16-.48-.039-1.11-.04-2.067-.04" clip-rule="evenodd"></path></g><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="m12.203 16.613 1.69 1.69a1.04 1.04 0 0 0 1.473 0l3.848-3.847"></path></symbol><symbol id="chat" viewBox="0 0 24 24"><path fill="currentColor" fill-rule="evenodd" d="m3.925 17.006 1.528-.95c.308.496.389 1.11.199 1.681L5.09 19.42l.237-.044c.44-.08.903-.162 1.299-.223.337-.053.784-.118 1.098-.118.459 0 .968.138 1.255.216l.077.02c.7.187 1.61.429 2.943.429 4.234 0 7.7-3.45 7.7-7.7a7.7 7.7 0 1 0-14.247 4.056zM2.917 20.25a.95.95 0 0 0 .882 1.25q.018 0 .036-.003c.252-.051 3.3-.662 3.89-.662.208 0 .492.076.868.176.739.197 1.833.489 3.407.489 5.225 0 9.5-4.253 9.5-9.5a9.5 9.5 0 1 0-17.576 5.006c.03.049.038.108.02.162z" clip-rule="evenodd"></path></symbol><symbol id="skeleton_l" viewBox="0 0 200 320"><rect width="200" height="266" rx="16"></rect><rect width="192" height="16" x="4" y="274" rx="8"></rect><rect width="128" height="16" x="4" y="296" opacity=".5" rx="8"></rect></symbol><symbol id="xhs" viewBox="0 0 20 20"><g clip-path="url(#a)"><path fill="#FF2442" d="M13.969 17H6.03A3.03 3.03 0 0 1 3 13.97V6.032A3.03 3.03 0 0 1 6.031 3h7.938A3.03 3.03 0 0 1 17 6.032v7.937A3.03 3.03 0 0 1 13.969 17"></path><path fill="#fff" fill-rule="evenodd" d="M15.276 10.24a.6.6 0 0 0-.317-.44.8.8 0 0 0-.388-.097h-.078c-.019 0-.019 0-.019-.02v-.465c0-.058 0-.116-.013-.174a.705.705 0 0 0-.362-.55.95.95 0 0 0-.44-.116h-.316c-.032 0-.032 0-.032-.026v-.22c0-.006 0-.013-.007-.013-.006-.006-.013 0-.013 0h-.685s-.006.007-.006.013v.239c0 .007-.007.007-.013.007h-.446c-.013 0-.013.006-.013.013v.653c0 .038 0 .038.039.038h.4c.04 0 .033.059.033.059v.51s0 .052-.026.052h-.653c-.032 0-.026.039-.026.039v.64s-.006.032.026.032h.64c.039 0 .032 0 .032.032v1.429c0 .038 0 .038.039.038h.633c.04 0 .04 0 .04-.038v-1.448c0-.013 0-.013.012-.013h1.028q.066-.002.123.026a.2.2 0 0 1 .122.18v.524c0 .117-.045.162-.142.162h-.536c-.013 0-.013 0-.013.013 0 .006.207.478.246.575v.006c0 .007.012.013.019.013h.226c.065 0 .226 0 .29-.006.06-.007.124-.013.182-.032a.6.6 0 0 0 .427-.582v-.88a1.4 1.4 0 0 0-.013-.174m-1.5-.55c0 .006-.006.013-.006.013h-.453c-.006 0-.006-.007-.013-.013v-.026l-.006-.55c0-.032 0-.032.032-.032h.323q.031-.002.052.007.07.021.071.09v.511m-1.842 1.519q-.001-.009-.013-.007h-.64c-.02 0-.02 0-.02-.019V9.108c0-.032 0-.032.033-.032h.381c.033 0 .033 0 .033-.032v-.64c0-.04 0-.033-.033-.033h-1.544c-.026 0-.033 0-.033.033v.64c0 .038 0 .032.033.032h.374c.033 0 .033 0 .033.032v2.049c0 .039 0 .039-.039.039h-.575c-.02 0-.026.013-.026.013l-.31.672-.007.013q-.001.008.026.006h2.308c.013 0 .013 0 .013-.013v-.659q.007-.01.006-.02M6.737 8.152h-.665a.014.014 0 0 0-.013.013c0 .168-.007 1.79-.007 2.61v.415c0 .129-.116.116-.123.116h-.323c-.02 0-.02 0-.02.02 0 .019.208.471.246.555q.008.011.026.013c.071 0 .336.006.414-.007a.6.6 0 0 0 .194-.058.58.58 0 0 0 .265-.336.7.7 0 0 0 .032-.239V9.73c0-.485 0-1.448-.006-1.57-.007 0-.013-.007-.02-.007m3.057 2.184h-.387c-.04 0-.065-.039-.052-.077l.517-1.164q.008-.011-.013-.013h-.582c-.045 0-.077-.051-.058-.09l.388-.866q.008-.012-.013-.013H8.91c-.006 0-.006 0-.013.006l-.407.918c-.039.084-.084.168-.116.252-.02.052-.046.104-.059.162a.2.2 0 0 0-.006.084c.006.07.039.13.103.168q.03.018.058.026a.4.4 0 0 0 .15.026h.258c.013 0-.259.588-.304.704a2 2 0 0 0-.065.168c-.006.026-.013.052-.006.078a.21.21 0 0 0 .103.174q.03.018.058.026a.4.4 0 0 0 .149.026h.731c.006 0 .006 0 .012-.006l.252-.57c0-.006-.006-.019-.013-.019m-1.7.407a.64.64 0 0 1-.058-.271c0-.045-.006-.084-.006-.13q-.011-.097-.013-.193c-.006-.071-.013-.142-.013-.213l-.02-.207a2 2 0 0 1-.012-.2 2 2 0 0 1-.013-.195q-.012-.106-.013-.213c0-.013 0-.032-.007-.039 0-.006-.025-.006-.032-.006h-.653c-.013 0-.013 0-.013.013.007.045.007.084.013.13.007.096.013.187.026.283l.02.22c.006.104.013.2.025.304.007.116.02.233.026.35.007.05.007.096.013.148q.018.167.065.323c.039.149.084.29.155.433q.066.147.162.265c.006.006.012.026.019.02 0 0 0-.007.006-.007.04-.084.33-.73.35-.776-.013-.02-.02-.013-.026-.039M5.568 9.077h-.685q-.008-.002-.006.006s0 .026-.007.033a2 2 0 0 0-.013.213q-.011.098-.013.194a2 2 0 0 0-.012.2l-.02.207c-.006.071-.013.142-.013.213a2 2 0 0 0-.013.194c-.006.046-.006.084-.006.13a.7.7 0 0 1-.058.271c-.013.026-.013.02 0 .052.019.039.303.672.349.769l.006.006c.007 0 .013-.013.02-.019.064-.084.116-.175.161-.265.065-.136.116-.284.155-.433.026-.11.045-.213.065-.323.006-.045.006-.097.013-.149.006-.116.02-.233.026-.349.006-.103.013-.2.026-.304l.019-.22a4 4 0 0 1 .026-.284c.006-.045.006-.084.013-.13-.02-.006-.02-.012-.033-.012m3.943 2.12h-.743a1 1 0 0 1-.336-.058q-.012-.001-.013.006l-.317.685q-.002.012.007.013a.6.6 0 0 0 .22.052H9.2c.006 0 .006 0 .013-.007l.31-.678q-.001-.012-.013-.013m5.08-2.12h.343q.039.002.078-.007a.357.357 0 0 0 .271-.42.35.35 0 0 0-.388-.271.354.354 0 0 0-.304.349v.343c-.006 0 0 .006 0 .006" clip-rule="evenodd"></path></g></symbol><symbol id="pause" viewBox="0 0 8 10"><path fill="currentColor" d="M1.167.333C.522.333 0 .856 0 1.5v7a1.167 1.167 0 0 0 2.333 0v-7c0-.644-.522-1.167-1.166-1.167M6.833.333C6.19.333 5.667.856 5.667 1.5v7A1.167 1.167 0 1 0 8 8.5v-7C8 .856 7.478.333 6.833.333"></path></symbol><symbol id="mention" viewBox="0 0 24 24"><path d="M15.853 8.977c.022-.364.044-.637.06-.791a.75.75 0 1 1 1.491.146c-.013.136-.034.39-.055.736-.066 1.1-.08 2.252-.008 3.322.148 2.218.65 3.48 1.256 3.48 1.197 0 1.898-1.896 1.898-3.87a8.001 8.001 0 1 0-3.994 6.928.75.75 0 1 1 .753 1.296 9.44 9.44 0 0 1-4.76 1.276 9.5 9.5 0 1 1 9.5-9.5c0 2.758-.965 5.37-3.397 5.37-1.37 0-2.13-1.077-2.504-2.907a4.356 4.356 0 0 1-7.949-2.459 4.356 4.356 0 0 1 7.695-2.793zm-.5 3.027a2.855 2.855 0 1 0-5.713.002 2.855 2.855 0 0 0 5.714-.001z"></path></symbol><symbol id="tab_btn_left" viewBox="0 0 20 20"><path d="M8.082 9.877a.17.17 0 0 0 0 .224l5.477 6.144a.76.76 0 0 1-.05 1.06.727.727 0 0 1-1.04-.05L6.44 10.492a.76.76 0 0 1 0-1.01l6.017-6.738a.727.727 0 0 1 1.04-.05.76.76 0 0 1 .049 1.06z"></path></symbol><symbol id="link_b" viewBox="0 0 20 20"><g fill="currentColor" fill-opacity=".8"><path d="M15.948 2.868a4.1 4.1 0 0 0-5.8 0L8.964 4.052a.753.753 0 0 0 1.066 1.065l1.183-1.184a2.595 2.595 0 0 1 3.67 0l1.184 1.184a2.595 2.595 0 0 1 0 3.67l-2.368 2.367a2.595 2.595 0 0 1-3.67 0l-.591-.592a.753.753 0 1 0-1.066 1.066l.592.591a4.1 4.1 0 0 0 5.8 0l2.368-2.367a4.1 4.1 0 0 0 0-5.8z"></path><path d="M4.052 17.132a4.1 4.1 0 0 0 5.8 0l1.361-1.361a.753.753 0 0 0-1.065-1.066l-1.361 1.362a2.595 2.595 0 0 1-3.67 0l-1.184-1.184a2.595 2.595 0 0 1 0-3.67l2.368-2.367a2.595 2.595 0 0 1 3.67 0l.591.592a.753.753 0 0 0 1.066-1.066l-.592-.592a4.1 4.1 0 0 0-5.8 0l-2.368 2.368a4.1 4.1 0 0 0 0 5.8z"></path></g></symbol><symbol id="imgNote" viewBox="0 0 20 20"><g fill="currentColor"><path d="M2.863 4.32C2.5 5.033 2.5 5.966 2.5 7.833v4.334c0 1.867 0 2.8.363 3.513.32.627.83 1.137 1.457 1.457.713.363 1.646.363 3.513.363h4.334c1.867 0 2.8 0 3.513-.363a3.33 3.33 0 0 0 1.457-1.457c.363-.713.363-1.646.363-3.513V7.833c0-1.867 0-2.8-.363-3.513a3.33 3.33 0 0 0-1.457-1.457c-.713-.363-1.646-.363-3.513-.363H7.833c-1.867 0-2.8 0-3.513.363-.627.32-1.137.83-1.457 1.457M5.001 15.8a1.83 1.83 0 0 1-.731-.676l2.397-2.397L8.22 14.28a.75.75 0 0 0 1.06 0l4.053-4.053L16 12.893c-.003.57-.011.994-.04 1.34-.037.464-.103.656-.159.766A1.83 1.83 0 0 1 15 15.8c-.11.056-.302.122-.765.16-.48.039-1.11.04-2.067.04H7.833c-.958 0-1.586-.001-2.067-.04-.463-.038-.655-.104-.765-.16M7.833 4h4.334c.958 0 1.586.001 2.067.04.463.038.655.104.765.16.345.176.625.456.801.801.056.11.122.302.16.765.039.48.04 1.11.04 2.067v2.94l-2.136-2.137a.75.75 0 0 0-1.061 0L8.75 12.69l-1.553-1.553a.75.75 0 0 0-1.06 0L4.003 13.27A97 97 0 0 1 4 12.167V7.833c0-.958.001-1.586.04-2.067.038-.463.104-.655.16-.765.176-.345.456-.625.801-.801.11-.056.302-.122.765-.16.48-.039 1.11-.04 2.067-.04"></path><path fill-opacity=".8" d="M7.917 6.875a1.042 1.042 0 1 0-2.084 0 1.042 1.042 0 0 0 2.084 0"></path></g></symbol><symbol id="collect" viewBox="0 0 24 24"><path fill="currentColor" d="M18.865 19.503a1.81 1.81 0 0 1-.737 1.649 1.82 1.82 0 0 1-1.8.196L12.2 19.546a.5.5 0 0 0-.4 0l-4.127 1.802a1.82 1.82 0 0 1-1.801-.196 1.81 1.81 0 0 1-.737-1.65l.452-4.384a.5.5 0 0 0-.127-.386l-2.994-3.32a1.81 1.81 0 0 1-.377-1.77c.2-.615.713-1.077 1.347-1.213l4.404-.945a.5.5 0 0 0 .326-.235l2.265-3.853a1.82 1.82 0 0 1 3.138 0l2.265 3.853a.5.5 0 0 0 .326.235l4.404.945a1.808 1.808 0 0 1 .97 2.984l-2.994 3.319a.5.5 0 0 0-.127.386zm-1.662-5.977 2.994-3.32q.004-.004.003-.007-.001-.006-.013-.01l-4.404-.945a2.3 2.3 0 0 1-1.5-1.083l-2.266-3.853Q12.014 4.302 12 4.3q-.015.002-.017.008L9.718 8.161a2.3 2.3 0 0 1-1.5 1.083l-4.405.945q-.012.004-.013.01 0 .003.003.008l2.994 3.32a2.3 2.3 0 0 1 .58 1.776l-.452 4.384q-.001.001.005.01l.01.003h.002q.006 0 .01-.002l4.128-1.801a2.3 2.3 0 0 1 1.84 0l4.127 1.801.012.002.01-.004q.008-.008.006-.009l-.452-4.384a2.3 2.3 0 0 1 .58-1.777"></path></symbol><symbol id="user_info_skeleton" viewBox="0 0 461 152"><rect width="112" height="24" rx="12"></rect><rect width="160" height="16" y="36" rx="8"></rect><rect width="280" height="16" y="68" rx="8"></rect><rect width="120" height="16" y="100" rx="8"></rect><rect width="64" height="16" y="136" rx="8"></rect><rect width="64" height="16" x="80" y="136" rx="8"></rect><rect width="64" height="16" x="160" y="136" rx="8"></rect></symbol><symbol id="ic_qq" viewBox="0 0 20 20"><path fill="currentColor" d="M5.142 17.2a.57.57 0 0 1-.22-.443c0-.471.461-.799.924-1.009a4.1 4.1 0 0 1-.835-1.428c-.374.437-.745.707-1.012.707-.417 0-.666-.435-.666-1.165 0-1.255.699-3.064 1.284-4.36.203-.447.305-.915.305-1.39C4.922 3.969 7.658 2.5 10 2.5s5.077 1.47 5.077 5.61c0 .478.102.945.305 1.392.586 1.296 1.285 3.104 1.285 4.36 0 .73-.25 1.165-.667 1.165-.267 0-.638-.27-1.012-.706a4.05 4.05 0 0 1-.836 1.428c.463.209.925.536.925 1.008a.57.57 0 0 1-.22.442c-.76.627-4.478.069-4.515.063a2.2 2.2 0 0 0-.679 0c-.024.004-1.557.238-2.86.238-.727 0-1.383-.073-1.661-.3"></path></symbol><symbol id="back" viewBox="0 0 20 20"><path fill="currentColor" d="M8.082 9.877a.17.17 0 0 0 0 .224l5.477 6.144a.76.76 0 0 1-.05 1.06.727.727 0 0 1-1.04-.05L6.44 10.492a.76.76 0 0 1 0-1.01l6.017-6.738a.727.727 0 0 1 1.04-.05.76.76 0 0 1 .049 1.06z"></path></symbol><symbol id="hotspot" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M6.275 15.5s-1.612-3.711 1.271-6.213L8.801 15.5c5.45 0 7.104-7.5 3.864-11.24 0 0-.903 1.11-2.042 2.229 0 0 .783-4.347-3.214-5.989 0 0-.742 3.011-3.29 5.23C.142 9.197 1.16 15.5 6.276 15.5" clip-rule="evenodd"></path></symbol><symbol id="weibo_f" viewBox="0 0 20 20"><path fill="currentColor" fill-opacity=".8" d="M11.449 6.194c1.944-.817 3.642-.865 4.262.024.33.474.299 1.138-.006 1.908-.14.354.043.41.313.49 1.095.341 2.315 1.166 2.315 2.618 0 2.405-3.457 5.433-8.652 5.433-3.963 0-8.014-1.927-8.014-5.096 0-1.657 1.046-3.573 2.848-5.381 2.406-2.413 5.212-3.513 6.268-2.453.465.466.51 1.275.211 2.24-.156.485.455.216.455.217m-2.5 1.794c-3.162.314-5.56 2.257-5.355 4.339s2.936 3.518 6.098 3.204 5.56-2.256 5.355-4.34c-.206-2.082-2.935-3.516-6.098-3.203m-1.302 6.648c-1.52-.492-2.165-1.998-1.499-3.355.654-1.33 2.355-2.082 3.86-1.69 1.557.404 2.352 1.879 1.715 3.31-.645 1.465-2.501 2.245-4.076 1.735m.858-2.851c-.49-.206-1.123.005-1.425.481-.306.477-.162 1.047.325 1.268.493.226 1.148.012 1.454-.478.3-.495.142-1.06-.354-1.271"></path></symbol><symbol id="nioPlay" viewBox="0 0 18 18"><path fill="#fff" d="m6.05 2.588 8.587 5.07a1.562 1.562 0 0 1 0 2.686L6.05 15.412a1.55 1.55 0 0 1-2.127-.554 1.56 1.56 0 0 1-.214-.79V3.932a1.556 1.556 0 0 1 2.34-1.344"></path></symbol><symbol id="agreed" viewBox="0 0 16 16"><path fill="currentColor" fill-rule="evenodd" d="M8 14.667A6.667 6.667 0 1 0 8 1.333a6.667 6.667 0 0 0 0 13.334" clip-rule="evenodd"></path><path fill="#fff" d="M11.497 6.35a.596.596 0 0 0-.014-.848.61.61 0 0 0-.857.014l-3.61 3.695L5.7 7.91a.61.61 0 0 0-.857 0 .596.596 0 0 0 0 .849l1.75 1.733a.61.61 0 0 0 .864-.007z"></path></symbol><symbol id="check_mark" viewBox="0 0 16 16"><path d="M14.958 3.623a.6.6 0 0 1 0 .849l-8.485 8.485a.6.6 0 0 1-.849 0L.91 8.243a.6.6 0 0 1 .849-.849l4.29 4.29 8.06-8.061a.6.6 0 0 1 .849 0"></path></symbol></svg></div><div id="app"><!--[--><!--[--><!--[--><!--[--><!--[--><!----><!----><div id="global" data-logged="1" class="layout limit" style="--40bdee49:1728px;" data-v-34b87540=""><div class="header-container" data-v-34b87540="" style="--67f219a2:1728px;" data-v-5c1b2170=""><header class="mask-paper" data-v-5c1b2170=""><a href="/explore?channel_type=web_user_page" class="" id="link-guide" style="display:flex;" data-v-5c1b2170=""><img crossorigin="anonymous" class="header-logo" style="pointer-events:none;" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAM0AAABgCAYAAAC+PvZZAAAACXBIWXMAACE4AAAhOAFFljFgAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAA0KSURBVHgB7Z1LbFTXGce/cz1UlRKc6SqRghRLmAq6Cd0EKa2UwZC2uwRYFhV7SwWEVApSUxW7UqTSRXlYTdVsakdtd7y6ahMeU6lZkE1gA6iA4kog0Z1rg1SBZ07P/94Zezy+j+8+z70z3w+ZGY+vZ65n7v98z3OOohKjtzfGqOU0SFOdFL1OWplbvdP7IY2RUF0ULZjPc9Hc63zpW+b7m+Q4C+re5zepxCgqEXp8b4OobUSh3jHfQRx1EoYU1TRfEM9ldf9Kk0qEddF4QiEjkvYkiUgEfxZdESl9Wd27NkeWsSIaPfZunWpLx8zd90iEIsRjkZS6RCObZtTdvy2QBQoVjWdV9Enz1SBBSI1rfeaLtj6FiEbEIuQKkgpEM0WJJ1fRuG7YpuXTpPUkCULuGMtT2zSVt9uWm2j0tj3HjFimSWIWoXimaWX0rFq4tEg5kLlo9PYfjdHK8z+KKyZYxXXZRvblUfNxKENc67Ly7CsRjGAdFL916ys9PnGSMiYzS2NO7jR5KWRBKBnZxjqpRdNxxy52KviCUE7gro18Y3cWwkklGlcwrWfXpQ9MqAimMDqyO22ckzimEcEIFaTuxjnf3nOIUpDI0ohghMrjqEn1r6vzlIDYohHBCAODVvvUg6uXKCaxRCOCEQaMRDEOO6ZxW2JEMMJgUSdqXXSNQQz4iYDa0kkRjDBw4Jo2JRPXKDBhiaZTVZXCpTCgmBpj7Qm7cyAypvGKl8++JkEYfI6r+9fORB0UbWkQxwjCcHCSE9+EisZ1yySOEYaHutehH06ge1Ypt2z0RaIdW6OPu3GLCuXDnxLt/V74MXfuEx3+JZWWyQNEhw6EH/PoMdHB92lgiKjf1AJ/ceXZaaoKEMyffht93LY9VBhbXjEX3P7o42YTFaWLY/ML5m95OfwYpWmgcPRpk01rBk1i83XP9LaJSXPzLgnJ2ffD6GMemhH6wt9JKBkISWpLgdniIEuT+cSdoePAD6KPmf00/OdvG9du84uUKXceeC5hP/uNyF/1sSi7GDM+cI77AwYJuG54zaUnxGa083ywco/+Q/TlLW+AKZZjxtqc8bM2G0TjWhkJ/tPhXoCvRB8XFWP9/LDn5mXJuflg0ex6nRKBi/zUB+HHfP4F0ZUvoi0rYqgPD69/DII7ZwaY+fNUIPWOtZnu/8FG90yrVG3TguHoT6KPwcXzqPDR0x6wmhBW88/BA4GfYABE+YvDyUWdnGN+nQLrRNNZn6xBQnK4VubcpzSU4L25/Af/bGdU4uRI4eM5rM1k/4PrLY3SYmXSsp+RABg2K9MPLAeynb0WB1YkarDBMaMZx3iRYDH+9ayKRo816rKoX0rwoXJcCMmYeRf/rz+g8qMbnUX6V1mzNJuc6qaYCx99AuBYmRs3iy+ylhXuINMFGbQ4Wbis0HqdNtZEU+UEwOYSiAauBss1+4yEHqK6DXqZtRQH9oUtrmhc10wSAOk4wsiYSTFzI1xLg84Je+9dvddF8+o0IyMNlEGtEtWqAZae5mOe074218oAZI2Wn/BeJyhZwKnd4Dn8znf5qf/xbu3G5xpAcB71ekGvxTlPuNY4Dud1w2fWMd4DWGfrLm27Yf5r4l6nuFkCK3P5k+jY5MSpfNwbTmMlRrkTv/H/GcfKAFwcf/0k/JjGj9cuwIM/8z/m3lWKBIXEoPP146OP/R/H33b0ULLXghXh9ASC2/eD/95SoN7q3vNiGrX2gDU4wfzSU8oFjvUKipsghCjBccFIO0ipaK51KENMGonJonUKnU4nnrG7pCw3+7WcU+aE09c0+oL/429kWDuYu0BDSdB7WzZqT1ydOFSr2V+DmTvS5GVpOGIM8s+PMl2zKCBcuDlCiWl3RNO5YxVOIA7ycl2SivE747yWGQ6zQ9pWUyUUuak+p1IdzXkVtjiWxk8c2xmzRTlIKroaaP0t3DgmCfAa2eZVZgo1LzBng0N/7HL3AWVC1a3Mq0xPoeoo5VoapJzt74nJCQSXcxTNf5nPDdH0ihdpUhTd0nTf4vls1SDw90S995xaC2LSLSmEA9Hh9x8yBy9bdLyyGik9ZruuyUoEPCxBKtbvPNHif/6zzizLvgsQ80OiMmsI/m2lmT/+VTZzVBDbXf8LJebUibX7eC9uP/Dc1RImRpB2rhnBlMDSWM7Tcy9ajIh+sx7x+3N9swpxMR5lWKBhnVcTBFx1fGEQwvuK96dM8d43F+soblZDNI9yNt1pajV+yLya9EA8mO15pFy9xJnu7pwY24kALtx6ErcXbViLmXFBLSxON3SetKheDtFwyFs0HEvGdSM5vWhomfFz9QR/IJwyzJvStZKIhpOyzNuN4Tw/50ODlWHN3pR5NbHAe3+Isfhi3tRWFiCaRbKNzWbNOHDO8w3GXHcpZiZjl/3mFWCKmxURzXLO7hknEcCJaTi9aHOFrt81OBS/hNNG/ldfNClntWh1Atqo5WbNOES5kdzlm6YOeLWNfiCmOxl1GQwqcH8t1uyw4qYpbrZvGeHYs3vcFSRzj2kYiYCXIgQ+yfS5Iaz9fX/3w8fF12ywW0FUGn3v9/0X8OsFSZqkOx90YxWu64WBy5ZoFC3gpkZtY2lib4yeIZuZtY+8s2fLKSaiAbgOO8YpMVivuOiaTdA05f5jolhO2QqEJWuxgmZZ0spBaLWAG8f8i7UddOZw3LPbBaRmbzPcIrdXK+B8uWsEBDHsnQFVyCZqckcGkz0bsSsazlThRwU08nFH+aDNo3akmCYgnQH8plmbKL2AG4eeP18gm3AyIkUVATmvE2RR0sxzl/6ziuC4BsZRC02TPVP2rA0ncfdlQa3zafzy+YQtMYO2mMYAo+5faeLW6wjQ+h9kC86eI0XNN+GIM8gqIF2MZYziWkWZ5lwRVLN7r7b2gD5GNkAAiC7WoAD7RoFGEOJEtijsXMKsAmITqfQPKGuGxbM0rVaTbLXT4CINq5AXmVXBuYQVF6VfbIhxmqv38J/1uAbxQFA9oOipwEGWIqxfrCy7Fgj5YIqa3XgG9Oy5qS+b/xpkAwgGF+RkX3HLRioWU2z9XLSg2APZNEyUgrgRz8QpwsKq9U/pRYF075uUGjxP1BQFv9e3xUulHniavd+siWalPUc1B7s625nJiQlZ/aLhNjZm2cjXdRd7pyqHWZlu60zcvVbAwfc3Pvb7mWzWUkPdKKp2hE1rixANZwGPIxktupgH2pnv/XZVNHDR9NaJeWOK7CQEYFEwWncvPFyk/fEFRvX+qa/4MLJ2j+YvrF8U42KAYNK0zjx8vNH15DZ8VpE0C2/YBK7ZvTXXDPTtuelcIpvM9gjaL7WLUXHLy+u/uIKJ04rTn5w4H5AASDN33c/dS9uKU1ayXKaq+C7wmf4H1onGC3bW8tGFgzcWXxCPXyzTjX2SEHdhP1ibrlvmdy7cGZp++Ll7Sdy7KjE7T6lByr/ItSJcK3Ntrv/hms+RM1b3q0GBMKoWkmREjruIBT6csP1S0vjgw2RlunQHxDQDQ9Epf02+St+wRoB1axOVLeu++XFw46ME/Ws4lyArk/Qi97MyaZ6vSlz5JyUG7nKRhWPMnamZ5JgPAQtrqBkqM3FMfR6Tu9JYGb+kQpkzR1kCS5HEvYJYgnZqywtjZdTd5oLfj3xFY93aRAFLw5m9Bx8YLlaWtZ60VqE/qTAsVgZEdX/4Hf/R7+Jtg5gFbjHz2nTQj2uBv1hrTdGK8zWVFcQFfiM0ZhHCFctrc1OIFR/i22/Gnw7gNzsT84luWGrG4MxTcmdlRpxfnEEJCZawuAavh4XQkSlFpszOIpGhnlboRGc9PjFtbk6SIAwLiuZMxmwq7JDwxQJX2me6iwkIwsCDa32kHRnPh4rGa+Rs7yNBGA5mgoL/XiKXpVX3mnBoj5MgDDJanfUrZPrBWsvZZBKMm6YyKOkKQgmBW9ZqTXMP5y+A/rz1ntU5N4KQB14cs9sLRXiwReM+aa21TxIDwgDhxuycOKaXWFttuE9uVCnCEQYCraY6MXssYu9PI8IRBgJFU+rB1URTYRKv4qy3N8ao5VzvbhMtCJUBgmFmyvx/PQUiHKFiLJIyQX8Cl6yXVNsHrrpqklUTyo7X6v/dtILxnioj9NaJM9bWFxCEUFQTDchxs2SBz0YZoscnTC2H7K1oIwgbmQlr809C5ts5SZwjlAK4Y9qZ6l3kL7unzgnX6sBdE/EIRaPVWbTFxKnyxyHXjQM9q6OmzR+RYq0jQeBiYhfVOp5FsB/6KlQAIh4hXzA1X83k4Yr5vhoViIhHyJZixbL6qmSBVfGQektiHiEmi+56ZMq5VLRYutjcDN1Fj+9tGD90UgQkhICAvmk8lHnspZRXgM/Fumh6cQVE7Z3mtN4x35lbqfcMKd5+SVrfctcXX1m5aVsovZRKNP3obY2d1B4ZI2UEpOg1M9KMEYSkdF2sUsXpdslrteBuNa7p395j7Zt5Z7/S8n8dgsfPv/PfFwAAAABJRU5ErkJggg==" data-v-5c1b2170=""></a><!--[--><div class="input-box" data-v-721de8bd=""><input id="search-input" value="" type="text" spellcheck="false" class="search-input" placeholder="搜索小红书" autocomplete="off" data-v-721de8bd=""><!----><div class="input-button" data-v-721de8bd=""><!----><div class="search-icon" data-v-721de8bd=""><svg class="reds-icon" width="20" height="20" data-v-721de8bd="" data-v-55b36ac6=""><use xlink:href="#search" data-v-55b36ac6=""></use></svg></div></div><!----></div><button class="reds-button-new min-width-search-icon large primary has-icon pure-icon min-width-search-icon" style="" data-v-721de8bd=""><span class="reds-button-new-box"><svg class="reds-icon reds-button__icon" width="16px" height="16px" data-v-55b36ac6=""><use xlink:href="#search" data-v-55b36ac6=""></use></svg><!--[--><!--]--><!----></span></button><!----><!--]--><div class="right" data-v-5c1b2170=""><div class="menu" data-v-5c1b2170="" data-v-d957886a=""><!----><div class="dropdown-nav" data-v-d957886a=""><!--[--><div data-v-d957886a="" data-v-1b03e45c=""><button class="reds-button-new channel-btn large text channel-btn" style="" data-v-d957886a=""><span class="reds-button-new-box"><!----><!--[--><!--]--><span class="reds-button-new-text"><!--[-->创作中心<!--]--></span></span></button></div><div data-v-d957886a="" data-v-1b03e45c=""><button class="reds-button-new channel-btn large text channel-btn" style="" data-v-d957886a=""><span class="reds-button-new-box"><!----><!--[--><!--]--><span class="reds-button-new-text"><!--[-->业务合作<!--]--></span></span></button></div><!--]--></div><div id="small-more-info" class="menu-icon-dropdown-nav" data-v-d957886a=""><div class="menu-icon-btn" data-v-d957886a=""><button class="reds-button-new large primary has-icon pure-icon" style="" data-v-d957886a=""><span class="reds-button-new-box"><svg class="reds-icon reds-button__icon" width="16px" height="16px" data-v-55b36ac6=""><use xlink:href="#menu" data-v-55b36ac6=""></use></svg><!--[--><!--]--><!----></span></button></div><!----></div></div></div></header></div><div class="main-container" data-v-34b87540=""><div class="side-bar" data-v-34b87540="" data-v-6a8c8289=""><ul class="channel-list" data-v-6a8c8289=""><div class="channel-list-content" data-v-6a8c8289=""><!--[--><!--[--><li id="explore-guide-refresh" class="" data-v-6a8c8289=""><a href="/explore?channel_id=homefeed_recommend&amp;channel_type=web_user_page" class="link-wrapper" target="_self" data-v-6a8c8289=""><svg class="reds-icon icon-wrapper" width="24" height="24" data-v-6a8c8289="" data-v-55b36ac6=""><use xlink:href="#home" data-v-55b36ac6=""></use></svg><span class="channel" data-v-6a8c8289="">发现</span></a></li><!--]--><!--[--><li id="" class="" data-v-6a8c8289=""><a target="_blank" href="https://creator.xiaohongshu.com/publish/publish?source=official" class="link-wrapper" data-v-6a8c8289=""><svg class="reds-icon icon-wrapper" width="24" height="24" data-v-6a8c8289="" data-v-55b36ac6=""><use xlink:href="#creator" data-v-55b36ac6=""></use></svg><span class="channel" data-v-6a8c8289="">发布</span></a></li><!--]--><!--[--><li class="link-wrapper bottom-channel" data-v-6a8c8289="" data-v-13c4f3b9=""><a href="/notification" class="link-wrapper bottom-channel" data-v-13c4f3b9=""><div class="badge-container" data-v-13c4f3b9="" data-v-0755b6ef=""><!--[--><svg class="reds-icon text-active" width="24" height="24" data-v-13c4f3b9="" data-v-0755b6ef-s="" data-v-55b36ac6=""><use xlink:href="#notification" data-v-55b36ac6=""></use></svg><!--]--><!----></div><span class="text channel" data-v-13c4f3b9="">通知</span></a></li><!--]--><!--[--><!--[--><!--[--><li class="user side-bar-component" data-v-a93a7d02=""><div class="link-wrapper" data-v-a93a7d02=""><a href="/user/profile/63ba6442000000002600603e" class="link-wrapper" data-v-a93a7d02=""><span class="reds-image-container gray responsive reds-avatar size-s" style="width:24px;" data-v-a93a7d02=""><!----><span class="reds-img-placeholder" style="padding-top: 100%;"></span><picture class="reds-img-box"><img crossorigin="anonymous" width="24" height="24" src="https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo31hms3tqmk2605otqch19go1uavoscag?imageView2/2/w/360/format/webp" data-load-status="loaded" loading="lazy" class="reds-img"></picture><div class="reds-img-box"><!----><!----><!--[--><i class="reds-avatar-border"></i><!--[--><!--]--><!--]--></div></span><span class="channel" data-v-a93a7d02="">我</span></a></div></li><!--]--><div class="bottom-channel bottom-menu-component" data-v-a93a7d02=""><a href="/user/profile/63ba6442000000002600603e" class="bottom-channel" data-v-a93a7d02=""><svg class="reds-icon" width="24" height="24" data-v-a93a7d02="" data-v-55b36ac6=""><use xlink:href="#me" data-v-55b36ac6=""></use></svg><span class="text" data-v-a93a7d02="">我</span></a><!----></div><!--]--><!--]--><!--]--><!----></div><div class="app-info" data-v-6a8c8289=""><p class="icp-info" data-v-6a8c8289=""><!--[--><!--[--><a title="小红书_沪ICP备" href="//beian.miit.gov.cn/" target="_blank" class="icp-text" data-v-6a8c8289="">沪ICP备13030189号</a>  | <!--]--><!--[--><a title="小红书_营业执照" href="//fe-video-qc.xhscdn.com/fe-platform/5581076bd6b6af2e0e943abb024ad0e16f2ebff6.pdf" target="_blank" class="icp-text" data-v-6a8c8289="">营业执照</a>  | <!--]--><!--[--><a title="小红书_沪公网安备" href="//www.beian.gov.cn/portal/registerSystemInfo?recordcode=31010102002533" target="_blank" class="icp-text" data-v-6a8c8289="">2024沪公网安备31010102002533号</a>  | <!--]--><!--[--><a title="小红书_网文" href="//fe-video-qc.xhscdn.com/fe-platform-file/104101b831hhkkll23u0678gtks7tu70004en2n231udpe" target="_blank" class="icp-text" data-v-6a8c8289="">增值电信业务经营许可证：沪B2-20150021</a>  | <!--]--><!--[--><a title="小红书_医疗器械网络交易服务" href="//fe-video-qc.xhscdn.com/fe-platform/410dce57bc12a6d7e5808060e47644fbe46f68ff.pdf" target="_blank" class="icp-text" data-v-6a8c8289="">医疗器械网络交易服务第三方平台备案：(沪)网械平台备字[2019]第00006号</a>  | <!--]--><!--[--><a title="小红书_互联网药品信息服务" href="//fe-video-qc.xhscdn.com/fe-platform/f37a08cacc088061beb38329c387c32fc48fc6fe.pdf" target="_blank" class="icp-text" data-v-6a8c8289="">互联网药品信息服务资格证书：(沪)-经营性-2023-0144</a>  | <!--]--><!--[--><a title="小红书_上海市互联网举报中心" href="//www.shjbzx.cn" target="_blank" class="icp-text" data-v-6a8c8289="">违法不良信息举报电话：4006676810</a>  | <!--]--><!--[--><a title="小红书_上海市互联网举报中心" href="//www.shjbzx.cn" target="_blank" class="icp-text" data-v-6a8c8289="">上海市互联网举报中心</a>  | <!--]--><!--[--><a title="网上有害信息举报专区" href="//www.12377.cn" target="_blank" class="icp-text" data-v-6a8c8289="">网上有害信息举报专区</a>  | <!--]--><!--[--><a title="小红书_沪公网安备" href="//dc.xhscdn.com/06c2adb0-b353-11e9-9d0c-7be9ff8961c1/自营经营者信息公示.pdf" target="_blank" class="icp-text" data-v-6a8c8289="">自营经营者信息</a>  | <!--]--><!--[--><a title="小红书_网络文化经营许可" href="//fe-video-qc.xhscdn.com/fe-platform/7970f6e8b70aedc995ba273d04b6b6751abcd63c.pdf" target="_blank" class="icp-text" data-v-6a8c8289="">网络文化经营许可证：沪网文(2024)1344-086号</a>  | <!--]--><!--[--><a href="https://beian.cac.gov.cn/api/static/fileUpload/principalOrithm/additional/user_c015445c-80ac-45f7-94d7-3871e961b1fe_d4425f3b-7f35-45af-b8d4-badd4424d6d5.pdf" target="_blank" class="icp-text" data-v-6a8c8289="">个性化推荐算法 网信算备310101216601302230019号</a> <!--]--><!--]--></p><div class="corp-info" data-v-6a8c8289=""><p data-v-6a8c8289="">© 2014-2024</p><p data-v-6a8c8289="">行吟信息科技（上海）有限公司</p><p data-v-6a8c8289="">地址：上海市黄浦区马当路388号C座</p><p data-v-6a8c8289="">电话：9501-3888</p></div></div><div class="divider" style="" data-v-6a8c8289="" data-v-39ecb380=""></div></ul><div id="explore-guide-menu" class="information-container" data-v-6a8c8289="" data-v-0370e1e6=""><!----><div class="information-wrapper" data-v-0370e1e6=""><svg class="reds-icon information-icon" width="24" height="24" data-v-0370e1e6="" data-v-55b36ac6=""><use xlink:href="#menu" data-v-55b36ac6=""></use></svg> 更多 </div><div class="app-info outside" data-v-0370e1e6=""><p class="icp-info" data-v-0370e1e6=""><!--[--><!--[--><a title="小红书_沪ICP备" href="//beian.miit.gov.cn/" target="_blank" class="icp-text" data-v-0370e1e6="">沪ICP备13030189号</a>  | <!--]--><!--[--><a title="小红书_营业执照" href="//fe-video-qc.xhscdn.com/fe-platform/5581076bd6b6af2e0e943abb024ad0e16f2ebff6.pdf" target="_blank" class="icp-text" data-v-0370e1e6="">营业执照</a>  | <!--]--><!--[--><a title="小红书_沪公网安备" href="//www.beian.gov.cn/portal/registerSystemInfo?recordcode=31010102002533" target="_blank" class="icp-text" data-v-0370e1e6="">2024沪公网安备31010102002533号</a>  | <!--]--><!--[--><a title="小红书_网文" href="//fe-video-qc.xhscdn.com/fe-platform-file/104101b831hhkkll23u0678gtks7tu70004en2n231udpe" target="_blank" class="icp-text" data-v-0370e1e6="">增值电信业务经营许可证：沪B2-20150021</a>  | <!--]--><!--[--><a title="小红书_医疗器械网络交易服务" href="//fe-video-qc.xhscdn.com/fe-platform/410dce57bc12a6d7e5808060e47644fbe46f68ff.pdf" target="_blank" class="icp-text" data-v-0370e1e6="">医疗器械网络交易服务第三方平台备案：(沪)网械平台备字[2019]第00006号</a>  | <!--]--><!--[--><a title="小红书_互联网药品信息服务" href="//fe-video-qc.xhscdn.com/fe-platform/f37a08cacc088061beb38329c387c32fc48fc6fe.pdf" target="_blank" class="icp-text" data-v-0370e1e6="">互联网药品信息服务资格证书：(沪)-经营性-2023-0144</a>  | <!--]--><!--[--><a title="小红书_上海市互联网举报中心" href="//www.shjbzx.cn" target="_blank" class="icp-text" data-v-0370e1e6="">违法不良信息举报电话：4006676810</a>  | <!--]--><!--[--><a title="小红书_上海市互联网举报中心" href="//www.shjbzx.cn" target="_blank" class="icp-text" data-v-0370e1e6="">上海市互联网举报中心</a>  | <!--]--><!--[--><a title="网上有害信息举报专区" href="//www.12377.cn" target="_blank" class="icp-text" data-v-0370e1e6="">网上有害信息举报专区</a>  | <!--]--><!--[--><a title="小红书_沪公网安备" href="//dc.xhscdn.com/06c2adb0-b353-11e9-9d0c-7be9ff8961c1/自营经营者信息公示.pdf" target="_blank" class="icp-text" data-v-0370e1e6="">自营经营者信息</a>  | <!--]--><!--[--><a title="小红书_网络文化经营许可" href="//fe-video-qc.xhscdn.com/fe-platform/7970f6e8b70aedc995ba273d04b6b6751abcd63c.pdf" target="_blank" class="icp-text" data-v-0370e1e6="">网络文化经营许可证：沪网文(2024)1344-086号</a>  | <!--]--><!--[--><a href="https://beian.cac.gov.cn/api/static/fileUpload/principalOrithm/additional/user_c015445c-80ac-45f7-94d7-3871e961b1fe_d4425f3b-7f35-45af-b8d4-badd4424d6d5.pdf" target="_blank" class="icp-text" data-v-0370e1e6="">个性化推荐算法 网信算备310101216601302230019号</a> <!--]--><!--]--></p><div class="corp-info" data-v-0370e1e6=""><p data-v-0370e1e6="">© 2014-2024</p><p data-v-0370e1e6="">行吟信息科技（上海）有限公司</p><p data-v-0370e1e6="">地址：上海市黄浦区马当路388号C座</p><p data-v-0370e1e6="">电话：9501-3888</p></div></div></div></div><div class="with-side-bar main-content" data-v-34b87540=""><!--[--><!----><!--[--><div id="userPageContainer" class="user-page" data-csr-exp="false" data-v-8069da68=""><!--[--><div class="user" data-v-8069da68="" data-v-6be60601=""><div class="user-info" data-v-6be60601=""><div class="avatar" data-v-6be60601=""><div class="avatar-wrapper" data-v-6be60601="" data-v-86ee68bc=""><img src="https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo31lvmkfehl80g5pvovm0ji2q3r980kf0?imageView2/2/w/540/format/webp|imageMogr2/strip2" fetchpriority="high" onerror="this.setAttribute('data-error', 1)" crossorigin="anonymous" decoding="async" data-xhs-img="" class="user-image" style="border:1px solid hsla(0, 0%, 0%, 0.08);" data-v-86ee68bc=""></div></div><div class="info-part" data-v-6be60601=""><div class="info" data-v-6be60601=""><div class="basic-info" data-v-6be60601="" data-v-1d90bc98=""><div class="avatar" data-v-1d90bc98=""><div class="avatar-wrapper" data-v-1d90bc98="" data-v-86ee68bc=""><img src="https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo31lvmkfehl80g5pvovm0ji2q3r980kf0?imageView2/2/w/540/format/webp|imageMogr2/strip2" fetchpriority="high" onerror="this.setAttribute('data-error', 1)" crossorigin="anonymous" decoding="async" data-xhs-img="" class="user-image" style="border:1px solid hsla(0, 0%, 0%, 0.08);" data-v-86ee68bc=""></div></div><div class="user-basic" data-v-1d90bc98=""><div class="user-nickname" data-v-1d90bc98=""><div class="user-name" data-v-1d90bc98="">大厂电报<!----></div></div><div class="user-content" data-v-1d90bc98=""><span class="user-redId" data-v-1d90bc98="">小红书号：95396675528</span><span class="user-IP" data-v-1d90bc98=""> IP属地：北京</span></div></div></div><!--[--><div class="user-desc" data-v-4947d265="">大厂资讯，每日电报
带你了解大厂动态和商业逻辑，看清大厂风云
有瓜速报，有料敢说，如有涉侵权随时踢我修改</div><div class="user-tags" data-v-4947d265=""><!--[--><div class="tag-item" data-v-4947d265=""><div class="gender" data-v-4947d265=""><svg class="reds-icon" width="12" height="12" data-v-4947d265="" data-v-55b36ac6=""><use xlink:href="#male" data-v-55b36ac6=""></use></svg><!----></div></div><!--]--></div><!--]--><div class="data-info" data-v-6be60601="" data-v-18b45ae8=""><div class="user-interactions" data-v-18b45ae8=""><!--[--><div data-v-18b45ae8=""><span class="count" data-v-18b45ae8="">39</span><span class="shows" data-v-18b45ae8="">关注</span></div><div data-v-18b45ae8=""><span class="count" data-v-18b45ae8="">2.5万</span><span class="shows" data-v-18b45ae8="">粉丝</span></div><div data-v-18b45ae8=""><span class="count" data-v-18b45ae8="">9.2万</span><span class="shows" data-v-18b45ae8="">获赞与收藏</span></div><!--]--></div></div><!----></div><div class="info-right-area" data-v-6be60601=""><div data-v-6be60601=""><div data-v-2f01971d=""><button class="reds-button-new follow-button large primary follow-button" style="" data-v-2f01971d=""><span class="reds-button-new-box"><!----><!--[--><!--]--><span class="reds-button-new-text"><!--[-->关注<!--]--></span></span></button><!----></div></div><div style="z-index:5;--0a52af4c:40px;" class="info-right-area-more-container" data-v-6be60601="" data-v-1af0f6e0="" data-v-1b03e45c=""><div class="report-entrance-wrapper" data-v-1af0f6e0=""><svg class="reds-icon" width="20" height="20" data-v-1af0f6e0="" data-v-55b36ac6=""><use xlink:href="#more" data-v-55b36ac6=""></use></svg></div></div></div></div></div></div><!--[--><div class="reds-sticky-box user-page-sticky" style="--4e45219e: all 0.4s cubic-bezier(0.2, 0, 0.25, 1) 0s;" data-v-bb2dbd52="" data-v-73916935=""><div class="reds-sticky" style="" data-v-73916935=""><!--[--><div class="tertiary center reds-tabs-list reds-tabs-list" style="padding:0px 0px;" data-v-bb2dbd52="" data-v-73916935-s=""><!--[--><!--[--><div class="reds-tab-item active sub-tab-list" style="padding:0px 16px;margin-right:0px;font-size:16px;" data-v-bb2dbd52=""><!----><!----><span>笔记</span></div><div class="reds-tab-item sub-tab-list" style="padding:0px 16px;margin-right:0px;font-size:16px;" data-v-bb2dbd52=""><div class="reds-tab-item__left"><!--[--><span class="lock-icon" data-v-bb2dbd52=""><svg class="reds-icon collection-icon" width="20" height="20" data-v-bb2dbd52="" data-v-55b36ac6=""><use xlink:href="#lock" data-v-55b36ac6=""></use></svg></span><!--]--></div><!----><span>收藏</span></div><!--]--><!--]--><!--[--><!--]--><!----><div class="active-tag" style="width: 64px; left: 461px;"></div></div><!--]--></div></div><!----><div class="feeds-tab-container" style="--4e45219e: all 0.4s cubic-bezier(0.2, 0, 0.25, 1) 0s;" data-v-bb2dbd52=""><div class="transform-container" style="transform: translate(0px, 0px); width: 2102px;" data-v-bb2dbd52=""><!--[--><div class="tab-content-item" style="height: auto; width: 1026.4px; overflow: scroll;" data-v-bb2dbd52="" data-v-64126f47=""><!----><!--[--><div id="userPostedFeeds" class="feeds-container" style="width: 100%; height: 2526px; visibility: visible;" data-v-330d9cca=""><!--[--><section data-v-a264b01a="" data-v-330d9cca="" class="note-item" data-width="1200" data-height="1600" data-index="0" style="--68479076: 16px; --1bd4d75c: 238.6px; --1e4add76: blur(42.5px); transform: translate(0px, 0px);"><div data-v-a264b01a=""><a data-v-a264b01a="" href="/explore/68bbfa85000000001d023c91" style="display: none;"></a><a data-v-a264b01a="" class="cover mask ld" target="_self" href="/user/profile/67f8fd81000000000e010b43/68bbfa85000000001d023c91?xsec_token=ABFIekrUMbMDCgiDUoz3KyuSRNNWYBGcJ_vSPS_4SLx6A=&amp;xsec_source=pc_user" style="height: 318px;"><img data-v-a264b01a="" src="https://sns-webpic-qc.xhscdn.com/202509081416/88049fbe310fb6d9042ff342757a4287/1040g2sg31m38d73llmt05pvovm0ji2q3egnrdso!nc_n_webp_mw_1" fetchpriority="high" loading="eager" decoding="async" data-xhs-img="" elementtiming="card-exposed" style="width: 100%; height: 100%; object-fit: cover;"><!----><div data-v-a264b01a="" class="top-tag-area"><div data-v-a264b01a="" class="top-wrapper">置顶</div></div><!----></a><div data-v-a264b01a="" class="footer"><a data-v-a264b01a="" target="_self" class="title"><span data-v-51ec0135="" data-v-a264b01a="">联通中标300万大单，腾讯云不服投诉，逆转了</span></a><div data-v-a264b01a="" class="author-wrapper"><a data-v-a264b01a="" aria-current="page" href="/user/profile/67f8fd81000000000e010b43?channel_type=web_user_page&amp;parent_page_channel_type=web_user_board&amp;xsec_token=&amp;xsec_source=pc_note" class="active router-link-exact-active author" target="_blank"><img data-v-a264b01a="" src="https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo31lvmkfehl80g5pvovm0ji2q3r980kf0?imageView2/2/w/60/format/webp|imageMogr2/strip" fetchpriority="auto" width="20" height="20" crossorigin="anonymous" loading="lazy" decoding="async" data-xhs-img="" class="author-avatar"><span data-v-a264b01a="" class="name">大厂电报</span></a><span data-v-dc3a3972="" data-v-a264b01a="" class="like-wrapper like-active"><span data-v-dc3a3972="" class="like-lottie" style="width: 16px; height: 16px;"></span><svg data-v-55b36ac6="" data-v-dc3a3972="" class="reds-icon like-icon" width="16" height="16"><use data-v-55b36ac6="" xlink:href="#like"></use></svg><span data-v-dc3a3972="" class="count" selected-disabled-search="">678</span></span></div></div></div></section><section data-v-a264b01a="" data-v-330d9cca="" class="note-item" data-width="1320" data-height="1757" data-index="1" style="--68479076: 16px; --1bd4d75c: 238.6px; --1e4add76: blur(42.5px); transform: translate(262.6px, 0px);"><div data-v-a264b01a=""><a data-v-a264b01a="" href="/explore/68baa2e3000000001d02ce69" style="display: none;"></a><a data-v-a264b01a="" class="cover mask ld" target="_self" href="/user/profile/67f8fd81000000000e010b43/68baa2e3000000001d02ce69?xsec_token=ABI_lIrulwxGs1-dlc0OoaSn0MQEFqpF7fpyKNyBwBAs0=&amp;xsec_source=pc_user" style="height: 318px;"><img data-v-a264b01a="" src="https://sns-webpic-qc.xhscdn.com/202509081416/7bdeab8ced93c345e6bdb7cd2cead218/1040g2sg31m2rmme64qhg5nv613509bs8upnjnlg!nc_n_webp_mw_1" fetchpriority="high" loading="eager" decoding="async" data-xhs-img="" elementtiming="card-exposed" style="width: 100%; height: 100%; object-fit: cover;"><!----><div data-v-a264b01a="" class="top-tag-area"><div data-v-a264b01a="" class="top-wrapper">置顶</div></div><!----></a><div data-v-a264b01a="" class="footer"><a data-v-a264b01a="" target="_self" class="title"><span data-v-51ec0135="" data-v-a264b01a="">杭州估值百亿独角兽暴雷？已三个月未发工资</span></a><div data-v-a264b01a="" class="author-wrapper"><a data-v-a264b01a="" aria-current="page" href="/user/profile/67f8fd81000000000e010b43?channel_type=web_user_page&amp;parent_page_channel_type=web_user_board&amp;xsec_token=&amp;xsec_source=pc_note" class="active router-link-exact-active author" target="_blank"><img data-v-a264b01a="" src="https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo31lvmkfehl80g5pvovm0ji2q3r980kf0?imageView2/2/w/60/format/webp|imageMogr2/strip" fetchpriority="auto" width="20" height="20" crossorigin="anonymous" loading="lazy" decoding="async" data-xhs-img="" class="author-avatar"><span data-v-a264b01a="" class="name">大厂电报</span></a><span data-v-dc3a3972="" data-v-a264b01a="" class="like-wrapper like-active"><span data-v-dc3a3972="" class="like-lottie" style="width: 16px; height: 16px;"></span><svg data-v-55b36ac6="" data-v-dc3a3972="" class="reds-icon like-icon" width="16" height="16"><use data-v-55b36ac6="" xlink:href="#like"></use></svg><span data-v-dc3a3972="" class="count" selected-disabled-search="">723</span></span></div></div></div></section><section data-v-a264b01a="" data-v-330d9cca="" class="note-item" data-width="1200" data-height="1600" data-index="2" style="--68479076: 16px; --1bd4d75c: 238.6px; --1e4add76: blur(42.5px); transform: translate(525.2px, 0px);"><div data-v-a264b01a=""><a data-v-a264b01a="" href="/explore/68bd9986000000001d01f20b" style="display: none;"></a><a data-v-a264b01a="" class="cover mask ld" target="_self" href="/user/profile/67f8fd81000000000e010b43/68bd9986000000001d01f20b?xsec_token=AB1l0HATZhILIBw3X4ghyQ3mix3f--GaDJZCPGNJQPuxk=&amp;xsec_source=pc_user" style="height: 318px;"><img data-v-a264b01a="" src="https://sns-webpic-qc.xhscdn.com/202509081416/b62ba595501960a0b6b16a8617711c31/1040g2sg31m4qr2knm8e05pvovm0ji2q3o5pp998!nc_n_webp_mw_1" fetchpriority="high" loading="eager" decoding="async" data-xhs-img="" elementtiming="card-exposed" style="width: 100%; height: 100%; object-fit: cover;"><!----><!----><!----></a><div data-v-a264b01a="" class="footer"><a data-v-a264b01a="" target="_self" class="title"><span data-v-51ec0135="" data-v-a264b01a="">前百度员工：离开大厂后，才知道有多难</span></a><div data-v-a264b01a="" class="author-wrapper"><a data-v-a264b01a="" aria-current="page" href="/user/profile/67f8fd81000000000e010b43?channel_type=web_user_page&amp;parent_page_channel_type=web_user_board&amp;xsec_token=&amp;xsec_source=pc_note" class="active router-link-exact-active author" target="_blank"><img data-v-a264b01a="" src="https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo31lvmkfehl80g5pvovm0ji2q3r980kf0?imageView2/2/w/60/format/webp|imageMogr2/strip" fetchpriority="auto" width="20" height="20" crossorigin="anonymous" loading="lazy" decoding="async" data-xhs-img="" class="author-avatar"><span data-v-a264b01a="" class="name">大厂电报</span></a><span data-v-dc3a3972="" data-v-a264b01a="" class="like-wrapper like-active"><span data-v-dc3a3972="" class="like-lottie" style="width: 16px; height: 16px;"></span><svg data-v-55b36ac6="" data-v-dc3a3972="" class="reds-icon like-icon" width="16" height="16"><use data-v-55b36ac6="" xlink:href="#like"></use></svg><span data-v-dc3a3972="" class="count" selected-disabled-search="">22</span></span></div></div></div></section><section data-v-a264b01a="" data-v-330d9cca="" class="note-item" data-width="1200" data-height="1600" data-index="3" style="--68479076: 16px; --1bd4d75c: 238.6px; --1e4add76: blur(42.5px); transform: translate(787.8px, 0px);"><div data-v-a264b01a=""><a data-v-a264b01a="" href="/explore/68bd7f96000000001d0234d7" style="display: none;"></a><a data-v-a264b01a="" class="cover mask ld" target="_self" href="/user/profile/67f8fd81000000000e010b43/68bd7f96000000001d0234d7?xsec_token=AB1l0HATZhILIBw3X4ghyQ3t1b4kC85WnEKQO0OYcO4Fw=&amp;xsec_source=pc_user" style="height: 318px;"><img data-v-a264b01a="" src="https://sns-webpic-qc.xhscdn.com/202509081416/02e3f53435c14f28f4c05978d81c0801/1040g00831m4mkmdim64g5pvovm0ji2q314cbf4g!nc_n_webp_mw_1" fetchpriority="high" loading="eager" decoding="async" data-xhs-img="" elementtiming="card-exposed" style="width: 100%; height: 100%; object-fit: cover;"><!----><!----><!----></a><div data-v-a264b01a="" class="footer"><a data-v-a264b01a="" target="_self" class="title"><span data-v-51ec0135="" data-v-a264b01a="">中元节当天，这家倒闭的新势力竟宣布复活了</span></a><div data-v-a264b01a="" class="author-wrapper"><a data-v-a264b01a="" aria-current="page" href="/user/profile/67f8fd81000000000e010b43?channel_type=web_user_page&amp;parent_page_channel_type=web_user_board&amp;xsec_token=&amp;xsec_source=pc_note" class="active router-link-exact-active author" target="_blank"><img data-v-a264b01a="" src="https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo31lvmkfehl80g5pvovm0ji2q3r980kf0?imageView2/2/w/60/format/webp|imageMogr2/strip" fetchpriority="auto" width="20" height="20" crossorigin="anonymous" loading="lazy" decoding="async" data-xhs-img="" class="author-avatar"><span data-v-a264b01a="" class="name">大厂电报</span></a><span data-v-dc3a3972="" data-v-a264b01a="" class="like-wrapper like-active"><span data-v-dc3a3972="" class="like-lottie" style="width: 16px; height: 16px;"></span><svg data-v-55b36ac6="" data-v-dc3a3972="" class="reds-icon like-icon" width="16" height="16"><use data-v-55b36ac6="" xlink:href="#like"></use></svg><span data-v-dc3a3972="" class="count" selected-disabled-search="">3</span></span></div></div></div></section><section data-v-a264b01a="" data-v-330d9cca="" class="note-item" data-width="1200" data-height="1600" data-index="4" style="--68479076: 16px; --1bd4d75c: 238.6px; --1e4add76: blur(42.5px); transform: translate(0px, 421px);"><div data-v-a264b01a=""><a data-v-a264b01a="" href="/explore/68bd71da000000001d03afb3" style="display: none;"></a><a data-v-a264b01a="" class="cover mask ld" target="_self" href="/user/profile/67f8fd81000000000e010b43/68bd71da000000001d03afb3?xsec_token=AB1l0HATZhILIBw3X4ghyQ3msn9J9S0-DeZb8C1-m9a5Y=&amp;xsec_source=pc_user" style="height: 318px;"><img data-v-a264b01a="" src="https://sns-webpic-qc.xhscdn.com/202509081416/94895e8807e1f0ce100ccd43ceda838d/1040g00831m4m9op15i1g5pvovm0ji2q3e6ekos8!nc_n_webp_mw_1" fetchpriority="high" loading="eager" decoding="async" data-xhs-img="" style="width: 100%; height: 100%; object-fit: cover;"><!----><!----><!----></a><div data-v-a264b01a="" class="footer"><a data-v-a264b01a="" target="_self" class="title"><span data-v-51ec0135="" data-v-a264b01a="">突发！13年知名亲子旅游平台一夜暴雷！</span></a><div data-v-a264b01a="" class="author-wrapper"><a data-v-a264b01a="" aria-current="page" href="/user/profile/67f8fd81000000000e010b43?channel_type=web_user_page&amp;parent_page_channel_type=web_user_board&amp;xsec_token=&amp;xsec_source=pc_note" class="active router-link-exact-active author" target="_blank"><img data-v-a264b01a="" src="https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo31lvmkfehl80g5pvovm0ji2q3r980kf0?imageView2/2/w/60/format/webp|imageMogr2/strip" fetchpriority="auto" width="20" height="20" crossorigin="anonymous" loading="lazy" decoding="async" data-xhs-img="" class="author-avatar"><span data-v-a264b01a="" class="name">大厂电报</span></a><span data-v-dc3a3972="" data-v-a264b01a="" class="like-wrapper like-active"><span data-v-dc3a3972="" class="like-lottie" style="width: 16px; height: 16px;"></span><svg data-v-55b36ac6="" data-v-dc3a3972="" class="reds-icon like-icon" width="16" height="16"><use data-v-55b36ac6="" xlink:href="#like"></use></svg><span data-v-dc3a3972="" class="count" selected-disabled-search="">9</span></span></div></div></div></section><section data-v-a264b01a="" data-v-330d9cca="" class="note-item" data-width="1320" data-height="1753" data-index="5" style="--68479076: 16px; --1bd4d75c: 238.6px; --1e4add76: blur(42.5px); transform: translate(262.6px, 421px);"><div data-v-a264b01a=""><a data-v-a264b01a="" href="/explore/68bcea41000000001d025011" style="display: none;"></a><a data-v-a264b01a="" class="cover mask ld" target="_self" href="/user/profile/67f8fd81000000000e010b43/68bcea41000000001d025011?xsec_token=ABBB6pzUpDgnwINr0J48WQ7vqrZCPIZ0mDNiDq6LiH_k0=&amp;xsec_source=pc_user" style="height: 317px;"><img data-v-a264b01a="" src="https://sns-webpic-qc.xhscdn.com/202509081416/094eadf20125c53ed75a82fa0442dbb9/1040g2sg31m44ta90ks3g5nv613509bs83hcqdto!nc_n_webp_mw_1" fetchpriority="auto" loading="lazy" decoding="async" data-xhs-img="" style="width: 100%; height: 100%; object-fit: cover;"><!----><!----><!----></a><div data-v-a264b01a="" class="footer"><a data-v-a264b01a="" target="_self" class="title"><span data-v-51ec0135="" data-v-a264b01a="">前百度高管创业失败：1.5万元欠薪都还不起</span></a><div data-v-a264b01a="" class="author-wrapper"><a data-v-a264b01a="" aria-current="page" href="/user/profile/67f8fd81000000000e010b43?channel_type=web_user_page&amp;parent_page_channel_type=web_user_board&amp;xsec_token=&amp;xsec_source=pc_note" class="active router-link-exact-active author" target="_blank"><img data-v-a264b01a="" src="https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo31lvmkfehl80g5pvovm0ji2q3r980kf0?imageView2/2/w/60/format/webp|imageMogr2/strip" fetchpriority="auto" width="20" height="20" crossorigin="anonymous" loading="lazy" decoding="async" data-xhs-img="" class="author-avatar"><span data-v-a264b01a="" class="name">大厂电报</span></a><span data-v-dc3a3972="" data-v-a264b01a="" class="like-wrapper like-active"><span data-v-dc3a3972="" class="like-lottie" style="width: 16px; height: 16px;"></span><svg data-v-55b36ac6="" data-v-dc3a3972="" class="reds-icon like-icon" width="16" height="16"><use data-v-55b36ac6="" xlink:href="#like"></use></svg><span data-v-dc3a3972="" class="count" selected-disabled-search="">28</span></span></div></div></div></section><section data-v-a264b01a="" data-v-330d9cca="" class="note-item" data-width="1200" data-height="1600" data-index="6" style="--68479076: 16px; --1bd4d75c: 238.6px; --1e4add76: blur(42.5px); transform: translate(525.2px, 421px);"><div data-v-a264b01a=""><a data-v-a264b01a="" href="/explore/68bc5f1b000000001d021f0d" style="display: none;"></a><a data-v-a264b01a="" class="cover mask ld" target="_self" href="/user/profile/67f8fd81000000000e010b43/68bc5f1b000000001d021f0d?xsec_token=ABBB6pzUpDgnwINr0J48WQ7iluC_i7H_BDtFXMdE_p5F4=&amp;xsec_source=pc_user" style="height: 318px;"><img data-v-a264b01a="" src="https://sns-webpic-qc.xhscdn.com/202509081416/6be756bafc3e45c0a8dd99fdecb9e0f6/1040g2sg31m3k2krrlihg5pvovm0ji2q3ff05ek8!nc_n_webp_mw_1" fetchpriority="auto" loading="lazy" decoding="async" data-xhs-img="" style="width: 100%; height: 100%; object-fit: cover;"><!----><!----><!----></a><div data-v-a264b01a="" class="footer"><a data-v-a264b01a="" target="_self" class="title"><span data-v-51ec0135="" data-v-a264b01a="">国内IT公司暴雷！欠薪10个月，员工集体炸锅</span></a><div data-v-a264b01a="" class="author-wrapper"><a data-v-a264b01a="" aria-current="page" href="/user/profile/67f8fd81000000000e010b43?channel_type=web_user_page&amp;parent_page_channel_type=web_user_board&amp;xsec_token=&amp;xsec_source=pc_note" class="active router-link-exact-active author" target="_blank"><img data-v-a264b01a="" src="https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo31lvmkfehl80g5pvovm0ji2q3r980kf0?imageView2/2/w/60/format/webp|imageMogr2/strip" fetchpriority="auto" width="20" height="20" crossorigin="anonymous" loading="lazy" decoding="async" data-xhs-img="" class="author-avatar"><span data-v-a264b01a="" class="name">大厂电报</span></a><span data-v-dc3a3972="" data-v-a264b01a="" class="like-wrapper like-active"><span data-v-dc3a3972="" class="like-lottie" style="width: 16px; height: 16px;"></span><svg data-v-55b36ac6="" data-v-dc3a3972="" class="reds-icon like-icon" width="16" height="16"><use data-v-55b36ac6="" xlink:href="#like"></use></svg><span data-v-dc3a3972="" class="count" selected-disabled-search="">333</span></span></div></div></div></section><section data-v-a264b01a="" data-v-330d9cca="" class="note-item" data-width="1200" data-height="1600" data-index="7" style="--68479076: 16px; --1bd4d75c: 238.6px; --1e4add76: blur(42.5px); transform: translate(787.8px, 421px);"><div data-v-a264b01a=""><a data-v-a264b01a="" href="/explore/68bc5a37000000001d037391" style="display: none;"></a><a data-v-a264b01a="" class="cover mask ld" target="_self" href="/user/profile/67f8fd81000000000e010b43/68bc5a37000000001d037391?xsec_token=ABBB6pzUpDgnwINr0J48WQ7sjjQXGh7Nox3Re3P8QnbZo=&amp;xsec_source=pc_user" style="height: 318px;"><img data-v-a264b01a="" src="https://sns-webpic-qc.xhscdn.com/202509081416/df40db2bc083b04d8b239e2abf8c5b8d/1040g2sg31m3k2krrlie05pvovm0ji2q3v5ue3a0!nc_n_webp_mw_1" fetchpriority="auto" loading="lazy" decoding="async" data-xhs-img="" style="width: 100%; height: 100%; object-fit: cover;"><!----><!----><!----></a><div data-v-a264b01a="" class="footer"><a data-v-a264b01a="" target="_self" class="title"><span data-v-51ec0135="" data-v-a264b01a="">苏宁欠4600万不还，玩"空壳公司"被法院锤爆</span></a><div data-v-a264b01a="" class="author-wrapper"><a data-v-a264b01a="" aria-current="page" href="/user/profile/67f8fd81000000000e010b43?channel_type=web_user_page&amp;parent_page_channel_type=web_user_board&amp;xsec_token=&amp;xsec_source=pc_note" class="active router-link-exact-active author" target="_blank"><img data-v-a264b01a="" src="https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo31lvmkfehl80g5pvovm0ji2q3r980kf0?imageView2/2/w/60/format/webp|imageMogr2/strip" fetchpriority="auto" width="20" height="20" crossorigin="anonymous" loading="lazy" decoding="async" data-xhs-img="" class="author-avatar"><span data-v-a264b01a="" class="name">大厂电报</span></a><span data-v-dc3a3972="" data-v-a264b01a="" class="like-wrapper like-active"><span data-v-dc3a3972="" class="like-lottie" style="width: 16px; height: 16px;"></span><svg data-v-55b36ac6="" data-v-dc3a3972="" class="reds-icon like-icon" width="16" height="16"><use data-v-55b36ac6="" xlink:href="#like"></use></svg><span data-v-dc3a3972="" class="count" selected-disabled-search="">140</span></span></div></div></div></section><section data-v-a264b01a="" data-v-330d9cca="" class="note-item" data-width="1200" data-height="1600" data-index="8" style="--68479076: 16px; --1bd4d75c: 238.6px; --1e4add76: blur(42.5px); transform: translate(262.6px, 841px);"><div data-v-a264b01a=""><a data-v-a264b01a="" href="/explore/68bb97d9000000001d023c21" style="display: none;"></a><a data-v-a264b01a="" class="cover mask ld" target="_self" href="/user/profile/67f8fd81000000000e010b43/68bb97d9000000001d023c21?xsec_token=ABFIekrUMbMDCgiDUoz3KyuUAJb3qMY4kNCT5AC2tE6II=&amp;xsec_source=pc_user" style="height: 318px;"><img data-v-a264b01a="" src="https://sns-webpic-qc.xhscdn.com/202509081416/e552f0716651fa94c4d9e50c77068297/1040g2sg31m2rmme64qh05nv613509bs853j283o!nc_n_webp_mw_1" fetchpriority="auto" loading="lazy" decoding="async" data-xhs-img="" style="width: 100%; height: 100%; object-fit: cover;"><!----><!----><!----></a><div data-v-a264b01a="" class="footer"><a data-v-a264b01a="" target="_self" class="title"><span data-v-51ec0135="" data-v-a264b01a="">什么事，中国移动还能发通告「处理」中国电信？</span></a><div data-v-a264b01a="" class="author-wrapper"><a data-v-a264b01a="" aria-current="page" href="/user/profile/67f8fd81000000000e010b43?channel_type=web_user_page&amp;parent_page_channel_type=web_user_board&amp;xsec_token=&amp;xsec_source=pc_note" class="active router-link-exact-active author" target="_blank"><img data-v-a264b01a="" src="https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo31lvmkfehl80g5pvovm0ji2q3r980kf0?imageView2/2/w/60/format/webp|imageMogr2/strip" fetchpriority="auto" width="20" height="20" crossorigin="anonymous" loading="lazy" decoding="async" data-xhs-img="" class="author-avatar"><span data-v-a264b01a="" class="name">大厂电报</span></a><span data-v-dc3a3972="" data-v-a264b01a="" class="like-wrapper like-active"><span data-v-dc3a3972="" class="like-lottie" style="width: 16px; height: 16px;"></span><svg data-v-55b36ac6="" data-v-dc3a3972="" class="reds-icon like-icon" width="16" height="16"><use data-v-55b36ac6="" xlink:href="#like"></use></svg><span data-v-dc3a3972="" class="count" selected-disabled-search="">45</span></span></div></div></div></section><section data-v-a264b01a="" data-v-330d9cca="" class="note-item" data-width="1200" data-height="1600" data-index="9" style="--68479076: 16px; --1bd4d75c: 238.6px; --1e4add76: blur(42.5px); transform: translate(0px, 842px);"><div data-v-a264b01a=""><a data-v-a264b01a="" href="/explore/68baff66000000001d039de3" style="display: none;"></a><a data-v-a264b01a="" class="cover mask ld" target="_self" href="/user/profile/67f8fd81000000000e010b43/68baff66000000001d039de3?xsec_token=ABI_lIrulwxGs1-dlc0OoaSt-fWNvDKpRkTnTyCBH-MAY=&amp;xsec_source=pc_user" style="height: 318px;"><img data-v-a264b01a="" src="https://sns-webpic-qc.xhscdn.com/202509081416/6409e36d545082d25bfde65a5f1ed620/1040g00831m29g70pm61g5pc1uuf86hauajanej8!nc_n_webp_mw_1" fetchpriority="auto" loading="lazy" decoding="async" data-xhs-img="" style="width: 100%; height: 100%; object-fit: cover;"><!----><!----><!----></a><div data-v-a264b01a="" class="footer"><a data-v-a264b01a="" target="_self" class="title"><span data-v-51ec0135="" data-v-a264b01a="">特斯拉为留马斯克，开出1万亿美元薪酬！</span></a><div data-v-a264b01a="" class="author-wrapper"><a data-v-a264b01a="" aria-current="page" href="/user/profile/67f8fd81000000000e010b43?channel_type=web_user_page&amp;parent_page_channel_type=web_user_board&amp;xsec_token=&amp;xsec_source=pc_note" class="active router-link-exact-active author" target="_blank"><img data-v-a264b01a="" src="https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo31lvmkfehl80g5pvovm0ji2q3r980kf0?imageView2/2/w/60/format/webp|imageMogr2/strip" fetchpriority="auto" width="20" height="20" crossorigin="anonymous" loading="lazy" decoding="async" data-xhs-img="" class="author-avatar"><span data-v-a264b01a="" class="name">大厂电报</span></a><span data-v-dc3a3972="" data-v-a264b01a="" class="like-wrapper like-active"><span data-v-dc3a3972="" class="like-lottie" style="width: 16px; height: 16px;"></span><svg data-v-55b36ac6="" data-v-dc3a3972="" class="reds-icon like-icon" width="16" height="16"><use data-v-55b36ac6="" xlink:href="#like"></use></svg><span data-v-dc3a3972="" class="count" selected-disabled-search="">6</span></span></div></div></div></section><section data-v-a264b01a="" data-v-330d9cca="" class="note-item" data-width="1200" data-height="1600" data-index="10" style="--68479076: 16px; --1bd4d75c: 238.6px; --1e4add76: blur(42.5px); transform: translate(525.2px, 842px);"><div data-v-a264b01a=""><a data-v-a264b01a="" href="/explore/68ba9a60000000001d029000" style="display: none;"></a><a data-v-a264b01a="" class="cover mask ld" target="_self" href="/user/profile/67f8fd81000000000e010b43/68ba9a60000000001d029000?xsec_token=ABI_lIrulwxGs1-dlc0OoaSl8Cd_099PWpvRDsh4tT4mk=&amp;xsec_source=pc_user" style="height: 318px;"><img data-v-a264b01a="" src="https://sns-webpic-qc.xhscdn.com/202509081416/2399ca7edb908827a03262c570ead19e/1040g2sg31m1rs34fl2gg5nv613509bs808tjar8!nc_n_webp_mw_1" fetchpriority="auto" loading="lazy" decoding="async" data-xhs-img="" style="width: 100%; height: 100%; object-fit: cover;"><!----><!----><!----></a><div data-v-a264b01a="" class="footer"><a data-v-a264b01a="" target="_self" class="title"><span data-v-51ec0135="" data-v-a264b01a="">医械行业巨头康乐保，将在中国大规模裁员</span></a><div data-v-a264b01a="" class="author-wrapper"><a data-v-a264b01a="" aria-current="page" href="/user/profile/67f8fd81000000000e010b43?channel_type=web_user_page&amp;parent_page_channel_type=web_user_board&amp;xsec_token=&amp;xsec_source=pc_note" class="active router-link-exact-active author" target="_blank"><img data-v-a264b01a="" src="https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo31lvmkfehl80g5pvovm0ji2q3r980kf0?imageView2/2/w/60/format/webp|imageMogr2/strip" fetchpriority="auto" width="20" height="20" crossorigin="anonymous" loading="lazy" decoding="async" data-xhs-img="" class="author-avatar"><span data-v-a264b01a="" class="name">大厂电报</span></a><span data-v-dc3a3972="" data-v-a264b01a="" class="like-wrapper like-active"><span data-v-dc3a3972="" class="like-lottie" style="width: 16px; height: 16px;"></span><svg data-v-55b36ac6="" data-v-dc3a3972="" class="reds-icon like-icon" width="16" height="16"><use data-v-55b36ac6="" xlink:href="#like"></use></svg><span data-v-dc3a3972="" class="count" selected-disabled-search="">7</span></span></div></div></div></section><section data-v-a264b01a="" data-v-330d9cca="" class="note-item" data-width="1200" data-height="1600" data-index="11" style="--68479076: 16px; --1bd4d75c: 238.6px; --1e4add76: blur(42.5px); transform: translate(787.8px, 842px);"><div data-v-a264b01a=""><a data-v-a264b01a="" href="/explore/68ba959f000000001d020212" style="display: none;"></a><a data-v-a264b01a="" class="cover mask ld" target="_self" href="/user/profile/67f8fd81000000000e010b43/68ba959f000000001d020212?xsec_token=ABI_lIrulwxGs1-dlc0OoaSoRc3ZnNtKxrkqetXpFajKk=&amp;xsec_source=pc_user" style="height: 318px;"><img data-v-a264b01a="" src="https://sns-webpic-qc.xhscdn.com/202509081416/f84e03a9276a4f1f7f0fe1fd6f3bdd0e/1040g2sg31m1rs34fl2g05nv613509bs8b40t5n0!nc_n_webp_mw_1" fetchpriority="auto" loading="lazy" decoding="async" data-xhs-img="" style="width: 100%; height: 100%; object-fit: cover;"><!----><!----><!----></a><div data-v-a264b01a="" class="footer"><a data-v-a264b01a="" target="_self" class="title"><span data-v-51ec0135="" data-v-a264b01a="">腾讯智影关停！同名公众号、视频号同步注销</span></a><div data-v-a264b01a="" class="author-wrapper"><a data-v-a264b01a="" aria-current="page" href="/user/profile/67f8fd81000000000e010b43?channel_type=web_user_page&amp;parent_page_channel_type=web_user_board&amp;xsec_token=&amp;xsec_source=pc_note" class="active router-link-exact-active author" target="_blank"><img data-v-a264b01a="" src="https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo31lvmkfehl80g5pvovm0ji2q3r980kf0?imageView2/2/w/60/format/webp|imageMogr2/strip" fetchpriority="auto" width="20" height="20" crossorigin="anonymous" loading="lazy" decoding="async" data-xhs-img="" class="author-avatar"><span data-v-a264b01a="" class="name">大厂电报</span></a><span data-v-dc3a3972="" data-v-a264b01a="" class="like-wrapper like-active"><span data-v-dc3a3972="" class="like-lottie" style="width: 16px; height: 16px;"></span><svg data-v-55b36ac6="" data-v-dc3a3972="" class="reds-icon like-icon" width="16" height="16"><use data-v-55b36ac6="" xlink:href="#like"></use></svg><span data-v-dc3a3972="" class="count" selected-disabled-search="">5</span></span></div></div></div></section><section data-v-a264b01a="" data-v-330d9cca="" class="note-item" data-width="1200" data-height="1600" data-index="12" style="--68479076: 16px; --1bd4d75c: 238.6px; --1e4add76: blur(42.5px); transform: translate(262.6px, 1262px);"><div data-v-a264b01a=""><a data-v-a264b01a="" href="/explore/68ba93d8000000001d0270de" style="display: none;"></a><a data-v-a264b01a="" class="cover mask ld" target="_self" href="/user/profile/67f8fd81000000000e010b43/68ba93d8000000001d0270de?xsec_token=ABI_lIrulwxGs1-dlc0OoaSpiqNtkUFq4hjbe2V6qooY0=&amp;xsec_source=pc_user" style="height: 318px;"><img data-v-a264b01a="" src="https://sns-webpic-qc.xhscdn.com/202509081416/f0d5a99b06e4f76e9811f26e535eb1e9/1040g2sg31m1rs34fl2f05nv613509bs8ebmhgog!nc_n_webp_mw_1" fetchpriority="auto" loading="lazy" decoding="async" data-xhs-img="" style="width: 100%; height: 100%; object-fit: cover;"><!----><!----><!----></a><div data-v-a264b01a="" class="footer"><a data-v-a264b01a="" target="_self" class="title"><span data-v-51ec0135="" data-v-a264b01a="">英伟达对华再推新芯片，向中国市场服软了吗？</span></a><div data-v-a264b01a="" class="author-wrapper"><a data-v-a264b01a="" aria-current="page" href="/user/profile/67f8fd81000000000e010b43?channel_type=web_user_page&amp;parent_page_channel_type=web_user_board&amp;xsec_token=&amp;xsec_source=pc_note" class="active router-link-exact-active author" target="_blank"><img data-v-a264b01a="" src="https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo31lvmkfehl80g5pvovm0ji2q3r980kf0?imageView2/2/w/60/format/webp|imageMogr2/strip" fetchpriority="auto" width="20" height="20" crossorigin="anonymous" loading="lazy" decoding="async" data-xhs-img="" class="author-avatar"><span data-v-a264b01a="" class="name">大厂电报</span></a><span data-v-dc3a3972="" data-v-a264b01a="" class="like-wrapper like-active"><span data-v-dc3a3972="" class="like-lottie" style="width: 16px; height: 16px;"></span><svg data-v-55b36ac6="" data-v-dc3a3972="" class="reds-icon like-icon" width="16" height="16"><use data-v-55b36ac6="" xlink:href="#like"></use></svg><span data-v-dc3a3972="" class="count" selected-disabled-search="">3</span></span></div></div></div></section><section data-v-a264b01a="" data-v-330d9cca="" class="note-item" data-width="1200" data-height="1600" data-index="13" style="--68479076: 16px; --1bd4d75c: 238.6px; --1e4add76: blur(42.5px); transform: translate(0px, 1263px);"><div data-v-a264b01a=""><a data-v-a264b01a="" href="/explore/68b9ac32000000001d0289c0" style="display: none;"></a><a data-v-a264b01a="" class="cover mask ld" target="_self" href="/user/profile/67f8fd81000000000e010b43/68b9ac32000000001d0289c0?xsec_token=ABTk71fNEul7zAXn0OLf_fLzmJAr06wmtYv0zxz9EfcOY=&amp;xsec_source=pc_user" style="height: 318px;"><img data-v-a264b01a="" src="https://sns-webpic-qc.xhscdn.com/202509081416/9cd6d23763229597aee61037e182704f/1040g2sg31m0va2i95e8g5pvovm0ji2q35chfn30!nc_n_webp_mw_1" fetchpriority="auto" loading="lazy" decoding="async" data-xhs-img="" style="width: 100%; height: 100%; object-fit: cover;"><!----><!----><!----></a><div data-v-a264b01a="" class="footer"><a data-v-a264b01a="" target="_self" class="title"><span data-v-51ec0135="" data-v-a264b01a="">违规收集数据，Shein被重罚至少12亿！</span></a><div data-v-a264b01a="" class="author-wrapper"><a data-v-a264b01a="" aria-current="page" href="/user/profile/67f8fd81000000000e010b43?channel_type=web_user_page&amp;parent_page_channel_type=web_user_board&amp;xsec_token=&amp;xsec_source=pc_note" class="active router-link-exact-active author" target="_blank"><img data-v-a264b01a="" src="https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo31lvmkfehl80g5pvovm0ji2q3r980kf0?imageView2/2/w/60/format/webp|imageMogr2/strip" fetchpriority="auto" width="20" height="20" crossorigin="anonymous" loading="lazy" decoding="async" data-xhs-img="" class="author-avatar"><span data-v-a264b01a="" class="name">大厂电报</span></a><span data-v-dc3a3972="" data-v-a264b01a="" class="like-wrapper like-active"><span data-v-dc3a3972="" class="like-lottie" style="width: 16px; height: 16px;"></span><svg data-v-55b36ac6="" data-v-dc3a3972="" class="reds-icon like-icon" width="16" height="16"><use data-v-55b36ac6="" xlink:href="#like"></use></svg><span data-v-dc3a3972="" class="count" selected-disabled-search="">24</span></span></div></div></div></section><section data-v-a264b01a="" data-v-330d9cca="" class="note-item" data-width="1200" data-height="1600" data-index="14" style="--68479076: 16px; --1bd4d75c: 238.6px; --1e4add76: blur(42.5px); transform: translate(525.2px, 1263px);"><div data-v-a264b01a=""><a data-v-a264b01a="" href="/explore/68b9a4e7000000001d0233f1" style="display: none;"></a><a data-v-a264b01a="" class="cover mask ld" target="_self" href="/user/profile/67f8fd81000000000e010b43/68b9a4e7000000001d0233f1?xsec_token=ABTk71fNEul7zAXn0OLf_fL6eqme5cPazkWaqJt8hEZGE=&amp;xsec_source=pc_user" style="height: 318px;"><img data-v-a264b01a="" src="https://sns-webpic-qc.xhscdn.com/202509081416/5aa29f934ccfd4412cecba5e6d7b0200/1040g2sg31m0va2i95e805pvovm0ji2q3fc0eg68!nc_n_webp_mw_1" fetchpriority="auto" loading="lazy" decoding="async" data-xhs-img="" style="width: 100%; height: 100%; object-fit: cover;"><!----><!----><!----></a><div data-v-a264b01a="" class="footer"><a data-v-a264b01a="" target="_self" class="title"><span data-v-51ec0135="" data-v-a264b01a="">市直副科辞编闯大厂8年，阿里前P8坦言后悔了</span></a><div data-v-a264b01a="" class="author-wrapper"><a data-v-a264b01a="" aria-current="page" href="/user/profile/67f8fd81000000000e010b43?channel_type=web_user_page&amp;parent_page_channel_type=web_user_board&amp;xsec_token=&amp;xsec_source=pc_note" class="active router-link-exact-active author" target="_blank"><img data-v-a264b01a="" src="https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo31lvmkfehl80g5pvovm0ji2q3r980kf0?imageView2/2/w/60/format/webp|imageMogr2/strip" fetchpriority="auto" width="20" height="20" crossorigin="anonymous" loading="lazy" decoding="async" data-xhs-img="" class="author-avatar"><span data-v-a264b01a="" class="name">大厂电报</span></a><span data-v-dc3a3972="" data-v-a264b01a="" class="like-wrapper like-active"><span data-v-dc3a3972="" class="like-lottie" style="width: 16px; height: 16px;"></span><svg data-v-55b36ac6="" data-v-dc3a3972="" class="reds-icon like-icon" width="16" height="16"><use data-v-55b36ac6="" xlink:href="#like"></use></svg><span data-v-dc3a3972="" class="count" selected-disabled-search="">25</span></span></div></div></div></section><section data-v-a264b01a="" data-v-330d9cca="" class="note-item" data-width="1200" data-height="1600" data-index="15" style="--68479076: 16px; --1bd4d75c: 238.6px; --1e4add76: blur(42.5px); transform: translate(787.8px, 1263px);"><div data-v-a264b01a=""><a data-v-a264b01a="" href="/explore/68b9a25d000000001d0296d2" style="display: none;"></a><a data-v-a264b01a="" class="cover mask ld" target="_self" href="/user/profile/67f8fd81000000000e010b43/68b9a25d000000001d0296d2?xsec_token=ABTk71fNEul7zAXn0OLf_fL-P6u2CInnYTitFf6-tiiu0=&amp;xsec_source=pc_user" style="height: 318px;"><img data-v-a264b01a="" src="https://sns-webpic-qc.xhscdn.com/202509081416/faeaf8365012793e1335c556550ad047/1040g2sg31m0va2i95e705pvovm0ji2q31i151ag!nc_n_webp_mw_1" fetchpriority="auto" loading="lazy" decoding="async" data-xhs-img="" style="width: 100%; height: 100%; object-fit: cover;"><!----><!----><!----></a><div data-v-a264b01a="" class="footer"><a data-v-a264b01a="" target="_self" class="title"><span data-v-51ec0135="" data-v-a264b01a="">字节Seed狂发期权，惹了其他部门众怒！</span></a><div data-v-a264b01a="" class="author-wrapper"><a data-v-a264b01a="" aria-current="page" href="/user/profile/67f8fd81000000000e010b43?channel_type=web_user_page&amp;parent_page_channel_type=web_user_board&amp;xsec_token=&amp;xsec_source=pc_note" class="active router-link-exact-active author" target="_blank"><img data-v-a264b01a="" src="https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo31lvmkfehl80g5pvovm0ji2q3r980kf0?imageView2/2/w/60/format/webp|imageMogr2/strip" fetchpriority="auto" width="20" height="20" crossorigin="anonymous" loading="lazy" decoding="async" data-xhs-img="" class="author-avatar"><span data-v-a264b01a="" class="name">大厂电报</span></a><span data-v-dc3a3972="" data-v-a264b01a="" class="like-wrapper like-active"><span data-v-dc3a3972="" class="like-lottie" style="width: 16px; height: 16px;"></span><svg data-v-55b36ac6="" data-v-dc3a3972="" class="reds-icon like-icon" width="16" height="16"><use data-v-55b36ac6="" xlink:href="#like"></use></svg><span data-v-dc3a3972="" class="count" selected-disabled-search="">10</span></span></div></div></div></section><section data-v-a264b01a="" data-v-330d9cca="" class="note-item" data-width="1200" data-height="1600" data-index="16" style="--68479076: 16px; --1bd4d75c: 238.6px; --1e4add76: blur(42.5px); transform: translate(262.6px, 1683px);"><div data-v-a264b01a=""><a data-v-a264b01a="" href="/explore/68b99714000000001d0261c2" style="display: none;"></a><a data-v-a264b01a="" class="cover mask ld" target="_self" href="/user/profile/67f8fd81000000000e010b43/68b99714000000001d0261c2?xsec_token=ABTk71fNEul7zAXn0OLf_fL1uKdeqOKkmFR8S237YRXmQ=&amp;xsec_source=pc_user" style="height: 318px;"><img data-v-a264b01a="" src="https://sns-webpic-qc.xhscdn.com/202509081416/b99b40e64c4052672b0a24e881c6c4a6/1040g00831m0ca02c58405pvovm0ji2q31q4vgug!nc_n_webp_mw_1" fetchpriority="auto" loading="lazy" decoding="async" data-xhs-img="" style="width: 100%; height: 100%; object-fit: cover;"><!----><!----><!----></a><div data-v-a264b01a="" class="footer"><a data-v-a264b01a="" target="_self" class="title"><span data-v-51ec0135="" data-v-a264b01a="">突发！奢侈品牌阿玛尼创始人离世</span></a><div data-v-a264b01a="" class="author-wrapper"><a data-v-a264b01a="" aria-current="page" href="/user/profile/67f8fd81000000000e010b43?channel_type=web_user_page&amp;parent_page_channel_type=web_user_board&amp;xsec_token=&amp;xsec_source=pc_note" class="active router-link-exact-active author" target="_blank"><img data-v-a264b01a="" src="https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo31lvmkfehl80g5pvovm0ji2q3r980kf0?imageView2/2/w/60/format/webp|imageMogr2/strip" fetchpriority="auto" width="20" height="20" crossorigin="anonymous" loading="lazy" decoding="async" data-xhs-img="" class="author-avatar"><span data-v-a264b01a="" class="name">大厂电报</span></a><span data-v-dc3a3972="" data-v-a264b01a="" class="like-wrapper like-active"><span data-v-dc3a3972="" class="like-lottie" style="width: 16px; height: 16px;"></span><svg data-v-55b36ac6="" data-v-dc3a3972="" class="reds-icon like-icon" width="16" height="16"><use data-v-55b36ac6="" xlink:href="#like"></use></svg><span data-v-dc3a3972="" class="count" selected-disabled-search="">7</span></span></div></div></div></section><section data-v-a264b01a="" data-v-330d9cca="" class="note-item" data-width="1200" data-height="1600" data-index="17" style="--68479076: 16px; --1bd4d75c: 238.6px; --1e4add76: blur(42.5px); transform: translate(0px, 1684px);"><div data-v-a264b01a=""><a data-v-a264b01a="" href="/explore/68b9967f000000001d034f3c" style="display: none;"></a><a data-v-a264b01a="" class="cover mask ld" target="_self" href="/user/profile/67f8fd81000000000e010b43/68b9967f000000001d034f3c?xsec_token=ABTk71fNEul7zAXn0OLf_fLyKMX9mF53Ako3MBqpFZsTU=&amp;xsec_source=pc_user" style="height: 318px;"><img data-v-a264b01a="" src="https://sns-webpic-qc.xhscdn.com/202509081416/a99901597197e904790b639bada5cf7b/1040g00831m0ca02c583g5pvovm0ji2q3lbo9gb0!nc_n_webp_mw_1" fetchpriority="auto" loading="lazy" decoding="async" data-xhs-img="" style="width: 100%; height: 100%; object-fit: cover;"><!----><!----><!----></a><div data-v-a264b01a="" class="footer"><a data-v-a264b01a="" target="_self" class="title"><span data-v-51ec0135="" data-v-a264b01a="">银行高管私吞客户上亿元，被害人竟然是……</span></a><div data-v-a264b01a="" class="author-wrapper"><a data-v-a264b01a="" aria-current="page" href="/user/profile/67f8fd81000000000e010b43?channel_type=web_user_page&amp;parent_page_channel_type=web_user_board&amp;xsec_token=&amp;xsec_source=pc_note" class="active router-link-exact-active author" target="_blank"><img data-v-a264b01a="" src="https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo31lvmkfehl80g5pvovm0ji2q3r980kf0?imageView2/2/w/60/format/webp|imageMogr2/strip" fetchpriority="auto" width="20" height="20" crossorigin="anonymous" loading="lazy" decoding="async" data-xhs-img="" class="author-avatar"><span data-v-a264b01a="" class="name">大厂电报</span></a><span data-v-dc3a3972="" data-v-a264b01a="" class="like-wrapper like-active"><span data-v-dc3a3972="" class="like-lottie" style="width: 16px; height: 16px;"></span><svg data-v-55b36ac6="" data-v-dc3a3972="" class="reds-icon like-icon" width="16" height="16"><use data-v-55b36ac6="" xlink:href="#like"></use></svg><span data-v-dc3a3972="" class="count" selected-disabled-search="">41</span></span></div></div></div></section><section data-v-a264b01a="" data-v-330d9cca="" class="note-item" data-width="1200" data-height="1600" data-index="18" style="--68479076: 16px; --1bd4d75c: 238.6px; --1e4add76: blur(42.5px); transform: translate(525.2px, 1684px);"><div data-v-a264b01a=""><a data-v-a264b01a="" href="/explore/68b968d7000000001d02ccf5" style="display: none;"></a><a data-v-a264b01a="" class="cover mask ld" target="_self" href="/user/profile/67f8fd81000000000e010b43/68b968d7000000001d02ccf5?xsec_token=ABTk71fNEul7zAXn0OLf_fL3BKdlR49s5Wv0oxpWlq8uE=&amp;xsec_source=pc_user" style="height: 318px;"><img data-v-a264b01a="" src="https://sns-webpic-qc.xhscdn.com/202509081416/a96075534a494348ee09683c3a07b448/1040g00831m0md7fl5e205pvovm0ji2q3pda5k20!nc_n_webp_mw_1" fetchpriority="auto" loading="lazy" decoding="async" data-xhs-img="" style="width: 100%; height: 100%; object-fit: cover;"><!----><!----><!----></a><div data-v-a264b01a="" class="footer"><a data-v-a264b01a="" target="_self" class="title"><span data-v-51ec0135="" data-v-a264b01a="">字节发布通报，直接辞退100人</span></a><div data-v-a264b01a="" class="author-wrapper"><a data-v-a264b01a="" aria-current="page" href="/user/profile/67f8fd81000000000e010b43?channel_type=web_user_page&amp;parent_page_channel_type=web_user_board&amp;xsec_token=&amp;xsec_source=pc_note" class="active router-link-exact-active author" target="_blank"><img data-v-a264b01a="" src="https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo31lvmkfehl80g5pvovm0ji2q3r980kf0?imageView2/2/w/60/format/webp|imageMogr2/strip" fetchpriority="auto" width="20" height="20" crossorigin="anonymous" loading="lazy" decoding="async" data-xhs-img="" class="author-avatar"><span data-v-a264b01a="" class="name">大厂电报</span></a><span data-v-dc3a3972="" data-v-a264b01a="" class="like-wrapper like-active"><span data-v-dc3a3972="" class="like-lottie" style="width: 16px; height: 16px;"></span><svg data-v-55b36ac6="" data-v-dc3a3972="" class="reds-icon like-icon" width="16" height="16"><use data-v-55b36ac6="" xlink:href="#like"></use></svg><span data-v-dc3a3972="" class="count" selected-disabled-search="">13</span></span></div></div></div></section><section data-v-a264b01a="" data-v-330d9cca="" class="note-item" data-width="1200" data-height="1600" data-index="19" style="--68479076: 16px; --1bd4d75c: 238.6px; --1e4add76: blur(42.5px); transform: translate(787.8px, 1684px);"><div data-v-a264b01a=""><a data-v-a264b01a="" href="/explore/68b95ccb000000001d01a4cc" style="display: none;"></a><a data-v-a264b01a="" class="cover mask ld" target="_self" href="/user/profile/67f8fd81000000000e010b43/68b95ccb000000001d01a4cc?xsec_token=ABTk71fNEul7zAXn0OLf_fLxO7mJggEz6YnA6MYuoUVzM=&amp;xsec_source=pc_user" style="height: 318px;"><img data-v-a264b01a="" src="https://sns-webpic-qc.xhscdn.com/202509081416/cc687ffb66605fed0c9167426254f429/1040g00831m0md7fl5e6g5pvovm0ji2q37alpc90!nc_n_webp_mw_1" fetchpriority="auto" loading="lazy" decoding="async" data-xhs-img="" style="width: 100%; height: 100%; object-fit: cover;"><!----><!----><!----></a><div data-v-a264b01a="" class="footer"><a data-v-a264b01a="" target="_self" class="title"><span data-v-51ec0135="" data-v-a264b01a="">🚗先看看中国汽车8月销量:</span></a><div data-v-a264b01a="" class="author-wrapper"><a data-v-a264b01a="" aria-current="page" href="/user/profile/67f8fd81000000000e010b43?channel_type=web_user_page&amp;parent_page_channel_type=web_user_board&amp;xsec_token=&amp;xsec_source=pc_note" class="active router-link-exact-active author" target="_blank"><img data-v-a264b01a="" src="https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo31lvmkfehl80g5pvovm0ji2q3r980kf0?imageView2/2/w/60/format/webp|imageMogr2/strip" fetchpriority="auto" width="20" height="20" crossorigin="anonymous" loading="lazy" decoding="async" data-xhs-img="" class="author-avatar"><span data-v-a264b01a="" class="name">大厂电报</span></a><span data-v-dc3a3972="" data-v-a264b01a="" class="like-wrapper like-active"><span data-v-dc3a3972="" class="like-lottie" style="width: 16px; height: 16px;"></span><svg data-v-55b36ac6="" data-v-dc3a3972="" class="reds-icon like-icon" width="16" height="16"><use data-v-55b36ac6="" xlink:href="#like"></use></svg><span data-v-dc3a3972="" class="count" selected-disabled-search="">6</span></span></div></div></div></section><section data-v-a264b01a="" data-v-330d9cca="" class="note-item" data-width="1200" data-height="1600" data-index="20" style="--68479076: 16px; --1bd4d75c: 238.6px; --1e4add76: blur(42.5px); transform: translate(262.6px, 2085px);"><div data-v-a264b01a=""><a data-v-a264b01a="" href="/explore/68b93352000000001d038be6" style="display: none;"></a><a data-v-a264b01a="" class="cover mask ld" target="_self" href="/user/profile/67f8fd81000000000e010b43/68b93352000000001d038be6?xsec_token=ABTk71fNEul7zAXn0OLf_fL3V_dL3cHLjZ6-_SHPdwLcw=&amp;xsec_source=pc_user" style="height: 318px;"><img data-v-a264b01a="" src="https://sns-webpic-qc.xhscdn.com/202509081416/b3bf9c7f3a3354ecb8c2c5f2fcb03e94/1040g00831m0ca02c58205pvovm0ji2q3obtb950!nc_n_webp_mw_1" fetchpriority="auto" loading="lazy" decoding="async" data-xhs-img="" style="width: 100%; height: 100%; object-fit: cover;"><!----><!----><!----></a><div data-v-a264b01a="" class="footer"><a data-v-a264b01a="" target="_self" class="title"><span data-v-51ec0135="" data-v-a264b01a="">字节芯片团队权限被注销？回应来了</span></a><div data-v-a264b01a="" class="author-wrapper"><a data-v-a264b01a="" aria-current="page" href="/user/profile/67f8fd81000000000e010b43?channel_type=web_user_page&amp;parent_page_channel_type=web_user_board&amp;xsec_token=&amp;xsec_source=pc_note" class="active router-link-exact-active author" target="_blank"><img data-v-a264b01a="" src="https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo31lvmkfehl80g5pvovm0ji2q3r980kf0?imageView2/2/w/60/format/webp|imageMogr2/strip" fetchpriority="auto" width="20" height="20" crossorigin="anonymous" loading="lazy" decoding="async" data-xhs-img="" class="author-avatar"><span data-v-a264b01a="" class="name">大厂电报</span></a><span data-v-dc3a3972="" data-v-a264b01a="" class="like-wrapper like-active"><span data-v-dc3a3972="" class="like-lottie" style="width: 16px; height: 16px;"></span><svg data-v-55b36ac6="" data-v-dc3a3972="" class="reds-icon like-icon" width="16" height="16"><use data-v-55b36ac6="" xlink:href="#like"></use></svg><span data-v-dc3a3972="" class="count" selected-disabled-search="">8</span></span></div></div></div></section><section data-v-a264b01a="" data-v-330d9cca="" class="note-item" data-width="1200" data-height="1600" data-index="21" style="--68479076: 16px; --1bd4d75c: 238.6px; --1e4add76: blur(42.5px); transform: translate(525.2px, 2086px);"><div data-v-a264b01a=""><a data-v-a264b01a="" href="/explore/68b930ba000000001d01d12c" style="display: none;"></a><a data-v-a264b01a="" class="cover mask ld" target="_self" href="/user/profile/67f8fd81000000000e010b43/68b930ba000000001d01d12c?xsec_token=ABTk71fNEul7zAXn0OLf_fL_jn-qEWrUELjMcpnM4X9dw=&amp;xsec_source=pc_user" style="height: 318px;"><img data-v-a264b01a="" src="https://sns-webpic-qc.xhscdn.com/202509081416/41bbec32de89582991aab70ad0b74833/1040g00831m0ca02c581g5pvovm0ji2q34fhc740!nc_n_webp_mw_1" fetchpriority="auto" loading="lazy" decoding="async" data-xhs-img="" style="width: 100%; height: 100%; object-fit: cover;"><!----><!----><!----></a><div data-v-a264b01a="" class="footer"><a data-v-a264b01a="" target="_self" class="title"><span data-v-51ec0135="" data-v-a264b01a="">爆料！SHEIN团建还要员工AA，挪年假或调休补</span></a><div data-v-a264b01a="" class="author-wrapper"><a data-v-a264b01a="" aria-current="page" href="/user/profile/67f8fd81000000000e010b43?channel_type=web_user_page&amp;parent_page_channel_type=web_user_board&amp;xsec_token=&amp;xsec_source=pc_note" class="active router-link-exact-active author" target="_blank"><img data-v-a264b01a="" src="https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo31lvmkfehl80g5pvovm0ji2q3r980kf0?imageView2/2/w/60/format/webp|imageMogr2/strip" fetchpriority="auto" width="20" height="20" crossorigin="anonymous" loading="lazy" decoding="async" data-xhs-img="" class="author-avatar"><span data-v-a264b01a="" class="name">大厂电报</span></a><span data-v-dc3a3972="" data-v-a264b01a="" class="like-wrapper like-active"><span data-v-dc3a3972="" class="like-lottie" style="width: 16px; height: 16px;"></span><svg data-v-55b36ac6="" data-v-dc3a3972="" class="reds-icon like-icon" width="16" height="16"><use data-v-55b36ac6="" xlink:href="#like"></use></svg><span data-v-dc3a3972="" class="count" selected-disabled-search="">153</span></span></div></div></div></section><section data-v-a264b01a="" data-v-330d9cca="" class="note-item" data-width="1200" data-height="1600" data-index="22" style="--68479076: 16px; --1bd4d75c: 238.6px; --1e4add76: blur(42.5px); transform: translate(787.8px, 2086px);"><div data-v-a264b01a=""><a data-v-a264b01a="" href="/explore/68b90ea3000000001d02413a" style="display: none;"></a><a data-v-a264b01a="" class="cover mask ld" target="_self" href="/user/profile/67f8fd81000000000e010b43/68b90ea3000000001d02413a?xsec_token=ABTk71fNEul7zAXn0OLf_fL-aYcZk5zuEmxLkg3H-_LEw=&amp;xsec_source=pc_user" style="height: 318px;"><img data-v-a264b01a="" src="https://sns-webpic-qc.xhscdn.com/202509081416/2ec139befd7b4386c1da17c905588dcd/1040g00831m0ca02c580g5pvovm0ji2q3i0r34v8!nc_n_webp_mw_1" fetchpriority="auto" loading="lazy" decoding="async" data-xhs-img="" style="width: 100%; height: 100%; object-fit: cover;"><!----><!----><!----></a><div data-v-a264b01a="" class="footer"><a data-v-a264b01a="" target="_self" class="title"><span data-v-51ec0135="" data-v-a264b01a="">某乎运营爆料：年薪30K*15，年终奖连续打折</span></a><div data-v-a264b01a="" class="author-wrapper"><a data-v-a264b01a="" aria-current="page" href="/user/profile/67f8fd81000000000e010b43?channel_type=web_user_page&amp;parent_page_channel_type=web_user_board&amp;xsec_token=&amp;xsec_source=pc_note" class="active router-link-exact-active author" target="_blank"><img data-v-a264b01a="" src="https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo31lvmkfehl80g5pvovm0ji2q3r980kf0?imageView2/2/w/60/format/webp|imageMogr2/strip" fetchpriority="auto" width="20" height="20" crossorigin="anonymous" loading="lazy" decoding="async" data-xhs-img="" class="author-avatar"><span data-v-a264b01a="" class="name">大厂电报</span></a><span data-v-dc3a3972="" data-v-a264b01a="" class="like-wrapper like-active"><span data-v-dc3a3972="" class="like-lottie" style="width: 16px; height: 16px;"></span><svg data-v-55b36ac6="" data-v-dc3a3972="" class="reds-icon like-icon" width="16" height="16"><use data-v-55b36ac6="" xlink:href="#like"></use></svg><span data-v-dc3a3972="" class="count" selected-disabled-search="">4</span></span></div></div></div></section><section data-v-a264b01a="" data-v-330d9cca="" class="note-item" data-width="1200" data-height="1600" data-index="23" style="--68479076: 16px; --1bd4d75c: 238.6px; --1e4add76: blur(42.5px); transform: translate(0px, 2105px);"><div data-v-a264b01a=""><a data-v-a264b01a="" href="/explore/68b86297000000001d02325f" style="display: none;"></a><a data-v-a264b01a="" class="cover mask ld" target="_self" href="/user/profile/67f8fd81000000000e010b43/68b86297000000001d02325f?xsec_token=ABB5oj41e5tyRt7zaMZnbQ4P5XWnRvx8WPo_k8hQU-EwQ=&amp;xsec_source=pc_user" style="height: 318px;"><img data-v-a264b01a="" src="https://sns-webpic-qc.xhscdn.com/202509081416/1b75774ce80b1512516fff2475ba97e1/1040g2sg31lvm66a2lif05pvovm0ji2q344i9jqg!nc_n_webp_mw_1" fetchpriority="auto" loading="lazy" decoding="async" data-xhs-img="" style="width: 100%; height: 100%; object-fit: cover;"><!----><!----><!----></a><div data-v-a264b01a="" class="footer"><a data-v-a264b01a="" target="_self" class="title"><span data-v-51ec0135="" data-v-a264b01a="">京东员工300万天津买房血泪史，太扎心了！</span></a><div data-v-a264b01a="" class="author-wrapper"><a data-v-a264b01a="" aria-current="page" href="/user/profile/67f8fd81000000000e010b43?channel_type=web_user_page&amp;parent_page_channel_type=web_user_board&amp;xsec_token=&amp;xsec_source=pc_note" class="active router-link-exact-active author" target="_blank"><img data-v-a264b01a="" src="https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo31lvmkfehl80g5pvovm0ji2q3r980kf0?imageView2/2/w/60/format/webp|imageMogr2/strip" fetchpriority="auto" width="20" height="20" crossorigin="anonymous" loading="lazy" decoding="async" data-xhs-img="" class="author-avatar"><span data-v-a264b01a="" class="name">大厂电报</span></a><span data-v-dc3a3972="" data-v-a264b01a="" class="like-wrapper like-active"><span data-v-dc3a3972="" class="like-lottie" style="width: 16px; height: 16px;"></span><svg data-v-55b36ac6="" data-v-dc3a3972="" class="reds-icon like-icon" width="16" height="16"><use data-v-55b36ac6="" xlink:href="#like"></use></svg><span data-v-dc3a3972="" class="count" selected-disabled-search="">104</span></span></div></div></div></section><!--]--><!--[--><!--]--><!--[--><!--]--><!--[--><!--]--><!--[--><!--]--><!--[--><!--]--></div><!--[--><div class="loading" data-v-5a8e0ee8="" data-v-330d9cca-s=""><div class="feeds-loading" data-v-5a8e0ee8="" data-v-330d9cca-s="" data-v-820f2ae6=""><div class="animate" style="width:30px;height:30px;" data-v-820f2ae6=""><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 50 50" width="50" height="50" preserveAspectRatio="xMidYMid meet" style="width: 100%; height: 100%; transform: translate3d(0px, 0px, 0px); content-visibility: visible;"><defs><clipPath id="__lottie_element_2"><rect width="50" height="50" x="0" y="0"></rect></clipPath><clipPath id="__lottie_element_4"><path d="M0,0 L100,0 L100,100 L0,100z"></path></clipPath><clipPath id="__lottie_element_8"><path d="M0,0 L100,0 L100,100 L0,100z"></path></clipPath><clipPath id="__lottie_element_15"><path d="M0,0 L100,0 L100,100 L0,100z"></path></clipPath></defs><g clip-path="url(#__lottie_element_2)"><g clip-path="url(#__lottie_element_4)" transform="matrix(0.5,0,0,0.5,0,0)" opacity="1" style="display: block;"><g clip-path="url(#__lottie_element_15)" transform="matrix(0,1,-1,0,100,0)" opacity="1" style="display: block;"><g transform="matrix(0,1,-1,0,100,0)" opacity="1" style="display: block;"><g opacity="1" transform="matrix(1,0,0,1,50,34.277000427246094)"><path stroke-linecap="round" stroke-linejoin="miter" fill-opacity="0" stroke-miterlimit="10" stroke="rgb(204,204,204)" stroke-opacity="1" stroke-width="6" d=" M24.156999588012695,9.276000022888184 C21.312999725341797,-1.406000018119812 11.57800006866455,-9.277000427246094 0.0010000000474974513,-9.277000427246094 C-11.57699966430664,-9.277000427246094 -21.312999725341797,-1.4049999713897705 -24.1560001373291,9.277000427246094"></path></g></g></g><g clip-path="url(#__lottie_element_8)" transform="matrix(0,-1,1,0,0,100)" opacity="1" style="display: block;"><g transform="matrix(0,1,-1,0,100,0)" opacity="1" style="display: block;"><g opacity="1" transform="matrix(1,0,0,1,50,34.277000427246094)"><path stroke-linecap="round" stroke-linejoin="miter" fill-opacity="0" stroke-miterlimit="10" stroke="rgb(204,204,204)" stroke-opacity="1" stroke-width="6" d=" M24.156999588012695,9.276000022888184 C21.312999725341797,-1.406000018119812 11.57800006866455,-9.277000427246094 0.0010000000474974513,-9.277000427246094 C-11.57699966430664,-9.277000427246094 -21.312999725341797,-1.4049999713897705 -24.1560001373291,9.277000427246094"></path></g></g></g></g></g></svg></div><span data-v-820f2ae6="">加载中</span></div></div><!--]--><!----><!--]--><!----><!----></div><div class="tab-content-item static-layout" style="height: auto; width: 1026.4px; overflow: scroll;" data-v-bb2dbd52="" data-v-64126f47=""><div class="sub-tab-list" data-v-64126f47=""><div class="tertiary left reds-tabs-list" style="padding:0px 0px;" data-v-64126f47=""><!--[--><!--]--><!--[--><!--]--><!----><div class="active-tag" style="width:0px;left:0px;transition:;"></div></div></div><!--[--><div id="" class="feeds-container static-layout" style="width: 100%; height: auto; visibility: visible;" data-v-330d9cca=""><!--[--><!--]--><!--[--><!--]--><!--[--><!--]--><!--[--><!--]--><!--[--><div class="empty-container" hide-collect="true" data-v-5a8e0ee8="" data-v-330d9cca-s=""><div class="empty"><svg class="reds-icon empty-icon" width="90" height="90" data-v-55b36ac6=""><use xlink:href="#user_empty_collect" data-v-55b36ac6=""></use></svg><!--[--><span class="empty-text">该用户已设置收藏内容不可见</span><!--]--></div></div><!--]--><!--[--><!--]--></div><!--[--><div class="loading" data-v-5a8e0ee8="" data-v-330d9cca-s=""><div class="feeds-loading" data-v-5a8e0ee8="" data-v-330d9cca-s="" data-v-820f2ae6=""><div class="animate" style="width:30px;height:30px;" data-v-820f2ae6=""><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 50 50" width="50" height="50" preserveAspectRatio="xMidYMid meet" style="width: 100%; height: 100%; transform: translate3d(0px, 0px, 0px); content-visibility: visible;"><defs><clipPath id="__lottie_element_22"><rect width="50" height="50" x="0" y="0"></rect></clipPath><clipPath id="__lottie_element_24"><path d="M0,0 L100,0 L100,100 L0,100z"></path></clipPath><clipPath id="__lottie_element_28"><path d="M0,0 L100,0 L100,100 L0,100z"></path></clipPath><clipPath id="__lottie_element_35"><path d="M0,0 L100,0 L100,100 L0,100z"></path></clipPath></defs><g clip-path="url(#__lottie_element_22)"><g clip-path="url(#__lottie_element_24)" transform="matrix(0.5,0,0,0.5,0,0)" opacity="1" style="display: block;"><g clip-path="url(#__lottie_element_35)" transform="matrix(0,1,-1,0,100,0)" opacity="1" style="display: block;"><g transform="matrix(0,1,-1,0,100,0)" opacity="1" style="display: block;"><g opacity="1" transform="matrix(1,0,0,1,50,34.277000427246094)"><path stroke-linecap="round" stroke-linejoin="miter" fill-opacity="0" stroke-miterlimit="10" stroke="rgb(204,204,204)" stroke-opacity="1" stroke-width="6" d=" M24.156999588012695,9.276000022888184 C21.312999725341797,-1.406000018119812 11.57800006866455,-9.277000427246094 0.0010000000474974513,-9.277000427246094 C-11.57699966430664,-9.277000427246094 -21.312999725341797,-1.4049999713897705 -24.1560001373291,9.277000427246094"></path></g></g></g><g clip-path="url(#__lottie_element_28)" transform="matrix(0,-1,1,0,0,100)" opacity="1" style="display: block;"><g transform="matrix(0,1,-1,0,100,0)" opacity="1" style="display: block;"><g opacity="1" transform="matrix(1,0,0,1,50,34.277000427246094)"><path stroke-linecap="round" stroke-linejoin="miter" fill-opacity="0" stroke-miterlimit="10" stroke="rgb(204,204,204)" stroke-opacity="1" stroke-width="6" d=" M24.156999588012695,9.276000022888184 C21.312999725341797,-1.406000018119812 11.57800006866455,-9.277000427246094 0.0010000000474974513,-9.277000427246094 C-11.57699966430664,-9.277000427246094 -21.312999725341797,-1.4049999713897705 -24.1560001373291,9.277000427246094"></path></g></g></g></g></g></svg></div><span data-v-820f2ae6="">加载中</span></div></div><!--]--><!----><!--]--><!----><!----></div><!--]--></div></div><!--]--><!----><div data-v-2ed9bdf4="" data-v-8069da68="" class="floating-btn-sets"><div data-v-4559bcd4="" data-v-8069da68="" data-v-2ed9bdf4-s="" class="back-top"><div data-v-4559bcd4="" class="btn-wrapper"><svg data-v-55b36ac6="" data-v-4559bcd4="" class="reds-icon" width="20" height="20"><use data-v-55b36ac6="" xlink:href="#arrow_top"></use></svg></div><div data-v-4559bcd4="" class="tip-container"><span data-v-4559bcd4="" class="tip-text">回到顶部</span></div></div></div><!----><!----><!--]--></div><!----><!--[--><!--]--><!----><!--]--><!--]--></div><div class="bottom-menu" data-v-34b87540="" data-v-3661fbb1=""><div class="channel-list" data-v-3661fbb1=""><!--[--><!--[--><div class="bottom-channel" data-v-3661fbb1=""><a href="/explore?channel_id=homefeed_recommend&amp;channel_type=web_user_page" class="bottom-channel" target="_self" data-v-3661fbb1=""><svg class="reds-icon" width="24" height="24" data-v-3661fbb1="" data-v-55b36ac6=""><use xlink:href="#home" data-v-55b36ac6=""></use></svg><span class="text" data-v-3661fbb1="">发现</span></a></div><!--]--><!--[--><div class="bottom-channel" data-v-3661fbb1=""><a target="_blank" href="https://creator.xiaohongshu.com/publish/publish?source=official" class="bottom-channel" data-v-3661fbb1=""><svg class="reds-icon" width="24" height="24" data-v-3661fbb1="" data-v-55b36ac6=""><use xlink:href="#creator" data-v-55b36ac6=""></use></svg><span class="text" data-v-3661fbb1="">发布</span></a></div><!--]--><!--[--><li class="link-wrapper bottom-channel" data-v-3661fbb1="" data-v-13c4f3b9=""><a href="/notification" class="link-wrapper bottom-channel" data-v-13c4f3b9=""><div class="badge-container" data-v-13c4f3b9="" data-v-0755b6ef=""><!--[--><svg class="reds-icon text-active" width="24" height="24" data-v-13c4f3b9="" data-v-0755b6ef-s="" data-v-55b36ac6=""><use xlink:href="#notification" data-v-55b36ac6=""></use></svg><!--]--><!----></div><span class="text channel" data-v-13c4f3b9="">通知</span></a></li><!--]--><!--[--><!--[--><!--[--><li class="user side-bar-component" data-v-a93a7d02=""><div class="link-wrapper" data-v-a93a7d02=""><a href="/user/profile/63ba6442000000002600603e" class="link-wrapper" data-v-a93a7d02=""><span class="reds-image-container gray responsive reds-avatar size-s" style="width:24px;" data-v-a93a7d02=""><!----><span class="reds-img-placeholder" style="padding-top: 100%;"></span><picture class="reds-img-box"><img crossorigin="anonymous" width="24" height="24" src="https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo31hms3tqmk2605otqch19go1uavoscag?imageView2/2/w/360/format/webp" data-load-status="loaded" loading="lazy" class="reds-img"></picture><div class="reds-img-box"><!----><!----><!--[--><i class="reds-avatar-border"></i><!--[--><!--]--><!--]--></div></span><span class="channel" data-v-a93a7d02="">我</span></a></div></li><!--]--><div class="bottom-channel bottom-menu-component" data-v-a93a7d02=""><a href="/user/profile/63ba6442000000002600603e" class="bottom-channel" data-v-a93a7d02=""><svg class="reds-icon" width="24" height="24" data-v-a93a7d02="" data-v-55b36ac6=""><use xlink:href="#me" data-v-55b36ac6=""></use></svg><span class="text" data-v-a93a7d02="">我</span></a><!----></div><!--]--><!--]--><!--]--></div></div></div></div><!--]--><div data-v-7a413e2c="" class="reds-alert"><div class="reds-alert-mask" style="display: none;"></div><div class="reds-alert-wrapper slot-content" style="width: 270px; display: none;"><!----><!----><div class="reds-alert-title"> </div><div class="reds-alert-content"><!----><!----></div><div class="reds-alert-footer reds-alert-footer__round-button vertical"><button class="reds-button-new reds-alert-footer__left small text reds-alert-footer__left"><span class="reds-button-new-box"><!----><span class="reds-button-new-text">我要申诉</span></span></button><button class="reds-button-new reds-alert-footer__right rounded medium primary reds-alert-footer__right rounded"><span class="reds-button-new-box"><!----><span class="reds-button-new-text">我知道了</span></span></button></div></div></div><div data-v-50d98839="" class="ad-wrap"></div><div data-v-50d98839="" class="reds-alert"><div class="reds-alert-mask" style="display: none;"></div><div class="reds-alert-wrapper slot-content" style="width: 270px; display: none;"><!----><!----><div class="reds-alert-title"><div data-v-50d98839="" class="title"> 温馨提示 </div> </div><div class="reds-alert-content"><!----><!----><div data-v-50d98839="" class="text"> 您的浏览器似乎开启了广告屏蔽插件，可能对正常使用造成影响，请移除插件或将小红书加入插件白名单后继续使用。 </div></div><div class="reds-alert-footer reds-alert-footer__round-button vertical"><!----><button class="reds-button-new reds-alert-footer__right block rounded medium primary reds-alert-footer__right block rounded"><span class="reds-button-new-box"><!----><span class="reds-button-new-text">我知道了</span></span></button></div></div></div><!----><!----><!----><!----><div data-v-fc1041fa="" class="container out right"><div data-v-fc1041fa="" class="header fullscreen-header"><div data-v-fc1041fa="" class="left"><button data-v-fc1041fa="" class="reds-button-new large icon has-icon pure-icon"><span class="reds-button-new-box"><svg data-v-55b36ac6="" class="reds-icon reds-button__icon" width="16px" height="16px"><use data-v-55b36ac6="" xlink:href="#ic_arrow_left"></use></svg><!----></span></button></div><div data-v-fc1041fa="" class="title"> 活动 </div><div data-v-fc1041fa="" class="right"><button data-v-fc1041fa="" class="reds-button-new large icon has-icon pure-icon"><span class="reds-button-new-box"><svg data-v-55b36ac6="" class="reds-icon reds-button__icon" width="16px" height="16px"><use data-v-55b36ac6="" xlink:href="#ic_share"></use></svg><!----></span></button></div></div><div data-v-fc1041fa="" class="header panel-header"><div data-v-fc1041fa="" class="left"><div data-v-fc1041fa=""><button data-v-fc1041fa="" class="reds-button-new dragger large icon has-icon pure-icon dragger"><span class="reds-button-new-box"><svg data-v-55b36ac6="" class="reds-icon reds-button__icon" width="16px" height="16px"><use data-v-55b36ac6="" xlink:href="#ic_dragger"></use></svg><!----></span></button></div></div><div data-v-fc1041fa="" class="title"> 活动 </div><div data-v-fc1041fa="" class="right"><div data-v-5cde0260="" data-v-fc1041fa="" class="anchor"><!----><button data-v-5cde0260="" class="reds-button-new share-icon large icon has-icon pure-icon share-icon"><span class="reds-button-new-box"><svg data-v-55b36ac6="" class="reds-icon reds-button__icon" width="16px" height="16px"><use data-v-55b36ac6="" xlink:href="#ic_share"></use></svg><!----></span></button></div><button data-v-fc1041fa="" class="reds-button-new close-icon large icon has-icon pure-icon close-icon"><span class="reds-button-new-box"><svg data-v-55b36ac6="" class="reds-icon reds-button__icon" width="16px" height="16px"><use data-v-55b36ac6="" xlink:href="#ic_close"></use></svg><!----></span></button></div></div><iframe data-v-fc1041fa="" src=""></iframe></div><!--]--><!--]--><!--]--><!--]--></div><script>window.__SSR__=true</script><script>window.__INITIAL_STATE__={"global":{"appSettings":{"notificationInterval":30,"prefetchTimeout":3001,"prefetchRedisExpires":259200000,"searchFilterGuideConfig":{"maxDailyShow":1,"maxTotalShow":3,"showInterval":1,"validDays":15,"autoCloseDelay":5000},"retryFeeds":true,"grayModeConfig":{"global":false,"dateRange":["2023-08-01 00:00:00","2023-08-19 23:59:59"],"greyRule":{"layout":{"enable":false,"pages":["Explore"]},"pages":["Explore"]},"disableLikeNotes":["64ce36f7000000000c036ba5"],"disableSearchHint":false},"NIO":true,"ICPInfoList":[{"label":"沪ICP备13030189号","link":"\u002F\u002Fbeian.miit.gov.cn\u002F","title":"小红书_沪ICP备"},{"label":"营业执照","link":"\u002F\u002Ffe-video-qc.xhscdn.com\u002Ffe-platform\u002F5581076bd6b6af2e0e943abb024ad0e16f2ebff6.pdf","title":"小红书_营业执照"},{"label":"2024沪公网安备31010102002533号","link":"\u002F\u002Fwww.beian.gov.cn\u002Fportal\u002FregisterSystemInfo?recordcode=31010102002533","title":"小红书_沪公网安备"},{"label":"增值电信业务经营许可证：沪B2-20150021","link":"\u002F\u002Ffe-video-qc.xhscdn.com\u002Ffe-platform-file\u002F104101b831hhkkll23u0678gtks7tu70004en2n231udpe","title":"小红书_网文"},{"label":"医疗器械网络交易服务第三方平台备案：(沪)网械平台备字[2019]第00006号","link":"\u002F\u002Ffe-video-qc.xhscdn.com\u002Ffe-platform\u002F410dce57bc12a6d7e5808060e47644fbe46f68ff.pdf","title":"小红书_医疗器械网络交易服务"},{"label":"互联网药品信息服务资格证书：(沪)-经营性-2023-0144","link":"\u002F\u002Ffe-video-qc.xhscdn.com\u002Ffe-platform\u002Ff37a08cacc088061beb38329c387c32fc48fc6fe.pdf","title":"小红书_互联网药品信息服务"},{"label":"违法不良信息举报电话：4006676810","link":"\u002F\u002Fwww.shjbzx.cn","title":"小红书_上海市互联网举报中心"},{"label":"上海市互联网举报中心","link":"\u002F\u002Fwww.shjbzx.cn","title":"小红书_上海市互联网举报中心"},{"label":"网上有害信息举报专区","link":"\u002F\u002Fwww.12377.cn","title":"网上有害信息举报专区"},{"label":"自营经营者信息","link":"\u002F\u002Fdc.xhscdn.com\u002F06c2adb0-b353-11e9-9d0c-7be9ff8961c1\u002F自营经营者信息公示.pdf","title":"小红书_沪公网安备"},{"label":"网络文化经营许可证：沪网文(2024)1344-086号","link":"\u002F\u002Ffe-video-qc.xhscdn.com\u002Ffe-platform\u002F7970f6e8b70aedc995ba273d04b6b6751abcd63c.pdf","title":"小红书_网络文化经营许可"},{"label":"个性化推荐算法 网信算备310101216601302230019号","link":"https:\u002F\u002Fbeian.cac.gov.cn\u002Fapi\u002Fstatic\u002FfileUpload\u002FprincipalOrithm\u002Fadditional\u002Fuser_c015445c-80ac-45f7-94d7-3871e961b1fe_d4425f3b-7f35-45af-b8d4-badd4424d6d5.pdf"}],"disableBanAlert":"false","showAdBlockAlert":0},"supportWebp":true,"serverTime":1757312197312,"grayMode":false,"referer":"https:\u002F\u002Fwww.xiaohongshu.com\u002Fexplore","pwaAddDesktopPrompt":undefined,"firstVisitUrl":undefined,"easyAccessModalVisible":{"addDesktopGuide":false,"collectGuide":false,"keyboardList":false,"miniWindowGuide":false},"currentLayout":"default","fullscreenLocking":false,"feedbackPopupVisible":false,"trackFps":false,"supportAVIF":true,"imgFormatCollect":{"ssr":["jpg","webp","avif"],"csr":["jpg"]},"isUndertake":false},"user":{"loggedIn":true,"activated":false,"userInfo":{"user_id":"63ba6442000000002600603e","nickname":"🌈胖胖的AI小岛✨","desc":"欢迎登岛！🏝️ 我是岛主胖胖。\n在这里，我用AI构筑一个温暖、治愈的世界。\n愿每一张图，都能成为你数字生活里的一个小小的慰藉。\n偶尔掉落AI创作心得和前沿资讯。\n📧aigc0520@163.com","gender":0,"images":"https:\u002F\u002Fsns-avatar-qc.xhscdn.com\u002Favatar\u002F1040g2jo31hms3tqmk2605otqch19go1uavoscag?imageView2\u002F2\u002Fw\u002F360\u002Fformat\u002Fwebp","imageb":"https:\u002F\u002Fsns-avatar-qc.xhscdn.com\u002Favatar\u002F1040g2jo31hms3tqmk2605otqch19go1uavoscag?imageView2\u002F2\u002Fw\u002F540\u002Fformat\u002Fwebp","guest":false,"red_id":"5319674636","userId":"63ba6442000000002600603e","redId":"5319674636"},"follow":[],"userPageData":{"tabPublic":{"collection":false,"collectionNote":{"display":false,"lock":false,"count":0},"collectionBoard":{"display":false,"lock":false,"count":0}},"extraInfo":{"fstatus":"none","blockType":"DEFAULT"},"result":{"message":"success","success":true,"code":0},"basicInfo":{"ipLocation":"北京","desc":"大厂资讯，每日电报\n带你了解大厂动态和商业逻辑，看清大厂风云\n有瓜速报，有料敢说，如有涉侵权随时踢我修改","imageb":"https:\u002F\u002Fsns-avatar-qc.xhscdn.com\u002Favatar\u002F1040g2jo31lvmkfehl80g5pvovm0ji2q3r980kf0?imageView2\u002F2\u002Fw\u002F540\u002Fformat\u002Fwebp","nickname":"大厂电报","images":"https:\u002F\u002Fsns-avatar-qc.xhscdn.com\u002Favatar\u002F1040g2jo31lvmkfehl80g5pvovm0ji2q3r980kf0?imageView2\u002F2\u002Fw\u002F360\u002Fformat\u002Fwebp","redId":"95396675528","gender":0},"interactions":[{"count":"39","type":"follows","name":"关注"},{"type":"fans","name":"粉丝","count":"25383"},{"type":"interaction","name":"获赞与收藏","count":"91787"}],"tags":[{"tagType":"info","icon":"http:\u002F\u002Fci.xiaohongshu.com\u002Ficons\u002Fuser\u002Fgender-male-v1.png"}]},"activeTab":{"key":0,"index":0,"query":"note","label":"笔记","lock":false,"subTabs":null,"feedType":0},"notes":[[{"id":"68bbfa85000000001d023c91","noteCard":{"type":"normal","displayTitle":"联通中标300万大单，腾讯云不服投诉，逆转了","user":{"nickName":"大厂电报","avatar":"https:\u002F\u002Fsns-avatar-qc.xhscdn.com\u002Favatar\u002F1040g2jo31lvmkfehl80g5pvovm0ji2q3r980kf0","userId":"67f8fd81000000000e010b43","nickname":"大厂电报"},"interactInfo":{"liked":false,"likedCount":"678","sticky":true},"cover":{"width":1200,"url":"","traceId":"","infoList":[{"imageScene":"WB_PRV","url":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002Fa86f8d3aa1117436b94b35563463b188\u002F1040g2sg31m38d73llmt05pvovm0ji2q3egnrdso!nc_n_webp_prv_1"},{"imageScene":"WB_DFT","url":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002F88049fbe310fb6d9042ff342757a4287\u002F1040g2sg31m38d73llmt05pvovm0ji2q3egnrdso!nc_n_webp_mw_1"}],"urlPre":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002Fa86f8d3aa1117436b94b35563463b188\u002F1040g2sg31m38d73llmt05pvovm0ji2q3egnrdso!nc_n_webp_prv_1","urlDefault":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002F88049fbe310fb6d9042ff342757a4287\u002F1040g2sg31m38d73llmt05pvovm0ji2q3egnrdso!nc_n_webp_mw_1","fileId":"","height":1600},"noteId":"68bbfa85000000001d023c91","xsecToken":"ABFIekrUMbMDCgiDUoz3KyuSRNNWYBGcJ_vSPS_4SLx6A="},"index":0,"exposed":false,"ssrRendered":true,"xsecToken":"ABFIekrUMbMDCgiDUoz3KyuSRNNWYBGcJ_vSPS_4SLx6A="},{"id":"68baa2e3000000001d02ce69","noteCard":{"cover":{"infoList":[{"imageScene":"WB_PRV","url":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002F83b31483899746dfd276e3d47056cd10\u002F1040g2sg31m2rmme64qhg5nv613509bs8upnjnlg!nc_n_webp_prv_1"},{"imageScene":"WB_DFT","url":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002F7bdeab8ced93c345e6bdb7cd2cead218\u002F1040g2sg31m2rmme64qhg5nv613509bs8upnjnlg!nc_n_webp_mw_1"}],"urlPre":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002F83b31483899746dfd276e3d47056cd10\u002F1040g2sg31m2rmme64qhg5nv613509bs8upnjnlg!nc_n_webp_prv_1","urlDefault":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002F7bdeab8ced93c345e6bdb7cd2cead218\u002F1040g2sg31m2rmme64qhg5nv613509bs8upnjnlg!nc_n_webp_mw_1","fileId":"","height":1757,"width":1320,"url":"","traceId":""},"noteId":"68baa2e3000000001d02ce69","xsecToken":"ABI_lIrulwxGs1-dlc0OoaSn0MQEFqpF7fpyKNyBwBAs0=","type":"normal","displayTitle":"杭州估值百亿独角兽暴雷？已三个月未发工资","user":{"nickName":"大厂电报","avatar":"https:\u002F\u002Fsns-avatar-qc.xhscdn.com\u002Favatar\u002F1040g2jo31lvmkfehl80g5pvovm0ji2q3r980kf0","userId":"67f8fd81000000000e010b43","nickname":"大厂电报"},"interactInfo":{"liked":false,"likedCount":"723","sticky":true}},"index":1,"exposed":false,"ssrRendered":true,"xsecToken":"ABI_lIrulwxGs1-dlc0OoaSn0MQEFqpF7fpyKNyBwBAs0="},{"id":"68bd9986000000001d01f20b","noteCard":{"interactInfo":{"liked":false,"likedCount":"22","sticky":false},"cover":{"urlDefault":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002Fb62ba595501960a0b6b16a8617711c31\u002F1040g2sg31m4qr2knm8e05pvovm0ji2q3o5pp998!nc_n_webp_mw_1","fileId":"","height":1600,"width":1200,"url":"","traceId":"","infoList":[{"imageScene":"WB_PRV","url":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002F0dfb62c8e4f88a1adf59c4c37808aad6\u002F1040g2sg31m4qr2knm8e05pvovm0ji2q3o5pp998!nc_n_webp_prv_1"},{"imageScene":"WB_DFT","url":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002Fb62ba595501960a0b6b16a8617711c31\u002F1040g2sg31m4qr2knm8e05pvovm0ji2q3o5pp998!nc_n_webp_mw_1"}],"urlPre":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002F0dfb62c8e4f88a1adf59c4c37808aad6\u002F1040g2sg31m4qr2knm8e05pvovm0ji2q3o5pp998!nc_n_webp_prv_1"},"noteId":"68bd9986000000001d01f20b","xsecToken":"AB1l0HATZhILIBw3X4ghyQ3mix3f--GaDJZCPGNJQPuxk=","type":"normal","displayTitle":"前百度员工：离开大厂后，才知道有多难","user":{"avatar":"https:\u002F\u002Fsns-avatar-qc.xhscdn.com\u002Favatar\u002F1040g2jo31lvmkfehl80g5pvovm0ji2q3r980kf0","userId":"67f8fd81000000000e010b43","nickname":"大厂电报","nickName":"大厂电报"}},"index":2,"exposed":false,"ssrRendered":true,"xsecToken":"AB1l0HATZhILIBw3X4ghyQ3mix3f--GaDJZCPGNJQPuxk="},{"id":"68bd7f96000000001d0234d7","noteCard":{"xsecToken":"AB1l0HATZhILIBw3X4ghyQ3t1b4kC85WnEKQO0OYcO4Fw=","type":"normal","displayTitle":"中元节当天，这家倒闭的新势力竟宣布复活了","user":{"userId":"67f8fd81000000000e010b43","nickname":"大厂电报","nickName":"大厂电报","avatar":"https:\u002F\u002Fsns-avatar-qc.xhscdn.com\u002Favatar\u002F1040g2jo31lvmkfehl80g5pvovm0ji2q3r980kf0"},"interactInfo":{"liked":false,"likedCount":"3","sticky":false},"cover":{"traceId":"","infoList":[{"imageScene":"WB_PRV","url":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002Fffa2188162e17c826e5383722af45447\u002F1040g00831m4mkmdim64g5pvovm0ji2q314cbf4g!nc_n_webp_prv_1"},{"imageScene":"WB_DFT","url":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002F02e3f53435c14f28f4c05978d81c0801\u002F1040g00831m4mkmdim64g5pvovm0ji2q314cbf4g!nc_n_webp_mw_1"}],"urlPre":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002Fffa2188162e17c826e5383722af45447\u002F1040g00831m4mkmdim64g5pvovm0ji2q314cbf4g!nc_n_webp_prv_1","urlDefault":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002F02e3f53435c14f28f4c05978d81c0801\u002F1040g00831m4mkmdim64g5pvovm0ji2q314cbf4g!nc_n_webp_mw_1","fileId":"","height":1600,"width":1200,"url":""},"noteId":"68bd7f96000000001d0234d7"},"index":3,"exposed":false,"ssrRendered":true,"xsecToken":"AB1l0HATZhILIBw3X4ghyQ3t1b4kC85WnEKQO0OYcO4Fw="},{"id":"68bd71da000000001d03afb3","noteCard":{"user":{"nickName":"大厂电报","avatar":"https:\u002F\u002Fsns-avatar-qc.xhscdn.com\u002Favatar\u002F1040g2jo31lvmkfehl80g5pvovm0ji2q3r980kf0","userId":"67f8fd81000000000e010b43","nickname":"大厂电报"},"interactInfo":{"liked":false,"likedCount":"9","sticky":false},"cover":{"url":"","traceId":"","infoList":[{"imageScene":"WB_PRV","url":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002F755cc00f159ceed275d0a7d6b0ddc304\u002F1040g00831m4m9op15i1g5pvovm0ji2q3e6ekos8!nc_n_webp_prv_1"},{"imageScene":"WB_DFT","url":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002F94895e8807e1f0ce100ccd43ceda838d\u002F1040g00831m4m9op15i1g5pvovm0ji2q3e6ekos8!nc_n_webp_mw_1"}],"urlPre":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002F755cc00f159ceed275d0a7d6b0ddc304\u002F1040g00831m4m9op15i1g5pvovm0ji2q3e6ekos8!nc_n_webp_prv_1","urlDefault":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002F94895e8807e1f0ce100ccd43ceda838d\u002F1040g00831m4m9op15i1g5pvovm0ji2q3e6ekos8!nc_n_webp_mw_1","fileId":"","height":1600,"width":1200},"noteId":"68bd71da000000001d03afb3","xsecToken":"AB1l0HATZhILIBw3X4ghyQ3msn9J9S0-DeZb8C1-m9a5Y=","type":"normal","displayTitle":"突发！13年知名亲子旅游平台一夜暴雷！"},"index":4,"exposed":false,"ssrRendered":true,"xsecToken":"AB1l0HATZhILIBw3X4ghyQ3msn9J9S0-DeZb8C1-m9a5Y="},{"id":"68bcea41000000001d025011","noteCard":{"user":{"nickname":"大厂电报","nickName":"大厂电报","avatar":"https:\u002F\u002Fsns-avatar-qc.xhscdn.com\u002Favatar\u002F1040g2jo31lvmkfehl80g5pvovm0ji2q3r980kf0","userId":"67f8fd81000000000e010b43"},"interactInfo":{"liked":false,"likedCount":"28","sticky":false},"cover":{"width":1320,"url":"","traceId":"","infoList":[{"imageScene":"WB_PRV","url":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002F85d5dc8aac6f306311e23fd8ade46a23\u002F1040g2sg31m44ta90ks3g5nv613509bs83hcqdto!nc_n_webp_prv_1"},{"imageScene":"WB_DFT","url":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002F094eadf20125c53ed75a82fa0442dbb9\u002F1040g2sg31m44ta90ks3g5nv613509bs83hcqdto!nc_n_webp_mw_1"}],"urlPre":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002F85d5dc8aac6f306311e23fd8ade46a23\u002F1040g2sg31m44ta90ks3g5nv613509bs83hcqdto!nc_n_webp_prv_1","urlDefault":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002F094eadf20125c53ed75a82fa0442dbb9\u002F1040g2sg31m44ta90ks3g5nv613509bs83hcqdto!nc_n_webp_mw_1","fileId":"","height":1753},"noteId":"68bcea41000000001d025011","xsecToken":"ABBB6pzUpDgnwINr0J48WQ7vqrZCPIZ0mDNiDq6LiH_k0=","type":"normal","displayTitle":"前百度高管创业失败：1.5万元欠薪都还不起"},"index":5,"exposed":false,"ssrRendered":true,"xsecToken":"ABBB6pzUpDgnwINr0J48WQ7vqrZCPIZ0mDNiDq6LiH_k0="},{"id":"68bc5f1b000000001d021f0d","noteCard":{"noteId":"68bc5f1b000000001d021f0d","xsecToken":"ABBB6pzUpDgnwINr0J48WQ7iluC_i7H_BDtFXMdE_p5F4=","type":"normal","displayTitle":"国内IT公司暴雷！欠薪10个月，员工集体炸锅","user":{"nickName":"大厂电报","avatar":"https:\u002F\u002Fsns-avatar-qc.xhscdn.com\u002Favatar\u002F1040g2jo31lvmkfehl80g5pvovm0ji2q3r980kf0","userId":"67f8fd81000000000e010b43","nickname":"大厂电报"},"interactInfo":{"liked":false,"likedCount":"333","sticky":false},"cover":{"infoList":[{"imageScene":"WB_PRV","url":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002F64d8fb70fb13fff5e2ddec103025b854\u002F1040g2sg31m3k2krrlihg5pvovm0ji2q3ff05ek8!nc_n_webp_prv_1"},{"imageScene":"WB_DFT","url":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002F6be756bafc3e45c0a8dd99fdecb9e0f6\u002F1040g2sg31m3k2krrlihg5pvovm0ji2q3ff05ek8!nc_n_webp_mw_1"}],"urlPre":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002F64d8fb70fb13fff5e2ddec103025b854\u002F1040g2sg31m3k2krrlihg5pvovm0ji2q3ff05ek8!nc_n_webp_prv_1","urlDefault":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002F6be756bafc3e45c0a8dd99fdecb9e0f6\u002F1040g2sg31m3k2krrlihg5pvovm0ji2q3ff05ek8!nc_n_webp_mw_1","fileId":"","height":1600,"width":1200,"url":"","traceId":""}},"index":6,"exposed":false,"ssrRendered":true,"xsecToken":"ABBB6pzUpDgnwINr0J48WQ7iluC_i7H_BDtFXMdE_p5F4="},{"id":"68bc5a37000000001d037391","noteCard":{"xsecToken":"ABBB6pzUpDgnwINr0J48WQ7sjjQXGh7Nox3Re3P8QnbZo=","type":"normal","displayTitle":"苏宁欠4600万不还，玩\"空壳公司\"被法院锤爆","user":{"nickName":"大厂电报","avatar":"https:\u002F\u002Fsns-avatar-qc.xhscdn.com\u002Favatar\u002F1040g2jo31lvmkfehl80g5pvovm0ji2q3r980kf0","userId":"67f8fd81000000000e010b43","nickname":"大厂电报"},"interactInfo":{"liked":false,"likedCount":"140","sticky":false},"cover":{"urlPre":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002F13d3bf8b9ad2e3efb417a13905c9131f\u002F1040g2sg31m3k2krrlie05pvovm0ji2q3v5ue3a0!nc_n_webp_prv_1","urlDefault":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002Fdf40db2bc083b04d8b239e2abf8c5b8d\u002F1040g2sg31m3k2krrlie05pvovm0ji2q3v5ue3a0!nc_n_webp_mw_1","fileId":"","height":1600,"width":1200,"url":"","traceId":"","infoList":[{"imageScene":"WB_PRV","url":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002F13d3bf8b9ad2e3efb417a13905c9131f\u002F1040g2sg31m3k2krrlie05pvovm0ji2q3v5ue3a0!nc_n_webp_prv_1"},{"imageScene":"WB_DFT","url":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002Fdf40db2bc083b04d8b239e2abf8c5b8d\u002F1040g2sg31m3k2krrlie05pvovm0ji2q3v5ue3a0!nc_n_webp_mw_1"}]},"noteId":"68bc5a37000000001d037391"},"index":7,"exposed":false,"ssrRendered":true,"xsecToken":"ABBB6pzUpDgnwINr0J48WQ7sjjQXGh7Nox3Re3P8QnbZo="},{"id":"68bb97d9000000001d023c21","noteCard":{"type":"normal","displayTitle":"什么事，中国移动还能发通告「处理」中国电信？","user":{"nickName":"大厂电报","avatar":"https:\u002F\u002Fsns-avatar-qc.xhscdn.com\u002Favatar\u002F1040g2jo31lvmkfehl80g5pvovm0ji2q3r980kf0","userId":"67f8fd81000000000e010b43","nickname":"大厂电报"},"interactInfo":{"liked":false,"likedCount":"45","sticky":false},"cover":{"width":1200,"url":"","traceId":"","infoList":[{"imageScene":"WB_PRV","url":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002Fd9e40f1cfb72134f964bc198b2c5c108\u002F1040g2sg31m2rmme64qh05nv613509bs853j283o!nc_n_webp_prv_1"},{"imageScene":"WB_DFT","url":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002Fe552f0716651fa94c4d9e50c77068297\u002F1040g2sg31m2rmme64qh05nv613509bs853j283o!nc_n_webp_mw_1"}],"urlPre":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002Fd9e40f1cfb72134f964bc198b2c5c108\u002F1040g2sg31m2rmme64qh05nv613509bs853j283o!nc_n_webp_prv_1","urlDefault":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002Fe552f0716651fa94c4d9e50c77068297\u002F1040g2sg31m2rmme64qh05nv613509bs853j283o!nc_n_webp_mw_1","fileId":"","height":1600},"noteId":"68bb97d9000000001d023c21","xsecToken":"ABFIekrUMbMDCgiDUoz3KyuUAJb3qMY4kNCT5AC2tE6II="},"index":8,"exposed":false,"ssrRendered":true,"xsecToken":"ABFIekrUMbMDCgiDUoz3KyuUAJb3qMY4kNCT5AC2tE6II="},{"id":"68baff66000000001d039de3","noteCard":{"user":{"nickName":"大厂电报","avatar":"https:\u002F\u002Fsns-avatar-qc.xhscdn.com\u002Favatar\u002F1040g2jo31lvmkfehl80g5pvovm0ji2q3r980kf0","userId":"67f8fd81000000000e010b43","nickname":"大厂电报"},"interactInfo":{"liked":false,"likedCount":"6","sticky":false},"cover":{"infoList":[{"imageScene":"WB_PRV","url":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002F090dab8978b5c09e79a54f9e6373e12d\u002F1040g00831m29g70pm61g5pc1uuf86hauajanej8!nc_n_webp_prv_1"},{"imageScene":"WB_DFT","url":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002F6409e36d545082d25bfde65a5f1ed620\u002F1040g00831m29g70pm61g5pc1uuf86hauajanej8!nc_n_webp_mw_1"}],"urlPre":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002F090dab8978b5c09e79a54f9e6373e12d\u002F1040g00831m29g70pm61g5pc1uuf86hauajanej8!nc_n_webp_prv_1","urlDefault":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002F6409e36d545082d25bfde65a5f1ed620\u002F1040g00831m29g70pm61g5pc1uuf86hauajanej8!nc_n_webp_mw_1","fileId":"","height":1600,"width":1200,"url":"","traceId":""},"noteId":"68baff66000000001d039de3","xsecToken":"ABI_lIrulwxGs1-dlc0OoaSt-fWNvDKpRkTnTyCBH-MAY=","type":"normal","displayTitle":"特斯拉为留马斯克，开出1万亿美元薪酬！"},"index":9,"exposed":false,"ssrRendered":true,"xsecToken":"ABI_lIrulwxGs1-dlc0OoaSt-fWNvDKpRkTnTyCBH-MAY="},{"id":"68ba9a60000000001d029000","noteCard":{"type":"normal","displayTitle":"医械行业巨头康乐保，将在中国大规模裁员","user":{"nickName":"大厂电报","avatar":"https:\u002F\u002Fsns-avatar-qc.xhscdn.com\u002Favatar\u002F1040g2jo31lvmkfehl80g5pvovm0ji2q3r980kf0","userId":"67f8fd81000000000e010b43","nickname":"大厂电报"},"interactInfo":{"liked":false,"likedCount":"7","sticky":false},"cover":{"width":1200,"url":"","traceId":"","infoList":[{"imageScene":"WB_PRV","url":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002Fa8eb2750f9f4a8eae94ed35592acb900\u002F1040g2sg31m1rs34fl2gg5nv613509bs808tjar8!nc_n_webp_prv_1"},{"url":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002F2399ca7edb908827a03262c570ead19e\u002F1040g2sg31m1rs34fl2gg5nv613509bs808tjar8!nc_n_webp_mw_1","imageScene":"WB_DFT"}],"urlPre":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002Fa8eb2750f9f4a8eae94ed35592acb900\u002F1040g2sg31m1rs34fl2gg5nv613509bs808tjar8!nc_n_webp_prv_1","urlDefault":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002F2399ca7edb908827a03262c570ead19e\u002F1040g2sg31m1rs34fl2gg5nv613509bs808tjar8!nc_n_webp_mw_1","fileId":"","height":1600},"noteId":"68ba9a60000000001d029000","xsecToken":"ABI_lIrulwxGs1-dlc0OoaSl8Cd_099PWpvRDsh4tT4mk="},"index":10,"exposed":false,"ssrRendered":true,"xsecToken":"ABI_lIrulwxGs1-dlc0OoaSl8Cd_099PWpvRDsh4tT4mk="},{"id":"68ba959f000000001d020212","noteCard":{"type":"normal","displayTitle":"腾讯智影关停！同名公众号、视频号同步注销","user":{"nickName":"大厂电报","avatar":"https:\u002F\u002Fsns-avatar-qc.xhscdn.com\u002Favatar\u002F1040g2jo31lvmkfehl80g5pvovm0ji2q3r980kf0","userId":"67f8fd81000000000e010b43","nickname":"大厂电报"},"interactInfo":{"liked":false,"likedCount":"5","sticky":false},"cover":{"fileId":"","height":1600,"width":1200,"url":"","traceId":"","infoList":[{"imageScene":"WB_PRV","url":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002F3972523f959623ffda8b59ca61ceff9b\u002F1040g2sg31m1rs34fl2g05nv613509bs8b40t5n0!nc_n_webp_prv_1"},{"url":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002Ff84e03a9276a4f1f7f0fe1fd6f3bdd0e\u002F1040g2sg31m1rs34fl2g05nv613509bs8b40t5n0!nc_n_webp_mw_1","imageScene":"WB_DFT"}],"urlPre":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002F3972523f959623ffda8b59ca61ceff9b\u002F1040g2sg31m1rs34fl2g05nv613509bs8b40t5n0!nc_n_webp_prv_1","urlDefault":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002Ff84e03a9276a4f1f7f0fe1fd6f3bdd0e\u002F1040g2sg31m1rs34fl2g05nv613509bs8b40t5n0!nc_n_webp_mw_1"},"noteId":"68ba959f000000001d020212","xsecToken":"ABI_lIrulwxGs1-dlc0OoaSoRc3ZnNtKxrkqetXpFajKk="},"index":11,"exposed":false,"ssrRendered":true,"xsecToken":"ABI_lIrulwxGs1-dlc0OoaSoRc3ZnNtKxrkqetXpFajKk="},{"id":"68ba93d8000000001d0270de","noteCard":{"cover":{"height":1600,"width":1200,"url":"","traceId":"","infoList":[{"imageScene":"WB_PRV","url":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002F8b47b03c4a86ee96765e457c0ef6bb25\u002F1040g2sg31m1rs34fl2f05nv613509bs8ebmhgog!nc_n_webp_prv_1"},{"imageScene":"WB_DFT","url":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002Ff0d5a99b06e4f76e9811f26e535eb1e9\u002F1040g2sg31m1rs34fl2f05nv613509bs8ebmhgog!nc_n_webp_mw_1"}],"urlPre":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002F8b47b03c4a86ee96765e457c0ef6bb25\u002F1040g2sg31m1rs34fl2f05nv613509bs8ebmhgog!nc_n_webp_prv_1","urlDefault":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002Ff0d5a99b06e4f76e9811f26e535eb1e9\u002F1040g2sg31m1rs34fl2f05nv613509bs8ebmhgog!nc_n_webp_mw_1","fileId":""},"noteId":"68ba93d8000000001d0270de","xsecToken":"ABI_lIrulwxGs1-dlc0OoaSpiqNtkUFq4hjbe2V6qooY0=","type":"normal","displayTitle":"英伟达对华再推新芯片，向中国市场服软了吗？","user":{"nickName":"大厂电报","avatar":"https:\u002F\u002Fsns-avatar-qc.xhscdn.com\u002Favatar\u002F1040g2jo31lvmkfehl80g5pvovm0ji2q3r980kf0","userId":"67f8fd81000000000e010b43","nickname":"大厂电报"},"interactInfo":{"sticky":false,"liked":false,"likedCount":"3"}},"index":12,"exposed":false,"ssrRendered":true,"xsecToken":"ABI_lIrulwxGs1-dlc0OoaSpiqNtkUFq4hjbe2V6qooY0="},{"id":"68b9ac32000000001d0289c0","noteCard":{"noteId":"68b9ac32000000001d0289c0","xsecToken":"ABTk71fNEul7zAXn0OLf_fLzmJAr06wmtYv0zxz9EfcOY=","type":"normal","displayTitle":"违规收集数据，Shein被重罚至少12亿！","user":{"nickName":"大厂电报","avatar":"https:\u002F\u002Fsns-avatar-qc.xhscdn.com\u002Favatar\u002F1040g2jo31lvmkfehl80g5pvovm0ji2q3r980kf0","userId":"67f8fd81000000000e010b43","nickname":"大厂电报"},"interactInfo":{"liked":false,"likedCount":"24","sticky":false},"cover":{"urlDefault":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002F9cd6d23763229597aee61037e182704f\u002F1040g2sg31m0va2i95e8g5pvovm0ji2q35chfn30!nc_n_webp_mw_1","fileId":"","height":1600,"width":1200,"url":"","traceId":"","infoList":[{"imageScene":"WB_PRV","url":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002F36a5abcc617e7fc2ebbfc34d7f6f5a82\u002F1040g2sg31m0va2i95e8g5pvovm0ji2q35chfn30!nc_n_webp_prv_1"},{"imageScene":"WB_DFT","url":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002F9cd6d23763229597aee61037e182704f\u002F1040g2sg31m0va2i95e8g5pvovm0ji2q35chfn30!nc_n_webp_mw_1"}],"urlPre":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002F36a5abcc617e7fc2ebbfc34d7f6f5a82\u002F1040g2sg31m0va2i95e8g5pvovm0ji2q35chfn30!nc_n_webp_prv_1"}},"index":13,"exposed":false,"ssrRendered":true,"xsecToken":"ABTk71fNEul7zAXn0OLf_fLzmJAr06wmtYv0zxz9EfcOY="},{"id":"68b9a4e7000000001d0233f1","noteCard":{"type":"normal","displayTitle":"市直副科辞编闯大厂8年，阿里前P8坦言后悔了","user":{"nickname":"大厂电报","nickName":"大厂电报","avatar":"https:\u002F\u002Fsns-avatar-qc.xhscdn.com\u002Favatar\u002F1040g2jo31lvmkfehl80g5pvovm0ji2q3r980kf0","userId":"67f8fd81000000000e010b43"},"interactInfo":{"sticky":false,"liked":false,"likedCount":"25"},"cover":{"height":1600,"width":1200,"url":"","traceId":"","infoList":[{"imageScene":"WB_PRV","url":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002F3d93682660463b91ee32bdca5953da81\u002F1040g2sg31m0va2i95e805pvovm0ji2q3fc0eg68!nc_n_webp_prv_1"},{"url":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002F5aa29f934ccfd4412cecba5e6d7b0200\u002F1040g2sg31m0va2i95e805pvovm0ji2q3fc0eg68!nc_n_webp_mw_1","imageScene":"WB_DFT"}],"urlPre":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002F3d93682660463b91ee32bdca5953da81\u002F1040g2sg31m0va2i95e805pvovm0ji2q3fc0eg68!nc_n_webp_prv_1","urlDefault":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002F5aa29f934ccfd4412cecba5e6d7b0200\u002F1040g2sg31m0va2i95e805pvovm0ji2q3fc0eg68!nc_n_webp_mw_1","fileId":""},"noteId":"68b9a4e7000000001d0233f1","xsecToken":"ABTk71fNEul7zAXn0OLf_fL6eqme5cPazkWaqJt8hEZGE="},"index":14,"exposed":false,"ssrRendered":true,"xsecToken":"ABTk71fNEul7zAXn0OLf_fL6eqme5cPazkWaqJt8hEZGE="},{"id":"68b9a25d000000001d0296d2","noteCard":{"displayTitle":"字节Seed狂发期权，惹了其他部门众怒！","user":{"nickName":"大厂电报","avatar":"https:\u002F\u002Fsns-avatar-qc.xhscdn.com\u002Favatar\u002F1040g2jo31lvmkfehl80g5pvovm0ji2q3r980kf0","userId":"67f8fd81000000000e010b43","nickname":"大厂电报"},"interactInfo":{"liked":false,"likedCount":"10","sticky":false},"cover":{"height":1600,"width":1200,"url":"","traceId":"","infoList":[{"imageScene":"WB_PRV","url":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002F2b89b93172f5fe7e8b51a87be257246b\u002F1040g2sg31m0va2i95e705pvovm0ji2q31i151ag!nc_n_webp_prv_1"},{"imageScene":"WB_DFT","url":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002Ffaeaf8365012793e1335c556550ad047\u002F1040g2sg31m0va2i95e705pvovm0ji2q31i151ag!nc_n_webp_mw_1"}],"urlPre":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002F2b89b93172f5fe7e8b51a87be257246b\u002F1040g2sg31m0va2i95e705pvovm0ji2q31i151ag!nc_n_webp_prv_1","urlDefault":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002Ffaeaf8365012793e1335c556550ad047\u002F1040g2sg31m0va2i95e705pvovm0ji2q31i151ag!nc_n_webp_mw_1","fileId":""},"noteId":"68b9a25d000000001d0296d2","xsecToken":"ABTk71fNEul7zAXn0OLf_fL-P6u2CInnYTitFf6-tiiu0=","type":"normal"},"index":15,"exposed":false,"ssrRendered":true,"xsecToken":"ABTk71fNEul7zAXn0OLf_fL-P6u2CInnYTitFf6-tiiu0="},{"id":"68b99714000000001d0261c2","noteCard":{"xsecToken":"ABTk71fNEul7zAXn0OLf_fL1uKdeqOKkmFR8S237YRXmQ=","type":"normal","displayTitle":"突发！奢侈品牌阿玛尼创始人离世","user":{"nickName":"大厂电报","avatar":"https:\u002F\u002Fsns-avatar-qc.xhscdn.com\u002Favatar\u002F1040g2jo31lvmkfehl80g5pvovm0ji2q3r980kf0","userId":"67f8fd81000000000e010b43","nickname":"大厂电报"},"interactInfo":{"likedCount":"7","sticky":false,"liked":false},"cover":{"fileId":"","height":1600,"width":1200,"url":"","traceId":"","infoList":[{"imageScene":"WB_PRV","url":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002Fcdcebbb640266074ef0e6f838dad0ca2\u002F1040g00831m0ca02c58405pvovm0ji2q31q4vgug!nc_n_webp_prv_1"},{"imageScene":"WB_DFT","url":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002Fb99b40e64c4052672b0a24e881c6c4a6\u002F1040g00831m0ca02c58405pvovm0ji2q31q4vgug!nc_n_webp_mw_1"}],"urlPre":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002Fcdcebbb640266074ef0e6f838dad0ca2\u002F1040g00831m0ca02c58405pvovm0ji2q31q4vgug!nc_n_webp_prv_1","urlDefault":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002Fb99b40e64c4052672b0a24e881c6c4a6\u002F1040g00831m0ca02c58405pvovm0ji2q31q4vgug!nc_n_webp_mw_1"},"noteId":"68b99714000000001d0261c2"},"index":16,"exposed":false,"ssrRendered":true,"xsecToken":"ABTk71fNEul7zAXn0OLf_fL1uKdeqOKkmFR8S237YRXmQ="},{"id":"68b9967f000000001d034f3c","noteCard":{"interactInfo":{"liked":false,"likedCount":"41","sticky":false},"cover":{"urlPre":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002Fc7b4bf69de329cfb6ec6f919e73d47b0\u002F1040g00831m0ca02c583g5pvovm0ji2q3lbo9gb0!nc_n_webp_prv_1","urlDefault":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002Fa99901597197e904790b639bada5cf7b\u002F1040g00831m0ca02c583g5pvovm0ji2q3lbo9gb0!nc_n_webp_mw_1","fileId":"","height":1600,"width":1200,"url":"","traceId":"","infoList":[{"imageScene":"WB_PRV","url":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002Fc7b4bf69de329cfb6ec6f919e73d47b0\u002F1040g00831m0ca02c583g5pvovm0ji2q3lbo9gb0!nc_n_webp_prv_1"},{"url":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002Fa99901597197e904790b639bada5cf7b\u002F1040g00831m0ca02c583g5pvovm0ji2q3lbo9gb0!nc_n_webp_mw_1","imageScene":"WB_DFT"}]},"noteId":"68b9967f000000001d034f3c","xsecToken":"ABTk71fNEul7zAXn0OLf_fLyKMX9mF53Ako3MBqpFZsTU=","type":"normal","displayTitle":"银行高管私吞客户上亿元，被害人竟然是……","user":{"avatar":"https:\u002F\u002Fsns-avatar-qc.xhscdn.com\u002Favatar\u002F1040g2jo31lvmkfehl80g5pvovm0ji2q3r980kf0","userId":"67f8fd81000000000e010b43","nickname":"大厂电报","nickName":"大厂电报"}},"index":17,"exposed":false,"ssrRendered":true,"xsecToken":"ABTk71fNEul7zAXn0OLf_fLyKMX9mF53Ako3MBqpFZsTU="},{"id":"68b968d7000000001d02ccf5","noteCard":{"noteId":"68b968d7000000001d02ccf5","xsecToken":"ABTk71fNEul7zAXn0OLf_fL3BKdlR49s5Wv0oxpWlq8uE=","type":"normal","displayTitle":"字节发布通报，直接辞退100人","user":{"nickName":"大厂电报","avatar":"https:\u002F\u002Fsns-avatar-qc.xhscdn.com\u002Favatar\u002F1040g2jo31lvmkfehl80g5pvovm0ji2q3r980kf0","userId":"67f8fd81000000000e010b43","nickname":"大厂电报"},"interactInfo":{"liked":false,"likedCount":"13","sticky":false},"cover":{"url":"","traceId":"","infoList":[{"imageScene":"WB_PRV","url":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002Fc58d61760fc00b933d1c82882d5da895\u002F1040g00831m0md7fl5e205pvovm0ji2q3pda5k20!nc_n_webp_prv_1"},{"imageScene":"WB_DFT","url":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002Fa96075534a494348ee09683c3a07b448\u002F1040g00831m0md7fl5e205pvovm0ji2q3pda5k20!nc_n_webp_mw_1"}],"urlPre":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002Fc58d61760fc00b933d1c82882d5da895\u002F1040g00831m0md7fl5e205pvovm0ji2q3pda5k20!nc_n_webp_prv_1","urlDefault":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002Fa96075534a494348ee09683c3a07b448\u002F1040g00831m0md7fl5e205pvovm0ji2q3pda5k20!nc_n_webp_mw_1","fileId":"","height":1600,"width":1200}},"index":18,"exposed":false,"ssrRendered":true,"xsecToken":"ABTk71fNEul7zAXn0OLf_fL3BKdlR49s5Wv0oxpWlq8uE="},{"id":"68b95ccb000000001d01a4cc","noteCard":{"user":{"nickName":"大厂电报","avatar":"https:\u002F\u002Fsns-avatar-qc.xhscdn.com\u002Favatar\u002F1040g2jo31lvmkfehl80g5pvovm0ji2q3r980kf0","userId":"67f8fd81000000000e010b43","nickname":"大厂电报"},"interactInfo":{"liked":false,"likedCount":"6","sticky":false},"cover":{"urlPre":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002Fdf293da92f986d5468a2d61e76ec0af4\u002F1040g00831m0md7fl5e6g5pvovm0ji2q37alpc90!nc_n_webp_prv_1","urlDefault":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002Fcc687ffb66605fed0c9167426254f429\u002F1040g00831m0md7fl5e6g5pvovm0ji2q37alpc90!nc_n_webp_mw_1","fileId":"","height":1600,"width":1200,"url":"","traceId":"","infoList":[{"url":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002Fdf293da92f986d5468a2d61e76ec0af4\u002F1040g00831m0md7fl5e6g5pvovm0ji2q37alpc90!nc_n_webp_prv_1","imageScene":"WB_PRV"},{"imageScene":"WB_DFT","url":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002Fcc687ffb66605fed0c9167426254f429\u002F1040g00831m0md7fl5e6g5pvovm0ji2q37alpc90!nc_n_webp_mw_1"}]},"noteId":"68b95ccb000000001d01a4cc","xsecToken":"ABTk71fNEul7zAXn0OLf_fLxO7mJggEz6YnA6MYuoUVzM=","type":"normal","displayTitle":"🚗先看看中国汽车8月销量:"},"index":19,"exposed":false,"ssrRendered":true,"xsecToken":"ABTk71fNEul7zAXn0OLf_fLxO7mJggEz6YnA6MYuoUVzM="},{"id":"68b93352000000001d038be6","noteCard":{"noteId":"68b93352000000001d038be6","xsecToken":"ABTk71fNEul7zAXn0OLf_fL3V_dL3cHLjZ6-_SHPdwLcw=","type":"normal","displayTitle":"字节芯片团队权限被注销？回应来了","user":{"nickName":"大厂电报","avatar":"https:\u002F\u002Fsns-avatar-qc.xhscdn.com\u002Favatar\u002F1040g2jo31lvmkfehl80g5pvovm0ji2q3r980kf0","userId":"67f8fd81000000000e010b43","nickname":"大厂电报"},"interactInfo":{"liked":false,"likedCount":"8","sticky":false},"cover":{"width":1200,"url":"","traceId":"","infoList":[{"imageScene":"WB_PRV","url":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002Fd335c1c880f01a89153283c458ce85f8\u002F1040g00831m0ca02c58205pvovm0ji2q3obtb950!nc_n_webp_prv_1"},{"imageScene":"WB_DFT","url":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002Fb3bf9c7f3a3354ecb8c2c5f2fcb03e94\u002F1040g00831m0ca02c58205pvovm0ji2q3obtb950!nc_n_webp_mw_1"}],"urlPre":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002Fd335c1c880f01a89153283c458ce85f8\u002F1040g00831m0ca02c58205pvovm0ji2q3obtb950!nc_n_webp_prv_1","urlDefault":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002Fb3bf9c7f3a3354ecb8c2c5f2fcb03e94\u002F1040g00831m0ca02c58205pvovm0ji2q3obtb950!nc_n_webp_mw_1","fileId":"","height":1600}},"index":20,"exposed":false,"ssrRendered":true,"xsecToken":"ABTk71fNEul7zAXn0OLf_fL3V_dL3cHLjZ6-_SHPdwLcw="},{"id":"68b930ba000000001d01d12c","noteCard":{"type":"normal","displayTitle":"爆料！SHEIN团建还要员工AA，挪年假或调休补","user":{"avatar":"https:\u002F\u002Fsns-avatar-qc.xhscdn.com\u002Favatar\u002F1040g2jo31lvmkfehl80g5pvovm0ji2q3r980kf0","userId":"67f8fd81000000000e010b43","nickname":"大厂电报","nickName":"大厂电报"},"interactInfo":{"liked":false,"likedCount":"153","sticky":false},"cover":{"height":1600,"width":1200,"url":"","traceId":"","infoList":[{"imageScene":"WB_PRV","url":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002Fbb71e8b37f4ca7bf71f73253388a9857\u002F1040g00831m0ca02c581g5pvovm0ji2q34fhc740!nc_n_webp_prv_1"},{"imageScene":"WB_DFT","url":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002F41bbec32de89582991aab70ad0b74833\u002F1040g00831m0ca02c581g5pvovm0ji2q34fhc740!nc_n_webp_mw_1"}],"urlPre":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002Fbb71e8b37f4ca7bf71f73253388a9857\u002F1040g00831m0ca02c581g5pvovm0ji2q34fhc740!nc_n_webp_prv_1","urlDefault":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002F41bbec32de89582991aab70ad0b74833\u002F1040g00831m0ca02c581g5pvovm0ji2q34fhc740!nc_n_webp_mw_1","fileId":""},"noteId":"68b930ba000000001d01d12c","xsecToken":"ABTk71fNEul7zAXn0OLf_fL_jn-qEWrUELjMcpnM4X9dw="},"index":21,"exposed":false,"ssrRendered":true,"xsecToken":"ABTk71fNEul7zAXn0OLf_fL_jn-qEWrUELjMcpnM4X9dw="},{"id":"68b90ea3000000001d02413a","noteCard":{"noteId":"68b90ea3000000001d02413a","xsecToken":"ABTk71fNEul7zAXn0OLf_fL-aYcZk5zuEmxLkg3H-_LEw=","type":"normal","displayTitle":"某乎运营爆料：年薪30K*15，年终奖连续打折","user":{"nickName":"大厂电报","avatar":"https:\u002F\u002Fsns-avatar-qc.xhscdn.com\u002Favatar\u002F1040g2jo31lvmkfehl80g5pvovm0ji2q3r980kf0","userId":"67f8fd81000000000e010b43","nickname":"大厂电报"},"interactInfo":{"liked":false,"likedCount":"4","sticky":false},"cover":{"width":1200,"url":"","traceId":"","infoList":[{"imageScene":"WB_PRV","url":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002Fe22738cd3e793e7f288bd9ca38e2f87f\u002F1040g00831m0ca02c580g5pvovm0ji2q3i0r34v8!nc_n_webp_prv_1"},{"imageScene":"WB_DFT","url":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002F2ec139befd7b4386c1da17c905588dcd\u002F1040g00831m0ca02c580g5pvovm0ji2q3i0r34v8!nc_n_webp_mw_1"}],"urlPre":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002Fe22738cd3e793e7f288bd9ca38e2f87f\u002F1040g00831m0ca02c580g5pvovm0ji2q3i0r34v8!nc_n_webp_prv_1","urlDefault":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002F2ec139befd7b4386c1da17c905588dcd\u002F1040g00831m0ca02c580g5pvovm0ji2q3i0r34v8!nc_n_webp_mw_1","fileId":"","height":1600}},"index":22,"exposed":false,"ssrRendered":true,"xsecToken":"ABTk71fNEul7zAXn0OLf_fL-aYcZk5zuEmxLkg3H-_LEw="},{"id":"68b86297000000001d02325f","noteCard":{"user":{"userId":"67f8fd81000000000e010b43","nickname":"大厂电报","nickName":"大厂电报","avatar":"https:\u002F\u002Fsns-avatar-qc.xhscdn.com\u002Favatar\u002F1040g2jo31lvmkfehl80g5pvovm0ji2q3r980kf0"},"interactInfo":{"liked":false,"likedCount":"104","sticky":false},"cover":{"fileId":"","height":1600,"width":1200,"url":"","traceId":"","infoList":[{"imageScene":"WB_PRV","url":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002Fe201692f721e2421540713bdf38915b0\u002F1040g2sg31lvm66a2lif05pvovm0ji2q344i9jqg!nc_n_webp_prv_1"},{"url":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002F1b75774ce80b1512516fff2475ba97e1\u002F1040g2sg31lvm66a2lif05pvovm0ji2q344i9jqg!nc_n_webp_mw_1","imageScene":"WB_DFT"}],"urlPre":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002Fe201692f721e2421540713bdf38915b0\u002F1040g2sg31lvm66a2lif05pvovm0ji2q344i9jqg!nc_n_webp_prv_1","urlDefault":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002F1b75774ce80b1512516fff2475ba97e1\u002F1040g2sg31lvm66a2lif05pvovm0ji2q344i9jqg!nc_n_webp_mw_1"},"noteId":"68b86297000000001d02325f","xsecToken":"ABB5oj41e5tyRt7zaMZnbQ4P5XWnRvx8WPo_k8hQU-EwQ=","type":"normal","displayTitle":"京东员工300万天津买房血泪史，太扎心了！"},"index":23,"exposed":false,"ssrRendered":true,"xsecToken":"ABB5oj41e5tyRt7zaMZnbQ4P5XWnRvx8WPo_k8hQU-EwQ="},{"id":"68b85fa2000000001d03afee","noteCard":{"user":{"nickName":"大厂电报","avatar":"https:\u002F\u002Fsns-avatar-qc.xhscdn.com\u002Favatar\u002F1040g2jo31lvmkfehl80g5pvovm0ji2q3r980kf0","userId":"67f8fd81000000000e010b43","nickname":"大厂电报"},"interactInfo":{"liked":false,"likedCount":"37","sticky":false},"cover":{"urlDefault":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002F3973db40cbbf19601ee79708ea65b5da\u002Fnotes_pre_post\u002F1040g3k031lvm66a55i0g5pvovm0ji2q3jodhke0!nc_n_webp_mw_1","fileId":"","height":1696,"width":1280,"url":"","traceId":"","infoList":[{"imageScene":"WB_PRV","url":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002F36cda132d49a20562a5b1edb61c91fcc\u002Fnotes_pre_post\u002F1040g3k031lvm66a55i0g5pvovm0ji2q3jodhke0!nc_n_webp_prv_1"},{"imageScene":"WB_DFT","url":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002F3973db40cbbf19601ee79708ea65b5da\u002Fnotes_pre_post\u002F1040g3k031lvm66a55i0g5pvovm0ji2q3jodhke0!nc_n_webp_mw_1"}],"urlPre":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002F36cda132d49a20562a5b1edb61c91fcc\u002Fnotes_pre_post\u002F1040g3k031lvm66a55i0g5pvovm0ji2q3jodhke0!nc_n_webp_prv_1"},"noteId":"68b85fa2000000001d03afee","xsecToken":"ABB5oj41e5tyRt7zaMZnbQ4C5UQzAZ123Ly32VGzulHPs=","type":"normal","displayTitle":"知名车企产线被强拆！吃老本但高管百万年薪"},"index":24,"exposed":false,"ssrRendered":true,"xsecToken":"ABB5oj41e5tyRt7zaMZnbQ4C5UQzAZ123Ly32VGzulHPs="},{"id":"68b85246000000001d0189f5","noteCard":{"displayTitle":"字节Seed员工增发百万期权，打工人羡慕哭","user":{"nickName":"大厂电报","avatar":"https:\u002F\u002Fsns-avatar-qc.xhscdn.com\u002Favatar\u002F1040g2jo31lvmkfehl80g5pvovm0ji2q3r980kf0","userId":"67f8fd81000000000e010b43","nickname":"大厂电报"},"interactInfo":{"liked":false,"likedCount":"5","sticky":false},"cover":{"traceId":"","infoList":[{"imageScene":"WB_PRV","url":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002F7c22fba280c330ff0a4b65ef18d19fad\u002F1040g2sg31lvm66a2lie05pvovm0ji2q30l3u3q8!nc_n_webp_prv_1"},{"imageScene":"WB_DFT","url":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002F0ae835de3bce72723cb255fa90745bcc\u002F1040g2sg31lvm66a2lie05pvovm0ji2q30l3u3q8!nc_n_webp_mw_1"}],"urlPre":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002F7c22fba280c330ff0a4b65ef18d19fad\u002F1040g2sg31lvm66a2lie05pvovm0ji2q30l3u3q8!nc_n_webp_prv_1","urlDefault":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002F0ae835de3bce72723cb255fa90745bcc\u002F1040g2sg31lvm66a2lie05pvovm0ji2q30l3u3q8!nc_n_webp_mw_1","fileId":"","height":1600,"width":1200,"url":""},"noteId":"68b85246000000001d0189f5","xsecToken":"ABB5oj41e5tyRt7zaMZnbQ4Embivuvx5D34zpSV-0xE6I=","type":"normal"},"index":25,"exposed":false,"ssrRendered":true,"xsecToken":"ABB5oj41e5tyRt7zaMZnbQ4Embivuvx5D34zpSV-0xE6I="},{"id":"68b84b58000000001d0277a3","noteCard":{"noteId":"68b84b58000000001d0277a3","xsecToken":"ABB5oj41e5tyRt7zaMZnbQ4P_4qwjXyBdJ5FDa4Xu78pA=","type":"normal","displayTitle":"律师爆料：阿里是全球知名公司，所以全球竞业","user":{"nickName":"大厂电报","avatar":"https:\u002F\u002Fsns-avatar-qc.xhscdn.com\u002Favatar\u002F1040g2jo31lvmkfehl80g5pvovm0ji2q3r980kf0","userId":"67f8fd81000000000e010b43","nickname":"大厂电报"},"interactInfo":{"likedCount":"9","sticky":false,"liked":false},"cover":{"infoList":[{"imageScene":"WB_PRV","url":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002F6d963a045f34dce02577896e1805d830\u002F1040g2sg31lvkr24klefg5pvovm0ji2q3u8fuqi0!nc_n_webp_prv_1"},{"imageScene":"WB_DFT","url":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002F2200ff78691364264a8f8c2d00f00d9c\u002F1040g2sg31lvkr24klefg5pvovm0ji2q3u8fuqi0!nc_n_webp_mw_1"}],"urlPre":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002F6d963a045f34dce02577896e1805d830\u002F1040g2sg31lvkr24klefg5pvovm0ji2q3u8fuqi0!nc_n_webp_prv_1","urlDefault":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002F2200ff78691364264a8f8c2d00f00d9c\u002F1040g2sg31lvkr24klefg5pvovm0ji2q3u8fuqi0!nc_n_webp_mw_1","fileId":"","height":1600,"width":1200,"url":"","traceId":""}},"index":26,"exposed":false,"ssrRendered":true,"xsecToken":"ABB5oj41e5tyRt7zaMZnbQ4P_4qwjXyBdJ5FDa4Xu78pA="},{"id":"68b84856000000001d03b857","noteCard":{"type":"normal","displayTitle":"中国移动子公司不发前8个月奖金，事情闹大了","user":{"nickName":"大厂电报","avatar":"https:\u002F\u002Fsns-avatar-qc.xhscdn.com\u002Favatar\u002F1040g2jo31lvmkfehl80g5pvovm0ji2q3r980kf0","userId":"67f8fd81000000000e010b43","nickname":"大厂电报"},"interactInfo":{"sticky":false,"liked":false,"likedCount":"99"},"cover":{"url":"","traceId":"","infoList":[{"imageScene":"WB_PRV","url":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002Ff5357a9cbb09e4b1de3b311ca7c21a30\u002F1040g2sg31lvkr24kleeg5pvovm0ji2q3td8mif8!nc_n_webp_prv_1"},{"imageScene":"WB_DFT","url":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002Ff5257043f79dea4f82bca57761624bca\u002F1040g2sg31lvkr24kleeg5pvovm0ji2q3td8mif8!nc_n_webp_mw_1"}],"urlPre":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002Ff5357a9cbb09e4b1de3b311ca7c21a30\u002F1040g2sg31lvkr24kleeg5pvovm0ji2q3td8mif8!nc_n_webp_prv_1","urlDefault":"http:\u002F\u002Fsns-webpic-qc.xhscdn.com\u002F202509081416\u002Ff5257043f79dea4f82bca57761624bca\u002F1040g2sg31lvkr24kleeg5pvovm0ji2q3td8mif8!nc_n_webp_mw_1","fileId":"","height":1600,"width":1200},"noteId":"68b84856000000001d03b857","xsecToken":"ABB5oj41e5tyRt7zaMZnbQ4LJ-QYYKYv8aBccia_dKApE="},"index":27,"exposed":false,"ssrRendered":true,"xsecToken":"ABB5oj41e5tyRt7zaMZnbQ4LJ-QYYKYv8aBccia_dKApE="}],[],[],[]],"isFetchingNotes":[false,false,false,false],"tabScrollTop":[0,0,0,0],"userFetchingStatus":"resolved","userNoteFetchingStatus":["resolved","","",""],"bannedInfo":{"userId":"","serverBanned":false,"code":0,"showAlert":false,"reason":"","api":""},"firstFetchNote":false,"noteQueries":[{"num":30,"cursor":"","userId":"67f8fd81000000000e010b43","page":1,"hasMore":false},{"num":30,"cursor":"","userId":"67f8fd81000000000e010b43","page":1,"hasMore":true},{"num":30,"cursor":"","userId":"67f8fd81000000000e010b43","page":1,"hasMore":true},{"num":30,"cursor":"","userId":"67f8fd81000000000e010b43","page":1,"hasMore":true}],"pageScrolled":0,"activeSubTab":undefined,"isOwnBoard":false},"board":{"boardListData":{},"isLoadingBoardList":false,"boardDetails":{},"boardFeedsMap":{},"boardPageStatus":"pending","userBoardList":[]},"login":{"loginMethod":undefined,"from":"","showLogin":false,"agreed":false,"showTooltip":false,"loginData":{"phone":"","authCode":""},"errors":{"phone":"","authCode":""},"qrData":{"backend":{"qrId":"","code":""},"image":"","status":"un_scanned"},"counter":undefined,"inAntiSpamChecking":false,"recentFrom":"","isObPagesVisible":false,"obPageFillInProgress":null,"verificationCodeStartTime":0,"ageSelectValue":"21","hobbySelectValue":[],"genderSelectValue":undefined,"inSpamCheckSendAuthCode":false,"isRegFusing":false,"loginStep":0,"isLogining":false,"loginPadMountedTime":0,"loginTips":"登录后推荐更懂你的笔记","isRiskUser":false,"closeLoginModal":false,"traceId":"","inAntiSpamCheckLogin":false},"feed":{"query":{"cursorScore":"","num":30,"refreshType":1,"noteIndex":0,"unreadBeginNoteId":"","unreadEndNoteId":"","unreadNoteCount":0,"category":"homefeed_recommend","searchKey":"","needNum":20,"imageFormats":[],"needFilterImage":false},"isFetching":false,"isError":false,"feedsWrapper":undefined,"undertakeNote":undefined,"feeds":[],"currentChannel":"homefeed_recommend","unreadInfo":{"cachedFeeds":[],"unreadBeginNoteId":"","unreadEndNoteId":"","unreadNoteCount":0,"timestamp":0},"validIds":{"noteIds":[]},"mfStatistics":{"timestamp":0,"visitTimes":0,"readFeedCount":0},"channels":undefined,"isResourceDisplay":false,"isActivityEnd":false,"cancelFeedRequest":false,"prefetchId":undefined,"mfRequestMetaData":{"start":null,"lasting":null},"placeholderFeeds":[],"feedsCacheLogInfo":{"flag":"unknown","errorCode":0,"isHitMfCache":false,"SSRDocumentChecked":false,"SSRDocumentCheckedSuccess":false},"isUsingPlaceholderFeeds":false,"placeholderFeedsConsumed":false,"isReplace":false,"isFirstSuccessFetched":false,"imgNoteFilterStatus":"unchecked","ssrRequestStatus":5,"ssrRenderExtra":""},"layout":{"layoutInfoReady":false,"columns":6,"columnsWithSidebar":6,"gap":{"vertical":12,"horizontal":24},"columnWidth":0,"interactionWidth":0,"widthType":"normal","bufferRow":4},"search":{"state":"auto","searchContext":{"keyword":"","page":1,"pageSize":20,"searchId":"","sort":"general","noteType":0,"extFlags":[],"filters":[],"geo":""},"feeds":[],"searchValue":"","suggestions":[],"userInputSugTrigger":"","keywordFrom":2,"tagSearch":[],"activeTagSearch":null,"searchFeedsWrapper":undefined,"currentSearchType":"all","hintWord":{"title":"搜索小红书","searchWord":"小红书网页版","hintWordRequestId":"default","type":"default"},"sugType":null,"queryTrendingInfo":undefined,"queryTrendingParams":{"source":"UserPage","searchType":"trend","lastQuery":"","lastQueryTime":0,"wordRequestSituation":"FIRST_ENTER","hintWord":"","hintWordType":"","hintWordRequestId":""},"queryTrendingFetched":false,"oneboxInfo":{},"hasMore":true,"firstEnterSearchPage":true,"userLists":[],"fetchUserListsStatus":"auto","isFetchingUserLists":false,"hasMoreUser":true,"searchCplId":undefined,"wordRequestId":undefined,"historyList":[],"searchPageHasPrevRoute":false,"searchHotSpots":[],"hotspotQueryNoteStep":"display","hotspotQueryNoteIndex":0,"canShowHotspotQueryNote":true,"forceHotspotSearch":false,"searchCardHotSpots":[],"isHotspotSearch":false,"filters":undefined,"activeFilters":[],"filterParams":undefined,"sessionId":"","rootSearchId":"","searchUserContext":{"keyword":"","searchId":"","page":1,"pageSize":15,"bizType":"web_search_user","requestId":""}},"activity":{"isOpen":false,"currentUrl":"","entryList":[]},"note":{"prevRouteData":{},"prevRoute":"Empty","commentTarget":{},"isImgFullscreen":false,"gotoPage":"","firstNoteId":"","autoOpenNote":false,"topCommentId":"","noteDetailMap":{"undefined":{"comments":{"list":[],"cursor":"","hasMore":true,"loading":false,"firstRequestFinish":false},"currentTime":0,"note":{}}},"serverRequestInfo":{"state":"success","errorCode":0,"errMsg":""},"volume":0,"recommendVideoMap":{},"videoFeedType":"note_source","rate":1,"currentNoteId":undefined,"forceScrollToComment":false,"mediaWidth":450,"noteHeight":800},"nioStore":{"collectionListDataSource":undefined,"error":undefined},"notification":{"isFetching":false,"activeTabKey":-1,"notificationCount":{"unreadCount":0,"mentions":0,"likes":0,"connections":0},"notificationMap":{"mentions":{"messageList":[],"hasMore":true,"cursor":""},"likes":{"messageList":[],"hasMore":true,"cursor":""},"connections":{"messageList":[],"hasMore":true,"cursor":""}}}}</script><div data-v-1b03e45c="" class="dropdown-container"><div data-v-1b03e45c="" class="dropdown-items" style="display: none;"><!----><li data-v-141cfafe=""><!----><span data-v-141cfafe="" class="text"><a data-v-d957886a="" data-v-141cfafe-s="" target="_blank" href="//creator.xiaohongshu.com/?source=official" class="link">创作服务</a></span><!----><span data-v-141cfafe="" class="right-icon"><svg data-v-55b36ac6="" data-v-d957886a="" class="reds-icon icon" width="20" height="20"><use data-v-55b36ac6="" xlink:href="#arrow_right_top"></use></svg></span><!----></li><!----><!----><!----><li data-v-141cfafe=""><!----><span data-v-141cfafe="" class="text"><a data-v-d957886a="" data-v-141cfafe-s="" target="_blank" href="//redlive.xiaohongshu.com?source=official" class="link">直播管理</a></span><!----><span data-v-141cfafe="" class="right-icon"><svg data-v-55b36ac6="" data-v-d957886a="" class="reds-icon icon" width="20" height="20"><use data-v-55b36ac6="" xlink:href="#arrow_right_top"></use></svg></span><!----></li><!----><!----><!----><li data-v-141cfafe=""><!----><span data-v-141cfafe="" class="text"><a data-v-d957886a="" data-v-141cfafe-s="" target="_blank" href="//www.xiaohongshu.com/zhibo/robs?source=official" class="link">电脑直播助手</a></span><!----><span data-v-141cfafe="" class="right-icon"><svg data-v-55b36ac6="" data-v-d957886a="" class="reds-icon icon" width="20" height="20"><use data-v-55b36ac6="" xlink:href="#arrow_right_top"></use></svg></span><!----></li><!----><!----></div></div><div data-v-1b03e45c="" class="dropdown-container"><div data-v-1b03e45c="" class="dropdown-items" style="display: none; visibility: visible; max-height: 920px; transform: translateX(1133px) translateY(64px);"><!----><li data-v-141cfafe=""><!----><span data-v-141cfafe="" class="text"><a data-v-d957886a="" data-v-141cfafe-s="" target="_blank" href="//pro.xiaohongshu.com" class="link">专业号</a></span><!----><span data-v-141cfafe="" class="right-icon"><svg data-v-55b36ac6="" data-v-d957886a="" class="reds-icon icon" width="20" height="20"><use data-v-55b36ac6="" xlink:href="#arrow_right_top"></use></svg></span><!----></li><!----><!----><!----><li data-v-141cfafe=""><!----><span data-v-141cfafe="" class="text"><a data-v-d957886a="" data-v-141cfafe-s="" target="_blank" href="//e.xiaohongshu.com/require-clue?sourcePage=6&amp;sourceId=994" class="link">推广合作</a></span><!----><span data-v-141cfafe="" class="right-icon"><svg data-v-55b36ac6="" data-v-d957886a="" class="reds-icon icon" width="20" height="20"><use data-v-55b36ac6="" xlink:href="#arrow_right_top"></use></svg></span><!----></li><!----><!----><!----><li data-v-141cfafe=""><!----><span data-v-141cfafe="" class="text"><a data-v-d957886a="" data-v-141cfafe-s="" target="_blank" href="//pgy.xiaohongshu.com/solar/to-home?source=official&amp;type=0" class="link">蒲公英</a></span><!----><span data-v-141cfafe="" class="right-icon"><svg data-v-55b36ac6="" data-v-d957886a="" class="reds-icon icon" width="20" height="20"><use data-v-55b36ac6="" xlink:href="#arrow_right_top"></use></svg></span><!----></li><!----><!----><!----><li data-v-141cfafe=""><!----><span data-v-141cfafe="" class="text"><a data-v-d957886a="" data-v-141cfafe-s="" target="_blank" href="//zhaoshang.xiaohongshu.com/merchant/login?from=xhsweb" class="link">商家入驻</a></span><!----><span data-v-141cfafe="" class="right-icon"><svg data-v-55b36ac6="" data-v-d957886a="" class="reds-icon icon" width="20" height="20"><use data-v-55b36ac6="" xlink:href="#arrow_right_top"></use></svg></span><!----></li><!----><!----><!----><li data-v-141cfafe=""><!----><span data-v-141cfafe="" class="text"><a data-v-d957886a="" data-v-141cfafe-s="" target="_blank" href="//creator.xiaohongshu.com/mcn-introduce?source=official" class="link">MCN入驻</a></span><!----><span data-v-141cfafe="" class="right-icon"><svg data-v-55b36ac6="" data-v-d957886a="" class="reds-icon icon" width="20" height="20"><use data-v-55b36ac6="" xlink:href="#arrow_right_top"></use></svg></span><!----></li><!----><!----></div></div><div data-v-1b03e45c="" class="dropdown-container info-right-area-more-container" style="z-index: 5;"><div data-v-1b03e45c="" class="dropdown-items" style="display: none;"><div data-v-1af0f6e0="" class="menu-wrapper" trigger="click" selected="false" multiselected="false"><div data-v-1af0f6e0="" class="menu-item"><span data-v-1af0f6e0="">举报</span></div></div></div></div><!----><script src="https://fe-static.xhscdn.com/as/v1/3e44/public/bf7d4e32677698655a5cadc581fd09b3.js" type="text/javascript" crossorigin="anonymous" data-formula-asset="1" data-formula-cdn-retry="1"></script><script src="https://fe-static.xhscdn.com/as/v1/f218/a15/public/04b29480233f4def5c875875b6bdc3b1.js" type="text/javascript" crossorigin="anonymous" data-formula-asset="1" data-formula-cdn-retry="1"></script><script src="https://fe-static.xhscdn.com/as/v1/f218/a29/public/0666f0acdeed38d4cd9084ade1739498.js" type="text/javascript" crossorigin="anonymous" data-formula-asset="1" data-formula-cdn-retry="1"></script><script src="https://fe-video-qc.xhscdn.com/fe-platform-file/104101b831lm16ed25m06cgm8b89g0000000001dmrsadm.js" type="text/javascript" crossorigin="anonymous" data-formula-asset="1" data-formula-cdn-retry="1"></script><deepl-input-controller translate="no"><template shadowrootmode="open"><link rel="stylesheet" href="chrome-extension://cofdbpoegempjloogbagkncekinflcnj/build/content.css"><div dir="ltr" style="visibility: initial !important;"><div class="dl-input-translation-container svelte-95aucy"><div></div></div></div></template></deepl-input-controller></body><div id="immersive-translate-popup" style="all: initial"><template shadowrootmode="open"><style>@charset "UTF-8";
/*!
 * Pico.css v1.5.6 (https://picocss.com)
 * Copyright 2019-2022 - Licensed under MIT
 */
/**
 * Theme: default
 */
#mount {
  --font-family: system-ui, -apple-system, "Segoe UI", "Roboto", "Ubuntu",
    "Cantarell", "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji",
    "Segoe UI Symbol", "Noto Color Emoji";
  --line-height: 1.5;
  --font-weight: 400;
  --font-size: 16px;
  --border-radius: 0.25rem;
  --border-width: 1px;
  --outline-width: 3px;
  --spacing: 1rem;
  --typography-spacing-vertical: 1.5rem;
  --block-spacing-vertical: calc(var(--spacing) * 2);
  --block-spacing-horizontal: var(--spacing);
  --grid-spacing-vertical: 0;
  --grid-spacing-horizontal: var(--spacing);
  --form-element-spacing-vertical: 0.75rem;
  --form-element-spacing-horizontal: 1rem;
  --nav-element-spacing-vertical: 1rem;
  --nav-element-spacing-horizontal: 0.5rem;
  --nav-link-spacing-vertical: 0.5rem;
  --nav-link-spacing-horizontal: 0.5rem;
  --form-label-font-weight: var(--font-weight);
  --transition: 0.2s ease-in-out;
  --modal-overlay-backdrop-filter: blur(0.25rem);
}
@media (min-width: 576px) {
  #mount {
    --font-size: 17px;
  }
}
@media (min-width: 768px) {
  #mount {
    --font-size: 18px;
  }
}
@media (min-width: 992px) {
  #mount {
    --font-size: 19px;
  }
}
@media (min-width: 1200px) {
  #mount {
    --font-size: 20px;
  }
}

@media (min-width: 576px) {
  #mount > header,
  #mount > main,
  #mount > footer,
  section {
    --block-spacing-vertical: calc(var(--spacing) * 2);
  }
}
@media (min-width: 768px) {
  #mount > header,
  #mount > main,
  #mount > footer,
  section {
    --block-spacing-vertical: calc(var(--spacing) * 2.5);
  }
}
@media (min-width: 992px) {
  #mount > header,
  #mount > main,
  #mount > footer,
  section {
    --block-spacing-vertical: calc(var(--spacing) * 3);
  }
}
@media (min-width: 1200px) {
  #mount > header,
  #mount > main,
  #mount > footer,
  section {
    --block-spacing-vertical: calc(var(--spacing) * 3.5);
  }
}

@media (min-width: 576px) {
  article {
    --block-spacing-horizontal: calc(var(--spacing) * 1.25);
  }
}
@media (min-width: 768px) {
  article {
    --block-spacing-horizontal: calc(var(--spacing) * 1.5);
  }
}
@media (min-width: 992px) {
  article {
    --block-spacing-horizontal: calc(var(--spacing) * 1.75);
  }
}
@media (min-width: 1200px) {
  article {
    --block-spacing-horizontal: calc(var(--spacing) * 2);
  }
}

dialog > article {
  --block-spacing-vertical: calc(var(--spacing) * 2);
  --block-spacing-horizontal: var(--spacing);
}
@media (min-width: 576px) {
  dialog > article {
    --block-spacing-vertical: calc(var(--spacing) * 2.5);
    --block-spacing-horizontal: calc(var(--spacing) * 1.25);
  }
}
@media (min-width: 768px) {
  dialog > article {
    --block-spacing-vertical: calc(var(--spacing) * 3);
    --block-spacing-horizontal: calc(var(--spacing) * 1.5);
  }
}

a {
  --text-decoration: none;
}
a.secondary,
a.contrast {
  --text-decoration: underline;
}

small {
  --font-size: 0.875em;
}

h1,
h2,
h3,
h4,
h5,
h6 {
  --font-weight: 700;
}

h1 {
  --font-size: 2rem;
  --typography-spacing-vertical: 3rem;
}

h2 {
  --font-size: 1.75rem;
  --typography-spacing-vertical: 2.625rem;
}

h3 {
  --font-size: 1.5rem;
  --typography-spacing-vertical: 2.25rem;
}

h4 {
  --font-size: 1.25rem;
  --typography-spacing-vertical: 1.874rem;
}

h5 {
  --font-size: 1.125rem;
  --typography-spacing-vertical: 1.6875rem;
}

[type="checkbox"],
[type="radio"] {
  --border-width: 2px;
}

[type="checkbox"][role="switch"] {
  --border-width: 2px;
}

thead th,
thead td,
tfoot th,
tfoot td {
  --border-width: 3px;
}

:not(thead, tfoot) > * > td {
  --font-size: 0.875em;
}

pre,
code,
kbd,
samp {
  --font-family: "Menlo", "Consolas", "Roboto Mono", "Ubuntu Monospace",
    "Noto Mono", "Oxygen Mono", "Liberation Mono", monospace,
    "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";
}

kbd {
  --font-weight: bolder;
}

[data-theme="light"],
#mount:not([data-theme="dark"]) {
  --background-color: #fff;
  --background-light-green: #f5f7f9;
  --color: hsl(205deg, 20%, 32%);
  --h1-color: hsl(205deg, 30%, 15%);
  --h2-color: #24333e;
  --h3-color: hsl(205deg, 25%, 23%);
  --h4-color: #374956;
  --h5-color: hsl(205deg, 20%, 32%);
  --h6-color: #4d606d;
  --muted-color: hsl(205deg, 10%, 50%);
  --muted-border-color: hsl(205deg, 20%, 94%);
  --primary: hsl(195deg, 85%, 41%);
  --primary-hover: hsl(195deg, 90%, 32%);
  --primary-focus: rgba(16, 149, 193, 0.125);
  --primary-inverse: #fff;
  --secondary: hsl(205deg, 15%, 41%);
  --secondary-hover: hsl(205deg, 20%, 32%);
  --secondary-focus: rgba(89, 107, 120, 0.125);
  --secondary-inverse: #fff;
  --contrast: hsl(205deg, 30%, 15%);
  --contrast-hover: #000;
  --contrast-focus: rgba(89, 107, 120, 0.125);
  --contrast-inverse: #fff;
  --mark-background-color: #fff2ca;
  --mark-color: #543a26;
  --ins-color: #388e3c;
  --del-color: #c62828;
  --blockquote-border-color: var(--muted-border-color);
  --blockquote-footer-color: var(--muted-color);
  --button-box-shadow: 0 0 0 rgba(0, 0, 0, 0);
  --button-hover-box-shadow: 0 0 0 rgba(0, 0, 0, 0);
  --form-element-background-color: transparent;
  --form-element-border-color: hsl(205deg, 14%, 68%);
  --form-element-color: var(--color);
  --form-element-placeholder-color: var(--muted-color);
  --form-element-active-background-color: transparent;
  --form-element-active-border-color: var(--primary);
  --form-element-focus-color: var(--primary-focus);
  --form-element-disabled-background-color: hsl(205deg, 18%, 86%);
  --form-element-disabled-border-color: hsl(205deg, 14%, 68%);
  --form-element-disabled-opacity: 0.5;
  --form-element-invalid-border-color: #c62828;
  --form-element-invalid-active-border-color: #d32f2f;
  --form-element-invalid-focus-color: rgba(211, 47, 47, 0.125);
  --form-element-valid-border-color: #388e3c;
  --form-element-valid-active-border-color: #43a047;
  --form-element-valid-focus-color: rgba(67, 160, 71, 0.125);
  --switch-background-color: hsl(205deg, 16%, 77%);
  --switch-color: var(--primary-inverse);
  --switch-checked-background-color: var(--primary);
  --range-border-color: hsl(205deg, 18%, 86%);
  --range-active-border-color: hsl(205deg, 16%, 77%);
  --range-thumb-border-color: var(--background-color);
  --range-thumb-color: var(--secondary);
  --range-thumb-hover-color: var(--secondary-hover);
  --range-thumb-active-color: var(--primary);
  --table-border-color: var(--muted-border-color);
  --table-row-stripped-background-color: #f6f8f9;
  --code-background-color: hsl(205deg, 20%, 94%);
  --code-color: var(--muted-color);
  --code-kbd-background-color: var(--contrast);
  --code-kbd-color: var(--contrast-inverse);
  --code-tag-color: hsl(330deg, 40%, 50%);
  --code-property-color: hsl(185deg, 40%, 40%);
  --code-value-color: hsl(40deg, 20%, 50%);
  --code-comment-color: hsl(205deg, 14%, 68%);
  --accordion-border-color: var(--muted-border-color);
  --accordion-close-summary-color: var(--color);
  --accordion-open-summary-color: var(--muted-color);
  --card-background-color: var(--background-color);
  --card-border-color: var(--muted-border-color);
  --card-box-shadow: 0.0145rem 0.029rem 0.174rem rgba(27, 40, 50, 0.01698),
    0.0335rem 0.067rem 0.402rem rgba(27, 40, 50, 0.024),
    0.0625rem 0.125rem 0.75rem rgba(27, 40, 50, 0.03),
    0.1125rem 0.225rem 1.35rem rgba(27, 40, 50, 0.036),
    0.2085rem 0.417rem 2.502rem rgba(27, 40, 50, 0.04302),
    0.5rem 1rem 6rem rgba(27, 40, 50, 0.06),
    0 0 0 0.0625rem rgba(27, 40, 50, 0.015);
  --card-sectionning-background-color: #fbfbfc;
  --dropdown-background-color: #fbfbfc;
  --dropdown-border-color: #e1e6eb;
  --dropdown-box-shadow: var(--card-box-shadow);
  --dropdown-color: var(--color);
  --dropdown-hover-background-color: hsl(205deg, 20%, 94%);
  --modal-overlay-background-color: rgba(213, 220, 226, 0.7);
  --progress-background-color: hsl(205deg, 18%, 86%);
  --progress-color: var(--primary);
  --loading-spinner-opacity: 0.5;
  --tooltip-background-color: var(--contrast);
  --tooltip-color: var(--contrast-inverse);
  --icon-checkbox: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(255, 255, 255)' stroke-width='4' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='20 6 9 17 4 12'%3E%3C/polyline%3E%3C/svg%3E");
  --icon-chevron: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(65, 84, 98)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'%3E%3C/polyline%3E%3C/svg%3E");
  --icon-chevron-button: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(255, 255, 255)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'%3E%3C/polyline%3E%3C/svg%3E");
  --icon-chevron-button-inverse: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(255, 255, 255)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'%3E%3C/polyline%3E%3C/svg%3E");
  --icon-close: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(115, 130, 140)' stroke-width='4' stroke-linecap='round' stroke-linejoin='round'%3E%3Cline x1='18' y1='6' x2='6' y2='18'%3E%3C/line%3E%3Cline x1='6' y1='6' x2='18' y2='18'%3E%3C/line%3E%3C/svg%3E");
  --icon-date: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(65, 84, 98)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Crect x='3' y='4' width='18' height='18' rx='2' ry='2'%3E%3C/rect%3E%3Cline x1='16' y1='2' x2='16' y2='6'%3E%3C/line%3E%3Cline x1='8' y1='2' x2='8' y2='6'%3E%3C/line%3E%3Cline x1='3' y1='10' x2='21' y2='10'%3E%3C/line%3E%3C/svg%3E");
  --icon-invalid: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(198, 40, 40)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Ccircle cx='12' cy='12' r='10'%3E%3C/circle%3E%3Cline x1='12' y1='8' x2='12' y2='12'%3E%3C/line%3E%3Cline x1='12' y1='16' x2='12.01' y2='16'%3E%3C/line%3E%3C/svg%3E");
  --icon-minus: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(255, 255, 255)' stroke-width='4' stroke-linecap='round' stroke-linejoin='round'%3E%3Cline x1='5' y1='12' x2='19' y2='12'%3E%3C/line%3E%3C/svg%3E");
  --icon-search: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(65, 84, 98)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Ccircle cx='11' cy='11' r='8'%3E%3C/circle%3E%3Cline x1='21' y1='21' x2='16.65' y2='16.65'%3E%3C/line%3E%3C/svg%3E");
  --icon-time: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(65, 84, 98)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Ccircle cx='12' cy='12' r='10'%3E%3C/circle%3E%3Cpolyline points='12 6 12 12 16 14'%3E%3C/polyline%3E%3C/svg%3E");
  --icon-valid: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(56, 142, 60)' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='20 6 9 17 4 12'%3E%3C/polyline%3E%3C/svg%3E");
  --icon-share: url("data:image/svg+xml;charset=utf-8;base64,PHN2ZyB3aWR0aD0nMjQnIGhlaWdodD0nMjQnIHZpZXdCb3g9JzAgMCAyNCAyNCcgZmlsbD0nbm9uZScgeG1sbnM9J2h0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnJz48cGF0aCBkPSdNMTguOTM0OCA4LjY0ODQ0QzIwLjg5NDEgOC42NDg0NCAyMi40ODU1IDcuMDU0NjkgMjIuNDg1NSA1LjA5NzY2QzIyLjQ4NTUgMy4xNDA2MiAyMC44OTE4IDEuNTQ2ODggMTguOTM0OCAxLjU0Njg4QzE2Ljk3NTQgMS41NDY4OCAxNS4zODQgMy4xNDA2MiAxNS4zODQgNS4wOTc2NkMxNS4zODQgNS4yOTkyMiAxNS40MDA0IDUuNDkzNzUgMTUuNDMzMiA1LjY4NTk0TDcuMzIzODMgOS4zNTM5MUM2LjcwOTc3IDguODQ1MzEgNS45MjIyNyA4LjU0MDYyIDUuMDY0NDUgOC41NDA2MkMzLjEwNTA4IDguNTQwNjIgMS41MTM2NyAxMC4xMzQ0IDEuNTEzNjcgMTIuMDkxNEMxLjUxMzY3IDE0LjA0ODQgMy4xMDc0MiAxNS42NDIyIDUuMDY0NDUgMTUuNjQyMkM1LjgzMzIgMTUuNjQyMiA2LjU0NTcgMTUuMzk2MSA3LjEyNjk1IDE0Ljk4MTNMMTIuNDk0MSAxNy45OTUzQzEyLjQxNjggMTguMjg1OSAxMi4zNzcgMTguNTg4MyAxMi4zNzcgMTguOTAyM0MxMi4zNzcgMjAuODYxNyAxMy45NzA3IDIyLjQ1MzEgMTUuOTI3NyAyMi40NTMxQzE3Ljg4NzEgMjIuNDUzMSAxOS40Nzg1IDIwLjg1OTQgMTkuNDc4NSAxOC45MDIzQzE5LjQ3ODUgMTYuOTQzIDE3Ljg4NDggMTUuMzUxNiAxNS45Mjc3IDE1LjM1MTZDMTQuOTU3NCAxNS4zNTE2IDE0LjA3ODUgMTUuNzQzIDEzLjQzNjMgMTYuMzczNEw4LjMyMjI3IDEzLjUwNDdDOC41MDk3NyAxMy4wNzExIDguNjE1MjMgMTIuNTk1MyA4LjYxNTIzIDEyLjA5MzhDOC42MTUyMyAxMS42ODEyIDguNTQ0OTIgMTEuMjg3NSA4LjQxNjAyIDEwLjkxOTVMMTYuMjIzIDcuMzg3NUMxNi44NzQ2IDguMTU2MjUgMTcuODQ5NiA4LjY0ODQ0IDE4LjkzNDggOC42NDg0NFpNNS4wNjQ0NSAxMy43Njk1QzQuMTQxMDIgMTMuNzY5NSAzLjM4ODY3IDEzLjAxNzIgMy4zODg2NyAxMi4wOTM4QzMuMzg4NjcgMTEuMTcwMyA0LjE0MTAyIDEwLjQxOCA1LjA2NDQ1IDEwLjQxOEM1Ljk4Nzg5IDEwLjQxOCA2Ljc0MDIzIDExLjE3MDMgNi43NDAyMyAxMi4wOTM4QzYuNzQwMjMgMTMuMDE3MiA1Ljk4Nzg5IDEzLjc2OTUgNS4wNjQ0NSAxMy43Njk1Wk0xNS45Mjc3IDE3LjIyNjZDMTYuODUxMiAxNy4yMjY2IDE3LjYwMzUgMTcuOTc4OSAxNy42MDM1IDE4LjkwMjNDMTcuNjAzNSAxOS44MjU4IDE2Ljg1MTIgMjAuNTc4MSAxNS45Mjc3IDIwLjU3ODFDMTUuMDA0MyAyMC41NzgxIDE0LjI1MiAxOS44MjU4IDE0LjI1MiAxOC45MDIzQzE0LjI1MiAxNy45Nzg5IDE1LjAwMiAxNy4yMjY2IDE1LjkyNzcgMTcuMjI2NlpNMTguOTM0OCAzLjQxOTUzQzE5Ljg1ODIgMy40MTk1MyAyMC42MTA1IDQuMTcxODcgMjAuNjEwNSA1LjA5NTMxQzIwLjYxMDUgNi4wMTg3NSAxOS44NTgyIDYuNzcxMDkgMTguOTM0OCA2Ljc3MTA5QzE4LjAxMTMgNi43NzEwOSAxNy4yNTkgNi4wMTg3NSAxNy4yNTkgNS4wOTUzMUMxNy4yNTkgNC4xNzE4NyAxOC4wMTEzIDMuNDE5NTMgMTguOTM0OCAzLjQxOTUzWicgZmlsbD0nIzgzODM4MycvPjwvc3ZnPiA=");
  --float-ball-more-button-border-color: #f6f6f6;
  --float-ball-more-button-background-color: #ffffff;
  --float-ball-more-button-svg-color: #6c6f73;
  color-scheme: light;
  --service-bg-hover: #f7faff;
  --service-bg: #fafbfb;
}

@media only screen and (prefers-color-scheme: dark) {
  #mount:not([data-theme="light"]) {
    --background-color: #11191f;
    --float-ball-more-button-background-color: #ffffff;
    --background-light-green: #141e26;
    --color: hsl(205deg, 16%, 77%);
    --h1-color: hsl(205deg, 20%, 94%);
    --h2-color: #e1e6eb;
    --h3-color: hsl(205deg, 18%, 86%);
    --h4-color: #c8d1d8;
    --h5-color: hsl(205deg, 16%, 77%);
    --h6-color: #afbbc4;
    --muted-color: hsl(205deg, 10%, 50%);
    --muted-border-color: #1f2d38;
    --primary: hsl(195deg, 85%, 41%);
    --primary-hover: hsl(195deg, 80%, 50%);
    --primary-focus: rgba(16, 149, 193, 0.25);
    --primary-inverse: #fff;
    --secondary: hsl(205deg, 15%, 41%);
    --secondary-hover: hsl(205deg, 10%, 50%);
    --secondary-focus: rgba(115, 130, 140, 0.25);
    --secondary-inverse: #fff;
    --contrast: hsl(205deg, 20%, 94%);
    --contrast-hover: #fff;
    --contrast-focus: rgba(115, 130, 140, 0.25);
    --contrast-inverse: #000;
    --mark-background-color: #d1c284;
    --mark-color: #11191f;
    --ins-color: #388e3c;
    --del-color: #c62828;
    --blockquote-border-color: var(--muted-border-color);
    --blockquote-footer-color: var(--muted-color);
    --button-box-shadow: 0 0 0 rgba(0, 0, 0, 0);
    --button-hover-box-shadow: 0 0 0 rgba(0, 0, 0, 0);
    --form-element-background-color: #11191f;
    --form-element-border-color: #374956;
    --form-element-color: var(--color);
    --form-element-placeholder-color: var(--muted-color);
    --form-element-active-background-color: var(
      --form-element-background-color
    );
    --form-element-active-border-color: var(--primary);
    --form-element-focus-color: var(--primary-focus);
    --form-element-disabled-background-color: hsl(205deg, 25%, 23%);
    --form-element-disabled-border-color: hsl(205deg, 20%, 32%);
    --form-element-disabled-opacity: 0.5;
    --form-element-invalid-border-color: #b71c1c;
    --form-element-invalid-active-border-color: #c62828;
    --form-element-invalid-focus-color: rgba(198, 40, 40, 0.25);
    --form-element-valid-border-color: #2e7d32;
    --form-element-valid-active-border-color: #388e3c;
    --form-element-valid-focus-color: rgba(56, 142, 60, 0.25);
    --switch-background-color: #374956;
    --switch-color: var(--primary-inverse);
    --switch-checked-background-color: var(--primary);
    --range-border-color: #24333e;
    --range-active-border-color: hsl(205deg, 25%, 23%);
    --range-thumb-border-color: var(--background-color);
    --range-thumb-color: var(--secondary);
    --range-thumb-hover-color: var(--secondary-hover);
    --range-thumb-active-color: var(--primary);
    --table-border-color: var(--muted-border-color);
    --table-row-stripped-background-color: rgba(115, 130, 140, 0.05);
    --code-background-color: #18232c;
    --code-color: var(--muted-color);
    --code-kbd-background-color: var(--contrast);
    --code-kbd-color: var(--contrast-inverse);
    --code-tag-color: hsl(330deg, 30%, 50%);
    --code-property-color: hsl(185deg, 30%, 50%);
    --code-value-color: hsl(40deg, 10%, 50%);
    --code-comment-color: #4d606d;
    --accordion-border-color: var(--muted-border-color);
    --accordion-active-summary-color: var(--primary);
    --accordion-close-summary-color: var(--color);
    --accordion-open-summary-color: var(--muted-color);
    --card-background-color: #141e26;
    --card-border-color: var(--card-background-color);
    --card-box-shadow: 0.0145rem 0.029rem 0.174rem rgba(0, 0, 0, 0.01698),
      0.0335rem 0.067rem 0.402rem rgba(0, 0, 0, 0.024),
      0.0625rem 0.125rem 0.75rem rgba(0, 0, 0, 0.03),
      0.1125rem 0.225rem 1.35rem rgba(0, 0, 0, 0.036),
      0.2085rem 0.417rem 2.502rem rgba(0, 0, 0, 0.04302),
      0.5rem 1rem 6rem rgba(0, 0, 0, 0.06), 0 0 0 0.0625rem rgba(0, 0, 0, 0.015);
    --card-sectionning-background-color: #18232c;
    --dropdown-background-color: hsl(205deg, 30%, 15%);
    --dropdown-border-color: #24333e;
    --dropdown-box-shadow: var(--card-box-shadow);
    --dropdown-color: var(--color);
    --dropdown-hover-background-color: rgba(36, 51, 62, 0.75);
    --modal-overlay-background-color: rgba(36, 51, 62, 0.8);
    --progress-background-color: #24333e;
    --progress-color: var(--primary);
    --loading-spinner-opacity: 0.5;
    --tooltip-background-color: var(--contrast);
    --tooltip-color: var(--contrast-inverse);
    --icon-checkbox: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(255, 255, 255)' stroke-width='4' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='20 6 9 17 4 12'%3E%3C/polyline%3E%3C/svg%3E");
    --icon-chevron: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(162, 175, 185)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'%3E%3C/polyline%3E%3C/svg%3E");
    --icon-chevron-button: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(255, 255, 255)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'%3E%3C/polyline%3E%3C/svg%3E");
    --icon-chevron-button-inverse: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(0, 0, 0)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'%3E%3C/polyline%3E%3C/svg%3E");
    --icon-close: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(115, 130, 140)' stroke-width='4' stroke-linecap='round' stroke-linejoin='round'%3E%3Cline x1='18' y1='6' x2='6' y2='18'%3E%3C/line%3E%3Cline x1='6' y1='6' x2='18' y2='18'%3E%3C/line%3E%3C/svg%3E");
    --icon-date: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(162, 175, 185)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Crect x='3' y='4' width='18' height='18' rx='2' ry='2'%3E%3C/rect%3E%3Cline x1='16' y1='2' x2='16' y2='6'%3E%3C/line%3E%3Cline x1='8' y1='2' x2='8' y2='6'%3E%3C/line%3E%3Cline x1='3' y1='10' x2='21' y2='10'%3E%3C/line%3E%3C/svg%3E");
    --icon-invalid: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(183, 28, 28)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Ccircle cx='12' cy='12' r='10'%3E%3C/circle%3E%3Cline x1='12' y1='8' x2='12' y2='12'%3E%3C/line%3E%3Cline x1='12' y1='16' x2='12.01' y2='16'%3E%3C/line%3E%3C/svg%3E");
    --icon-minus: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(255, 255, 255)' stroke-width='4' stroke-linecap='round' stroke-linejoin='round'%3E%3Cline x1='5' y1='12' x2='19' y2='12'%3E%3C/line%3E%3C/svg%3E");
    --icon-search: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(162, 175, 185)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Ccircle cx='11' cy='11' r='8'%3E%3C/circle%3E%3Cline x1='21' y1='21' x2='16.65' y2='16.65'%3E%3C/line%3E%3C/svg%3E");
    --icon-time: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(162, 175, 185)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Ccircle cx='12' cy='12' r='10'%3E%3C/circle%3E%3Cpolyline points='12 6 12 12 16 14'%3E%3C/polyline%3E%3C/svg%3E");
    --icon-valid: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(46, 125, 50)' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='20 6 9 17 4 12'%3E%3C/polyline%3E%3C/svg%3E");
    --icon-share: url("data:image/svg+xml;charset=utf-8;base64,PHN2ZyB3aWR0aD0nMjInIGhlaWdodD0nMjInIHZpZXdCb3g9JzAgMCAyMiAyMicgZmlsbD0nbm9uZScgeG1sbnM9J2h0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnJz48cGF0aCBkPSdNMTcuOTM0OCA3LjY0ODQ0QzE5Ljg5NDEgNy42NDg0NCAyMS40ODU1IDYuMDU0NjkgMjEuNDg1NSA0LjA5NzY2QzIxLjQ4NTUgMi4xNDA2MiAxOS44OTE4IDAuNTQ2ODc1IDE3LjkzNDggMC41NDY4NzVDMTUuOTc1NCAwLjU0Njg3NSAxNC4zODQgMi4xNDA2MiAxNC4zODQgNC4wOTc2NkMxNC4zODQgNC4yOTkyMiAxNC40MDA0IDQuNDkzNzUgMTQuNDMzMiA0LjY4NTk0TDYuMzIzODMgOC4zNTM5MUM1LjcwOTc3IDcuODQ1MzEgNC45MjIyNyA3LjU0MDYyIDQuMDY0NDUgNy41NDA2MkMyLjEwNTA4IDcuNTQwNjIgMC41MTM2NzIgOS4xMzQzOCAwLjUxMzY3MiAxMS4wOTE0QzAuNTEzNjcyIDEzLjA0ODQgMi4xMDc0MiAxNC42NDIyIDQuMDY0NDUgMTQuNjQyMkM0LjgzMzIgMTQuNjQyMiA1LjU0NTcgMTQuMzk2MSA2LjEyNjk1IDEzLjk4MTNMMTEuNDk0MSAxNi45OTUzQzExLjQxNjggMTcuMjg1OSAxMS4zNzcgMTcuNTg4MyAxMS4zNzcgMTcuOTAyM0MxMS4zNzcgMTkuODYxNyAxMi45NzA3IDIxLjQ1MzEgMTQuOTI3NyAyMS40NTMxQzE2Ljg4NzEgMjEuNDUzMSAxOC40Nzg1IDE5Ljg1OTQgMTguNDc4NSAxNy45MDIzQzE4LjQ3ODUgMTUuOTQzIDE2Ljg4NDggMTQuMzUxNiAxNC45Mjc3IDE0LjM1MTZDMTMuOTU3NCAxNC4zNTE2IDEzLjA3ODUgMTQuNzQzIDEyLjQzNjMgMTUuMzczNEw3LjMyMjI3IDEyLjUwNDdDNy41MDk3NyAxMi4wNzExIDcuNjE1MjMgMTEuNTk1MyA3LjYxNTIzIDExLjA5MzhDNy42MTUyMyAxMC42ODEyIDcuNTQ0OTIgMTAuMjg3NSA3LjQxNjAyIDkuOTE5NTNMMTUuMjIzIDYuMzg3NUMxNS44NzQ2IDcuMTU2MjUgMTYuODQ5NiA3LjY0ODQ0IDE3LjkzNDggNy42NDg0NFpNNC4wNjQ0NSAxMi43Njk1QzMuMTQxMDIgMTIuNzY5NSAyLjM4ODY3IDEyLjAxNzIgMi4zODg2NyAxMS4wOTM4QzIuMzg4NjcgMTAuMTcwMyAzLjE0MTAyIDkuNDE3OTcgNC4wNjQ0NSA5LjQxNzk3QzQuOTg3ODkgOS40MTc5NyA1Ljc0MDIzIDEwLjE3MDMgNS43NDAyMyAxMS4wOTM4QzUuNzQwMjMgMTIuMDE3MiA0Ljk4Nzg5IDEyLjc2OTUgNC4wNjQ0NSAxMi43Njk1Wk0xNC45Mjc3IDE2LjIyNjZDMTUuODUxMiAxNi4yMjY2IDE2LjYwMzUgMTYuOTc4OSAxNi42MDM1IDE3LjkwMjNDMTYuNjAzNSAxOC44MjU4IDE1Ljg1MTIgMTkuNTc4MSAxNC45Mjc3IDE5LjU3ODFDMTQuMDA0MyAxOS41NzgxIDEzLjI1MiAxOC44MjU4IDEzLjI1MiAxNy45MDIzQzEzLjI1MiAxNi45Nzg5IDE0LjAwMiAxNi4yMjY2IDE0LjkyNzcgMTYuMjI2NlpNMTcuOTM0OCAyLjQxOTUzQzE4Ljg1ODIgMi40MTk1MyAxOS42MTA1IDMuMTcxODcgMTkuNjEwNSA0LjA5NTMxQzE5LjYxMDUgNS4wMTg3NSAxOC44NTgyIDUuNzcxMDkgMTcuOTM0OCA1Ljc3MTA5QzE3LjAxMTMgNS43NzEwOSAxNi4yNTkgNS4wMTg3NSAxNi4yNTkgNC4wOTUzMUMxNi4yNTkgMy4xNzE4NyAxNy4wMTEzIDIuNDE5NTMgMTcuOTM0OCAyLjQxOTUzWicgZmlsbD0nI0I2QjZCNicvPjwvc3ZnPiA=");
    color-scheme: dark;
    --service-bg-hover: #22292f;
    --service-bg: rgba(0, 0, 0, 0.1);
  }
}
[data-theme="dark"] {
  --background-color: #11191f;
  --float-ball-more-button-background-color: #ffffff;
  --background-light-green: #141e26;
  --color: hsl(205deg, 16%, 77%);
  --h1-color: hsl(205deg, 20%, 94%);
  --h2-color: #e1e6eb;
  --h3-color: hsl(205deg, 18%, 86%);
  --h4-color: #c8d1d8;
  --h5-color: hsl(205deg, 16%, 77%);
  --h6-color: #afbbc4;
  --muted-color: hsl(205deg, 10%, 50%);
  --muted-border-color: #1f2d38;
  --primary: hsl(195deg, 85%, 41%);
  --primary-hover: hsl(195deg, 80%, 50%);
  --primary-focus: rgba(16, 149, 193, 0.25);
  --primary-inverse: #fff;
  --secondary: hsl(205deg, 15%, 41%);
  --secondary-hover: hsl(205deg, 10%, 50%);
  --secondary-focus: rgba(115, 130, 140, 0.25);
  --secondary-inverse: #fff;
  --contrast: hsl(205deg, 20%, 94%);
  --contrast-hover: #fff;
  --contrast-focus: rgba(115, 130, 140, 0.25);
  --contrast-inverse: #000;
  --mark-background-color: #d1c284;
  --mark-color: #11191f;
  --ins-color: #388e3c;
  --del-color: #c62828;
  --blockquote-border-color: var(--muted-border-color);
  --blockquote-footer-color: var(--muted-color);
  --button-box-shadow: 0 0 0 rgba(0, 0, 0, 0);
  --button-hover-box-shadow: 0 0 0 rgba(0, 0, 0, 0);
  --form-element-background-color: #11191f;
  --form-element-border-color: #374956;
  --form-element-color: var(--color);
  --form-element-placeholder-color: var(--muted-color);
  --form-element-active-background-color: var(--form-element-background-color);
  --form-element-active-border-color: var(--primary);
  --form-element-focus-color: var(--primary-focus);
  --form-element-disabled-background-color: hsl(205deg, 25%, 23%);
  --form-element-disabled-border-color: hsl(205deg, 20%, 32%);
  --form-element-disabled-opacity: 0.5;
  --form-element-invalid-border-color: #b71c1c;
  --form-element-invalid-active-border-color: #c62828;
  --form-element-invalid-focus-color: rgba(198, 40, 40, 0.25);
  --form-element-valid-border-color: #2e7d32;
  --form-element-valid-active-border-color: #388e3c;
  --form-element-valid-focus-color: rgba(56, 142, 60, 0.25);
  --switch-background-color: #374956;
  --switch-color: var(--primary-inverse);
  --switch-checked-background-color: var(--primary);
  --range-border-color: #24333e;
  --range-active-border-color: hsl(205deg, 25%, 23%);
  --range-thumb-border-color: var(--background-color);
  --range-thumb-color: var(--secondary);
  --range-thumb-hover-color: var(--secondary-hover);
  --range-thumb-active-color: var(--primary);
  --table-border-color: var(--muted-border-color);
  --table-row-stripped-background-color: rgba(115, 130, 140, 0.05);
  --code-background-color: #18232c;
  --code-color: var(--muted-color);
  --code-kbd-background-color: var(--contrast);
  --code-kbd-color: var(--contrast-inverse);
  --code-tag-color: hsl(330deg, 30%, 50%);
  --code-property-color: hsl(185deg, 30%, 50%);
  --code-value-color: hsl(40deg, 10%, 50%);
  --code-comment-color: #4d606d;
  --accordion-border-color: var(--muted-border-color);
  --accordion-active-summary-color: var(--primary);
  --accordion-close-summary-color: var(--color);
  --accordion-open-summary-color: var(--muted-color);
  --card-background-color: #141e26;
  --card-border-color: var(--card-background-color);
  --card-box-shadow: 0.0145rem 0.029rem 0.174rem rgba(0, 0, 0, 0.01698),
    0.0335rem 0.067rem 0.402rem rgba(0, 0, 0, 0.024),
    0.0625rem 0.125rem 0.75rem rgba(0, 0, 0, 0.03),
    0.1125rem 0.225rem 1.35rem rgba(0, 0, 0, 0.036),
    0.2085rem 0.417rem 2.502rem rgba(0, 0, 0, 0.04302),
    0.5rem 1rem 6rem rgba(0, 0, 0, 0.06), 0 0 0 0.0625rem rgba(0, 0, 0, 0.015);
  --card-sectionning-background-color: #18232c;
  --dropdown-background-color: hsl(205deg, 30%, 15%);
  --dropdown-border-color: #24333e;
  --dropdown-box-shadow: var(--card-box-shadow);
  --dropdown-color: var(--color);
  --dropdown-hover-background-color: rgba(36, 51, 62, 0.75);
  --modal-overlay-background-color: rgba(36, 51, 62, 0.8);
  --progress-background-color: #24333e;
  --progress-color: var(--primary);
  --loading-spinner-opacity: 0.5;
  --tooltip-background-color: var(--contrast);
  --tooltip-color: var(--contrast-inverse);
  --icon-checkbox: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(255, 255, 255)' stroke-width='4' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='20 6 9 17 4 12'%3E%3C/polyline%3E%3C/svg%3E");
  --icon-chevron: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(162, 175, 185)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'%3E%3C/polyline%3E%3C/svg%3E");
  --icon-chevron-button: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(255, 255, 255)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'%3E%3C/polyline%3E%3C/svg%3E");
  --icon-chevron-button-inverse: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(0, 0, 0)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'%3E%3C/polyline%3E%3C/svg%3E");
  --icon-close: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(115, 130, 140)' stroke-width='4' stroke-linecap='round' stroke-linejoin='round'%3E%3Cline x1='18' y1='6' x2='6' y2='18'%3E%3C/line%3E%3Cline x1='6' y1='6' x2='18' y2='18'%3E%3C/line%3E%3C/svg%3E");
  --icon-date: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(162, 175, 185)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Crect x='3' y='4' width='18' height='18' rx='2' ry='2'%3E%3C/rect%3E%3Cline x1='16' y1='2' x2='16' y2='6'%3E%3C/line%3E%3Cline x1='8' y1='2' x2='8' y2='6'%3E%3C/line%3E%3Cline x1='3' y1='10' x2='21' y2='10'%3E%3C/line%3E%3C/svg%3E");
  --icon-invalid: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(183, 28, 28)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Ccircle cx='12' cy='12' r='10'%3E%3C/circle%3E%3Cline x1='12' y1='8' x2='12' y2='12'%3E%3C/line%3E%3Cline x1='12' y1='16' x2='12.01' y2='16'%3E%3C/line%3E%3C/svg%3E");
  --icon-minus: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(255, 255, 255)' stroke-width='4' stroke-linecap='round' stroke-linejoin='round'%3E%3Cline x1='5' y1='12' x2='19' y2='12'%3E%3C/line%3E%3C/svg%3E");
  --icon-search: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(162, 175, 185)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Ccircle cx='11' cy='11' r='8'%3E%3C/circle%3E%3Cline x1='21' y1='21' x2='16.65' y2='16.65'%3E%3C/line%3E%3C/svg%3E");
  --icon-time: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(162, 175, 185)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Ccircle cx='12' cy='12' r='10'%3E%3C/circle%3E%3Cpolyline points='12 6 12 12 16 14'%3E%3C/polyline%3E%3C/svg%3E");
  --icon-valid: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='rgb(46, 125, 50)' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='20 6 9 17 4 12'%3E%3C/polyline%3E%3C/svg%3E");
  --icon-share: url("data:image/svg+xml;charset=utf-8;base64,PHN2ZyB3aWR0aD0nMjInIGhlaWdodD0nMjInIHZpZXdCb3g9JzAgMCAyMiAyMicgZmlsbD0nbm9uZScgeG1sbnM9J2h0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnJz48cGF0aCBkPSdNMTcuOTM0OCA3LjY0ODQ0QzE5Ljg5NDEgNy42NDg0NCAyMS40ODU1IDYuMDU0NjkgMjEuNDg1NSA0LjA5NzY2QzIxLjQ4NTUgMi4xNDA2MiAxOS44OTE4IDAuNTQ2ODc1IDE3LjkzNDggMC41NDY4NzVDMTUuOTc1NCAwLjU0Njg3NSAxNC4zODQgMi4xNDA2MiAxNC4zODQgNC4wOTc2NkMxNC4zODQgNC4yOTkyMiAxNC40MDA0IDQuNDkzNzUgMTQuNDMzMiA0LjY4NTk0TDYuMzIzODMgOC4zNTM5MUM1LjcwOTc3IDcuODQ1MzEgNC45MjIyNyA3LjU0MDYyIDQuMDY0NDUgNy41NDA2MkMyLjEwNTA4IDcuNTQwNjIgMC41MTM2NzIgOS4xMzQzOCAwLjUxMzY3MiAxMS4wOTE0QzAuNTEzNjcyIDEzLjA0ODQgMi4xMDc0MiAxNC42NDIyIDQuMDY0NDUgMTQuNjQyMkM0LjgzMzIgMTQuNjQyMiA1LjU0NTcgMTQuMzk2MSA2LjEyNjk1IDEzLjk4MTNMMTEuNDk0MSAxNi45OTUzQzExLjQxNjggMTcuMjg1OSAxMS4zNzcgMTcuNTg4MyAxMS4zNzcgMTcuOTAyM0MxMS4zNzcgMTkuODYxNyAxMi45NzA3IDIxLjQ1MzEgMTQuOTI3NyAyMS40NTMxQzE2Ljg4NzEgMjEuNDUzMSAxOC40Nzg1IDE5Ljg1OTQgMTguNDc4NSAxNy45MDIzQzE4LjQ3ODUgMTUuOTQzIDE2Ljg4NDggMTQuMzUxNiAxNC45Mjc3IDE0LjM1MTZDMTMuOTU3NCAxNC4zNTE2IDEzLjA3ODUgMTQuNzQzIDEyLjQzNjMgMTUuMzczNEw3LjMyMjI3IDEyLjUwNDdDNy41MDk3NyAxMi4wNzExIDcuNjE1MjMgMTEuNTk1MyA3LjYxNTIzIDExLjA5MzhDNy42MTUyMyAxMC42ODEyIDcuNTQ0OTIgMTAuMjg3NSA3LjQxNjAyIDkuOTE5NTNMMTUuMjIzIDYuMzg3NUMxNS44NzQ2IDcuMTU2MjUgMTYuODQ5NiA3LjY0ODQ0IDE3LjkzNDggNy42NDg0NFpNNC4wNjQ0NSAxMi43Njk1QzMuMTQxMDIgMTIuNzY5NSAyLjM4ODY3IDEyLjAxNzIgMi4zODg2NyAxMS4wOTM4QzIuMzg4NjcgMTAuMTcwMyAzLjE0MTAyIDkuNDE3OTcgNC4wNjQ0NSA5LjQxNzk3QzQuOTg3ODkgOS40MTc5NyA1Ljc0MDIzIDEwLjE3MDMgNS43NDAyMyAxMS4wOTM4QzUuNzQwMjMgMTIuMDE3MiA0Ljk4Nzg5IDEyLjc2OTUgNC4wNjQ0NSAxMi43Njk1Wk0xNC45Mjc3IDE2LjIyNjZDMTUuODUxMiAxNi4yMjY2IDE2LjYwMzUgMTYuOTc4OSAxNi42MDM1IDE3LjkwMjNDMTYuNjAzNSAxOC44MjU4IDE1Ljg1MTIgMTkuNTc4MSAxNC45Mjc3IDE5LjU3ODFDMTQuMDA0MyAxOS41NzgxIDEzLjI1MiAxOC44MjU4IDEzLjI1MiAxNy45MDIzQzEzLjI1MiAxNi45Nzg5IDE0LjAwMiAxNi4yMjY2IDE0LjkyNzcgMTYuMjI2NlpNMTcuOTM0OCAyLjQxOTUzQzE4Ljg1ODIgMi40MTk1MyAxOS42MTA1IDMuMTcxODcgMTkuNjEwNSA0LjA5NTMxQzE5LjYxMDUgNS4wMTg3NSAxOC44NTgyIDUuNzcxMDkgMTcuOTM0OCA1Ljc3MTA5QzE3LjAxMTMgNS43NzEwOSAxNi4yNTkgNS4wMTg3NSAxNi4yNTkgNC4wOTUzMUMxNi4yNTkgMy4xNzE4NyAxNy4wMTEzIDIuNDE5NTMgMTcuOTM0OCAyLjQxOTUzWicgZmlsbD0nI0I2QjZCNicvPjwvc3ZnPiA=");
  color-scheme: dark;
  --service-bg: rgba(0, 0, 0, 0.1);
}

progress,
[type="checkbox"],
[type="radio"],
[type="range"] {
  accent-color: var(--primary);
}

/**
 * Document
 * Content-box & Responsive typography
 */
*,
*::before,
*::after {
  box-sizing: border-box;
  background-repeat: no-repeat;
}

::before,
::after {
  text-decoration: inherit;
  vertical-align: inherit;
}

:where(#mount) {
  -webkit-tap-highlight-color: transparent;
  -webkit-text-size-adjust: 100%;
  -moz-text-size-adjust: 100%;
  text-size-adjust: 100%;
  background-color: var(--background-color);
  color: var(--color);
  font-weight: var(--font-weight);
  font-size: var(--font-size);
  line-height: var(--line-height);
  font-family: var(--font-family);
  text-rendering: optimizeLegibility;
  overflow-wrap: break-word;
  cursor: default;
  -moz-tab-size: 4;
  -o-tab-size: 4;
  tab-size: 4;
}

/**
 * Sectioning
 * Container and responsive spacings for header, main, footer
 */
main {
  display: block;
}

#mount {
  width: 100%;
  margin: 0;
}
#mount > header,
#mount > main,
#mount > footer {
  width: 100%;
  margin-right: auto;
  margin-left: auto;
  padding: var(--block-spacing-vertical) var(--block-spacing-horizontal);
}
@media (min-width: 576px) {
  #mount > header,
  #mount > main,
  #mount > footer {
    padding: 2px !important;
  }
}
@media (min-width: 992px) {
  #mount > header,
  #mount > main,
  #mount > footer {
    padding: 0 12px !important;
  }
}
@media (min-width: 1200px) {
  #mount > header,
  #mount > main,
  #mount > footer {
    padding: 0 24px !important;
  }
}

/**
* Container
*/
.container,
.container-fluid {
  width: 100%;
  margin-right: auto;
  margin-left: auto;
  padding-right: var(--spacing);
  padding-left: var(--spacing);
}
/* 
@media (min-width: 576px) {
  .container {
    max-width: 510px;
    padding-right: 0;
    padding-left: 0;
  }
}
@media (min-width: 768px) {
  .container {
    max-width: 700px;
  }
} */
@media (min-width: 992px) {
  .container {
    max-width: 920px;
  }
}
@media (min-width: 1200px) {
  .container {
    max-width: 1130px;
  }
}

/**
 * Section
 * Responsive spacings for section
 */
section {
  margin-bottom: var(--block-spacing-vertical);
}

/**
* Grid
* Minimal grid system with auto-layout columns
*/
.grid {
  grid-column-gap: var(--grid-spacing-horizontal);
  grid-row-gap: var(--grid-spacing-vertical);
  display: grid;
  grid-template-columns: 1fr;
  margin: 0;
}
@media (min-width: 1280px) {
  .grid {
    grid-template-columns: repeat(auto-fit, minmax(0%, 1fr));
  }
}
.grid > * {
  min-width: 0;
}

/**
 * Horizontal scroller (<figure>)
 */
figure {
  display: block;
  margin: 0;
  padding: 0;
  overflow-x: auto;
}
figure figcaption {
  padding: calc(var(--spacing) * 0.5) 0;
  color: var(--muted-color);
}

/**
 * Typography
 */
b,
strong {
  font-weight: bolder;
}

sub,
sup {
  position: relative;
  font-size: 0.75em;
  line-height: 0;
  vertical-align: baseline;
}

sub {
  bottom: -0.25em;
}

sup {
  top: -0.5em;
}

address,
blockquote,
dl,
figure,
form,
ol,
p,
pre,
table,
ul {
  margin-top: 0;
  margin-bottom: var(--typography-spacing-vertical);
  color: var(--color);
  font-style: normal;
  font-weight: var(--font-weight);
  font-size: var(--font-size);
}

a,
[role="link"] {
  --color: var(--primary);
  --background-color: transparent;
  outline: none;
  background-color: var(--background-color);
  color: var(--color);
  -webkit-text-decoration: var(--text-decoration);
  text-decoration: var(--text-decoration);
  transition: background-color var(--transition), color var(--transition),
    box-shadow var(--transition), -webkit-text-decoration var(--transition);
  transition: background-color var(--transition), color var(--transition),
    text-decoration var(--transition), box-shadow var(--transition);
  transition: background-color var(--transition), color var(--transition),
    text-decoration var(--transition), box-shadow var(--transition),
    -webkit-text-decoration var(--transition);
}
a:is([aria-current], :hover, :active, :focus),
[role="link"]:is([aria-current], :hover, :active, :focus) {
  --color: var(--primary-hover);
  --text-decoration: underline;
}
a:focus,
[role="link"]:focus {
  --background-color: var(--primary-focus);
}
a.secondary,
[role="link"].secondary {
  --color: var(--secondary);
}
a.secondary:is([aria-current], :hover, :active, :focus),
[role="link"].secondary:is([aria-current], :hover, :active, :focus) {
  --color: var(--secondary-hover);
}
a.secondary:focus,
[role="link"].secondary:focus {
  --background-color: var(--secondary-focus);
}
a.contrast,
[role="link"].contrast {
  --color: var(--contrast);
}
a.contrast:is([aria-current], :hover, :active, :focus),
[role="link"].contrast:is([aria-current], :hover, :active, :focus) {
  --color: var(--contrast-hover);
}
a.contrast:focus,
[role="link"].contrast:focus {
  --background-color: var(--contrast-focus);
}

h1,
h2,
h3,
h4,
h5,
h6 {
  margin-top: 0;
  margin-bottom: var(--typography-spacing-vertical);
  color: var(--color);
  font-weight: var(--font-weight);
  font-size: var(--font-size);
  font-family: var(--font-family);
}

h1 {
  --color: var(--h1-color);
}

h2 {
  --color: var(--h2-color);
}

h3 {
  --color: var(--h3-color);
}

h4 {
  --color: var(--h4-color);
}

h5 {
  --color: var(--h5-color);
}

h6 {
  --color: var(--h6-color);
}

:where(address, blockquote, dl, figure, form, ol, p, pre, table, ul)
  ~ :is(h1, h2, h3, h4, h5, h6) {
  margin-top: var(--typography-spacing-vertical);
}

hgroup,
.headings {
  margin-bottom: var(--typography-spacing-vertical);
}
hgroup > *,
.headings > * {
  margin-bottom: 0;
}
hgroup > *:last-child,
.headings > *:last-child {
  --color: var(--muted-color);
  --font-weight: unset;
  font-size: 1rem;
  font-family: unset;
}

p {
  margin-bottom: var(--typography-spacing-vertical);
}

small {
  font-size: var(--font-size);
}

:where(dl, ol, ul) {
  padding-right: 0;
  padding-left: var(--spacing);
  -webkit-padding-start: var(--spacing);
  padding-inline-start: var(--spacing);
  -webkit-padding-end: 0;
  padding-inline-end: 0;
}
:where(dl, ol, ul) li {
  margin-bottom: calc(var(--typography-spacing-vertical) * 0.25);
}

:where(dl, ol, ul) :is(dl, ol, ul) {
  margin: 0;
  margin-top: calc(var(--typography-spacing-vertical) * 0.25);
}

ul li {
  list-style: square;
}

mark {
  padding: 0.125rem 0.25rem;
  background-color: var(--mark-background-color);
  color: var(--mark-color);
  vertical-align: baseline;
}

blockquote {
  display: block;
  margin: var(--typography-spacing-vertical) 0;
  padding: var(--spacing);
  border-right: none;
  border-left: 0.25rem solid var(--blockquote-border-color);
  -webkit-border-start: 0.25rem solid var(--blockquote-border-color);
  border-inline-start: 0.25rem solid var(--blockquote-border-color);
  -webkit-border-end: none;
  border-inline-end: none;
}
blockquote footer {
  margin-top: calc(var(--typography-spacing-vertical) * 0.5);
  color: var(--blockquote-footer-color);
}

abbr[title] {
  border-bottom: 1px dotted;
  text-decoration: none;
  cursor: help;
}

ins {
  color: var(--ins-color);
  text-decoration: none;
}

del {
  color: var(--del-color);
}

::-moz-selection {
  background-color: var(--primary-focus);
}

::selection {
  background-color: var(--primary-focus);
}

/**
 * Embedded content
 */
:where(audio, canvas, iframe, img, svg, video) {
  vertical-align: middle;
}

audio,
video {
  display: inline-block;
}

audio:not([controls]) {
  display: none;
  height: 0;
}

:where(iframe) {
  border-style: none;
}

img {
  max-width: 100%;
  height: auto;
  border-style: none;
}

:where(svg:not([fill])) {
  fill: currentColor;
}

svg:not(#mount) {
  overflow: hidden;
}

/**
 * Button
 */
button {
  margin: 0;
  overflow: visible;
  font-family: inherit;
  text-transform: none;
}

button,
[type="button"],
[type="reset"],
[type="submit"] {
  -webkit-appearance: button;
}

button {
  display: block;
  width: 100%;
  margin-bottom: var(--spacing);
}

[role="button"] {
  display: inline-block;
  text-decoration: none;
}

button,
input[type="submit"],
input[type="button"],
input[type="reset"],
[role="button"] {
  --background-color: var(--primary);
  --border-color: var(--primary);
  --color: var(--primary-inverse);
  --box-shadow: var(--button-box-shadow, 0 0 0 rgba(0, 0, 0, 0));
  padding: var(--form-element-spacing-vertical)
    var(--form-element-spacing-horizontal);
  border: var(--border-width) solid var(--border-color);
  border-radius: var(--border-radius);
  outline: none;
  background-color: var(--background-color);
  box-shadow: var(--box-shadow);
  color: var(--color);
  font-weight: var(--font-weight);
  font-size: 1rem;
  line-height: var(--line-height);
  text-align: center;
  cursor: pointer;
  transition: background-color var(--transition), border-color var(--transition),
    color var(--transition), box-shadow var(--transition);
}
button:is([aria-current], :hover, :active, :focus),
input[type="submit"]:is([aria-current], :hover, :active, :focus),
input[type="button"]:is([aria-current], :hover, :active, :focus),
input[type="reset"]:is([aria-current], :hover, :active, :focus),
[role="button"]:is([aria-current], :hover, :active, :focus) {
  --background-color: var(--primary-hover);
  --border-color: var(--primary-hover);
  --box-shadow: var(--button-hover-box-shadow, 0 0 0 rgba(0, 0, 0, 0));
  --color: var(--primary-inverse);
}
button:focus,
input[type="submit"]:focus,
input[type="button"]:focus,
input[type="reset"]:focus,
[role="button"]:focus {
  --box-shadow: var(--button-hover-box-shadow, 0 0 0 rgba(0, 0, 0, 0)),
    0 0 0 var(--outline-width) var(--primary-focus);
}

:is(
    button,
    input[type="submit"],
    input[type="button"],
    [role="button"]
  ).secondary,
input[type="reset"] {
  --background-color: var(--secondary);
  --border-color: var(--secondary);
  --color: var(--secondary-inverse);
  cursor: pointer;
}
:is(
    button,
    input[type="submit"],
    input[type="button"],
    [role="button"]
  ).secondary:is([aria-current], :hover, :active, :focus),
input[type="reset"]:is([aria-current], :hover, :active, :focus) {
  --background-color: var(--secondary-hover);
  --border-color: var(--secondary-hover);
  --color: var(--secondary-inverse);
}
:is(
    button,
    input[type="submit"],
    input[type="button"],
    [role="button"]
  ).secondary:focus,
input[type="reset"]:focus {
  --box-shadow: var(--button-hover-box-shadow, 0 0 0 rgba(0, 0, 0, 0)),
    0 0 0 var(--outline-width) var(--secondary-focus);
}

:is(
    button,
    input[type="submit"],
    input[type="button"],
    [role="button"]
  ).contrast {
  --background-color: var(--contrast);
  --border-color: var(--contrast);
  --color: var(--contrast-inverse);
}
:is(
    button,
    input[type="submit"],
    input[type="button"],
    [role="button"]
  ).contrast:is([aria-current], :hover, :active, :focus) {
  --background-color: var(--contrast-hover);
  --border-color: var(--contrast-hover);
  --color: var(--contrast-inverse);
}
:is(
    button,
    input[type="submit"],
    input[type="button"],
    [role="button"]
  ).contrast:focus {
  --box-shadow: var(--button-hover-box-shadow, 0 0 0 rgba(0, 0, 0, 0)),
    0 0 0 var(--outline-width) var(--contrast-focus);
}

:is(
    button,
    input[type="submit"],
    input[type="button"],
    [role="button"]
  ).outline,
input[type="reset"].outline {
  --background-color: transparent;
  --color: var(--primary);
}
:is(
    button,
    input[type="submit"],
    input[type="button"],
    [role="button"]
  ).outline:is([aria-current], :hover, :active, :focus),
input[type="reset"].outline:is([aria-current], :hover, :active, :focus) {
  --background-color: transparent;
  --color: var(--primary-hover);
}

:is(
    button,
    input[type="submit"],
    input[type="button"],
    [role="button"]
  ).outline.secondary,
input[type="reset"].outline {
  --color: var(--secondary);
}
:is(
    button,
    input[type="submit"],
    input[type="button"],
    [role="button"]
  ).outline.secondary:is([aria-current], :hover, :active, :focus),
input[type="reset"].outline:is([aria-current], :hover, :active, :focus) {
  --color: var(--secondary-hover);
}

:is(
    button,
    input[type="submit"],
    input[type="button"],
    [role="button"]
  ).outline.contrast {
  --color: var(--contrast);
}
:is(
    button,
    input[type="submit"],
    input[type="button"],
    [role="button"]
  ).outline.contrast:is([aria-current], :hover, :active, :focus) {
  --color: var(--contrast-hover);
}

:where(
    button,
    [type="submit"],
    [type="button"],
    [type="reset"],
    [role="button"]
  )[disabled],
:where(fieldset[disabled])
  :is(
    button,
    [type="submit"],
    [type="button"],
    [type="reset"],
    [role="button"]
  ),
a[role="button"]:not([href]) {
  opacity: 0.5;
  pointer-events: none;
}

/**
 * Form elements
 */
input,
optgroup,
select,
textarea {
  margin: 0;
  font-size: 1rem;
  line-height: var(--line-height);
  font-family: inherit;
  letter-spacing: inherit;
}

input {
  overflow: visible;
}

select {
  text-transform: none;
}

legend {
  max-width: 100%;
  padding: 0;
  color: inherit;
  white-space: normal;
}

textarea {
  overflow: auto;
}

[type="checkbox"],
[type="radio"] {
  padding: 0;
}

::-webkit-inner-spin-button,
::-webkit-outer-spin-button {
  height: auto;
}

[type="search"] {
  -webkit-appearance: textfield;
  outline-offset: -2px;
}

[type="search"]::-webkit-search-decoration {
  -webkit-appearance: none;
}

::-webkit-file-upload-button {
  -webkit-appearance: button;
  font: inherit;
}

::-moz-focus-inner {
  padding: 0;
  border-style: none;
}

:-moz-focusring {
  outline: none;
}

:-moz-ui-invalid {
  box-shadow: none;
}

::-ms-expand {
  display: none;
}

[type="file"],
[type="range"] {
  padding: 0;
  border-width: 0;
}

input:not([type="checkbox"], [type="radio"], [type="range"]) {
  height: calc(
    1rem * var(--line-height) + var(--form-element-spacing-vertical) * 2 +
      var(--border-width) * 2
  );
}

fieldset {
  margin: 0;
  margin-bottom: var(--spacing);
  padding: 0;
  border: 0;
}

label,
fieldset legend {
  display: block;
  margin-bottom: calc(var(--spacing) * 0.25);
  font-weight: var(--form-label-font-weight, var(--font-weight));
}

input:not([type="checkbox"], [type="radio"]),
select,
textarea {
  width: 100%;
}

input:not([type="checkbox"], [type="radio"], [type="range"], [type="file"]),
select,
textarea {
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
  padding: var(--form-element-spacing-vertical)
    var(--form-element-spacing-horizontal);
}

input,
select,
textarea {
  --background-color: var(--form-element-background-color);
  --border-color: var(--form-element-border-color);
  --color: var(--form-element-color);
  --box-shadow: none;
  border: var(--border-width) solid var(--border-color);
  border-radius: var(--border-radius);
  outline: none;
  background-color: var(--background-color);
  box-shadow: var(--box-shadow);
  color: var(--color);
  font-weight: var(--font-weight);
  transition: background-color var(--transition), border-color var(--transition),
    color var(--transition), box-shadow var(--transition);
}

input:not(
    [type="submit"],
    [type="button"],
    [type="reset"],
    [type="checkbox"],
    [type="radio"],
    [readonly]
  ):is(:active, :focus),
:where(select, textarea):is(:active, :focus) {
  --background-color: var(--form-element-active-background-color);
}

input:not(
    [type="submit"],
    [type="button"],
    [type="reset"],
    [role="switch"],
    [readonly]
  ):is(:active, :focus),
:where(select, textarea):is(:active, :focus) {
  --border-color: var(--form-element-active-border-color);
}

input:not(
    [type="submit"],
    [type="button"],
    [type="reset"],
    [type="range"],
    [type="file"],
    [readonly]
  ):focus,
select:focus,
textarea:focus {
  --box-shadow: 0 0 0 var(--outline-width) var(--form-element-focus-color);
}

input:not([type="submit"], [type="button"], [type="reset"])[disabled],
select[disabled],
textarea[disabled],
:where(fieldset[disabled])
  :is(
    input:not([type="submit"], [type="button"], [type="reset"]),
    select,
    textarea
  ) {
  --background-color: var(--form-element-disabled-background-color);
  --border-color: var(--form-element-disabled-border-color);
  opacity: var(--form-element-disabled-opacity);
  pointer-events: none;
}

:where(input, select, textarea):not(
    [type="checkbox"],
    [type="radio"],
    [type="date"],
    [type="datetime-local"],
    [type="month"],
    [type="time"],
    [type="week"]
  )[aria-invalid] {
  padding-right: calc(
    var(--form-element-spacing-horizontal) + 1.5rem
  ) !important;
  padding-left: var(--form-element-spacing-horizontal);
  -webkit-padding-start: var(--form-element-spacing-horizontal) !important;
  padding-inline-start: var(--form-element-spacing-horizontal) !important;
  -webkit-padding-end: calc(
    var(--form-element-spacing-horizontal) + 1.5rem
  ) !important;
  padding-inline-end: calc(
    var(--form-element-spacing-horizontal) + 1.5rem
  ) !important;
  background-position: center right 0.75rem;
  background-size: 1rem auto;
  background-repeat: no-repeat;
}
:where(input, select, textarea):not(
    [type="checkbox"],
    [type="radio"],
    [type="date"],
    [type="datetime-local"],
    [type="month"],
    [type="time"],
    [type="week"]
  )[aria-invalid="false"] {
  background-image: var(--icon-valid);
}
:where(input, select, textarea):not(
    [type="checkbox"],
    [type="radio"],
    [type="date"],
    [type="datetime-local"],
    [type="month"],
    [type="time"],
    [type="week"]
  )[aria-invalid="true"] {
  background-image: var(--icon-invalid);
}
:where(input, select, textarea)[aria-invalid="false"] {
  --border-color: var(--form-element-valid-border-color);
}
:where(input, select, textarea)[aria-invalid="false"]:is(:active, :focus) {
  --border-color: var(--form-element-valid-active-border-color) !important;
  --box-shadow: 0 0 0 var(--outline-width) var(--form-element-valid-focus-color) !important;
}
:where(input, select, textarea)[aria-invalid="true"] {
  --border-color: var(--form-element-invalid-border-color);
}
:where(input, select, textarea)[aria-invalid="true"]:is(:active, :focus) {
  --border-color: var(--form-element-invalid-active-border-color) !important;
  --box-shadow: 0 0 0 var(--outline-width)
    var(--form-element-invalid-focus-color) !important;
}

[dir="rtl"]
  :where(input, select, textarea):not([type="checkbox"], [type="radio"]):is(
    [aria-invalid],
    [aria-invalid="true"],
    [aria-invalid="false"]
  ) {
  background-position: center left 0.75rem;
}

input::placeholder,
input::-webkit-input-placeholder,
textarea::placeholder,
textarea::-webkit-input-placeholder,
select:invalid {
  color: var(--form-element-placeholder-color);
  opacity: 1;
}

input:not([type="checkbox"], [type="radio"]),
select,
textarea {
  margin-bottom: var(--spacing);
}

select::-ms-expand {
  border: 0;
  background-color: transparent;
}
select:not([multiple], [size]) {
  padding-right: calc(var(--form-element-spacing-horizontal) + 1.5rem);
  padding-left: var(--form-element-spacing-horizontal);
  -webkit-padding-start: var(--form-element-spacing-horizontal);
  padding-inline-start: var(--form-element-spacing-horizontal);
  -webkit-padding-end: calc(var(--form-element-spacing-horizontal) + 1.5rem);
  padding-inline-end: calc(var(--form-element-spacing-horizontal) + 1.5rem);
  background-image: var(--icon-chevron);
  background-position: center right 0.75rem;
  background-size: 1rem auto;
  background-repeat: no-repeat;
}

[dir="rtl"] select:not([multiple], [size]) {
  background-position: center left 0.75rem;
}

:where(input, select, textarea) + small {
  display: block;
  width: 100%;
  margin-top: calc(var(--spacing) * -0.75);
  margin-bottom: var(--spacing);
  color: var(--muted-color);
}

label > :where(input, select, textarea) {
  margin-top: calc(var(--spacing) * 0.25);
}

/**
 * Form elements
 * Checkboxes & Radios
 */
[type="checkbox"],
[type="radio"] {
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
  width: 1.25em;
  height: 1.25em;
  margin-top: -0.125em;
  margin-right: 0.375em;
  margin-left: 0;
  -webkit-margin-start: 0;
  margin-inline-start: 0;
  -webkit-margin-end: 0.375em;
  margin-inline-end: 0.375em;
  border-width: var(--border-width);
  font-size: inherit;
  vertical-align: middle;
  cursor: pointer;
}
[type="checkbox"]::-ms-check,
[type="radio"]::-ms-check {
  display: none;
}
[type="checkbox"]:checked,
[type="checkbox"]:checked:active,
[type="checkbox"]:checked:focus,
[type="radio"]:checked,
[type="radio"]:checked:active,
[type="radio"]:checked:focus {
  --background-color: var(--primary);
  --border-color: var(--primary);
  background-image: var(--icon-checkbox);
  background-position: center;
  background-size: 0.75em auto;
  background-repeat: no-repeat;
}
[type="checkbox"] ~ label,
[type="radio"] ~ label {
  display: inline-block;
  margin-right: 0.375em;
  margin-bottom: 0;
  cursor: pointer;
}

[type="checkbox"]:indeterminate {
  --background-color: var(--primary);
  --border-color: var(--primary);
  background-image: var(--icon-minus);
  background-position: center;
  background-size: 0.75em auto;
  background-repeat: no-repeat;
}

[type="radio"] {
  border-radius: 50%;
}
[type="radio"]:checked,
[type="radio"]:checked:active,
[type="radio"]:checked:focus {
  --background-color: var(--primary-inverse);
  border-width: 0.35em;
  background-image: none;
}

[type="checkbox"][role="switch"] {
  --background-color: var(--switch-background-color);
  --border-color: var(--switch-background-color);
  --color: var(--switch-color);
  width: 2.25em;
  height: 1.25em;
  border: var(--border-width) solid var(--border-color);
  border-radius: 1.25em;
  background-color: var(--background-color);
  line-height: 1.25em;
}
[type="checkbox"][role="switch"]:focus {
  --background-color: var(--switch-background-color);
  --border-color: var(--switch-background-color);
}
[type="checkbox"][role="switch"]:checked {
  --background-color: var(--switch-checked-background-color);
  --border-color: var(--switch-checked-background-color);
}
[type="checkbox"][role="switch"]:before {
  display: block;
  width: calc(1.25em - (var(--border-width) * 2));
  height: 100%;
  border-radius: 50%;
  background-color: var(--color);
  content: "";
  transition: margin 0.1s ease-in-out;
}
[type="checkbox"][role="switch"]:checked {
  background-image: none;
}
[type="checkbox"][role="switch"]:checked::before {
  margin-left: calc(1.125em - var(--border-width));
  -webkit-margin-start: calc(1.125em - var(--border-width));
  margin-inline-start: calc(1.125em - var(--border-width));
}

[type="checkbox"][aria-invalid="false"],
[type="checkbox"]:checked[aria-invalid="false"],
[type="radio"][aria-invalid="false"],
[type="radio"]:checked[aria-invalid="false"],
[type="checkbox"][role="switch"][aria-invalid="false"],
[type="checkbox"][role="switch"]:checked[aria-invalid="false"] {
  --border-color: var(--form-element-valid-border-color);
}
[type="checkbox"][aria-invalid="true"],
[type="checkbox"]:checked[aria-invalid="true"],
[type="radio"][aria-invalid="true"],
[type="radio"]:checked[aria-invalid="true"],
[type="checkbox"][role="switch"][aria-invalid="true"],
[type="checkbox"][role="switch"]:checked[aria-invalid="true"] {
  --border-color: var(--form-element-invalid-border-color);
}

/**
 * Form elements
 * Alternatives input types (Not Checkboxes & Radios)
 */
[type="color"]::-webkit-color-swatch-wrapper {
  padding: 0;
}
[type="color"]::-moz-focus-inner {
  padding: 0;
}
[type="color"]::-webkit-color-swatch {
  border: 0;
  border-radius: calc(var(--border-radius) * 0.5);
}
[type="color"]::-moz-color-swatch {
  border: 0;
  border-radius: calc(var(--border-radius) * 0.5);
}

input:not([type="checkbox"], [type="radio"], [type="range"], [type="file"]):is(
    [type="date"],
    [type="datetime-local"],
    [type="month"],
    [type="time"],
    [type="week"]
  ) {
  --icon-position: 0.75rem;
  --icon-width: 1rem;
  padding-right: calc(var(--icon-width) + var(--icon-position));
  background-image: var(--icon-date);
  background-position: center right var(--icon-position);
  background-size: var(--icon-width) auto;
  background-repeat: no-repeat;
}
input:not(
    [type="checkbox"],
    [type="radio"],
    [type="range"],
    [type="file"]
  )[type="time"] {
  background-image: var(--icon-time);
}

[type="date"]::-webkit-calendar-picker-indicator,
[type="datetime-local"]::-webkit-calendar-picker-indicator,
[type="month"]::-webkit-calendar-picker-indicator,
[type="time"]::-webkit-calendar-picker-indicator,
[type="week"]::-webkit-calendar-picker-indicator {
  width: var(--icon-width);
  margin-right: calc(var(--icon-width) * -1);
  margin-left: var(--icon-position);
  opacity: 0;
}

[dir="rtl"]
  :is(
    [type="date"],
    [type="datetime-local"],
    [type="month"],
    [type="time"],
    [type="week"]
  ) {
  text-align: right;
}

[type="file"] {
  --color: var(--muted-color);
  padding: calc(var(--form-element-spacing-vertical) * 0.5) 0;
  border: 0;
  border-radius: 0;
  background: none;
}
[type="file"]::file-selector-button {
  --background-color: var(--secondary);
  --border-color: var(--secondary);
  --color: var(--secondary-inverse);
  margin-right: calc(var(--spacing) / 2);
  margin-left: 0;
  -webkit-margin-start: 0;
  margin-inline-start: 0;
  -webkit-margin-end: calc(var(--spacing) / 2);
  margin-inline-end: calc(var(--spacing) / 2);
  padding: calc(var(--form-element-spacing-vertical) * 0.5)
    calc(var(--form-element-spacing-horizontal) * 0.5);
  border: var(--border-width) solid var(--border-color);
  border-radius: var(--border-radius);
  outline: none;
  background-color: var(--background-color);
  box-shadow: var(--box-shadow);
  color: var(--color);
  font-weight: var(--font-weight);
  font-size: 1rem;
  line-height: var(--line-height);
  text-align: center;
  cursor: pointer;
  transition: background-color var(--transition), border-color var(--transition),
    color var(--transition), box-shadow var(--transition);
}
[type="file"]::file-selector-button:is(:hover, :active, :focus) {
  --background-color: var(--secondary-hover);
  --border-color: var(--secondary-hover);
}
[type="file"]::-webkit-file-upload-button {
  --background-color: var(--secondary);
  --border-color: var(--secondary);
  --color: var(--secondary-inverse);
  margin-right: calc(var(--spacing) / 2);
  margin-left: 0;
  -webkit-margin-start: 0;
  margin-inline-start: 0;
  -webkit-margin-end: calc(var(--spacing) / 2);
  margin-inline-end: calc(var(--spacing) / 2);
  padding: calc(var(--form-element-spacing-vertical) * 0.5)
    calc(var(--form-element-spacing-horizontal) * 0.5);
  border: var(--border-width) solid var(--border-color);
  border-radius: var(--border-radius);
  outline: none;
  background-color: var(--background-color);
  box-shadow: var(--box-shadow);
  color: var(--color);
  font-weight: var(--font-weight);
  font-size: 1rem;
  line-height: var(--line-height);
  text-align: center;
  cursor: pointer;
  -webkit-transition: background-color var(--transition),
    border-color var(--transition), color var(--transition),
    box-shadow var(--transition);
  transition: background-color var(--transition), border-color var(--transition),
    color var(--transition), box-shadow var(--transition);
}
[type="file"]::-webkit-file-upload-button:is(:hover, :active, :focus) {
  --background-color: var(--secondary-hover);
  --border-color: var(--secondary-hover);
}
[type="file"]::-ms-browse {
  --background-color: var(--secondary);
  --border-color: var(--secondary);
  --color: var(--secondary-inverse);
  margin-right: calc(var(--spacing) / 2);
  margin-left: 0;
  margin-inline-start: 0;
  margin-inline-end: calc(var(--spacing) / 2);
  padding: calc(var(--form-element-spacing-vertical) * 0.5)
    calc(var(--form-element-spacing-horizontal) * 0.5);
  border: var(--border-width) solid var(--border-color);
  border-radius: var(--border-radius);
  outline: none;
  background-color: var(--background-color);
  box-shadow: var(--box-shadow);
  color: var(--color);
  font-weight: var(--font-weight);
  font-size: 1rem;
  line-height: var(--line-height);
  text-align: center;
  cursor: pointer;
  -ms-transition: background-color var(--transition),
    border-color var(--transition), color var(--transition),
    box-shadow var(--transition);
  transition: background-color var(--transition), border-color var(--transition),
    color var(--transition), box-shadow var(--transition);
}
[type="file"]::-ms-browse:is(:hover, :active, :focus) {
  --background-color: var(--secondary-hover);
  --border-color: var(--secondary-hover);
}

[type="range"] {
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
  width: 100%;
  height: 1.25rem;
  background: none;
}
[type="range"]::-webkit-slider-runnable-track {
  width: 100%;
  height: 0.25rem;
  border-radius: var(--border-radius);
  background-color: var(--range-border-color);
  -webkit-transition: background-color var(--transition),
    box-shadow var(--transition);
  transition: background-color var(--transition), box-shadow var(--transition);
}
[type="range"]::-moz-range-track {
  width: 100%;
  height: 0.25rem;
  border-radius: var(--border-radius);
  background-color: var(--range-border-color);
  -moz-transition: background-color var(--transition),
    box-shadow var(--transition);
  transition: background-color var(--transition), box-shadow var(--transition);
}
[type="range"]::-ms-track {
  width: 100%;
  height: 0.25rem;
  border-radius: var(--border-radius);
  background-color: var(--range-border-color);
  -ms-transition: background-color var(--transition),
    box-shadow var(--transition);
  transition: background-color var(--transition), box-shadow var(--transition);
}
[type="range"]::-webkit-slider-thumb {
  -webkit-appearance: none;
  width: 1.25rem;
  height: 1.25rem;
  margin-top: -0.5rem;
  border: 2px solid var(--range-thumb-border-color);
  border-radius: 50%;
  background-color: var(--range-thumb-color);
  cursor: pointer;
  -webkit-transition: background-color var(--transition),
    transform var(--transition);
  transition: background-color var(--transition), transform var(--transition);
}
[type="range"]::-moz-range-thumb {
  -webkit-appearance: none;
  width: 1.25rem;
  height: 1.25rem;
  margin-top: -0.5rem;
  border: 2px solid var(--range-thumb-border-color);
  border-radius: 50%;
  background-color: var(--range-thumb-color);
  cursor: pointer;
  -moz-transition: background-color var(--transition),
    transform var(--transition);
  transition: background-color var(--transition), transform var(--transition);
}
[type="range"]::-ms-thumb {
  -webkit-appearance: none;
  width: 1.25rem;
  height: 1.25rem;
  margin-top: -0.5rem;
  border: 2px solid var(--range-thumb-border-color);
  border-radius: 50%;
  background-color: var(--range-thumb-color);
  cursor: pointer;
  -ms-transition: background-color var(--transition),
    transform var(--transition);
  transition: background-color var(--transition), transform var(--transition);
}
[type="range"]:hover,
[type="range"]:focus {
  --range-border-color: var(--range-active-border-color);
  --range-thumb-color: var(--range-thumb-hover-color);
}
[type="range"]:active {
  --range-thumb-color: var(--range-thumb-active-color);
}
[type="range"]:active::-webkit-slider-thumb {
  transform: scale(1.25);
}
[type="range"]:active::-moz-range-thumb {
  transform: scale(1.25);
}
[type="range"]:active::-ms-thumb {
  transform: scale(1.25);
}

input:not(
    [type="checkbox"],
    [type="radio"],
    [type="range"],
    [type="file"]
  )[type="search"] {
  -webkit-padding-start: calc(var(--form-element-spacing-horizontal) + 1.75rem);
  padding-inline-start: calc(var(--form-element-spacing-horizontal) + 1.75rem);
  border-radius: 5rem;
  background-image: var(--icon-search);
  background-position: center left 1.125rem;
  background-size: 1rem auto;
  background-repeat: no-repeat;
}
input:not(
    [type="checkbox"],
    [type="radio"],
    [type="range"],
    [type="file"]
  )[type="search"][aria-invalid] {
  -webkit-padding-start: calc(
    var(--form-element-spacing-horizontal) + 1.75rem
  ) !important;
  padding-inline-start: calc(
    var(--form-element-spacing-horizontal) + 1.75rem
  ) !important;
  background-position: center left 1.125rem, center right 0.75rem;
}
input:not(
    [type="checkbox"],
    [type="radio"],
    [type="range"],
    [type="file"]
  )[type="search"][aria-invalid="false"] {
  background-image: var(--icon-search), var(--icon-valid);
}
input:not(
    [type="checkbox"],
    [type="radio"],
    [type="range"],
    [type="file"]
  )[type="search"][aria-invalid="true"] {
  background-image: var(--icon-search), var(--icon-invalid);
}

[type="search"]::-webkit-search-cancel-button {
  -webkit-appearance: none;
  display: none;
}

[dir="rtl"]
  :where(input):not(
    [type="checkbox"],
    [type="radio"],
    [type="range"],
    [type="file"]
  )[type="search"] {
  background-position: center right 1.125rem;
}
[dir="rtl"]
  :where(input):not(
    [type="checkbox"],
    [type="radio"],
    [type="range"],
    [type="file"]
  )[type="search"][aria-invalid] {
  background-position: center right 1.125rem, center left 0.75rem;
}

/**
 * Table
 */
:where(table) {
  width: 100%;
  border-collapse: collapse;
  border-spacing: 0;
  text-indent: 0;
}

th,
td {
  padding: calc(var(--spacing) / 2) var(--spacing);
  border-bottom: var(--border-width) solid var(--table-border-color);
  color: var(--color);
  font-weight: var(--font-weight);
  font-size: var(--font-size);
  text-align: left;
  text-align: start;
}

tfoot th,
tfoot td {
  border-top: var(--border-width) solid var(--table-border-color);
  border-bottom: 0;
}

table[role="grid"] tbody tr:nth-child(odd) {
  background-color: var(--table-row-stripped-background-color);
}

/**
 * Code
 */
pre,
code,
kbd,
samp {
  font-size: 0.875em;
  font-family: var(--font-family);
}

pre {
  -ms-overflow-style: scrollbar;
  overflow: auto;
}

pre,
code,
kbd {
  border-radius: var(--border-radius);
  background: var(--code-background-color);
  color: var(--code-color);
  font-weight: var(--font-weight);
  line-height: initial;
}

code,
kbd {
  display: inline-block;
  padding: 0.375rem 0.5rem;
}

pre {
  display: block;
  margin-bottom: var(--spacing);
  overflow-x: auto;
}
pre > code {
  display: block;
  padding: var(--spacing);
  background: none;
  font-size: 14px;
  line-height: var(--line-height);
}

code b {
  color: var(--code-tag-color);
  font-weight: var(--font-weight);
}
code i {
  color: var(--code-property-color);
  font-style: normal;
}
code u {
  color: var(--code-value-color);
  text-decoration: none;
}
code em {
  color: var(--code-comment-color);
  font-style: normal;
}

kbd {
  background-color: var(--code-kbd-background-color);
  color: var(--code-kbd-color);
  vertical-align: baseline;
}

/**
 * Miscs
 */
hr {
  height: 0;
  border: 0;
  border-top: 1px solid var(--muted-border-color);
  color: inherit;
}

[hidden],
template {
  display: none !important;
}

canvas {
  display: inline-block;
}

/**
 * Accordion (<details>)
 */
details {
  display: block;
  margin-bottom: var(--spacing);
  padding-bottom: var(--spacing);
  border-bottom: var(--border-width) solid var(--accordion-border-color);
}
details summary {
  line-height: 1rem;
  list-style-type: none;
  cursor: pointer;
  transition: color var(--transition);
}
details summary:not([role]) {
  color: var(--accordion-close-summary-color);
}
details summary::-webkit-details-marker {
  display: none;
}
details summary::marker {
  display: none;
}
details summary::-moz-list-bullet {
  list-style-type: none;
}
details summary::after {
  display: block;
  width: 1rem;
  height: 1rem;
  -webkit-margin-start: calc(var(--spacing, 1rem) * 0.5);
  margin-inline-start: calc(var(--spacing, 1rem) * 0.5);
  float: right;
  transform: rotate(-90deg);
  background-image: var(--icon-chevron);
  background-position: right center;
  background-size: 1rem auto;
  background-repeat: no-repeat;
  content: "";
  transition: transform var(--transition);
}
details summary:focus {
  outline: none;
}
details summary:focus:not([role="button"]) {
  color: var(--accordion-active-summary-color);
}
details summary[role="button"] {
  width: 100%;
  text-align: left;
}
details summary[role="button"]::after {
  height: calc(1rem * var(--line-height, 1.5));
  background-image: var(--icon-chevron-button);
}
details summary[role="button"]:not(.outline).contrast::after {
  background-image: var(--icon-chevron-button-inverse);
}
details[open] > summary {
  margin-bottom: calc(var(--spacing));
}
details[open] > summary:not([role]):not(:focus) {
  color: var(--accordion-open-summary-color);
}
details[open] > summary::after {
  transform: rotate(0);
}

[dir="rtl"] details summary {
  text-align: right;
}
[dir="rtl"] details summary::after {
  float: left;
  background-position: left center;
}

/**
 * Card (<article>)
 */
article {
  margin: var(--block-spacing-vertical) 0;
  padding: var(--block-spacing-vertical) var(--block-spacing-horizontal);
  border-radius: var(--border-radius);
  background: var(--card-background-color);
  box-shadow: var(--card-box-shadow);
}
article > header,
article > footer {
  margin-right: calc(var(--block-spacing-horizontal) * -1);
  margin-left: calc(var(--block-spacing-horizontal) * -1);
  padding: calc(var(--block-spacing-vertical) * 0.66)
    var(--block-spacing-horizontal);
  background-color: var(--card-sectionning-background-color);
}
article > header {
  margin-top: calc(var(--block-spacing-vertical) * -1);
  margin-bottom: var(--block-spacing-vertical);
  border-bottom: var(--border-width) solid var(--card-border-color);
  border-top-right-radius: var(--border-radius);
  border-top-left-radius: var(--border-radius);
}
article > footer {
  margin-top: var(--block-spacing-vertical);
  margin-bottom: calc(var(--block-spacing-vertical) * -1);
  border-top: var(--border-width) solid var(--card-border-color);
  border-bottom-right-radius: var(--border-radius);
  border-bottom-left-radius: var(--border-radius);
}

/**
 * Modal (<dialog>)
 */
#mount {
  --scrollbar-width: 0px;
}

dialog {
  display: flex;
  z-index: 999;
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  align-items: center;
  justify-content: center;
  width: inherit;
  min-width: 100%;
  height: inherit;
  min-height: 100%;
  padding: var(--spacing);
  border: 0;
  -webkit-backdrop-filter: var(--modal-overlay-backdrop-filter);
  backdrop-filter: var(--modal-overlay-backdrop-filter);
  background-color: var(--modal-overlay-background-color);
  color: var(--color);
}
dialog article {
  max-height: calc(100vh - var(--spacing) * 2);
  overflow: auto;
}
@media (min-width: 576px) {
  dialog article {
    max-width: 510px;
  }
}
@media (min-width: 768px) {
  dialog article {
    max-width: 700px;
  }
}
dialog article > header,
dialog article > footer {
  padding: calc(var(--block-spacing-vertical) * 0.5)
    var(--block-spacing-horizontal);
}
dialog article > header .close {
  margin: 0;
  margin-left: var(--spacing);
  float: right;
}
dialog article > footer {
  text-align: right;
}
dialog article > footer [role="button"] {
  margin-bottom: 0;
}
dialog article > footer [role="button"]:not(:first-of-type) {
  margin-left: calc(var(--spacing) * 0.5);
}
dialog article p:last-of-type {
  margin: 0;
}
dialog article .close {
  display: block;
  width: 1rem;
  height: 1rem;
  margin-top: calc(var(--block-spacing-vertical) * -0.5);
  margin-bottom: var(--typography-spacing-vertical);
  margin-left: auto;
  background-image: var(--icon-close);
  background-position: center;
  background-size: auto 1rem;
  background-repeat: no-repeat;
  opacity: 0.5;
  transition: opacity var(--transition);
}
dialog article .close:is([aria-current], :hover, :active, :focus) {
  opacity: 1;
}
dialog:not([open]),
dialog[open="false"] {
  display: none;
}

.modal-is-open {
  padding-right: var(--scrollbar-width, 0px);
  overflow: hidden;
  pointer-events: none;
}
.modal-is-open dialog {
  pointer-events: auto;
}

:where(.modal-is-opening, .modal-is-closing) dialog,
:where(.modal-is-opening, .modal-is-closing) dialog > article {
  animation-duration: 0.2s;
  animation-timing-function: ease-in-out;
  animation-fill-mode: both;
}
:where(.modal-is-opening, .modal-is-closing) dialog {
  animation-duration: 0.8s;
  animation-name: modal-overlay;
}
:where(.modal-is-opening, .modal-is-closing) dialog > article {
  animation-delay: 0.2s;
  animation-name: modal;
}

.modal-is-closing dialog,
.modal-is-closing dialog > article {
  animation-delay: 0s;
  animation-direction: reverse;
}

@keyframes modal-overlay {
  from {
    -webkit-backdrop-filter: none;
    backdrop-filter: none;
    background-color: transparent;
  }
}
@keyframes modal {
  from {
    transform: translateY(-100%);
    opacity: 0;
  }
}
/**
 * Nav
 */
:where(nav li)::before {
  float: left;
  content: "​";
}

nav,
nav ul {
  display: flex;
}

nav {
  justify-content: space-between;
}
nav ol,
nav ul {
  align-items: center;
  margin-bottom: 0;
  padding: 0;
  list-style: none;
}
nav ol:first-of-type,
nav ul:first-of-type {
  margin-left: calc(var(--nav-element-spacing-horizontal) * -1);
}
nav ol:last-of-type,
nav ul:last-of-type {
  margin-right: calc(var(--nav-element-spacing-horizontal) * -1);
}
nav li {
  display: inline-block;
  margin: 0;
  padding: var(--nav-element-spacing-vertical)
    var(--nav-element-spacing-horizontal);
}
nav li > * {
  --spacing: 0;
}
nav :where(a, [role="link"]) {
  display: inline-block;
  margin: calc(var(--nav-link-spacing-vertical) * -1)
    calc(var(--nav-link-spacing-horizontal) * -1);
  padding: var(--nav-link-spacing-vertical) var(--nav-link-spacing-horizontal);
  border-radius: var(--border-radius);
  text-decoration: none;
}
nav :where(a, [role="link"]):is([aria-current], :hover, :active, :focus) {
  text-decoration: none;
}
nav[aria-label="breadcrumb"] {
  align-items: center;
  justify-content: start;
}
nav[aria-label="breadcrumb"] ul li:not(:first-child) {
  -webkit-margin-start: var(--nav-link-spacing-horizontal);
  margin-inline-start: var(--nav-link-spacing-horizontal);
}
nav[aria-label="breadcrumb"] ul li:not(:last-child) ::after {
  position: absolute;
  width: calc(var(--nav-link-spacing-horizontal) * 2);
  -webkit-margin-start: calc(var(--nav-link-spacing-horizontal) / 2);
  margin-inline-start: calc(var(--nav-link-spacing-horizontal) / 2);
  content: "/";
  color: var(--muted-color);
  text-align: center;
}
nav[aria-label="breadcrumb"] a[aria-current] {
  background-color: transparent;
  color: inherit;
  text-decoration: none;
  pointer-events: none;
}
nav [role="button"] {
  margin-right: inherit;
  margin-left: inherit;
  padding: var(--nav-link-spacing-vertical) var(--nav-link-spacing-horizontal);
}

aside nav,
aside ol,
aside ul,
aside li {
  display: block;
}
aside li {
  padding: calc(var(--nav-element-spacing-vertical) * 0.5)
    var(--nav-element-spacing-horizontal);
}
aside li a {
  display: block;
}
aside li [role="button"] {
  margin: inherit;
}

[dir="rtl"] nav[aria-label="breadcrumb"] ul li:not(:last-child) ::after {
  content: "\\";
}

/**
 * Progress
 */
progress {
  display: inline-block;
  vertical-align: baseline;
}

progress {
  -webkit-appearance: none;
  -moz-appearance: none;
  display: inline-block;
  appearance: none;
  width: 100%;
  height: 0.5rem;
  margin-bottom: calc(var(--spacing) * 0.5);
  overflow: hidden;
  border: 0;
  border-radius: var(--border-radius);
  background-color: var(--progress-background-color);
  color: var(--progress-color);
}
progress::-webkit-progress-bar {
  border-radius: var(--border-radius);
  background: none;
}
progress[value]::-webkit-progress-value {
  background-color: var(--progress-color);
}
progress::-moz-progress-bar {
  background-color: var(--progress-color);
}
@media (prefers-reduced-motion: no-preference) {
  progress:indeterminate {
    background: var(--progress-background-color)
      linear-gradient(
        to right,
        var(--progress-color) 30%,
        var(--progress-background-color) 30%
      )
      top left/150% 150% no-repeat;
    animation: progress-indeterminate 1s linear infinite;
  }
  progress:indeterminate[value]::-webkit-progress-value {
    background-color: transparent;
  }
  progress:indeterminate::-moz-progress-bar {
    background-color: transparent;
  }
}

@media (prefers-reduced-motion: no-preference) {
  [dir="rtl"] progress:indeterminate {
    animation-direction: reverse;
  }
}

@keyframes progress-indeterminate {
  0% {
    background-position: 200% 0;
  }
  100% {
    background-position: -200% 0;
  }
}
/**
 * Dropdown ([role="list"])
 */
details[role="list"],
li[role="list"] {
  position: relative;
}

details[role="list"] summary + ul,
li[role="list"] > ul {
  display: flex;
  z-index: 99;
  position: absolute;
  top: auto;
  right: 0;
  left: 0;
  flex-direction: column;
  margin: 0;
  padding: 0;
  border: var(--border-width) solid var(--dropdown-border-color);
  border-radius: var(--border-radius);
  border-top-right-radius: 0;
  border-top-left-radius: 0;
  background-color: var(--dropdown-background-color);
  box-shadow: var(--card-box-shadow);
  color: var(--dropdown-color);
  white-space: nowrap;
}
details[role="list"] summary + ul li,
li[role="list"] > ul li {
  width: 100%;
  margin-bottom: 0;
  padding: calc(var(--form-element-spacing-vertical) * 0.5)
    var(--form-element-spacing-horizontal);
  list-style: none;
}
details[role="list"] summary + ul li:first-of-type,
li[role="list"] > ul li:first-of-type {
  margin-top: calc(var(--form-element-spacing-vertical) * 0.5);
}
details[role="list"] summary + ul li:last-of-type,
li[role="list"] > ul li:last-of-type {
  margin-bottom: calc(var(--form-element-spacing-vertical) * 0.5);
}
details[role="list"] summary + ul li a,
li[role="list"] > ul li a {
  display: block;
  margin: calc(var(--form-element-spacing-vertical) * -0.5)
    calc(var(--form-element-spacing-horizontal) * -1);
  padding: calc(var(--form-element-spacing-vertical) * 0.5)
    var(--form-element-spacing-horizontal);
  overflow: hidden;
  color: var(--dropdown-color);
  text-decoration: none;
  text-overflow: ellipsis;
}
details[role="list"] summary + ul li a:hover,
li[role="list"] > ul li a:hover {
  background-color: var(--dropdown-hover-background-color);
}

details[role="list"] summary::after,
li[role="list"] > a::after {
  display: block;
  width: 1rem;
  height: calc(1rem * var(--line-height, 1.5));
  -webkit-margin-start: 0.5rem;
  margin-inline-start: 0.5rem;
  float: right;
  transform: rotate(0deg);
  background-position: right center;
  background-size: 1rem auto;
  background-repeat: no-repeat;
  content: "";
}

details[role="list"] {
  padding: 0;
  border-bottom: none;
}
details[role="list"] summary {
  margin-bottom: 0;
}
details[role="list"] summary:not([role]) {
  height: calc(
    1rem * var(--line-height) + var(--form-element-spacing-vertical) * 2 +
      var(--border-width) * 2
  );
  padding: var(--form-element-spacing-vertical)
    var(--form-element-spacing-horizontal);
  border: var(--border-width) solid var(--form-element-border-color);
  border-radius: var(--border-radius);
  background-color: var(--form-element-background-color);
  color: var(--form-element-placeholder-color);
  line-height: inherit;
  cursor: pointer;
  transition: background-color var(--transition), border-color var(--transition),
    color var(--transition), box-shadow var(--transition);
}
details[role="list"] summary:not([role]):active,
details[role="list"] summary:not([role]):focus {
  border-color: var(--form-element-active-border-color);
  background-color: var(--form-element-active-background-color);
}
details[role="list"] summary:not([role]):focus {
  box-shadow: 0 0 0 var(--outline-width) var(--form-element-focus-color);
}
details[role="list"][open] summary {
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
details[role="list"][open] summary::before {
  display: block;
  z-index: 1;
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  background: none;
  content: "";
  cursor: default;
}

nav details[role="list"] summary,
nav li[role="list"] a {
  display: flex;
  direction: ltr;
}

nav details[role="list"] summary + ul,
nav li[role="list"] > ul {
  min-width: -moz-fit-content;
  min-width: fit-content;
  border-radius: var(--border-radius);
}
nav details[role="list"] summary + ul li a,
nav li[role="list"] > ul li a {
  border-radius: 0;
}

nav details[role="list"] summary,
nav details[role="list"] summary:not([role]) {
  height: auto;
  padding: var(--nav-link-spacing-vertical) var(--nav-link-spacing-horizontal);
}
nav details[role="list"][open] summary {
  border-radius: var(--border-radius);
}
nav details[role="list"] summary + ul {
  margin-top: var(--outline-width);
  -webkit-margin-start: 0;
  margin-inline-start: 0;
}
nav details[role="list"] summary[role="link"] {
  margin-bottom: calc(var(--nav-link-spacing-vertical) * -1);
  line-height: var(--line-height);
}
nav details[role="list"] summary[role="link"] + ul {
  margin-top: calc(var(--nav-link-spacing-vertical) + var(--outline-width));
  -webkit-margin-start: calc(var(--nav-link-spacing-horizontal) * -1);
  margin-inline-start: calc(var(--nav-link-spacing-horizontal) * -1);
}

li[role="list"]:hover > ul,
li[role="list"] a:active ~ ul,
li[role="list"] a:focus ~ ul {
  display: flex;
}
li[role="list"] > ul {
  display: none;
  margin-top: calc(var(--nav-link-spacing-vertical) + var(--outline-width));
  -webkit-margin-start: calc(
    var(--nav-element-spacing-horizontal) - var(--nav-link-spacing-horizontal)
  );
  margin-inline-start: calc(
    var(--nav-element-spacing-horizontal) - var(--nav-link-spacing-horizontal)
  );
}
li[role="list"] > a::after {
  background-image: var(--icon-chevron);
}

/**
 * Loading ([aria-busy=true])
 */
[aria-busy="true"] {
  cursor: progress;
}

[aria-busy="true"]:not(input, select, textarea)::before {
  display: inline-block;
  width: 1em;
  height: 1em;
  border: 0.1875em solid currentColor;
  border-radius: 1em;
  border-right-color: transparent;
  content: "";
  vertical-align: text-bottom;
  vertical-align: -0.125em;
  animation: spinner 0.75s linear infinite;
  opacity: var(--loading-spinner-opacity);
}
[aria-busy="true"]:not(input, select, textarea):not(:empty)::before {
  margin-right: calc(var(--spacing) * 0.5);
  margin-left: 0;
  -webkit-margin-start: 0;
  margin-inline-start: 0;
  -webkit-margin-end: calc(var(--spacing) * 0.5);
  margin-inline-end: calc(var(--spacing) * 0.5);
}
[aria-busy="true"]:not(input, select, textarea):empty {
  text-align: center;
}

button[aria-busy="true"],
input[type="submit"][aria-busy="true"],
input[type="button"][aria-busy="true"],
input[type="reset"][aria-busy="true"],
a[aria-busy="true"] {
  pointer-events: none;
}

@keyframes spinner {
  to {
    transform: rotate(360deg);
  }
}
/**
 * Tooltip ([data-tooltip])
 */
[data-tooltip] {
  position: relative;
}
[data-tooltip]:not(a, button, input) {
  border-bottom: 1px dotted;
  text-decoration: none;
  cursor: help;
}
[data-tooltip][data-placement="top"]::before,
[data-tooltip][data-placement="top"]::after,
[data-tooltip]::before,
[data-tooltip]::after {
  display: block;
  z-index: 99;
  position: absolute;
  bottom: 100%;
  left: 50%;
  padding: 0.25rem 0.5rem;
  overflow: hidden;
  transform: translate(-50%, -0.25rem);
  border-radius: var(--border-radius);
  background: var(--tooltip-background-color);
  content: attr(data-tooltip);
  color: var(--tooltip-color);
  font-style: normal;
  font-weight: var(--font-weight);
  font-size: 0.875rem;
  text-decoration: none;
  text-overflow: ellipsis;
  white-space: nowrap;
  opacity: 0;
  pointer-events: none;
}
[data-tooltip][data-placement="top"]::after,
[data-tooltip]::after {
  padding: 0;
  transform: translate(-50%, 0rem);
  border-top: 0.3rem solid;
  border-right: 0.3rem solid transparent;
  border-left: 0.3rem solid transparent;
  border-radius: 0;
  background-color: transparent;
  content: "";
  color: var(--tooltip-background-color);
}
[data-tooltip][data-placement="bottom"]::before,
[data-tooltip][data-placement="bottom"]::after {
  top: 100%;
  bottom: auto;
  transform: translate(-50%, 0.25rem);
}
[data-tooltip][data-placement="bottom"]:after {
  transform: translate(-50%, -0.3rem);
  border: 0.3rem solid transparent;
  border-bottom: 0.3rem solid;
}
[data-tooltip][data-placement="left"]::before,
[data-tooltip][data-placement="left"]::after {
  top: 50%;
  right: 100%;
  bottom: auto;
  left: auto;
  transform: translate(-0.25rem, -50%);
}
[data-tooltip][data-placement="left"]:after {
  transform: translate(0.3rem, -50%);
  border: 0.3rem solid transparent;
  border-left: 0.3rem solid;
}
[data-tooltip][data-placement="right"]::before,
[data-tooltip][data-placement="right"]::after {
  top: 50%;
  right: auto;
  bottom: auto;
  left: 100%;
  transform: translate(0.25rem, -50%);
}
[data-tooltip][data-placement="right"]:after {
  transform: translate(-0.3rem, -50%);
  border: 0.3rem solid transparent;
  border-right: 0.3rem solid;
}
[data-tooltip]:focus::before,
[data-tooltip]:focus::after,
[data-tooltip]:hover::before,
[data-tooltip]:hover::after {
  opacity: 1;
}
@media (hover: hover) and (pointer: fine) {
  [data-tooltip][data-placement="bottom"]:focus::before,
  [data-tooltip][data-placement="bottom"]:focus::after,
  [data-tooltip][data-placement="bottom"]:hover [data-tooltip]:focus::before,
  [data-tooltip][data-placement="bottom"]:hover [data-tooltip]:focus::after,
  [data-tooltip]:hover::before,
  [data-tooltip]:hover::after {
    animation-duration: 0.2s;
    animation-name: tooltip-slide-top;
  }
  [data-tooltip][data-placement="bottom"]:focus::after,
  [data-tooltip][data-placement="bottom"]:hover [data-tooltip]:focus::after,
  [data-tooltip]:hover::after {
    animation-name: tooltip-caret-slide-top;
  }
  [data-tooltip][data-placement="bottom"]:focus::before,
  [data-tooltip][data-placement="bottom"]:focus::after,
  [data-tooltip][data-placement="bottom"]:hover::before,
  [data-tooltip][data-placement="bottom"]:hover::after {
    animation-duration: 0.2s;
    animation-name: tooltip-slide-bottom;
  }
  [data-tooltip][data-placement="bottom"]:focus::after,
  [data-tooltip][data-placement="bottom"]:hover::after {
    animation-name: tooltip-caret-slide-bottom;
  }
  [data-tooltip][data-placement="left"]:focus::before,
  [data-tooltip][data-placement="left"]:focus::after,
  [data-tooltip][data-placement="left"]:hover::before,
  [data-tooltip][data-placement="left"]:hover::after {
    animation-duration: 0.2s;
    animation-name: tooltip-slide-left;
  }
  [data-tooltip][data-placement="left"]:focus::after,
  [data-tooltip][data-placement="left"]:hover::after {
    animation-name: tooltip-caret-slide-left;
  }
  [data-tooltip][data-placement="right"]:focus::before,
  [data-tooltip][data-placement="right"]:focus::after,
  [data-tooltip][data-placement="right"]:hover::before,
  [data-tooltip][data-placement="right"]:hover::after {
    animation-duration: 0.2s;
    animation-name: tooltip-slide-right;
  }
  [data-tooltip][data-placement="right"]:focus::after,
  [data-tooltip][data-placement="right"]:hover::after {
    animation-name: tooltip-caret-slide-right;
  }
}
@keyframes tooltip-slide-top {
  from {
    transform: translate(-50%, 0.75rem);
    opacity: 0;
  }
  to {
    transform: translate(-50%, -0.25rem);
    opacity: 1;
  }
}
@keyframes tooltip-caret-slide-top {
  from {
    opacity: 0;
  }
  50% {
    transform: translate(-50%, -0.25rem);
    opacity: 0;
  }
  to {
    transform: translate(-50%, 0rem);
    opacity: 1;
  }
}
@keyframes tooltip-slide-bottom {
  from {
    transform: translate(-50%, -0.75rem);
    opacity: 0;
  }
  to {
    transform: translate(-50%, 0.25rem);
    opacity: 1;
  }
}
@keyframes tooltip-caret-slide-bottom {
  from {
    opacity: 0;
  }
  50% {
    transform: translate(-50%, -0.5rem);
    opacity: 0;
  }
  to {
    transform: translate(-50%, -0.3rem);
    opacity: 1;
  }
}
@keyframes tooltip-slide-left {
  from {
    transform: translate(0.75rem, -50%);
    opacity: 0;
  }
  to {
    transform: translate(-0.25rem, -50%);
    opacity: 1;
  }
}
@keyframes tooltip-caret-slide-left {
  from {
    opacity: 0;
  }
  50% {
    transform: translate(0.05rem, -50%);
    opacity: 0;
  }
  to {
    transform: translate(0.3rem, -50%);
    opacity: 1;
  }
}
@keyframes tooltip-slide-right {
  from {
    transform: translate(-0.75rem, -50%);
    opacity: 0;
  }
  to {
    transform: translate(0.25rem, -50%);
    opacity: 1;
  }
}
@keyframes tooltip-caret-slide-right {
  from {
    opacity: 0;
  }
  50% {
    transform: translate(-0.05rem, -50%);
    opacity: 0;
  }
  to {
    transform: translate(-0.3rem, -50%);
    opacity: 1;
  }
}

/**
 * Accessibility & User interaction
 */
[aria-controls] {
  cursor: pointer;
}

[aria-disabled="true"],
[disabled] {
  cursor: not-allowed;
}

[aria-hidden="false"][hidden] {
  display: initial;
}

[aria-hidden="false"][hidden]:not(:focus) {
  clip: rect(0, 0, 0, 0);
  position: absolute;
}

a,
area,
button,
input,
label,
select,
summary,
textarea,
[tabindex] {
  -ms-touch-action: manipulation;
}

[dir="rtl"] {
  direction: rtl;
}

/**
* Reduce Motion Features
*/
@media (prefers-reduced-motion: reduce) {
  *:not([aria-busy="true"]),
  :not([aria-busy="true"])::before,
  :not([aria-busy="true"])::after {
    background-attachment: initial !important;
    animation-duration: 1ms !important;
    animation-delay: -1ms !important;
    animation-iteration-count: 1 !important;
    scroll-behavior: auto !important;
    transition-delay: 0s !important;
    transition-duration: 0s !important;
  }
}

#mount#mount {
  /* --primary: rgb(227, 59, 126); */
  --primary: #ea4c89;
  --primary-hover: #f082ac;
  --icon-xia: url("data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPGcgaWQ9IkZyYW1lIj4KPHBhdGggaWQ9IlZlY3RvciIgZD0iTTguMDAyOTEgOS42Nzk4M0wzLjgzMzM5IDUuNTEyMjFMMy4wMjUzOSA2LjMxOTgzTDguMDAzMjkgMTEuMjk1MUwxMi45NzYyIDYuMzE5ODNMMTIuMTY3OSA1LjUxMjIxTDguMDAyOTEgOS42Nzk4M1oiIGZpbGw9IiM4MzgzODMiLz4KPC9nPgo8L3N2Zz4K");
  --switch-checked-background-color: var(--primary);
}

li.select-link.select-link:hover > ul {
  display: none;
}
li.select-link.select-link > ul {
  display: none;
}
li.select-link.select-link a:focus ~ ul {
  display: none;
}

li.select-link.select-link a:active ~ ul {
  display: none;
}
li.select-link-active.select-link-active > ul {
  display: flex;
}
li.select-link-active.select-link-active:hover > ul {
  display: flex;
}

li.select-link-active.select-link-active a:focus ~ ul {
  display: flex;
}

li.select-link-active.select-link-active a:active ~ ul {
  display: flex;
}
ul.select-link-ul.select-link-ul {
  right: 0px;
  left: auto;
}

a.select-link-selected {
  background-color: var(--primary-focus);
}
.immersive-translate-no-select {
  -webkit-touch-callout: none; /* iOS Safari */
  -webkit-user-select: none; /* Safari */
  -khtml-user-select: none; /* Konqueror HTML */
  -moz-user-select: none; /* Old versions of Firefox */
  -ms-user-select: none; /* Internet Explorer/Edge */
  user-select: none;
}

/* li[role="list"].no-arrow > a::after { */
/*   background-image: none; */
/*   width: 0; */
/*   color: var(--color); */
/* } */
li[role="list"].no-arrow {
  margin-left: 8px;
  padding-right: 0;
}
li[role="list"] > a::after {
  -webkit-margin-start: 0.2rem;
  margin-inline-start: 0.2rem;
}

li[role="list"].no-arrow > a,
li[role="list"].no-arrow > a:link,
li[role="list"].no-arrow > a:visited {
  color: var(--secondary);
}

select.min-select {
  --form-element-spacing-horizontal: 0;
  margin-bottom: 4px;
  max-width: 128px;
  overflow: hidden;
  color: var(--primary);
  font-size: 13px;
  border: none;
  padding: 0;
  padding-right: 20px;
  padding-left: 8px;
  text-overflow: ellipsis;
  color: var(--color);

}
select.min-select-secondary {
  color: var(--color);
}
select.min-select:focus {
  outline: none;
  border: none;
  --box-shadow: none;
}
select.min-select-no-arrow {
  background-image: none;
  padding-right: 0;
}

select.min-select-left {
  padding-right: 0px;
  /* padding-left: 24px; */
  /* background-position: center left 0; */
  text-overflow: ellipsis;
  text-align: left;
}

.muted {
  color: var(--muted-color);
}

.select.button-select {
  --background-color: var(--secondary-hover);
  --border-color: var(--secondary-hover);
  --color: var(--secondary-inverse);
  cursor: pointer;
  --box-shadow: var(--button-box-shadow, 0 0 0 rgba(0, 0, 0, 0));
  padding: var(--form-element-spacing-vertical)
    var(--form-element-spacing-horizontal);
  border: var(--border-width) solid var(--border-color);
  border-radius: var(--border-radius);
  outline: none;
  background-color: var(--background-color);
  box-shadow: var(--box-shadow);
  color: var(--color);
  font-weight: var(--font-weight);
  font-size: 16px;
  line-height: var(--line-height);
  text-align: center;
  cursor: pointer;
  transition: background-color var(--transition), border-color var(--transition),
    color var(--transition), box-shadow var(--transition);
  -webkit-appearance: button;
  margin: 0;
  margin-bottom: 0px;
  overflow: visible;
  font-family: inherit;
  text-transform: none;
}

body {
  padding: 0;
  margin: 0 auto;
  min-width: 268px;
  border-radius: 10px;
}

.popup-container {
  font-size: 16px;
  --font-size: 16px;
  color: #666;
  background-color: var(--popup-footer-background-color);
  width: 316px;
  min-width: 316px;
}

.popup-content {
  background-color: var(--popup-content-background-color);
  border-radius: 0px 0px 12px 12px;
  padding: 16px 20px;
}

.immersive-translate-popup-overlay {
  position: fixed;
  top: 0;
  left: 0;
  height: 100%;
  width: 100%;
  touch-action: none;
}

.immersive-translate-popup-wrapper {
  background: var(--background-color);
  border-radius: 10px;
  border: 1px solid var(--muted-border-color);
}

#mount#mount {
  --font-family: system-ui, -apple-system, "Segoe UI", "Roboto", "Ubuntu",
    "Cantarell", "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji",
    "Segoe UI Symbol", "Noto Color Emoji";
  --line-height: 1.5;
  --font-weight: 400;
  --font-size: 16px;
  --border-radius: 4px;
  --border-width: 1px;
  --outline-width: 3px;
  --spacing: 16px;
  --typography-spacing-vertical: 24px;
  --block-spacing-vertical: calc(var(--spacing) * 2);
  --block-spacing-horizontal: var(--spacing);
  --grid-spacing-vertical: 0;
  --grid-spacing-horizontal: var(--spacing);
  --form-element-spacing-vertical: 12px;
  --form-element-spacing-horizontal: 16px;
  --nav-element-spacing-vertical: 16px;
  --nav-element-spacing-horizontal: 8px;
  --nav-link-spacing-vertical: 8px;
  --nav-link-spacing-horizontal: 8px;
  --form-label-font-weight: var(--font-weight);
  --transition: 0.2s ease-in-out;
  --modal-overlay-backdrop-filter: blur(4px);
}

[data-theme="light"],
#mount:not([data-theme="dark"]) {
  --popup-footer-background-color: #e8eaeb;
  --popup-content-background-color: #ffffff;
  --popup-item-background-color: #f3f5f6;
  --popup-item-hover-background-color: #eaeced;
  --popup-trial-pro-background-color: #f9fbfc;
  --text-black-2: #222222;
  --text-gray-2: #222222;
  --text-gray-6: #666666;
  --text-gray-9: #999999;
  --text-gray-c2: #c2c2c2;
  --service-select-content-shadow: 0px 2px 12px 0px rgba(75, 76, 77, 0.2);
  --service-select-border-color: #fafafa;
  --service-select-selected-background-color: #f3f5f6;
  --download-app-background: linear-gradient(83deg, #FACCDE -0.87%, #FCE7EF 43.13%, #FBD6E4 72.08%, #FFB3D1 96.34%);
}

@media only screen and (prefers-color-scheme: dark) {
  #mount:not([data-theme="light"]) {
    --popup-footer-background-color: #0d0d0d;
    --popup-content-background-color: #191919;
    --popup-item-background-color: #272727;
    --popup-item-hover-background-color: #333333;
    --popup-trial-pro-background-color: #222222;
    --text-black-2: #ffffff;
    --text-gray-2: #dbdbdb;
    --text-gray-6: #b3b3b3;
    --text-gray-9: #777777;
    --text-gray-c2: #5b5b5b;
    --service-select-content-shadow: 0px 2px 12px 0px rgba(0, 0, 0, 0.9);
    --service-select-border-color: #2c2c2c;
    --service-select-selected-background-color: #333333;
    --download-app-background: linear-gradient(83deg, rgba(250, 204, 222, 0.90) -0.87%, rgba(252, 231, 239, 0.90) 43.13%, rgba(251, 214, 228, 0.90) 72.08%, rgba(255, 179, 209, 0.90) 96.34%);
  }
}

[data-theme="dark"] {
  --popup-footer-background-color: #0d0d0d;
  --popup-content-background-color: #191919;
  --popup-item-background-color: #272727;
  --popup-item-hover-background-color: #333333;
  --popup-trial-pro-background-color: #222222;
  --text-black-2: #ffffff;
  --text-gray-2: #dbdbdb;
  --text-gray-6: #b3b3b3;
  --text-gray-9: #777777;
  --text-gray-c2: #5b5b5b;
  --service-select-content-shadow: 0px 2px 12px 0px rgba(0, 0, 0, 0.9);
  --service-select-border-color: #2c2c2c;
  --service-select-selected-background-color: #333333;
}

.text-balck {
  color: var(--text-black-2);
}

.text-gray-2 {
  color: var(--text-gray-2);
}

.text-gray-6 {
  color: var(--text-gray-6);
}

.text-gray-9 {
  color: var(--text-gray-9);
}

.text-gray-c2 {
  color: var(--text-gray-c2);
}

#mount {
  min-width: 268px;
}

.main-button {
  font-size: 15px;
  vertical-align: middle;
  border-radius: 12px;
  padding: unset;
  height: 44px;
  line-height: 44px;
}

.pt-4 {
  padding-top: 16px;
}

.p-2 {
  padding: 8px;
}

.pl-5 {
  padding-left: 48px;
}

.p-0 {
  padding: 0;
}

.pl-2 {
  padding-left: 8px;
}

.pl-4 {
  padding-left: 24px;
}

.pt-2 {
  padding-top: 8px;
}

.pb-2 {
  padding-bottom: 8px;
}

.pb-4 {
  padding-bottom: 16px;
}

.pb-5 {
  padding-bottom: 20px;
}

.pr-5 {
  padding-right: 48px;
}

.text-sm {
  font-size: 13px;
}

.text-base {
  font-size: 16px;
}

.w-full {
  width: 100%;
}

.flex {
  display: flex;
}

.flex-row {
  flex-direction: row;
}

.flex-wrap {
  flex-wrap: wrap;
}

.flex-end {
  justify-content: flex-end;
}

.flex-grow {
  flex-grow: 1;
}

.justify-between {
  justify-content: space-between;
}

.mb-0 {
  margin-bottom: 0px;
}

.mb-2 {
  margin-bottom: 8px;
}

.mb-4 {
  margin-bottom: 16px;
}

.mb-3 {
  margin-bottom: 12px;
}

.inline-block {
  display: inline-block;
}

.py-2 {
  padding-top: 8px;
  padding-bottom: 8px;
}

.py-2-5 {
  padding-top: 6px;
  padding-bottom: 6px;
}

.mt-0 {
  margin-top: 0;
}

.mt-2 {
  margin-top: 8px;
}

.mt-3 {
  margin-top: 12px;
}

.mt-4 {
  margin-top: 16px;
}

.mt-5 {
  margin-top: 20px;
}

.mt-6 {
  margin-top: 24px;
}

.mb-1 {
  margin-bottom: 4px;
}

.ml-4 {
  margin-left: 24px;
}

.ml-3 {
  margin-left: 16px;
}

.ml-2 {
  margin-left: 8px;
}

.ml-1 {
  margin-left: 4px;
}

.mr-1 {
  margin-right: 4px;
}

.mr-2 {
  margin-right: 8px;
}

.mr-3 {
  margin-right: 16px;
}

.mx-2 {
  margin-left: 8px;
  margin-right: 8px;
}

.pl-3 {
  padding-left: 12px;
}

.pr-3 {
  padding-right: 12px;
}

.p-3 {
  padding: 12px;
}

.px-1 {
  padding-left: 4px;
  padding-right: 4px;
}

.px-3 {
  padding-left: 12px;
  padding-right: 12px;
}

.pt-3 {
  padding-top: 12px;
}

.px-6 {
  padding-left: 18px;
  padding-right: 18px;
}

.px-4 {
  padding-left: 16px;
  padding-right: 16px;
}

.pt-6 {
  padding-top: 20px;
}

.py-3 {
  padding-top: 12px;
  padding-bottom: 12px;
}

.py-0 {
  padding-top: 0;
  padding-bottom: 0;
}

.left-auto {
  left: auto !important;
}

.max-h-28 {
  max-height: 112px;
}

.max-h-30 {
  max-height: 120px;
}

.overflow-y-scroll {
  overflow-y: scroll;
}

.text-xs {
  font-size: 12px;
}

.flex-1 {
  flex: 1;
}

.flex-3 {
  flex: 3;
}

.flex-4 {
  flex: 4;
}

.flex-2 {
  flex: 2;
}

.items-center {
  align-items: center;
}

.max-content {
  width: max-content;
}

.justify-center {
  justify-content: center;
}

.items-end {
  align-items: flex-end;
}

.items-baseline {
  align-items: baseline;
}

.my-5 {
  margin-top: 48px;
  margin-bottom: 48px;
}

.my-4 {
  margin-top: 24px;
  margin-bottom: 24px;
}

.my-3 {
  margin-top: 16px;
  margin-bottom: 16px;
}

.pt-3 {
  padding-top: 12px;
}

.px-3 {
  padding-left: 12px;
  padding-right: 12px;
}

.pt-2 {
  padding-top: 8px;
}

.px-2 {
  padding-left: 8px;
  padding-right: 8px;
}

.pt-1 {
  padding-top: 4px;
}

.px-1 {
  padding-left: 4px;
  padding-right: 4px;
}

.pb-2 {
  padding-bottom: 8px;
}

.justify-end {
  justify-content: flex-end;
}

.w-auto {
  width: auto;
}

.shrink-0 {
  flex-shrink: 0;
}

select.language-select,
select.translate-service,
select.min-select {
  --form-element-spacing-horizontal: 0;
  margin-bottom: 0px;
  max-width: unset;
  flex: 1;
  overflow: hidden;
  font-size: 13px;
  border: none;
  border-radius: 8px;
  padding-right: 30px;
  padding-left: 0px;
  background-position: center right 12px;
  background-size: 16px auto;
  background-image: var(--icon-xia);
  text-overflow: ellipsis;
  color: var(--text-gray-2);
  background-color: transparent;
  box-shadow: unset !important;
  cursor: pointer;
}

select.more {
  background-position: center right;
  padding-right: 20px;
}

select.transform-padding-left {
  padding-left: 12px;
  transform: translateX(-12px);
  background-position: center right 0px;
}

select.translate-service {
  color: var(--text-black-2);
}

/* dark use black, for windows */
@media (prefers-color-scheme: dark) {
  select.language-select option,
  select.translate-service option,
  select.min-select option {
    background-color: #666666;
  }
}

.text-overflow-ellipsis {
  text-overflow: ellipsis;
  overflow: hidden;
  white-space: nowrap;
}

.max-w-20 {
  max-width: 180px;
  white-space: nowrap;
}

select.min-select-secondary {
  color: var(--color);
}

select.min-select:focus {
  outline: none;
  border: none;
  --box-shadow: none;
}

select.min-select-no-arrow {
  background-image: none;
  padding-right: 0;
}

select.min-select-left {
  padding-right: 0px;
  /* padding-left: 24px; */
  /* background-position: center left 0; */
  text-overflow: ellipsis;
  text-align: left;
}

.popup-footer {
  background-color: var(--popup-footer-background-color);
  height: 40px;
}

.text-right {
  text-align: right;
}

.clickable {
  cursor: pointer;
}

.close {
  cursor: pointer;
  width: 16px;
  height: 16px;
  background-image: var(--icon-close);
  background-position: center;
  background-size: auto 1rem;
  background-repeat: no-repeat;
  opacity: 0.5;
  transition: opacity var(--transition);
}

.padding-two-column {
  padding-left: 40px;
  padding-right: 40px;
}

.muted {
  color: #999;
}

.text-label {
  color: #666;
}

.display-none {
  display: none;
}

/* dark use #18232c */
@media (prefers-color-scheme: dark) {
  .text-label {
    color: #9ca3af;
  }
}

.text-decoration-none {
  text-decoration: none;
}

.text-decoration-none:is([aria-current], :hover, :active, :focus),
[role="link"]:is([aria-current], :hover, :active, :focus) {
  --text-decoration: none !important;
  background-color: transparent !important;
}

.language-select-container {
  position: relative;
  width: 100%;
  background-color: var(--popup-item-background-color);
  height: 55px;
  border-radius: 12px;
}

select.language-select {
  color: var(--text-black-2);
  font-size: 14px;
  padding: 8px 24px 24px 16px;
  position: absolute;
  border-radius: 12px;
  position: absolute;
  left: 0;
  right: 0;
  top: 0;
  bottom: 0;
}

select.text-gray-6 {
  color: var(--text-gray-6);
}

.language-select-container label {
  position: absolute;
  bottom: 10px;
  left: 16px;
  font-size: 12px;
  color: var(--text-gray-9);
  line-height: 12px;
  margin: 0;
}

.translation-service-container {
  background-color: var(--popup-item-background-color);
  border-radius: 12px;
}

.min-select-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 44px;
  background-color: var(--popup-item-background-color);
  padding-left: 16px;
}

.min-select-container:first-child {
  border-top-left-radius: 10px;
  border-top-right-radius: 10px;
}

.min-select-container:last-child {
  border-bottom-left-radius: 10px;
  border-bottom-right-radius: 10px;
}

.min-select-container:only-child {
  border-radius: 10px;
}

.translate-mode {
  width: 44px;
  height: 44px;
  border-radius: 22px;
  background-color: var(--popup-item-background-color);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  cursor: pointer;
}

.translate-mode svg {
  fill: var(--text-gray-2);
}

.widgets-container {
  display: flex;
  align-items: stretch;
  justify-content: space-between;
  width: 100%;
  gap: 9px;
}

/* 当只有两个小组件时的样式优化 */
.widgets-container.widgets-two-items {
  gap: 16px;
}

.widgets-container.widgets-two-items .widget-item {
  flex: 0 1 auto;
  min-width: 93px;
  max-width: 120px;
}

.widget-item {
  display: flex;
  max-width: 93px;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  background-color: var(--popup-item-background-color);
  font-size: 12px;
  min-height: 44px;
  height: 100%;
  border-radius: 8px;
  cursor: pointer;
  flex: 1;
  padding: 8px 4px;
  text-align: center;
}

.widget-icon-text {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  color: var(--text-gray-2);
}

.share-button-container {
  display: flex;
  align-items: center;
  cursor: pointer;
  padding: 2px 3px 0 8px;
}

.share-button-container svg {
  fill: var(--text-gray-9);
}

.min-select-container:hover,
.language-select-container:hover,
.widget-item:hover,
.translate-mode:hover {
  background-color: var(--popup-item-hover-background-color);
}

.main-button:hover {
  background-color: #f5508f;
}

.share-button-container:hover {
  background-color: var(--popup-item-background-color);
  border-radius: 6px;
}

.error-boundary {
  background: #fff2f0;
  border: 1px solid #ffccc7;
  display: flex;
  padding: 12px;
  font-size: 14px;
  color: rgba(0, 0, 0, 0.88);
  word-break: break-all;
  margin: 12px;
  border-radius: 12px;
  flex-direction: column;
}

.upgrade-pro {
  border-radius: 11px;
  background: linear-gradient(57deg, #272727 19.8%, #696969 82.2%);
  padding: 2px 8px;
  transform: scale(0.85);
}

.upgrade-pro span {
  background: linear-gradient(180deg, #ffeab4 17.65%, #f8c235 85.29%);
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  font-size: 12px;
  margin-left: 4px;
}

.upgrade-pro svg {
  margin-top: -2px;
}

.upgrade-pro:hover {
  background: linear-gradient(57deg, #3d3d3d 19.8%, #949494 82.2%);
}

.border-bottom-radius-0 {
  border-bottom-left-radius: 0 !important;
  border-bottom-right-radius: 0 !important;
}

.trial-pro-container {
  border-radius: 0px 0px 12px 12px;
  background: var(--popup-trial-pro-background-color);
  display: flex;
  align-items: center;
  height: 44px;
  padding-left: 16px;
  padding-right: 12px;
  font-size: 12px;
}

.trial-pro-container label {
  line-height: 13px;
  color: var(--text-black-2);
}

.trial-pro-container img {
  margin-left: 5px;
}

.cursor-pointer {
  cursor: pointer;
}

.upgrade-pro-discount-act {
  height: 25px;
  display: flex;
  padding: 0 4px;
  align-items: center;
  border-radius: 15px;
  background: linear-gradient(
    90deg,
    #cefbfa 11.33%,
    #d7f56f 63.75%,
    #fccd5e 100%
  );
  transform: scale(0.9);
  box-shadow: 0px 1.8px 3.6px 0px rgba(0, 0, 0, 0.1);
  cursor: pointer;
}

.upgrade-pro-discount-act span {
  font-size: 12px;
  font-weight: 700;
  margin-left: 4px;
  color: #222222;
}

.upgrade-pro-discount-act:hover {
  text-decoration: unset;
  background: linear-gradient(
    90deg,
    #e2fffe 11.33%,
    #e6ff91 63.75%,
    #ffdf93 100%
  );
}

.custom-select-container {
  width: 200px;
  position: relative;
  flex: 1;
}

#translation-service-select {
  padding-right: 12px;
  padding-left: 6px;
}

.custom-select-content {
  border-radius: 12px;
  background: var(--popup-content-background-color);
  box-shadow: var(--service-select-content-shadow);
  border: 1px solid var(--service-select-border-color);
  padding: 4px 5px;
  position: absolute;
  left: 0;
  right: 0;
  z-index: 100;
  overflow-y: auto;
}

.custom-select-item.default {
  width: 100%;
  padding: 0;
}

.custom-select-item {
  font-size: 13px;
  padding: 5px 6px;
  border-radius: 8px;
  display: flex;
  align-items: center;
  cursor: pointer;
  color: var(--text-black-2);
  width: auto;
  overflow: hidden;
  height: 30px;
  line-height: 30px;
}

.custom-select-item-img {
  width: 20px;
  height: 20px;
  margin-right: 4px;
}

@media (prefers-color-scheme: dark) {
  .custom-select-item-img {
    margin-right: 6px;
  }
}

.custom-select-content .custom-select-item.selected,
.custom-select-content .custom-select-item:hover {
  background: var(--service-select-selected-background-color);
}

.custom-select-item > span {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.custom-select-item-pro {
  font-size: 12px;
  margin-left: 6px;
}

.custom-select-item-pro img {
  margin: 0 3px;
  width: 20px;
}

.custom-select-group-header {
  font-size: 12px;
  font-weight: 500;
  color: var(--text-gray-9);
  padding: 6px 8px 4px;
  margin-top: 2px;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.more-container {
  position: relative;
}

.new-menu-indicator {
  position: absolute;
  width: 8px;
  height: 8px;
  background-color: #ef3434;
  border-radius: 50%;
  right: 18px;
  top: 4px;
}

.download-app {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  border-radius: 8px;
  background: var(--download-app-background);
  padding: 4px 8px;
  color: #ea4c89;
  font-size: 12px;
  cursor: pointer;
  transition: all 0.2s ease-in-out;
}

/* Popup 动画效果 */
@keyframes popup-fade-in {
  from {
    opacity: 0;
    transform: translateY(10px) scale(0.95);
  }
  to {
    opacity: 1;
    transform: translateY(0) scale(1);
  }
}

@keyframes popup-fade-out {
  from {
    opacity: 1;
    transform: translateY(0) scale(1);
  }
  to {
    opacity: 0;
    transform: translateY(10px) scale(0.95);
  }
}

.popup-generic-content {
  animation: popup-fade-in 0.2s ease-out;
}

.popup-generic-content.hiding {
  animation: popup-fade-out 0.15s ease-in;
}

html {
  font-size: 17px;
}

@media print {
  .imt-fb-container {
    display: none !important;
  }
}

#mount#mount {
  position: absolute;
  display: none;
  min-width: 250px;
  height: auto;
  --font-size: 17px;
  font-size: 17px;
}

/* float-ball */
.imt-fb-container {
  position: fixed;
  padding: 0;
  top: 335px;
  width: fit-content;
  display: flex;
  flex-direction: column;
  display: none;
  direction: ltr;
}

.imt-fb-container.left {
  align-items: flex-start;
  left: 0;
}

.imt-fb-container.right {
  align-items: flex-end;
  right: 0;
}

.imt-fb-btn {
  cursor: pointer;
  background: var(--float-ball-more-button-background-color);
  height: 36px;
  width: 56px;
  box-shadow: 2px 6px 10px 0px #0e121629;
}

.imt-fb-btn.left {
  border-top-right-radius: 36px;
  border-bottom-right-radius: 36px;
}

.imt-fb-btn.right {
  border-top-left-radius: 36px;
  border-bottom-left-radius: 36px;
}

.imt-fb-btn div {
  background: var(--float-ball-more-button-background-color);
  height: 36px;
  width: 54px;
  display: flex;
  align-items: center;
}

.imt-fb-btn.left div {
  border-top-right-radius: 34px;
  border-bottom-right-radius: 34px;
  justify-content: flex-end;
}

.imt-fb-btn.right div {
  border-top-left-radius: 34px;
  border-bottom-left-radius: 34px;
}

.imt-fb-logo-img {
  width: 20px;
  height: 20px;
  margin: 0 10px;
}

.imt-fb-logo-img-big-bg {
  width: 28px;
  height: 28px;
  margin: 0;
  padding: 4px;
  background-color: #ed6d8f;
  border-radius: 50%;
  margin: 0 5px;
}

.imt-float-ball-translated {
  position: absolute;
  width: 11px;
  height: 11px;
  bottom: 4px;
  right: 20px;
}

.btn-animate {
  -webkit-transform: translate3d(0, 0, 0);
  transform: translate3d(0, 0, 0);
  -webkit-transition: -webkit-transform ease-out 250ms;
  transition: -webkit-transform ease-out 250ms;
  transition: transform ease-out 250ms;
  transition: transform ease-out 250ms, -webkit-transform ease-out 250ms;
}

.imt-fb-setting-btn {
  margin-right: 18px;
  width: 28px;
  height: 28px;
}

.immersive-translate-popup-wrapper {
  background: var(--background-color);
  border-radius: 20px;
  box-shadow: 2px 10px 24px 0px #0e121614;
  border: none;
}

.popup-container {
  border-radius: 20px;
}

.popup-content {
  border-radius: 20px 20px 12px 12px;
}
.popup-footer {
  border-radius: 20px;
}

.imt-fb-close-button {
  pointer-events: all;
  cursor: pointer;
  position: absolute;
  margin-top: -10px;
}

.imt-fb-close-content {
  padding: 22px;
  width: 320px;
  pointer-events: all;
}

.imt-fb-close-title {
  font-weight: 500;
  color: var(--h2-color);
}

.imt-fb-close-radio-content {
  background-color: var(--background-light-green);
  padding: 8px 20px;
}

.imt-fb-radio-sel,
.imt-fb-radio-nor {
  width: 16px;
  height: 16px;
  border-radius: 8px;
  flex-shrink: 0;
}

.imt-fb-radio-sel {
  border: 2px solid var(--primary);
  display: flex;
  align-items: center;
  justify-content: center;
}

.imt-fb-radio-sel div {
  width: 8px;
  height: 8px;
  border-radius: 4px;
  background-color: var(--primary);
}

.imt-fb-radio-nor {
  border: 2px solid #d3d4d6;
}

.imt-fb-primary-btn {
  background-color: var(--primary);
  width: 72px;
  height: 32px;
  color: white;
  border-radius: 8px;
  text-align: center;
  line-height: 32px;
  font-size: 16px;
  cursor: pointer;
}

.imt-fb-default-btn {
  border: 1px solid var(--primary);
  width: 72px;
  height: 32px;
  border-radius: 8px;
  color: var(--primary);
  line-height: 32px;
  text-align: center;
  font-size: 16px;
  cursor: pointer;
}

.imt-fb-guide-container {
  width: 312px;
  transform: translateY(-45%);
}

.imt-fb-guide-bg {
  position: absolute;
  left: 30px;
  right: 0;
  top: 0;
  bottom: 0;
  z-index: -1;
  height: 100%;
  width: 90%;
}

.imt-fb-guide-bg.left {
  transform: scaleX(-1);
}

.imt-fb-guide-content {
  margin: 16px -30px 80px 0px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.imt-fb-guide-content.left {
  margin: 16px 21px 60px 32px;
}

.imt-fb-guide-img {
  width: 220px;
  height: 112px;
}

.imt-fb-guide-message {
  font-size: 14px;
  line-height: 28px;
  color: #333333;
  white-space: pre-wrap;
  text-align: center;
  font-weight: 700;
  margin-bottom: 20px;
}

.imt-manga-guide-message {
  font-size: 16px;
  line-height: 24px;
  color: #333333;
  text-align: center;
  font-weight: 500;
  margin-bottom: 12px;
}

.imt-fb-guide-button {
  margin-top: 16px;
  line-height: 40px;
  height: 40px;
  padding: 0 20px;
  width: unset;
}

.imt-fb-more-buttons {
  box-shadow: 0px 2px 10px 0px #00000014;
  border: none;
  background: var(--float-ball-more-button-background-color);
  width: 36px;
  display: flex;
  flex-direction: column;
  border-radius: 18px;
  margin-top: 0px;
  padding: 7px 0 7px 0;
}

.imt-fb-more-buttons > div {
  margin: auto;
}

.imt-fb-side,
.imt-fb-reward {
  border-radius: 50%;
  cursor: pointer;
  pointer-events: all;
  position: relative;
}

.imt-fb-side {
  margin: 10px 0;
}

.imt-fb-new-badge {
  width: 26px;
  height: 14px;
  padding: 3px;
  background-color: #f53f3f;
  border-radius: 4px;
  position: absolute;
  top: -5px;
  right: 15px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.imt-fb-side *,
.imt-fb-reward * {
  pointer-events: all;
}

.imt-fb-more-button {
  width: 36px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
}
/* Sheet.css */
.immersive-translate-sheet {
  position: fixed;
  transform: translateY(100%);
  /* Start off screen */
  left: 0;
  right: 0;
  background-color: white;
  transition: transform 0.3s ease-out;
  /* Smooth slide transition */
  box-shadow: 0px -2px 10px rgba(0, 0, 0, 0.1);
  /* Ensure it's above other content */
  bottom: 0;
  border-top-left-radius: 16px;
  border-top-right-radius: 16px;
  overflow: hidden;
}

.immersive-translate-sheet.visible {
  transform: translateY(0);
}

.immersive-translate-sheet-backdrop {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.5);
  opacity: 0;
  transition: opacity 0.3s ease-out;
}

.immersive-translate-sheet-backdrop.visible {
  opacity: 1;
}

.popup-container-sheet {
  max-width: 100vw;
  width: 100vw;
}

.imt-no-events svg * {
  pointer-events: none !important;
}

.imt-manga-button {
  width: 36px;
  display: flex;
  flex-direction: column;
  position: relative;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  pointer-events: all;
  margin: 0 0 10px 0;
  background-color: var(--float-ball-more-button-background-color);
  border-radius: 18px;
  filter: drop-shadow(0px 2px 10px rgba(0, 0, 0, 0.08));
  opacity: 0.5;
  right: 8px;
  padding: 10px 0 4px 0;
}

.imt-manga-feedback {
  cursor: pointer;
  margin-bottom: 10px;
}

.imt-fb-feedback {
  cursor: pointer;
  margin-top: 10px;
}

.imt-fb-upgrade-button {
  cursor: pointer;
  margin-top: 10px;
}

.imt-manga-button:hover {
  opacity: 1;
}

.imt-manga-translated {
  position: absolute;
  left: 24px;
  top: 20px;
}

.imt-float-ball-loading {
  animation: imt-loading-animation 0.6s infinite linear !important;
}

.imt-manga-guide-bg {
  position: absolute;
  left: 0;
  right: 0;
  top: 0;
  bottom: 0;
  z-index: -1;
  width: 372px;
  transform: translateY(-50%);
}
.imt-manga-guide-content {
  position: absolute;
  top: 15px;
  left: 0;
  right: 0;
  margin: 0 40px 0;
}

.img-manga-guide-button {
  width: fit-content;
  margin: 0 auto;
}

.img-manga-close {
  position: absolute;
  bottom: -200px;
  width: 32px;
  height: 32px;
  left: 0;
  right: 0;
  margin: auto;
  cursor: pointer;
}

.imt-fb-container.dragging .imt-fb-more-buttons,
.imt-fb-container.dragging .imt-manga-button,
.imt-fb-container.dragging .btn-animate:not(.imt-fb-btn) {
  display: none !important;
}

.imt-fb-container.dragging .imt-fb-btn {
  border-radius: 50% !important;
  width: 36px !important;
  height: 36px !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  cursor: move !important;
}

.imt-fb-container.dragging .imt-fb-btn div {
  border-radius: 50% !important;
  width: 36px !important;
  height: 36px !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  margin: 0 !important;
}

.imt-fb-container.dragging .imt-fb-btn.left,
.imt-fb-container.dragging .imt-fb-btn.right {
  border-radius: 50% !important;
}

.imt-fb-container.dragging .imt-fb-btn.left div,
.imt-fb-container.dragging .imt-fb-btn.right div {
  border-radius: 50% !important;
}

.imt-fb-container.dragging .imt-fb-logo-img {
  margin: 0 !important;
  padding: 4px !important;
}

.imt-fb-container.dragging .imt-float-ball-translated {
  right: 2px !important;
  bottom: 2px !important;
}

@-webkit-keyframes imt-loading-animation {
  from {
    -webkit-transform: rotate(0deg);
  }

  to {
    -webkit-transform: rotate(359deg);
  }
}

@keyframes imt-loading-animation {
  from {
    transform: rotate(0deg);
  }

  to {
    transform: rotate(359deg);
  }
}
</style><div id="mount" style="display: block;"><div class="imt-fb-container right notranslate " style="z-index: 2147483637; pointer-events: none; right: 0px; top: 327px; display: flex;"><div class="btn-animate" style="transform: translateX(-4px); opacity: 0.7; padding-left: 10px;"><div class=" btn-animate" style="position: relative; pointer-events: all; display: inline-block; opacity: 1;"><div><div class="imt-fb-btn imt-fb-more-button imt-fb-side"><svg width="22" height="22" viewBox="0 0 22 22" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M8.60547 12.9228C8.84029 12.9228 9.03755 13.0022 9.19629 13.161C9.3551 13.3198 9.43457 13.5171 9.43457 13.7519V18.5107C9.43457 18.7453 9.35513 18.9426 9.19629 19.1015C9.03755 19.2602 8.84029 19.3398 8.60547 19.3398H3.8457C3.61127 19.3397 3.41464 19.26 3.25586 19.1015C3.09712 18.9426 3.01758 18.7453 3.01758 18.5107V13.7519C3.01758 13.517 3.09712 13.3198 3.25586 13.161C3.41465 13.0023 3.61125 12.9229 3.8457 12.9228H8.60547ZM17.208 12.9228C17.4427 12.9228 17.6399 13.0022 17.7988 13.161C17.9575 13.3198 18.0371 13.5171 18.0371 13.7519V18.5107C18.0371 18.7453 17.9576 18.9426 17.7988 19.1015C17.6399 19.2602 17.4427 19.3398 17.208 19.3398H12.4492C12.2144 19.3398 12.0171 19.2602 11.8584 19.1015C11.6995 18.9426 11.6201 18.7453 11.6201 18.5107V13.7519C11.6201 13.517 11.6995 13.3198 11.8584 13.161C12.0171 13.0022 12.2144 12.9228 12.4492 12.9228H17.208ZM4.39258 17.9648H8.05957V14.2978H4.39258V17.9648ZM12.9951 17.9648H16.6621V14.2978H12.9951V17.9648ZM14.7598 2.92179C14.8641 2.57295 15.3576 2.57295 15.4619 2.92179L15.9561 4.57511C16.1376 5.18219 16.5965 5.66815 17.1924 5.8837L18.7412 6.44327C19.0635 6.56002 19.0633 7.01583 18.7412 7.13273L17.1924 7.69327C16.5966 7.90881 16.1376 8.39389 15.9561 9.00089L15.4619 10.6552C15.3575 11.0038 14.8642 11.0037 14.7598 10.6552L14.2646 9.00089C14.0831 8.39401 13.625 7.90881 13.0293 7.69327L11.4805 7.13273C11.158 7.01598 11.1579 6.55996 11.4805 6.44327L13.0293 5.8837C13.6251 5.66814 14.0831 5.18219 14.2646 4.57511L14.7598 2.92179ZM8.60547 4.32023C8.84029 4.32023 9.03755 4.39977 9.19629 4.55851C9.35496 4.71727 9.43448 4.91396 9.43457 5.14835V9.90812C9.43457 10.1429 9.35518 10.3402 9.19629 10.4989C9.03755 10.6578 8.84029 10.7372 8.60547 10.7372H3.8457C3.61131 10.7371 3.41463 10.6576 3.25586 10.4989C3.09712 10.3402 3.01758 10.1429 3.01758 9.90812V5.14835C3.01767 4.91386 3.09721 4.71731 3.25586 4.55851C3.41466 4.39986 3.61121 4.32032 3.8457 4.32023H8.60547ZM4.39258 9.36222H8.05957V5.69523H4.39258V9.36222Z" fill="#666666"></path></svg><svg width="14" height="14" viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg" style="position: absolute; right: 0px; top: 0px; display: none; transform: translate(30%, -30%);"><g clip-path="url(#clip0_34242_2353)"><path d="M7 14C5.14348 14 3.36301 13.2625 2.05025 11.9497C0.737498 10.637 0 8.85652 0 7C0 5.14348 0.737498 3.36301 2.05025 2.05025C3.36301 0.737498 5.14348 0 7 0C8.85652 0 10.637 0.737498 11.9497 2.05025C13.2625 3.36301 14 5.14348 14 7C14 8.85652 13.2625 10.637 11.9497 11.9497C10.637 13.2625 8.85652 14 7 14Z" fill="#B1B1B1" fill-opacity="0.32"></path><mask id="mask0_34242_2353" maskUnits="userSpaceOnUse" x="1" y="1" width="12" height="12" style="mask-type: alpha;"><rect x="1" y="1" width="12" height="12" fill="#D9D9D9"></rect></mask><g mask="url(#mask0_34242_2353)"><path d="M7.86447 3.67324H6.13622V4.72999L4.80409 3.39199C4.75018 3.33699 4.70972 3.27808 4.68272 3.21524C4.65572 3.15241 4.64222 3.09533 4.64222 3.04399C4.64222 2.93141 4.68193 2.8352 4.76134 2.75537C4.84076 2.67562 4.94514 2.63574 5.07447 2.63574H8.98322C9.12864 2.63574 9.25147 2.68883 9.35172 2.79499C9.45189 2.90124 9.50197 3.04578 9.50197 3.22862C9.50197 3.35203 9.46122 3.46245 9.37972 3.55987C9.29822 3.65737 9.18897 3.69516 9.05197 3.67324H8.90197V6.36774C8.90197 6.51316 8.85214 6.63599 8.75247 6.73624C8.65272 6.83641 8.53051 6.88649 8.38585 6.88649C8.24118 6.88649 8.11809 6.83641 8.01659 6.73624C7.91518 6.63599 7.86447 6.51316 7.86447 6.36774V3.67324ZM6.4816 11.974V9.13599H4.57509C4.36193 9.13599 4.19043 9.06703 4.06059 8.92912C3.93076 8.79112 3.86584 8.62983 3.86584 8.44524C3.86584 8.35591 3.88509 8.26499 3.92359 8.17249C3.96209 8.08008 4.01984 7.99437 4.09684 7.91537L5.09872 6.89549V6.36149L2.32422 3.58412C2.22664 3.48645 2.1788 3.37678 2.18072 3.25512C2.18272 3.13345 2.23155 3.02483 2.32722 2.92924C2.42489 2.83158 2.53614 2.78274 2.66097 2.78274C2.7858 2.78274 2.89701 2.83158 2.99459 2.92924L10.9898 10.9245C11.0863 11.0209 11.1351 11.13 11.1361 11.2516C11.1371 11.3733 11.0898 11.4839 10.9941 11.5835C10.8984 11.6772 10.7867 11.7235 10.6588 11.7225C10.5311 11.7215 10.4194 11.6732 10.3237 11.5776L7.87909 9.13599L7.51909 9.14199V11.974C7.51909 12.1195 7.46926 12.2423 7.3696 12.3425C7.26985 12.4427 7.14764 12.4927 7.00297 12.4927C6.8583 12.4927 6.73522 12.4427 6.63372 12.3425C6.5323 12.2423 6.4816 12.1195 6.4816 11.974ZM5.35909 8.09849H6.83872L6.08834 7.35124L6.09434 7.35724L5.35909 8.09849Z" fill="white"></path></g></g><defs><clipPath id="clip0_34242_2353"><rect width="14" height="14" fill="white"></rect></clipPath></defs></svg></div></div></div></div><div hidden="" class="imt-no-events btn-animate " id="manga-button" style="position: relative;"><div class="imt-manga-button" style="transform: translateX(2px);"><div class=" " style="position: relative; pointer-events: all; display: inline-block; opacity: 1;"><div><svg class="imt-manga-feedback" width="22" height="22" viewBox="0 0 22 22" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M11.0003 14.2749C11.213 14.2749 11.3895 14.2047 11.5299 14.0643C11.6705 13.9239 11.7408 13.7473 11.7408 13.5345C11.7408 13.3218 11.6705 13.1453 11.5299 13.0049C11.3895 12.8645 11.213 12.7943 11.0003 12.7943C10.7877 12.7943 10.6111 12.8645 10.4707 13.0049C10.3302 13.1453 10.2599 13.3218 10.2599 13.5345C10.2599 13.7473 10.3302 13.9239 10.4707 14.0643C10.6111 14.2047 10.7877 14.2749 11.0003 14.2749ZM11.0003 11.0842C11.1954 11.0842 11.3587 11.0185 11.4903 10.8869C11.622 10.7552 11.6878 10.5918 11.6878 10.3967V6.23645C11.6878 6.04135 11.622 5.87803 11.4903 5.74649C11.3587 5.6148 11.1954 5.54895 11.0003 5.54895C10.8052 5.54895 10.6419 5.6148 10.5104 5.74649C10.3787 5.87803 10.3128 6.04135 10.3128 6.23645V10.3967C10.3128 10.5918 10.3787 10.7552 10.5104 10.8869C10.6419 11.0185 10.8052 11.0842 11.0003 11.0842ZM5.53562 16.8311L3.70045 18.666C3.43966 18.9269 3.13968 18.9861 2.80051 18.8434C2.4615 18.7005 2.29199 18.4434 2.29199 18.072V4.73816C2.29199 4.27509 2.45241 3.88314 2.77324 3.5623C3.09408 3.24147 3.48603 3.08105 3.9491 3.08105H18.0516C18.5146 3.08105 18.9066 3.24147 19.2274 3.5623C19.5482 3.88314 19.7087 4.27509 19.7087 4.73816V15.174C19.7087 15.637 19.5482 16.029 19.2274 16.3498C18.9066 16.6706 18.5146 16.8311 18.0516 16.8311H5.53562ZM4.95033 15.4561H18.0516C18.1221 15.4561 18.1868 15.4266 18.2454 15.3678C18.3042 15.3092 18.3337 15.2445 18.3337 15.174V4.73816C18.3337 4.66758 18.3042 4.60295 18.2454 4.54428C18.1868 4.48546 18.1221 4.45605 18.0516 4.45605H3.9491C3.87851 4.45605 3.81389 4.48546 3.75522 4.54428C3.6964 4.60295 3.66699 4.66758 3.66699 4.73816V16.7254L4.95033 15.4561Z" fill="#666666"></path></svg></div></div><div style="position: relative;"><svg width="32" height="32" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg"><g id="manhua"><path id="Vector" d="M14.8853 4.92364C14.8853 4.92364 16.3905 10.4362 22.6668 4C22.6668 4 20.3381 10.8907 25.3364 10.0843C25.3364 10.0843 22.0563 15.6994 29 18.0599C29 18.0599 22.9934 19.306 21.1617 28C21.1617 28 17.7679 24.54 14.8853 27.3549C14.8853 27.3549 13.3233 23.5724 7.33097 26.27C7.33097 26.27 10.1141 20.6549 4.83179 21.0507C4.83179 21.0507 7.16057 18.8955 3 15.9047C3 15.9047 7.50137 16.1833 6.33697 11.7117C6.33697 11.7117 10.0005 12.3421 8.66576 6.82957C8.65156 6.81491 12.4855 9.80574 14.8853 4.92364Z" fill="#ED6D8F"></path><path id="Vector_2" d="M20.8599 13.7022C20.885 13.1361 20.9543 12.5713 20.9959 12.0052C21.0337 11.568 20.8107 11.2794 20.3876 11.18C20.0759 11.1013 19.7508 11.0867 19.433 11.137C19.1951 11.1945 18.9542 11.2396 18.7113 11.2721C18.2403 11.3028 17.9973 11.5275 17.9796 11.988C17.977 12.0833 17.9596 12.1777 17.928 12.268C17.3034 13.9102 16.6774 15.5499 16.0503 17.1873C16.0301 17.2401 16.0062 17.2904 15.9671 17.3776C15.7291 16.8975 15.4281 16.4898 15.2745 15.9986C14.8073 14.5152 14.3186 13.033 13.8312 11.5594C13.6826 11.1112 13.3489 10.9344 12.8754 11.0216C12.7889 11.0365 12.7008 11.0398 12.6134 11.0314C12.2241 10.9938 11.8311 11.0404 11.4623 11.1677C11.0946 11.2991 10.9498 11.557 11.0152 11.9254C11.0428 12.0371 11.0643 12.1503 11.0795 12.2643C11.1223 13.1902 11.1777 14.1087 11.2054 15.0321C11.257 16.7992 11.2117 18.5651 11.0858 20.3284C11.0644 20.6354 11.0304 20.9424 11.0228 21.2494C11.0115 21.6092 11.1613 21.7811 11.5266 21.8143C11.9976 21.8573 12.4711 21.8708 12.9421 21.9088C13.0309 21.9201 13.121 21.9003 13.1962 21.8528C13.2714 21.8053 13.3268 21.7334 13.3527 21.6497C13.3996 21.5394 13.4252 21.4216 13.4282 21.3022C13.4295 20.8258 13.4207 20.3493 13.4081 19.8741C13.393 19.3264 13.3917 18.7763 13.3438 18.231C13.2857 17.5839 13.266 16.934 13.2847 16.2847C13.2847 16.2466 13.291 16.2073 13.2985 16.1312C13.3338 16.2024 13.3514 16.2356 13.3665 16.2712C13.9017 17.5228 14.3617 18.8037 14.7443 20.1074C14.7928 20.2421 14.7928 20.3889 14.7443 20.5237C14.6322 20.8196 14.7141 21.037 14.9659 21.1377C15.4445 21.3268 15.9331 21.4926 16.4155 21.6731C16.4865 21.7033 16.566 21.7091 16.6408 21.6895C16.7157 21.6698 16.7815 21.6259 16.8273 21.565C16.9085 21.4643 16.9743 21.3526 17.0225 21.2335C17.0537 21.1374 17.0798 21.0399 17.1006 20.9412C17.3185 20.2425 17.5653 19.5499 17.7517 18.8438C17.9785 17.9723 18.2624 17.1158 18.6018 16.2798C18.6201 16.2439 18.6411 16.2094 18.6647 16.1766C18.6761 16.2319 18.6761 16.254 18.6761 16.2761C18.6345 17.59 18.5955 18.8978 18.5501 20.2056C18.5363 20.5949 18.491 20.9829 18.4809 21.3722C18.4721 21.705 18.6207 21.8708 18.9557 21.9002C19.4355 21.9432 19.9191 21.9592 20.4002 21.9973C20.4888 22.0079 20.5784 21.9875 20.653 21.9399C20.7277 21.8922 20.7827 21.8203 20.8082 21.7369C20.8531 21.6305 20.8766 21.5167 20.8775 21.4017C20.88 20.7668 20.8674 20.132 20.8674 19.4971C20.8662 19.2846 20.8687 19.0722 20.8523 18.8622C20.8158 18.3968 20.7264 17.9314 20.7339 17.4685C20.7515 16.2122 20.8044 14.9572 20.8599 13.7022Z" fill="white"></path></g></svg><svg hidden="true" class="imt-manga-translated" width="11" height="11" viewBox="0 0 11 11" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="5.5" cy="5.5" r="5.5" fill="#68CD52"></circle><path d="M1.40857 5.87858L2.24148 5.18962L4.15344 6.64214C4.15344 6.64214 6.33547 4.15566 9.00658 2.48145L9.32541 2.87514C9.32541 2.87514 6.28665 5.55844 4.71735 9.07881L1.40857 5.87858Z" fill="white"></path></svg></div><svg class="imt-float-ball-loading" hidden="true" width="19" height="19" viewBox="0 0 19 19" fill="none" xmlns="http://www.w3.org/2000/svg" style="margin: 9px;"><path d="M9.42859 0C9.84288 0 10.1929 0.387143 10.1929 0.847143V3.99429C10.1929 4.45429 9.84431 4.84143 9.42859 4.84143C9.01431 4.84143 8.66431 4.45571 8.66431 3.99429V0.847143C8.66431 0.387143 9.01288 0 9.42859 0Z" fill="#E9E9E9"></path><path d="M14.1301 1.38877C14.5158 1.62591 14.6301 2.12163 14.4258 2.52305L12.9515 5.19448C12.901 5.28714 12.8325 5.36876 12.75 5.43455C12.6675 5.50035 12.5727 5.54898 12.4712 5.5776C12.3696 5.60621 12.2634 5.61424 12.1586 5.60119C12.0539 5.58814 11.9529 5.55429 11.8615 5.50163C11.6787 5.38432 11.5468 5.20237 11.4923 4.9921C11.4377 4.78184 11.4645 4.55874 11.5672 4.36734L13.0415 1.69591C13.2686 1.29448 13.7443 1.15305 14.1301 1.38877Z" fill="#989697"></path><path d="M17.4685 4.75707C17.5813 4.95451 17.6123 5.18824 17.5549 5.40825C17.4975 5.62826 17.3563 5.81705 17.1614 5.93422L14.4971 7.52564C14.0971 7.76993 13.6014 7.62422 13.3657 7.20707C13.2532 7.00994 13.2222 6.77667 13.2793 6.55702C13.3365 6.33737 13.4771 6.14874 13.6714 6.03136L16.3357 4.43993C16.7371 4.21993 17.2557 4.34136 17.4685 4.7585V4.75707Z" fill="#9B999A"></path><path d="M18.8572 9.42835C18.8572 9.84263 18.47 10.1926 18.01 10.1926H14.8629C14.4029 10.1926 14.0157 9.84406 14.0157 9.42835C14.0157 9.01406 14.4029 8.66406 14.8629 8.66406H18.01C18.47 8.66406 18.8572 9.01263 18.8572 9.42835Z" fill="#A3A1A2"></path><path d="M17.4686 14.1303C17.3515 14.3134 17.1697 14.4455 16.9594 14.5003C16.7491 14.5552 16.5259 14.5286 16.3343 14.426L13.6629 12.9517C13.5702 12.9012 13.4886 12.8327 13.4228 12.7503C13.357 12.6678 13.3084 12.573 13.2798 12.4714C13.2512 12.3698 13.2431 12.2636 13.2562 12.1589C13.2692 12.0542 13.3031 11.9532 13.3558 11.8617C13.4731 11.6789 13.655 11.547 13.8653 11.4925C14.0755 11.4379 14.2986 11.4647 14.49 11.5674L17.1615 13.0417C17.5629 13.2689 17.7043 13.7446 17.4686 14.1303Z" fill="#ABA9AA"></path><path opacity="0.7" d="M14.1 17.4686C13.9026 17.5814 13.6689 17.6124 13.4489 17.555C13.2288 17.4976 13.04 17.3564 12.9229 17.1615L11.3315 14.4972C11.0872 14.0972 11.2329 13.6015 11.65 13.3658C11.8472 13.2533 12.0804 13.2224 12.3001 13.2795C12.5197 13.3366 12.7084 13.4773 12.8257 13.6715L14.4172 16.3358C14.6372 16.7372 14.5157 17.2558 14.0986 17.4686H14.1Z" fill="#B2B2B2"></path><path opacity="0.6" d="M9.42859 18.8571C9.01431 18.8571 8.66431 18.4699 8.66431 18.0099V14.8628C8.66431 14.4028 9.01288 14.0156 9.42859 14.0156C9.84288 14.0156 10.1929 14.4028 10.1929 14.8628V18.0099C10.1929 18.4699 9.84431 18.8571 9.42859 18.8571Z" fill="#BAB8B9"></path><path opacity="0.5" d="M4.72717 17.4685C4.5441 17.3514 4.41195 17.1696 4.35713 16.9593C4.30231 16.749 4.32885 16.5258 4.43145 16.3342L5.90574 13.6628C5.95622 13.5701 6.02472 13.4885 6.1072 13.4227C6.18969 13.3569 6.2845 13.3083 6.38606 13.2797C6.48762 13.251 6.59387 13.243 6.69857 13.2561C6.80327 13.2691 6.90431 13.303 6.99574 13.3556C7.38145 13.5914 7.49431 14.0885 7.29002 14.4899L5.81574 17.1614C5.5886 17.5628 5.11288 17.7042 4.72717 17.4685Z" fill="#C2C0C1"></path><path opacity="0.4" d="M1.38862 14.1002C1.27584 13.9027 1.24483 13.669 1.30223 13.449C1.35964 13.229 1.50089 13.0402 1.69576 12.923L4.36004 11.3316C4.76004 11.0873 5.25576 11.233 5.49147 11.6502C5.60393 11.8473 5.63491 12.0806 5.5778 12.3002C5.52069 12.5199 5.38 12.7085 5.18576 12.8259L2.52004 14.4173C2.12004 14.6373 1.60004 14.5159 1.38862 14.0987V14.1002Z" fill="#CBCBCB"></path><path d="M0 9.42835C0 9.01406 0.387143 8.66406 0.847143 8.66406H3.99429C4.45429 8.66406 4.84143 9.01263 4.84143 9.42835C4.84143 9.84263 4.45571 10.1926 3.99429 10.1926H0.847143C0.387143 10.1926 0 9.84406 0 9.42835Z" fill="#D2D2D2"></path><path opacity="0.2" d="M1.38852 4.72705C1.50561 4.54398 1.68746 4.41183 1.89774 4.35701C2.10803 4.30219 2.33125 4.32873 2.52281 4.43133L5.19424 5.90562C5.28689 5.9561 5.36851 6.0246 5.43431 6.10708C5.5001 6.18957 5.54874 6.28438 5.57735 6.38594C5.60597 6.48749 5.61399 6.59375 5.60094 6.69845C5.5879 6.80315 5.55405 6.90419 5.50138 6.99562C5.38407 7.17844 5.20212 7.31029 4.99186 7.36484C4.78159 7.4194 4.55849 7.39263 4.3671 7.2899L1.69567 5.81562C1.29424 5.58847 1.15281 5.11276 1.38852 4.72705Z" fill="#DADADA"></path><path d="M4.75719 1.38849C4.95463 1.27571 5.18837 1.24471 5.40838 1.30211C5.62838 1.35952 5.81718 1.50077 5.93434 1.69564L7.52577 4.35992C7.77005 4.75992 7.62434 5.25564 7.20719 5.49135C7.01006 5.60381 6.77679 5.63479 6.55714 5.57768C6.33749 5.52056 6.14886 5.37988 6.03148 5.18564L4.44005 2.51992C4.22005 2.11992 4.34148 1.59992 4.75862 1.38849H4.75719Z" fill="#E2E2E2"></path></svg></div></div><div class=" " style="position: relative; pointer-events: all; display: inline-block; opacity: 1;"><div><div style="display: flex; align-items: center; flex-direction: row;"><svg width="14" height="14" viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg" style="display: block; opacity: 0;"><g clip-path="url(#clip0_2589_9951)"><path d="M7 14C5.14348 14 3.36301 13.2625 2.05025 11.9497C0.737498 10.637 0 8.85652 0 7C0 5.14348 0.737498 3.36301 2.05025 2.05025C3.36301 0.737498 5.14348 0 7 0C8.85652 0 10.637 0.737498 11.9497 2.05025C13.2625 3.36301 14 5.14348 14 7C14 8.85652 13.2625 10.637 11.9497 11.9497C10.637 13.2625 8.85652 14 7 14ZM4.183 5.064L6.118 7L4.183 8.936C4.12409 8.99361 4.07719 9.06234 4.04502 9.1382C4.01285 9.21406 3.99605 9.29554 3.99559 9.37794C3.99513 9.46034 4.01101 9.54201 4.04234 9.61823C4.07366 9.69444 4.11978 9.76369 4.17805 9.82195C4.23631 9.88022 4.30556 9.92634 4.38177 9.95766C4.45799 9.98898 4.53966 10.0049 4.62206 10.0044C4.70446 10.004 4.78594 9.98715 4.8618 9.95498C4.93766 9.92281 5.00639 9.87591 5.064 9.817L7 7.882L8.936 9.817C9.05327 9.93168 9.21104 9.99548 9.37506 9.99457C9.53908 9.99365 9.69612 9.92809 9.8121 9.8121C9.92809 9.69612 9.99365 9.53908 9.99457 9.37506C9.99548 9.21104 9.93168 9.05327 9.817 8.936L7.882 7L9.817 5.064C9.87591 5.00639 9.92281 4.93766 9.95498 4.8618C9.98715 4.78594 10.004 4.70446 10.0044 4.62206C10.0049 4.53966 9.98898 4.45799 9.95766 4.38177C9.92634 4.30556 9.88022 4.23631 9.82195 4.17805C9.76369 4.11978 9.69444 4.07366 9.61823 4.04234C9.54201 4.01101 9.46034 3.99513 9.37794 3.99559C9.29554 3.99605 9.21406 4.01285 9.1382 4.04502C9.06234 4.07719 8.99361 4.12409 8.936 4.183L7 6.118L5.064 4.183C4.94673 4.06832 4.78896 4.00452 4.62494 4.00543C4.46092 4.00635 4.30388 4.07191 4.1879 4.1879C4.07191 4.30388 4.00635 4.46092 4.00543 4.62494C4.00452 4.78896 4.06832 4.94673 4.183 5.064Z" fill="#B1B1B1" fill-opacity="0.32"></path></g><defs><clipPath id="clip0_2589_9951"><rect width="14" height="14" fill="white"></rect></clipPath></defs></svg><div class="imt-fb-btn  right btn-animate " dir="ltr" style="transform: translateX(15px); opacity: 0.7;"><div><svg class="imt-fb-logo-img imt-fb-logo-img-big-bg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="20" height="20"><path fill="none" d="M0 0h24v24H0z"></path><path d="M5 15v2a2 2 0 0 0 1.85 1.995L7 19h3v2H7a4 4 0 0 1-4-4v-2h2zm13-5l4.4 11h-2.155l-1.201-3h-4.09l-1.199 3h-2.154L16 10h2zm-1 2.885L15.753 16h2.492L17 12.885zM8 2v2h4v7H8v3H6v-3H2V4h4V2h2zm9 1a4 4 0 0 1 4 4v2h-2V7a2 2 0 0 0-2-2h-3V3h3zM6 6H4v3h2V6zm4 0H8v3h2V6z" fill="rgba(255,255,255,1)"></path></svg><svg hidden="true" class="imt-float-ball-translated" width="11" height="11" viewBox="0 0 11 11" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="5.5" cy="5.5" r="5.5" fill="#68CD52"></circle><path d="M1.40857 5.87858L2.24148 5.18962L4.15344 6.64214C4.15344 6.64214 6.33547 4.15566 9.00658 2.48145L9.32541 2.87514C9.32541 2.87514 6.28665 5.55844 4.71735 9.07881L1.40857 5.87858Z" fill="white"></path></svg></div></div><svg width="14" height="14" viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg" style="display: none; opacity: 0;"><g clip-path="url(#clip0_2589_9951)"><path d="M7 14C5.14348 14 3.36301 13.2625 2.05025 11.9497C0.737498 10.637 0 8.85652 0 7C0 5.14348 0.737498 3.36301 2.05025 2.05025C3.36301 0.737498 5.14348 0 7 0C8.85652 0 10.637 0.737498 11.9497 2.05025C13.2625 3.36301 14 5.14348 14 7C14 8.85652 13.2625 10.637 11.9497 11.9497C10.637 13.2625 8.85652 14 7 14ZM4.183 5.064L6.118 7L4.183 8.936C4.12409 8.99361 4.07719 9.06234 4.04502 9.1382C4.01285 9.21406 3.99605 9.29554 3.99559 9.37794C3.99513 9.46034 4.01101 9.54201 4.04234 9.61823C4.07366 9.69444 4.11978 9.76369 4.17805 9.82195C4.23631 9.88022 4.30556 9.92634 4.38177 9.95766C4.45799 9.98898 4.53966 10.0049 4.62206 10.0044C4.70446 10.004 4.78594 9.98715 4.8618 9.95498C4.93766 9.92281 5.00639 9.87591 5.064 9.817L7 7.882L8.936 9.817C9.05327 9.93168 9.21104 9.99548 9.37506 9.99457C9.53908 9.99365 9.69612 9.92809 9.8121 9.8121C9.92809 9.69612 9.99365 9.53908 9.99457 9.37506C9.99548 9.21104 9.93168 9.05327 9.817 8.936L7.882 7L9.817 5.064C9.87591 5.00639 9.92281 4.93766 9.95498 4.8618C9.98715 4.78594 10.004 4.70446 10.0044 4.62206C10.0049 4.53966 9.98898 4.45799 9.95766 4.38177C9.92634 4.30556 9.88022 4.23631 9.82195 4.17805C9.76369 4.11978 9.69444 4.07366 9.61823 4.04234C9.54201 4.01101 9.46034 3.99513 9.37794 3.99559C9.29554 3.99605 9.21406 4.01285 9.1382 4.04502C9.06234 4.07719 8.99361 4.12409 8.936 4.183L7 6.118L5.064 4.183C4.94673 4.06832 4.78896 4.00452 4.62494 4.00543C4.46092 4.00635 4.30388 4.07191 4.1879 4.1879C4.07191 4.30388 4.00635 4.46092 4.00543 4.62494C4.00452 4.78896 4.06832 4.94673 4.183 5.064Z" fill="#B1B1B1" fill-opacity="0.32"></path></g><defs><clipPath id="clip0_2589_9951"><rect width="14" height="14" fill="white"></rect></clipPath></defs></svg></div></div></div><div style="position: relative; width: 100%; opacity: 0;"><div title="关闭悬浮球" class="imt-fb-close-button" style="transform: translateX(100%);"><svg width="14" height="14" viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_2589_9951)"><path d="M7 14C5.14348 14 3.36301 13.2625 2.05025 11.9497C0.737498 10.637 0 8.85652 0 7C0 5.14348 0.737498 3.36301 2.05025 2.05025C3.36301 0.737498 5.14348 0 7 0C8.85652 0 10.637 0.737498 11.9497 2.05025C13.2625 3.36301 14 5.14348 14 7C14 8.85652 13.2625 10.637 11.9497 11.9497C10.637 13.2625 8.85652 14 7 14ZM4.183 5.064L6.118 7L4.183 8.936C4.12409 8.99361 4.07719 9.06234 4.04502 9.1382C4.01285 9.21406 3.99605 9.29554 3.99559 9.37794C3.99513 9.46034 4.01101 9.54201 4.04234 9.61823C4.07366 9.69444 4.11978 9.76369 4.17805 9.82195C4.23631 9.88022 4.30556 9.92634 4.38177 9.95766C4.45799 9.98898 4.53966 10.0049 4.62206 10.0044C4.70446 10.004 4.78594 9.98715 4.8618 9.95498C4.93766 9.92281 5.00639 9.87591 5.064 9.817L7 7.882L8.936 9.817C9.05327 9.93168 9.21104 9.99548 9.37506 9.99457C9.53908 9.99365 9.69612 9.92809 9.8121 9.8121C9.92809 9.69612 9.99365 9.53908 9.99457 9.37506C9.99548 9.21104 9.93168 9.05327 9.817 8.936L7.882 7L9.817 5.064C9.87591 5.00639 9.92281 4.93766 9.95498 4.8618C9.98715 4.78594 10.004 4.70446 10.0044 4.62206C10.0049 4.53966 9.98898 4.45799 9.95766 4.38177C9.92634 4.30556 9.88022 4.23631 9.82195 4.17805C9.76369 4.11978 9.69444 4.07366 9.61823 4.04234C9.54201 4.01101 9.46034 3.99513 9.37794 3.99559C9.29554 3.99605 9.21406 4.01285 9.1382 4.04502C9.06234 4.07719 8.99361 4.12409 8.936 4.183L7 6.118L5.064 4.183C4.94673 4.06832 4.78896 4.00452 4.62494 4.00543C4.46092 4.00635 4.30388 4.07191 4.1879 4.1879C4.07191 4.30388 4.00635 4.46092 4.00543 4.62494C4.00452 4.78896 4.06832 4.94673 4.183 5.064Z" fill="#B1B1B1" fill-opacity="0.32"></path></g><defs><clipPath id="clip0_2589_9951"><rect width="14" height="14" fill="white"></rect></clipPath></defs></svg></div></div><div class="imt-fb-more-buttons btn-animate" style="margin-top: 10px; transform: translateX(60px);"><div class=" btn-animate" style="position: relative; pointer-events: all; display: inline-block; opacity: 1;"><div><div class="imt-fb-more-button"><svg width="22" height="22" viewBox="0 0 22 22" fill="none" xmlns="http://www.w3.org/2000/svg" style="width: 22px; height: 22px;"><path d="M16 7.66699H10.375" stroke="#666666" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"></path><path d="M11.625 14.333L6 14.333" stroke="#666666" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"></path><path d="M14.125 16C15.1605 16 16 15.1605 16 14.125C16 13.0895 15.1605 12.25 14.125 12.25C13.0895 12.25 12.25 13.0895 12.25 14.125C12.25 15.1605 13.0895 16 14.125 16Z" stroke="#666666" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"></path><path d="M7.875 9.75C8.91053 9.75 9.75 8.91053 9.75 7.875C9.75 6.83947 8.91053 6 7.875 6C6.83947 6 6 6.83947 6 7.875C6 8.91053 6.83947 9.75 7.875 9.75Z" stroke="#666666" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"></path><rect x="3" y="3" width="16" height="16" rx="1.66667" stroke="#666666" stroke-width="1.4"></rect></svg></div></div></div><div class=" btn-animate" style="position: relative; pointer-events: all; display: inline-block; opacity: 1;"><div><div class="imt-fb-more-button"><svg class="imt-fb-feedback" width="22" height="22" viewBox="0 0 22 22" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M11.0003 14.2749C11.213 14.2749 11.3895 14.2047 11.5299 14.0643C11.6705 13.9239 11.7408 13.7473 11.7408 13.5345C11.7408 13.3218 11.6705 13.1453 11.5299 13.0049C11.3895 12.8645 11.213 12.7943 11.0003 12.7943C10.7877 12.7943 10.6111 12.8645 10.4707 13.0049C10.3302 13.1453 10.2599 13.3218 10.2599 13.5345C10.2599 13.7473 10.3302 13.9239 10.4707 14.0643C10.6111 14.2047 10.7877 14.2749 11.0003 14.2749ZM11.0003 11.0842C11.1954 11.0842 11.3587 11.0185 11.4903 10.8869C11.622 10.7552 11.6878 10.5918 11.6878 10.3967V6.23645C11.6878 6.04135 11.622 5.87803 11.4903 5.74649C11.3587 5.6148 11.1954 5.54895 11.0003 5.54895C10.8052 5.54895 10.6419 5.6148 10.5104 5.74649C10.3787 5.87803 10.3128 6.04135 10.3128 6.23645V10.3967C10.3128 10.5918 10.3787 10.7552 10.5104 10.8869C10.6419 11.0185 10.8052 11.0842 11.0003 11.0842ZM5.53562 16.8311L3.70045 18.666C3.43966 18.9269 3.13968 18.9861 2.80051 18.8434C2.4615 18.7005 2.29199 18.4434 2.29199 18.072V4.73816C2.29199 4.27509 2.45241 3.88314 2.77324 3.5623C3.09408 3.24147 3.48603 3.08105 3.9491 3.08105H18.0516C18.5146 3.08105 18.9066 3.24147 19.2274 3.5623C19.5482 3.88314 19.7087 4.27509 19.7087 4.73816V15.174C19.7087 15.637 19.5482 16.029 19.2274 16.3498C18.9066 16.6706 18.5146 16.8311 18.0516 16.8311H5.53562ZM4.95033 15.4561H18.0516C18.1221 15.4561 18.1868 15.4266 18.2454 15.3678C18.3042 15.3092 18.3337 15.2445 18.3337 15.174V4.73816C18.3337 4.66758 18.3042 4.60295 18.2454 4.54428C18.1868 4.48546 18.1221 4.45605 18.0516 4.45605H3.9491C3.87851 4.45605 3.81389 4.48546 3.75522 4.54428C3.6964 4.60295 3.66699 4.66758 3.66699 4.73816V16.7254L4.95033 15.4561Z" fill="#666666"></path></svg></div></div></div></div></div></div></template></div></html>