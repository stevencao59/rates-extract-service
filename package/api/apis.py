import datetime
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from ..configs.sql_configs import SqlConfigs
from ..components.aggregate_worker import AggregateWorker

app = FastAPI()

class Request(BaseModel):
    maturity_date: datetime.date
    reference_rate: str
    rate_floor: float
    rate_ceiling: float
    rate_spread: float

@app.post("/rates_payload/")
def retrieve_rate(request: Request):
    # Example: {"maturity_date": "2022-11-23","reference_rate": "SOFR","rate_floor": 0.02,"rate_ceiling": 0.1,"rate_spread": 0.02}
    item = {'maturity_date': request.maturity_date, 
            'reference_rate':request.reference_rate, 
            'rate_floor': request.rate_floor, 
            'rate_ceiling': request.rate_ceiling, 
            'rate_spread': request.rate_spread}

    worker = AggregateWorker(SqlConfigs.db_name)
    results = worker.doWork(**item)
    return results

@app.get("/rates/")
def get_rate(maturity_date:datetime.date, reference_rate, rate_floor: float, rate_ceiling: float, rate_spread: float):
    # Example: Link http://127.0.0.1:8000/rates/?maturity_date=2022-11-23&reference_rate=SOFR&rate_floor=0.02&rate_ceiling=0.10&rate_spread=0.02
    item = {'maturity_date': maturity_date, 'reference_rate':reference_rate, 'rate_floor': rate_floor, 'rate_ceiling': rate_ceiling, 'rate_spread': rate_spread}

    worker = AggregateWorker(SqlConfigs.db_name)
    results = worker.doWork(**item)
    return results


class ServiceWorker(object):
    def startService(self):
        uvicorn.run(app, host="127.0.0.1", port=8000)