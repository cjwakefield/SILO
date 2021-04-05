import Harvester
from pyhunter import PyHunter

class Harvester_Email(Harvester.Harvester): 
    def __init__(self,domain,API_KEY):
        self.hunter = PyHunter(API_KEY)
        self.domain = domain
        self.get_data()       

    def get_data(self,limit=5, offset=2):
       self.json = self.hunter.domain_search(company=self.domain, limit=self.limit, offset=self.offset) # pass in the limit and offset

    def formated_data(self):
        return self.json
    
    def structured_data(self):
        return str(self.formated_data())

    def __str__(self): 
        return str(self.structured_data())

