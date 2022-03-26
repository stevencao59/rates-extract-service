# Extract Job Worker
from package.configs.extract_configs import ExtractConfigs
from package.configs.sql_configs import SqlConfigs
from package.components.extract_worker import ExtractWorker

# Rest Service Worker
from package.api.apis import ServiceWorker

if __name__ == '__main__':
    # worker = ExtractWorker(ExtractConfigs.url, ExtractConfigs.html_cols, SqlConfigs.db_name, SqlConfigs.insert_params)
    # worker.doWork()

    serviceWorker = ServiceWorker()
    serviceWorker.startService()