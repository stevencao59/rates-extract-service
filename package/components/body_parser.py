
from bs4 import BeautifulSoup
from ..models.rate_object import InterestRateItem

class HtmlParser(object):
    def __init__(self, htmlBody):
        self.parser = BeautifulSoup(htmlBody, 'html.parser')

    def getItems(self, html_cols):
        res = []
        tables = self.parser.find_all('table')
        table = tables[0] if tables else None
        tr = table.tbody.find_all('tr')
        for t in tr:
            kDict = dict(zip(html_cols, t.text.strip('\n').split('\n')))
            item = InterestRateItem(**kDict)
            res.append(item)
        return res
    
    def getFileUri(self):
        def condition(item):
            return item.has_attr('data-form-name') and item.attrs['data-form-name']=='Forward Curve' and item.has_attr('href')

        res = [a.attrs['href'] for a in self.parser.find_all('a') if condition(a)]
        return res[0] if res else None    