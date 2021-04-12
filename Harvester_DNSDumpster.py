from dnsdumpster.DNSDumpsterAPI import DNSDumpsterAPI
import Harvester
from rich.console import Console
from rich.table import Table
#https://github.com/PaulSec/API-dnsdumpster.com
class Harvester_DNSDumpster(Harvester.Harvester): 
    def __init__(self,domain):
        self.domain = domain 
        self.get_data()

    def get_data(self):
        self.res =  DNSDumpsterAPI().search(self.domain)
        self.image = self.res.pop("image_data")
        self.xls = self.res.pop("xls_data")
        #for ip in self.res
              

        #print(self.res )
    def formated_data(self): #the formated data that can be used by python
        domainlist = self.res.get("dns_records").get("host")
        returnlist = []
        for domain in domainlist: 
            returnlist.append(domain.get("domain"))
        return returnlist
    
    def structured_data(self): #the data formated to be printed to the terminal 
        console = Console()
        table = Table(show_header=True, header_style="bold green")
        table.add_column("Sub Domains")
        for row in self.formated_data():
            table.add_row(row)
        console.print(table)
        return ""

    def __str__(self): 
        return str(self.formated_data())
