from dnsdumpster.DNSDumpsterAPI import DNSDumpsterAPI
import Harvester
class Harvester_DNSDumpster(Harvester.Harvester): 
    def __init__(self,domain):
        self.domain = domain 

    def get_data(self):
        self.res =  DNSDumpsterAPI().search(self.domain)
        self.res.pop("image_data")
        self.res.pop("xls_data")
        #for ip in self.res
              

        #print(self.res )

    def __str__(self): 
        return str(self.res)
