import json
import sys
import argparse 
import socket
from rich.console import Console

import Harvester
import Harvester_Nmap
import Harvester_DNSDumpster
import Harvester_Email
import Harvester_GitHub
import Harvester_Ipstack

class Silo(object):   

    def __init__(self): 
        #global vars
        self.harvesters = []

        #get the CMD arguemnts
        parser = argparse.ArgumentParser(description='Silo')
        parser.add_argument("-v" ,"--verbosity", help="increase output verbosity")
        parser.add_argument("-a" ,"--active",action='store_true', help="active nmap scan of domain")# add a al flag that goes off of a and will scan every domain
        parser.add_argument("-d" ,"--domain", help="the domain that will be scanned",required=True)

        self.args = parser.parse_args()
        #print(self.args)

        #get the API KEY
        with open('APIKEY.json') as f:
            self.keys = json.load(f)
            #print(self.keys)

        #check to see if domain is up
        try:
            self.ip = socket.gethostbyname(self.args.domain)   
        except:
            print("The Domain provided does not resolve\n")
            exit(1)

        #append the harvesters based of the argument inputs
        self.Append_Harvester_Lists()
        #go out and harvest the data
        self.Harvest()

    def Append_Harvester_Lists(self):

        if self.keys.get("API_KEY_IPSTACK") != "":
            self.harvesters.append(Harvester_Ipstack.Harvester_Ipstack(self.args.domain , self.keys.get("API_KEY_IPSTACK")))

        Dns_Dumpster = Harvester_DNSDumpster.Harvester_DNSDumpster(self.args.domain)
        self.scanDomainList = Dns_Dumpster.formated_data()
        self.harvesters.append(Dns_Dumpster)

        #add the needed harvesters
        if(self.args.active == 1):
            tmp =  Harvester_Nmap.Harvester_Nmap([self.args.domain])
            self.harvesters.append(tmp)

        if self.keys.get("API_HUNTER") != "":
            self.harvesters.append(Harvester_Email.Harvester_Email(self.args.domain , self.keys.get("API_HUNTER")))
               

        if self.keys.get("API_KEY_GIT_HUB") != "":
            self.harvesters.append(Harvester_GitHub.Harvester_GitHub(self.args.domain , self.keys.get("API_KEY_GIT_HUB")))
             
    def Harvest(self): 
        console = Console()
        for harvester in self.harvesters:
            harvester.get_data()
        
        for harvester  in self.harvesters:
            print(harvester.structured_data())
            #harvester.structured_data(); 


if __name__ == "__main__":
   Silo()