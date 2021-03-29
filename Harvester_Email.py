import Harvester
from pyhunter import PyHunter

class Harvester_Email(Harvester.Harvester): 
    def __init__(self,domain,API_KEY):
        self.hunter = PyHunter(API_KEY)
        self.domain = domain
       

    def get_data(self):
       self.out = self.hunter.domain_search(company=self.domain, limit=5, offset=2)
       return out

    def formated_data(self):
        return str(self)
    
    def structured_data(self):
        return str(self)

    def __str__(self): 
        return ""

