import requests
from bs4 import BeautifulSoup
import csv
import re


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}


cnbc_all = []
url = "https://www.cnbc.com/world/?region=world"
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, "html.parser")
headlines = soup.find_all('div',{'class':'LatestNews-headlineWrapper'})
len(headlines)
for i in range(len(headlines)):
    cnbc_all.append(headlines[i].text)
    # print(headlines[i].text)

cnbc_all = [w.replace('Ago', '') for w in cnbc_all]
for i in cnbc_all:
    print(i)


cgnt_all = []
url_cgnt = "https://www.cgtn.com/"
r_cgnt = requests.get(url_cgnt, headers=headers)
soup_cgnt = BeautifulSoup(r_cgnt.content, "html.parser")
headlines_cgnt = soup_cgnt.find_all('div',{'class':'shortheadline'})
len(headlines_cgnt)
for i in range(len(headlines_cgnt)):
    cgnt_all.append(headlines_cgnt[i].text)
    print(headlines_cgnt[i].text)


rostec_all = []
url_rostec = "http://www.rostec.ru"
r_rostec = requests.get(url_rostec, headers=headers)
soup_rostec = BeautifulSoup(r_rostec.content, "html.parser")
headlines_rostec = soup_rostec.find_all('span', class_='text')
for i in range(len(headlines_rostec)):
    rostec_all.append(headlines_rostec[i].text)
    print(headlines_rostec[i].text)


with open('parse_news.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(cnbc_all)
    writer.writerow(cgnt_all)
    writer.writerow(rostec_all)


with open('parse_news_txt.txt', 'w') as f:
    f.write('\n'.join(cnbc_all))
    f.write('\n'.join(cgnt_all))
    f.write('\n'.join(rostec_all))
