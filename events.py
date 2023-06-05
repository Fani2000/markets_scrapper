import requests
import json
from bs4 import BeautifulSoup

class Events:
    """
    * Allows you to the current events 
    """
    def __init__(self, url) -> None:
       self.CLASSES = ["eventon_events_list"] 
       self.url = url
       self.content = []
       self.soup = None

    def get_soup(self):
       res = requests.get(self.url, headers={'content-type': 'application/json'})
       self.content = res.content
       self.soup = BeautifulSoup(self.content, features="html.parser")
     
    def get_events(self):
        self.get_soup()
        # self.events = self.soup.css.select(f".{self.CLASSES[0]}")
        self.events = self.soup.find_all('a')
        for event in self.events:
            url = event.get('href') or ""
            if 'co.za/markets/' in url:
                self.save_events('./data/markets_url.txt',url)
            if '/category/' in url:
                self.save_events('./data/categories_url.txt', url)
            if '/market-days/' in url:
                self.save_events('./data/market_days.txt', url)
            if '/market-types/' in url:
                self.save_events('./data/market_types.txt', url)
                
    def save_events(self,file, url):
        with open(file, '+a') as file:
            file.write(url)
            file.write('\n')

    def get_event_details(self, url):
        pass
