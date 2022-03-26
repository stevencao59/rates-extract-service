import os.path


class Utilities(object):
    @staticmethod
    def checkFileExists(filename):
        return os.path.isfile(filename)