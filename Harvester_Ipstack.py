import Harvester
import rich
from ipstack import GeoLookup
class Harvester_Ipstack(Harvester.Harvester): 
    def __init__(self,domain,API_KEY):
        self.domain = domain
        self.API_KEY = API_KEY
        self.get_data()

    def get_data(self):
        geo_lookup = GeoLookup(self.API_KEY)
        self.locations = geo_lookup.get_location(self.domain)

    def formated_data(self):
        return self.locations
    
    def structured_data(self):
        return str(self.formated_data())

    def __str__(self): 
        return ""
