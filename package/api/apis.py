import logging
import datetime
import uvicorn
from fastapi import FastAPI
from ..configs.sql_configs import SqlConfigs
from ..components.aggregate_worker import AggregateWorker

logger=logging.getLogger(__name__)

app = FastAPI()

@app.get("/rates/")
def get_rate(maturity_date:datetime.date, reference_rate, rate_floor: float, rate_ceiling: float, rate_spread: float):
    # Test Link http://127.0.0.1:8000/rates/?maturity_date=2022-3-23&reference_rate=SOFR&rate_floor=0.02&rate_ceiling=0.10&rate_spread=0.02
    item = {'maturity_date': maturity_date, 'reference_date':reference_rate, 'rate_floor': rate_floor, 'rate_ceiling': rate_ceiling, 'rate_spread': rate_spread}

    worker = AggregateWorker(SqlConfigs.db_name)
    results = worker.getItems(**item)
    return results

class ServiceWorker(object):
    def startService(self):
        uvicorn.run(app, host="127.0.0.1", port=8000)