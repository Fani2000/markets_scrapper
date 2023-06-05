html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

# from bs4 import BeautifulSoup

# soup = BeautifulSoup(html_doc, 'html.parser')

# print(soup.title, soup.title.string)

# print(soup.find('a'), soup.find('a').get('href'))
# print(soup.find_all('a'))

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By

# driver = webdriver.Firefox()

# driver.get("http://www.python.org")

# elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)

# driver.implicitly_wait(120)
# driver.close()