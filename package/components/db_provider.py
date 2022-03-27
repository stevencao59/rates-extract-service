import traceback
import sqlite3
from ..configs.sql_configs import SqlConfigs
from .utilities import Utilities
class DbProvider(object):
    def __init__(self, *args, **kwargs):
        self.logger = Utilities.createLogger(__name__)
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
                self.logger.error(f'Error occurred while executing query! {traceback.format_exc()}')
        return func

    def getQuery(f):
        def func(self, *args, **kwargs):
            try:
                res = f(self, *args, **kwargs)
                return res
            except:
                self.logger.error(f'Error occurred while running get query! {traceback.format_exc()}')
        return func

    @executeQuery
    def createTable(self):
        self.conn.execute(SqlConfigs.create_table)                            

    @executeQuery
    def insertOrUpdateItems(self, *args, **kwargs):
        items, select_param, insert_params, update_params = args
        for item in items:
            self.logger.info(f'Updating item {Utilities.generateParam(item, insert_params)}')
            sel = self.selectItem(item, select_param)
            if sel:
                self.updateItem(item, update_params)
            else:
                self.insertItem(item, insert_params)

    @getQuery
    def selectItem(self, *args, **kwargs):
        cur = self.conn.cursor()
        cur.execute(SqlConfigs.select_items, Utilities.generateParam(*args))
        return cur.fetchall()

    @executeQuery
    def insertItem(self, *args, **kwargs):
        self.conn.execute(SqlConfigs.insert_items, Utilities.generateParam(*args))

    @executeQuery
    def updateItem(self, *args, **kwargs):
        self.conn.execute(SqlConfigs.update_items, Utilities.generateParam(*args))

    @getQuery
    def getItems(self, *args, **kwargs):
        [date,] = args
        params = [date.strftime("%Y-%m-%d")]*3
        cur = self.conn.cursor()
        cur.execute(SqlConfigs.get_items, params)
        return cur.fetchall()

