import requests
import os
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from time import sleep
from random import randint
import time
#
# driver = webdriver.Chrome(os.getcwd() + '/chromedriver')
#
# url = "http://www.rostec.ru"
# driver.get(url)
# sleep(randint(3, 5))
#
# soup = BeautifulSoup(driver.page_source, 'html.parser')
# driver.quit()
#
# links = soup.find_all("a")
# top10 = set()
# for link in links:
#     top10.add(link.get("href"))
# for link in top10:
#     print(link)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
# url = "http://www.rostec.ru"
# r = requests.get(url, headers=headers)
# soup = BeautifulSoup(r.content, "html.parser")
# headlines = soup.find_all('span',{'class':'text'})
# len(headlines)
# for i in range(len(headlines)):
#     print(headlines[i].text)

# url = "https://www.cnbc.com/world/?region=world"
# r = requests.get(url, headers=headers)
# soup = BeautifulSoup(r.content, "html.parser")
# headlines = soup.find_all('div',{'class':'LatestNews-headlineWrapper'})
# len(headlines)
# for i in range(len(headlines)):
#     print(headlines[i].text)

# url = "https://www.cgtn.com/"
# r = requests.get(url, headers=headers)
# soup = BeautifulSoup(r.content, "html.parser")
# headlines = soup.find_all('div',{'class':'shortheadline'})
# len(headlines)
# for i in range(len(headlines)):
#     print(headlines[i].text)

url = "https://www.bloomberg.com/markets"
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, "html.parser")
headlines = soup.find_all('a')
len(headlines)
for i in range(len(headlines)):
    print(headlines[i].text)
