"""
2. создать простейшего чат-бота в Telegram
3. обработать ответы не менее, чем на 3 фразы и 3 команды.
1. реализовать чат-бота с некоторой логикой. Например, можно реализовать чат-бота:
● еженедельник (можно вносить планы, спрашивать бота что по плану на завтра и т.д.).
● чат-бот по контролю расходов (вносите покупки, их стоимость, чат-бот сортирует по категориям затрат, выводит статистику за период и т.д.).
● чат-бот для заказа еды.
"""
import json
import telebot
import csv
from telebot import types
import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime
from multiprocessing import Process
import threading
import re
import yfinance as yf

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}

bot = telebot.TeleBot('____________________________________')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f"Привет, {message.from_user.first_name} {message.from_user.last_name} выбирай новости!"
    markup = types.ReplyKeyboardMarkup(row_width=5)
    itembtn1 = types.KeyboardButton('Ростех')
    itembtn2 = types.KeyboardButton('CNBC')
    itembtn3 = types.KeyboardButton('Chinadaily')
    itembtn4 = types.KeyboardButton('Eweek')
    itembtn5 = types.KeyboardButton('Scitechdaily')
    itembtn6 = types.KeyboardButton('Skiencedaily')
    itembtn7 = types.KeyboardButton('Валюты')
    itembtn8 = types.KeyboardButton('Рынки')
    itembtn9 = types.KeyboardButton('Финансовые')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6, itembtn7, itembtn8, itembtn9)
    msg = bot.reply_to(message, mess, reply_markup=markup)
    # bot.send_message(message.chat.id, mess, reply_markup=markup, parse_mode='html')
    # bot.register_next_step_handler(msg, process_step)

@bot.message_handler(content_types=['text'])
def get_text(message):
    all_salaries = 0
    all_num = 0
    with open('vacancies_qms.txt') as json_file:
        list_of_vacancies_qms = json.load(json_file)
    for i in list_of_vacancies_qms:
        y = i['items']
        num = 0
        sum_salaries = 0
        for i in y:
            if i['salary'] != None:
                salary = i['salary']
                if salary['from'] != None:
                    num += 1
                    salary['from']
                    sum_salaries += salary['from']
        all_salaries += sum_salaries
        all_num += num
    average_salary = all_salaries / all_num
    average_salary = float('{:.2f}'.format(average_salary))
    with open('tags_list_vac_qms.txt') as json_file:
        tags_list_vac_qms = json.load(json_file)
    counts = dict()
    for sublist in tags_list_vac_qms:
        for x in sublist:
            if x in counts:
                counts[x] += 1
            else:
                counts[x] = 1
        ans_0 = average_salary
        mess_0 = f"Средняя заработная плата специалистов по качеству в Москве (рубли): {ans_0}"
    if message.text == 'зарплата':
        bot.send_message(message.chat.id, mess_0, parse_mode='html')
    elif message.text == 'навыки':
        ans_1 = sorted(counts.items(), reverse=True, key=lambda x: x[1])[0:10]
        mess = f"Выводим ТОП-10 навыков и процент их встречаемости: {ans_1}"
        bot.send_message(message.chat.id, mess)
    elif message.text=='Ростех':
        # todo open from csv file and set in rostec_news()
        rostec_all = []
        url_rostec = "http://www.rostec.ru"
        r_rostec = requests.get(url_rostec, headers=headers, timeout=10)
        soup_rostec = BeautifulSoup(r_rostec.content, "html.parser")
        headlines_rostec = soup_rostec.find_all('span', class_='text')
        for i in range(len(headlines_rostec)):
            rostec_all.append(headlines_rostec[i].text)
        news = (''.join(rostec_all))
        mess = f"{news}"
        bot.send_message(message.chat.id, mess, parse_mode='html')
    elif message.text == 'Chinadaily':
        chinadaily_all = []
        url = "https://www.chinadaily.com.cn/china/governmentandpolicy"
        r = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(r.content, "html.parser")
        headlines = soup.find_all('span', {'class': 'tw3_01_2_t'})
        len(headlines)
        for i in range(len(headlines)):
            chinadaily_all.append(headlines[i].text)
        news = (''.join(chinadaily_all))
        mess = f"{news}"
        bot.send_message(message.chat.id, mess, parse_mode='html')
    elif message.text == 'CNBC':
        cnbc_all = []
        url = "https://www.cnbc.com/world/?region=world"
        r = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(r.content, "html.parser")
        headlines = soup.find_all('div', {'class': 'LatestNews-headlineWrapper'})
        len(headlines)
        for i in range(len(headlines)):
            cnbc_all.append(headlines[i].text)
        news = ('\n''\n'.join(cnbc_all))
        news = news.replace('Ago', ' ')
        mess = f"{news}"
        bot.send_message(message.chat.id, mess, parse_mode='html')
    elif message.text == 'Eweek':
        eweek_all = []
        url = "https://www.eweek.com/"
        r = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(r.content, "html.parser")
        headlines = soup.find_all('h3', {'class': 'entry-title td-module-title'})
        len(headlines)
        for i in range(len(headlines)):
            eweek_all.append(headlines[i].text)
        news = ('\n''\n'.join(eweek_all))
        mess = f"{news}"
        bot.send_message(message.chat.id, mess, parse_mode='html')
    elif message.text == 'Scitechdaily':
        ski_all = []
        url = "https://scitechdaily.com/"
        r = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(r.content, "html.parser")
        headlines = soup.find_all('h3', {'class': 'cp-title-small'})
        len(headlines)
        for i in range(len(headlines)):
            ski_all.append(headlines[i].text)
        news = ('\n''\n'.join(ski_all))
        mess = f"{news}"
        bot.send_message(message.chat.id, mess)
    elif message.text == 'Skiencedaily':
        skiencedaily_all = []
        url = "https://www.sciencedaily.com"
        r = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(r.content, "html.parser")
        headlines = soup.find_all('div', {'class': 'sidebar-headline clearfix'})
        len(headlines)
        for i in range(len(headlines)):
            skiencedaily_all.append(headlines[i].text)
        news = ('\n''\n'.join(skiencedaily_all))
        mess = f"{news}"
        bot.send_message(message.chat.id, mess, parse_mode='html')
    elif message.text == 'Валюты':
        data_1 = yf.Tickers('BTC-USD EURUSD=X GC=F SI=F CL=F')
        news = data_1.history(period='Last')['Close']
        mess = f"{news}"
        bot.send_message(message.chat.id, mess, parse_mode='html')
    elif message.text == 'Рынки':
        data_2 = yf.Tickers('NQ=F YM=F ES=F ^FTSE ^GDAXI ^N225')
        news = data_2.history(period='Last')['Close']
        mess = f"{news}"
        bot.send_message(message.chat.id, mess, parse_mode='html')
    else:
        bot.send_message(message.chat.id, 'я не понял', parse_mode='html')




bot.polling(none_stop=True)