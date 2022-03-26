from .html_reader import HtmlReader
from .body_parser import HtmlParser
from .db_provider import DbProvider
from .utilities import Utilities

class ExtractWorker(object):
    def __init__(self, url, html_cols, db_name, insert_params):
        self.db_name = db_name
        self.url = url
        self.html_cols = html_cols
        self.insert_params = insert_params

    def extractItems(self):
        body = HtmlReader.getHtmlBody(self.url)
        self.parser = HtmlParser(body)
        return self.parser.getItems(self.html_cols)        

    def insertItems(self, items):
        with DbProvider(self.db_name) as provider:
            provider.insertItems(items, self.insert_params)

    def doWork(self):
        if not Utilities.checkFileExists(self.db_name):
            self.createTable()
        items = self.extractItems()
        self.insertItems(items)
    
    def createTable(self):
        with DbProvider(self.db_name) as provider:
            provider.createTable()
