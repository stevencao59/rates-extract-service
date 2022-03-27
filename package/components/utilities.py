import os.path
import logging

class Utilities(object):
    @staticmethod
    def checkFileExists(filename):
        return os.path.isfile(filename)
    
    @staticmethod
    def createLogger(name):
        logging.basicConfig()
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)
        return logger
    
    @staticmethod
    def generateParam(*args):
        [item, params]  = args
        return [getattr(item, field) for field in params]