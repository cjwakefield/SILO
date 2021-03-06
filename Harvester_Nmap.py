import nmap 
import Harvester
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

class Harvester_Nmap(Harvester.Harvester): 
    def __init__(self,domainlist):
        self.domainlist = domainlist
        self.nmap = nmap.PortScanner()
        self.get_data()
        
    def get_data(self, ports='21-443'):
        for domain in self.domainlist:
            self.nmap.scan(domain, ports)

    def formated_data(self):
        nmapList = []
        for domain in self.nmap.all_hosts():
            nmapList.append(str(self.nmap[domain]))
        return nmapList
    
    def structured_data(self):
        for domain in self.nmap.all_hosts():
            results = self.nmap[domain]
        return Panel(str(results))

    def __str__(self): 
        #return str([str(self.nmap[domain]) for domain in self.domainlist])#look up documentaion
        return str(self.formated_data())
        #for domain in self.domainlist:
        #    return str(self.nmap[domain])

