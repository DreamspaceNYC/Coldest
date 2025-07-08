// Service Worker for PWA functionality
const CACHE_NAME = 'tiktok-hooks-v1';
const urlsToCache = [
  '/',
  '/static/js/bundle.js',
  '/static/css/main.css',
  '/manifest.json'
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then((cache) => cache.addAll(urlsToCache))
  );
});

self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request)
      .then((response) => {
        // Return cached version or fetch from network
        return response || fetch(event.request);
      })
  );
});

// Offline hook generation fallback
self.addEventListener('message', (event) => {
  if (event.data && event.data.type === 'GENERATE_OFFLINE_HOOKS') {
    const { topic, count } = event.data;
    
    // Simple offline hook templates
    const templates = [
      `This ${topic} hack will blow your mind`,
      `Nobody talks about this ${topic} secret`,
      `You're doing ${topic} wrong - here's why`,
      `This changes everything about ${topic}`,
      `The ${topic} mistake everyone makes`
    ];
    
    const hooks = templates.slice(0, count).map((template, index) => ({
      id: index + 1,
      text: template
    }));
    
    event.ports[0].postMessage({ hooks });
  }
});