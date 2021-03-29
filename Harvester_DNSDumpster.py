from dnsdumpster.DNSDumpsterAPI import DNSDumpsterAPI
import Harvester
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
        return str(self.formated_data())

    def __str__(self): 
        return str(self.structured_data())
