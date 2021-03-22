import nmap 
import Harvester
class Harvester_Nmap(Harvester.Harvester): 
    def __init__(self,domainlist):
        self.domainlist = domainlist
        self.nmap = nmap.PortScanner()

    def get_data(self):
        for domain in self.domainlist:
            self.nmap.scan(domain, '22-443')

    def formated_data(self):
        return str(self.nmap["127.0.0.1"])
    
    def structured_data(self):
        return str(self.nmap["127.0.0.1"])

    def __str__(self): 
        return str(self.nmap["127.0.0.1"])

