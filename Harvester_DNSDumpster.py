from dnsdumpster.DNSDumpsterAPI import DNSDumpsterAPI
import Harvester
#https://github.com/PaulSec/API-dnsdumpster.com
class Harvester_DNSDumpster(Harvester.Harvester): 
    def __init__(self,domain):
        self.domain = domain 

    def get_data(self):
        self.res =  DNSDumpsterAPI().search(self.domain)
        self.image = self.res.pop("image_data")
        self.xls = self.res.pop("xls_data")
        #for ip in self.res
              

        #print(self.res )
    def formated_data(self): #printed data
        return str(self)
    
    def structured_data(self): #  the to str
        return str(self)

    def __str__(self): 
        return str(self.res)
