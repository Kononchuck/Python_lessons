#
# import time
# import os
# from selenium import webdriver
# from bs4 import BeautifulSoup

# # put the driver in the folder of this code
# driver = webdriver.Chrome(os.getcwd() + '/chromedriver')
#
# driver.get("https://www.bloomberg.com/quote/IBVC:IND")
# time.sleep(3)
# real_soup = BeautifulSoup(driver.page_source, 'html.parser')
# open_ = real_soup.find("span", {"class": "priceText__1853e8a5"}).text
# print(f"Price: {open_}")
# time.sleep(3)
# driver.quit()




import os
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from time import sleep
from random import randint

driver = webdriver.Chrome(os.getcwd() + '/chromedriver')

url = "http://www.rostec.ru"
driver.get(url)
sleep(randint(3, 5))

soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()

links = soup.find_all("a")
top10 = set()
for link in links:
    top10.add(link.get("href"))
for link in top10:
    print(link)

