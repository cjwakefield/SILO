from dnsdumpster.DNSDumpsterAPI import DNSDumpsterAPI
class Harvester_DNSDumpster(Harvest): 
    def __init__(self,domain):
        self.domain = domain 

    def get_data(self):
        self.res =  DNSDumpsterAPI({'verbose': True}).search('microsoft.com')

    def __str__(self): 
        print(res)
