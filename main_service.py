# Rest Service Worker
from package.api.apis import ServiceWorker

if __name__ == '__main__':
    serviceWorker = ServiceWorker()
    serviceWorker.startService()