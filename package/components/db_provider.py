import traceback
import logging
import sqlite3
from ..configs.sql_configs import SqlConfigs

logger=logging.getLogger(__name__)

class DbProvider(object):
    def __init__(self, *args, **kwargs):
        [self.db_name,] = args

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        return self
  
    def __exit__(self, *args, **kwargs):
        self.conn.close()

    def executeQuery(f):
        def func(self, *args, **kwargs):
            try:
                f(self, *args, **kwargs)
                self.conn.commit()
            except:
                logger.error(f'Error occurred while executing query! {traceback.format_exc()}')
        return func

    def getQuery(f):
        def func(self, *args, **kwargs):
            try:
                return f(self, *args, **kwargs)
            except:
                logger.error(f'Error occurred while running get query! {traceback.format_exc()}')
        return func

    @executeQuery
    def createTable(self):
        self.conn.execute(SqlConfigs.create_table)                            

    @executeQuery
    def insertItems(self, *args, **kwargs):
        items, insert_params = args
        for item in items:
            insertList = [getattr(item, field) for field in insert_params]
            self.insertItem(insertList)

    @executeQuery
    def insertItem(self, *args, **kwargs):
        [item,] = args
        self.conn.execute(SqlConfigs.insert_items, item)

    @getQuery
    def getItems(self, *args, **kwargs):
        [date,] = args
        params = [date.strftime("%Y-%m-%d")]*3
        cur = self.conn.cursor()
        cur.execute(SqlConfigs.get_items, params)
        return cur.fetchall()

