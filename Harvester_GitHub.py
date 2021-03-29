import Harvester
from github import Github

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
        return str(self.formated_data())

    def __str__(self): 
        return self.structured_data()

