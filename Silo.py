import json
import sys
import argparse 
import socket

import Harvester
import Harvester_Nmap
import Harvester_DNSDumpster



class Silo(object):   

    def __init__(self): 
        #global vars
        self.harvesters = []

        #get the CMD arguemnts
        parser = argparse.ArgumentParser(description='Silo')
        parser.add_argument("-v" ,"--verbosity", help="increase output verbosity")
        parser.add_argument("-a" ,"--active",action='store_true', help="active nmap scan of domain")
        parser.add_argument("-d" ,"--domain", help="the doamin tha  t will be scanned",required=True)

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
            exit(1)

        #add the needed harvesters
        if(self.args.active == 1):
            tmp =  Harvester_Nmap.Harvester_Nmap([self.args.domain])
            self.harvesters.append(tmp)

        self.harvesters.append(Harvester_DNSDumpster.Harvester_DNSDumpster(self.args.domain))

        self.Harvest()

    def Harvest(self): 
        for harvester in self.harvesters:
            harvester.get_data()
        
        for harvester  in self.harvesters:
            print(harvester)



if __name__ == "__main__":
   Silo()