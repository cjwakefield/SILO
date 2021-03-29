import Harvester
from extract_emails import EmailExtractor
from extract_emails.browsers import ChromeBrowser
from googlesearch import search
from bs4 import BeautifulSoup
import urllib
import re
import theharvester

class Harvester_Email(Harvester.Harvester): 
    def __init__(self,domain):
        self.domain = domain

    def get_email(self, url):
        try:
            thepage = urllib.request.urlopen(url)
            list = []
            if(thepage.getcode() == 200):
                    regx = "[a-z0-9]+@" + self.domain
                    list = re.findall(regx, str(thepage.read().decode("utf-8")) )
        except ValueError:
            list = []
        
        return list

    def get_data(self):
        q = "intext:\"*@"+self.domain+"\""
        for result in search(q, num=10, stop=10, pause=2):
            print(result)
            print(str(self.get_email(result)))
        

    def formated_data(self):
        return str(self)
    
    def structured_data(self):
        return str(self)

    def __str__(self): 
        return ""

