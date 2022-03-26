import urllib.request

class HtmlReader(object):
    @staticmethod
    def getHtmlBody(url):
        with urllib.request.urlopen(url) as uo:
            byte = uo.read()
            decodedStr = byte.decode('utf-8')
            return decodedStr