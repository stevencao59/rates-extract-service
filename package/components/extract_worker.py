from .html_reader import HtmlReader
from .body_parser import HtmlParser
from .db_provider import DbProvider

from .utilities import Utilities
logger = Utilities.createLogger(__name__)

class ExtractWorker(object):
    def __init__(self, url, html_cols, db_name, select_params, insert_params, update_params):
        self.db_name = db_name
        self.url = url
        self.html_cols = html_cols
        self.insert_params = insert_params
        self.select_params = select_params
        self.update_params = update_params

    def extractItems(self):
        logger.info(f'Extracting html body from {self.url}...')
        body = HtmlReader.getHtmlBody(self.url)
        self.parser = HtmlParser(body)
        res = self.parser.getItems(self.html_cols)
        logger.info('Items have been extracted without issue!')
        return res      

    def insertItems(self, items):
        with DbProvider(self.db_name) as provider:
            provider.insertOrUpdateItems(items, self.select_params, self.insert_params, self.update_params)
        logger.info(f'Items have been inserted/updated without issue!')

    def checkDbFile(self):
        logger.info('Checking if db file exists...')
        if not Utilities.checkFileExists(self.db_name):
            logger.warn('Db file does not exist. Creating a new one...')
            self.createTable()

    def doWork(self):
        logger.info('Extract work is starting...')
        if not Utilities.checkFileExists(self.db_name):
            self.createTable()
        items = self.extractItems()
        self.insertItems(items)
        logger.info('Extract work is finished without issue!')
    
    def createTable(self):
        with DbProvider(self.db_name) as provider:
            provider.createTable()
        logger.info('New Db file is created!')
