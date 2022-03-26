import logging
from .db_provider import DbProvider

logger=logging.getLogger(__name__)

class AggregateWorker(object):
    def __init__(self, db_name):
        self.db_name = db_name

    def getItems(self, *args, **kwargs):
        with DbProvider(self.db_name) as provider:
            items = provider.getItems(kwargs['maturity_date'])
            logger.info(items)
        return items
