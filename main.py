#!/usr/bin/env python3

from events import Events
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

urls = [
    "https://capemarkets.co.za/",
    "https://capemarkets.co.za/food-markets/",
    "https://capemarkets.co.za/craft-markets/",
    "https://capemarkets.co.za/night-markets/",
    "https://capemarkets.co.za/farmers-markets/",
    "https://capemarkets.co.za/popups-fairs-festivals/",
    "https://capemarkets.co.za/pet-friendly-markets/",
    "https://capemarkets.co.za/category/markets/market-types/vintage-antiques-collectibles-markets/",
    "https://capemarkets.co.za/cape-town-markets/",
    "https://capemarkets.co.za/category/markets/market-days/monday-markets-cape-town/",
    "https://capemarkets.co.za/category/markets/market-days/tuesday-markets-cape-town/",
    "https://capemarkets.co.za/category/markets/market-days/wednesday-markets/",
    "https://capemarkets.co.za/category/markets/market-days/thursday-markets/",
    "https://capemarkets.co.za/category/markets/market-days/friday-markets/",
    "https://capemarkets.co.za/saturday-markets/",
    "https://capemarkets.co.za/sunday-markets/",
    "https://capemarkets.co.za/category/markets/market-types/vintage-antiques-collectibles-markets/",
]


driver = webdriver.Chrome()
driver.get('https://www.python.org')

if __name__ == '__main__':
    # events = Events(urls[0]) 
    # events.get_events()
    

    print('Running')