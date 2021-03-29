import nmap 
import Harvester
class Harvester_Nmap(Harvester.Harvester): 
    def __init__(self,domainlist):
        self.domainlist = domainlist
        self.nmap = nmap.PortScanner()

    def get_data(self, ports='21-443'):
        for domain in self.domainlist:
            self.nmap.scan(domain, ports)

    def formated_data(self):
        for domain in self.domainlist:
            return str(self.nmap[domain])
    
    def structured_data(self):
        return str(self)

    def __str__(self): 
        return str([str(self.nmap[domain]) for domain in self.domainlist])#look up documentaion
        #for domain in self.domainlist:
        #    return str(self.nmap[domain])

