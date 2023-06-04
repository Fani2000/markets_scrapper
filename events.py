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
        self.events = self.soup.css.select(f".{self.CLASSES[0]}")

        for event in self.events:
            schema = list(event.children)[0]
            # soup = BeautifulSoup(schema, features="html.parser")
            print(self.soup)
            
            # print(schema.css.select('.desc_trig_outter'))
            


    def get_event_details(self):
        pass

    def save_events(self):
        pass