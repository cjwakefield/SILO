import json
import sys
import argparse 
from  Harvester import Harvester
from  Harvester_Other import Harvester_Other
from  Harvester_API import Harvester_API

import socket

class Silo(object):   

    def __init__(self): 
        #global vars
        self.harvesters = []

        #get the CMD arguemnts
        parser = argparse.ArgumentParser(description='Silo')
        parser.add_argument("-v" ,"--verbosity", help="increase output verbosity")
        parser.add_argument("-a" ,"--active",action='store_true', help="active nmap scan of domain")
        parser.add_argument("-d" ,"--domain", help="the doamin that will be scanned",required=True)

        self.args = parser.parse_args()
        print(self.args)

        #get the API KEY
        with open('APIKEY.json') as f:
            self.keys = json.load(f)
            print(self.keys)

        #check to see if domain is up
        try:
            self.ip = socket.gethostbyname(self.args.domain)   
        except:
            print("The Domain provided does not resolve\n")

        #add the needed harvesters
        if(self.args.active != 1):
            self.harvesters.append(Harvester())

        self.Harvest() 

    def Harvest(self): 
        for harvester  in self.harvesters:
            harvester.get_data()


if __name__ == "__main__":
   Silo()