import json
import argparse 
class Silo(object):   

    def __init__(self): 
        #get the CMD arguemnts
        parser = argparse.ArgumentParser(description='Silo')
        parser.add_argument("-v" ,"--verbosity", help="increase output verbosity")
        parser.add_argument("-a" ,"--active", help="active nmap scan of domain")
        parser.add_argument("-d" ,"--domain", help="the doamin that will be scanned",required=True)

        args = parser.parse_args()
        print(args)

        #get the API KEY
        with open('APIKEY.json') as f:
            self.keys = json.load(f)
            print(self.keys)
        self.Harvest() 

    def Harvest(self): 
        pass


if __name__ == "__main__":
   Silo()