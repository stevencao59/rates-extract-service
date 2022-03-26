import logging
from .db_provider import DbProvider
from ..configs.sql_configs import SqlConfigs

logger=logging.getLogger(__name__)

class AggregateWorker(object):
    def __init__(self, db_name):
        self.db_name = db_name

    def getResponse(self, items, reference_rate, spread, ceiling, floor):
        def getValue(rate):
            val = rate+spread
            return ceiling if val>ceiling else floor if val<floor else val

        def formatDate(date):
            return date.replace(' 00:00:00', '')

        res = []
        for item in items:
            rate = item['libor_rate'] if reference_rate=='LIBOR' else item['sofr_rate'] if reference_rate=='SOFR' else None
            res.append({'date': formatDate(item['date']), 'rate': getValue(rate)})
        
        return res

    def getItems(self, *args, **kwargs):
        items = []
        with DbProvider(self.db_name) as provider:
            items = [dict(a) for a in [zip(SqlConfigs.query_cols, a) for a in provider.getItems(kwargs['maturity_date'])]]
        return items
    
    def doWork(self, *args, **kwargs):
        items = self.getItems(*args, **kwargs)
        return self.getResponse(items, kwargs['reference_rate'], kwargs['rate_spread'], kwargs['rate_ceiling'], kwargs['rate_floor'])
