"use strict";var precacheConfig=[["/index.html","f28480f36ea65af9562235e9e6b2ade2"],["/static/css/main.bd36c8fb.css","db0da9495934ef61d4cc3c30db7bdae1"],["/static/js/main.24ddefd9.js","65cf0a4e4cdd3edd8a05b721dcab93f7"],["/static/media/angela.6701ac8e.png","6701ac8e769ac9781ede6dec1168e956"],["/static/media/armchair.b7ca700c.svg","b7ca700c796157e512a174c460562df5"],["/static/media/fa-brands-400.1dae819a.woff","1dae819a32feafdc34fea670ab758519"],["/static/media/fa-brands-400.31b5f53e.ttf","31b5f53e002d3212b7f1ae50cd1d31dc"],["/static/media/fa-brands-400.3619e460.svg","3619e4601d77994662036eb903b64eee"],["/static/media/fa-brands-400.5ac8c4fe.woff2","5ac8c4fec34fe5e740ab560e4a90240b"],["/static/media/fa-brands-400.f384cdc0.eot","f384cdc0b0ee351ae21dc896031c40d6"],["/static/media/fa-regular-400.2ed38dba.ttf","2ed38dbad5ce736060bb41f229eb2dce"],["/static/media/fa-regular-400.5cf78fbc.woff","5cf78fbc2341f5fac935bf17dcf5e84e"],["/static/media/fa-regular-400.779d7ea0.woff2","779d7ea0b9f54514b905e24343e71c4e"],["/static/media/fa-regular-400.7e62ee01.svg","7e62ee01f6e4e617ddfa13b70d925a5a"],["/static/media/fa-regular-400.a5e47772.eot","a5e47772ae220b65945186a7532411af"],["/static/media/fa-solid-900.0d38abcb.eot","0d38abcb91b2dd56e8babd915233caca"],["/static/media/fa-solid-900.62e22419.woff2","62e224193aeed0b428e83d1cccfd6d91"],["/static/media/fa-solid-900.68b7c284.woff","68b7c2849c46507aef459d047d5e7696"],["/static/media/fa-solid-900.7bc0b08b.svg","7bc0b08bd858d78a561191a308e0bcd4"],["/static/media/fa-solid-900.ba67efc7.ttf","ba67efc77a5fe272922aebf9d42ad1da"],["/static/media/login.cdbce77d.png","cdbce77d96b5fe3ce2dc084764b4d5e9"],["/static/media/login01.70308ff5.svg","70308ff5861578fc87108b644c1623ed"],["/static/media/login02.87b0f741.svg","87b0f7417ab6b35eb3a4ac5773bf0840"],["/static/media/login03.b5644218.svg","b5644218cddef92153a3f36916fda0ac"]],cacheName="sw-precache-v3-sw-precache-webpack-plugin-"+(self.registration?self.registration.scope:""),ignoreUrlParametersMatching=[/^utm_/],addDirectoryIndex=function(e,a){var t=new URL(e);return"/"===t.pathname.slice(-1)&&(t.pathname+=a),t.toString()},cleanResponse=function(a){return a.redirected?("body"in a?Promise.resolve(a.body):a.blob()).then(function(e){return new Response(e,{headers:a.headers,status:a.status,statusText:a.statusText})}):Promise.resolve(a)},createCacheKey=function(e,a,t,n){var c=new URL(e);return n&&c.pathname.match(n)||(c.search+=(c.search?"&":"")+encodeURIComponent(a)+"="+encodeURIComponent(t)),c.toString()},isPathWhitelisted=function(e,a){if(0===e.length)return!0;var t=new URL(a).pathname;return e.some(function(e){return t.match(e)})},stripIgnoredUrlParameters=function(e,t){var a=new URL(e);return a.hash="",a.search=a.search.slice(1).split("&").map(function(e){return e.split("=")}).filter(function(a){return t.every(function(e){return!e.test(a[0])})}).map(function(e){return e.join("=")}).join("&"),a.toString()},hashParamName="_sw-precache",urlsToCacheKeys=new Map(precacheConfig.map(function(e){var a=e[0],t=e[1],n=new URL(a,self.location),c=createCacheKey(n,hashParamName,t,/\.\w{8}\./);return[n.toString(),c]}));function setOfCachedUrls(e){return e.keys().then(function(e){return e.map(function(e){return e.url})}).then(function(e){return new Set(e)})}self.addEventListener("install",function(e){e.waitUntil(caches.open(cacheName).then(function(n){return setOfCachedUrls(n).then(function(t){return Promise.all(Array.from(urlsToCacheKeys.values()).map(function(a){if(!t.has(a)){var e=new Request(a,{credentials:"same-origin"});return fetch(e).then(function(e){if(!e.ok)throw new Error("Request for "+a+" returned a response with status "+e.status);return cleanResponse(e).then(function(e){return n.put(a,e)})})}}))})}).then(function(){return self.skipWaiting()}))}),self.addEventListener("activate",function(e){var t=new Set(urlsToCacheKeys.values());e.waitUntil(caches.open(cacheName).then(function(a){return a.keys().then(function(e){return Promise.all(e.map(function(e){if(!t.has(e.url))return a.delete(e)}))})}).then(function(){return self.clients.claim()}))}),self.addEventListener("fetch",function(a){if("GET"===a.request.method){var e,t=stripIgnoredUrlParameters(a.request.url,ignoreUrlParametersMatching),n="index.html";(e=urlsToCacheKeys.has(t))||(t=addDirectoryIndex(t,n),e=urlsToCacheKeys.has(t));var c="/index.html";!e&&"navigate"===a.request.mode&&isPathWhitelisted(["^(?!\\/__).*"],a.request.url)&&(t=new URL(c,self.location).toString(),e=urlsToCacheKeys.has(t)),e&&a.respondWith(caches.open(cacheName).then(function(e){return e.match(urlsToCacheKeys.get(t)).then(function(e){if(e)return e;throw Error("The cached response that was expected is missing.")})}).catch(function(e){return console.warn('Couldn\'t serve response for "%s" from cache: %O',a.request.url,e),fetch(a.request)}))}});