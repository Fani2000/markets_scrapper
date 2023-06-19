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
       self.markets = []

    def get_soup(self):
       res = requests.get(self.url, headers={'content-type': 'application/json'})
       self.content = res.content
       self.soup = BeautifulSoup(self.content, features="html.parser")
     
    def get_events_links(self):
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

    def event_details(self,url):
            res = requests.get(url, headers={'content-type': 'application/json'})
            content = res.content
            soup = BeautifulSoup(content, features="html.parser")
            main_content = soup.find("div", {"class": "main-content"})

            related_posts_containers = soup.find('section', {"class": "related-posts"})
            related_posts = related_posts_containers.find_all("a", {"class": "image-link"})
            related_urls = [url.get('href') for url in related_posts]


            print('Event Information====================================================================')
            # print(main_content)
            header_text = main_content.find('div', {"class": "the-post-header"}).get_text().split('\n')[4]
            featured_image_url = main_content.find('a', {"class": "image-link"}).get('href')
            post_details = main_content.find('div', {"class": "post-content"}).get_text().split('\n')

            market = {
                "title": header_text,
                "image": featured_image_url,
                "content": post_details
            }

            self.markets.append(market)

            with open('./data/markets.json', '+a') as f: 
                _markets = json.dumps(self.markets)
                f.write(_markets)
                # pass

            # print(related_urls)
            for url in related_urls:
                # print(url)
                self.save_events('./data/markets_url.txt',url)
            # print('Event_inforamtion',header_text, featured_image_url, post_details)

    def get_events(self):
        print('events......')
        with open('data/markets_url.txt', '+r') as file:
            urls = file.read().split('\n')
            urls.pop()

            for url in urls:
                self.event_details(url)

    def save_events(self,file, url):
        with open(file, '+a') as file:
            file.write(url)
            file.write('\n')

    def get_event_details(self, url):
        pass
