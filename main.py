#!/usr/bin/env python3

import time
from events import Events

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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




# events = driver.find_element(By.CLASS_NAME, "eventon_events_list")
# upcoming_events_text = events.text

# with open('upcomingEvents.txt', "+w") as file:
#     file.write(title)
#     file.write(upcoming_events_text)


# driver.save_screenshot('snapshot.png')


if __name__ == '__main__':
    events = Events(urls[0]) 
    events.get_events()
    # driver = webdriver.Firefox()
    # driver.get(urls[0])
    # title = driver.title

    # links = driver.find_elements(By.TAG_NAME, 'a')
    # print(links)

    # driver.implicitly_wait(120)

    # links[3].click()


    # print(title)
    # print(driver.find_element(By.CLASS_NAME, "main-full").text)
    # print(driver.find_elements(By.TAG_NAME, "img"))
    # print(driver.find_elements(By.TAG_NAME, "a")[0])


    

    print('Running')