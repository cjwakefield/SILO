import Harvester
from pyhunter import PyHunter
from rich.console import Console
from rich.table import Table

class Harvester_Email(Harvester.Harvester): 
    def __init__(self,domain,API_KEY):
        self.hunter = PyHunter(API_KEY)
        self.domain = domain
        self.get_data()       

    def get_data(self,limit=5, offset=2):
       self.json = self.hunter.domain_search(company=self.domain, limit=limit, offset=offset) # pass in the limit and offset

    def formated_data(self):
        return self.json
    
    def structured_data(self):
        table = Table(title="Domain Email Data" ,show_header=True, header_style="bold green")
        emails = self.json.get("emails")
        table.add_column("Email")
        table.add_column("FirstName")
        table.add_column("LastName")
        table.add_column("PhoneNumber")
        for email in emails:
            table.add_row(email.get("value"),email.get("first_name"),email.get("last_name"),email.get("phone_number"))
        return table

    def __str__(self): 
        return str(self.structured_data())

