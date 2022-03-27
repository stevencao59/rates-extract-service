# Extract Job Worker
from package.configs.extract_configs import ExtractConfigs
from package.configs.sql_configs import SqlConfigs
from package.components.extract_worker import ExtractWorker

if __name__ == '__main__':
    worker = ExtractWorker(
        ExtractConfigs.url,\
        ExtractConfigs.html_cols,\
        SqlConfigs.db_name,\
        SqlConfigs.select_params,\
        SqlConfigs.insert_params,\
        SqlConfigs.update_params)
    worker.doWork()
