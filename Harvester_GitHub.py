import Harvester
from github import Github
from rich.console import Console
from rich.table import Table

class Harvester_GitHub(Harvester.Harvester): 
    def __init__(self,domain, API_KEY):
        self.g = Github(API_KEY)
        self.domain = domain

    def get_data(self):
        self.repos = self.g.search_repositories(query=self.domain)

    def formated_data(self):
        returnList = []
        for repo in self.repos:
            returnList.append(repo.full_name)
        return returnList
    
    def structured_data(self):
        table = Table(title="GitHub Repos" ,show_header=True, header_style="bold green")
        table.add_column("Repos")
        for repo in self.repos:
            table.add_row(str(repo.full_name))
        return table

    def __str__(self): 
        return self.structured_data()

