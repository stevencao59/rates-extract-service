import datetime

class InterestRateItem(object):
    def __init__(self, resetDate, liborRate, sofrRate, *args, **kwargs):
        self.resetDate = resetDate
        self.liborRate = liborRate
        self.sofrRate = sofrRate
    
    @property
    def date(self):
        return datetime.datetime.strptime(self.resetDate, '%m/%d/%Y')

    @property
    def libor_rate(self):
        return float(self.liborRate.strip('%'))/100
    
    @property
    def sofr_rate(self):
        return float(self.sofrRate.strip('%'))/100
    