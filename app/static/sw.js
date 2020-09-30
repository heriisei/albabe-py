var CACHE_STATIC = 'static-v0.1';
var CACHE_DYNAMIC = 'dynamic-v0.1';
var STATIC_FILES = [
  'http://127.0.0.1:5000/',
  'https://cdnjs.cloudflare.com/ajax/libs/bulma/0.7.2/css/bulma.min.css',
];

self.addEventListener('install', event => {
  self.skipWaiting();
  console.log('[Service Worker] installing service worker...' ,  event);
  // cache API
  event.waitUntil(
    caches.open(CACHE_STATIC) // store the asstes to cache
      .then( cache => {
        console.log('[Service Worker] Caching Core Assest...');
        //cache.add('/src/js/app.js'); // add single asset to cache
        // cache multiple assest
        // set precache of core assets
        return cache.addAll(STATIC_FILES)
      }).then( () => {
        console.log('[Service Worker] install completed')
      })
  )
});

self.addEventListener('activate', event => {
  //
  console.log('[Service Worker] Activate service worker...' ,  event);
  // clean up the old version caches
  event.waitUntil(
    caches.keys() // to store the list of cache in the storage
      .then( keyList => {
        return Promise.all(keyList.map( key => { // convert list array to promise wait untul all list is get
          if (key !== CACHE_STATIC && key !== CACHE_DYNAMIC) { // check if the name of list cache not the current our assets
            console.log('[Service Worker] Removing Old Cache', key);
            return caches.delete(key);
          };
        }));
      })
  )
  return self.clients.claim();
});

// self.addEventListener('fetch', event => {
//   console.log('[ServiceWorker] Fetch', event.request.url);
//   event.respondWith(
//     caches.open(CACHE_DYNAMIC).then( cache => {
//       return fetch(event.request).then( response => {
//         cache.put(event.request, response.clone());
//         return response || cache.match(event.request).then( response => {
//         return response || fetch(event.request);
//         });
//       });
//     })
//   );
// });


self.addEventListener('fetch', event => {
  event.respondWith(
    caches.open(CACHE_DYNAMIC).then(function(cache) {
      return cache.match(event.request).then(function (response) {
        return response || fetch(event.request).then(function(response) {
          cache.put(event.request, response.clone());
          return response;
        });
      });
    })
  )
});