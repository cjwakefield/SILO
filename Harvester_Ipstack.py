import Harvester
import rich
from ipstack import GeoLookup
from rich.console import Console
from rich.table import Table

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
        table = Table(title="Domain Info" ,show_header=True, header_style="bold green")
        table.add_column("IP")
        table.add_column("City")
        table.add_column("Zip'")
        table.add_column("Latitude")
        table.add_column("Longitude")
        table.add_row(str(self.locations.get("ip")),str(self.locations.get("city")),str(self.locations.get("zip")),str(self.locations.get("latitude")),str(self.locations.get("longitude")))
        return table

    def __str__(self): 
        return ""
