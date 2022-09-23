"""
2. создать простейшего чат-бота в Telegram
3. обработать ответы не менее, чем на 3 фразы и 3 команды.
1. реализовать чат-бота с некоторой логикой. Например, можно реализовать чат-бота:
● еженедельник (можно вносить планы, спрашивать бота что по плану на завтра и т.д.).
● чат-бот по контролю расходов (вносите покупки, их стоимость, чат-бот сортирует по категориям затрат, выводит статистику за период и т.д.).
● чат-бот для заказа еды.
"""
import csv
import json
import telebot
import requests
from pprint import pformat
import pprint
from bs4 import BeautifulSoup
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
bot = telebot.TeleBot('5716230886:AAHaofAizle1XCPd_30envWpVqhpI6P36jA')


# @bot.message_handler(commands=['start'])
# def start(message):
#     mess = f"Привет, <b>{message.from_user.first_name} {message.from_user.last_name}" \
#            f" напиши - зарплата или - навыки, и получишь информацию о средней з\п специалиста по качеству и топ " \
#            f"навыков требуемых для специальности.</b>"
#     bot.send_message(message.chat.id, mess, parse_mode='html')
#
#
# @bot.message_handler(content_types=['text'])
# def get_text(message):
#     all_salaries = 0
#     all_num = 0
#     with open('vacancies_qms.txt') as json_file:
#         list_of_vacancies_qms = json.load(json_file)
#     for i in list_of_vacancies_qms:
#         y = i['items']
#         num = 0
#         sum_salaries = 0
#         for i in y:
#             if i['salary'] != None:
#                 salary = i['salary']
#                 if salary['from'] != None:
#                     num += 1
#                     salary['from']
#                     sum_salaries += salary['from']
#         all_salaries += sum_salaries
#         all_num += num
#     average_salary = all_salaries / all_num
#     average_salary = float('{:.2f}'.format(average_salary))
#     with open('tags_list_vac_qms.txt') as json_file:
#         tags_list_vac_qms = json.load(json_file)
#     counts = dict()
#     for sublist in tags_list_vac_qms:
#         for x in sublist:
#             if x in counts:
#                 counts[x] += 1
#             else:
#                 counts[x] = 1
#         ans_0 = average_salary
#         mess_0 = f"Средняя заработная плата специалистов по качеству в Москве (рубли): {ans_0}"
#     if message.text == 'зарплата':
#         bot.send_message(message.chat.id, mess_0, parse_mode='html')
#     elif message.text == 'навыки':
#         ans_1 = sorted(counts.items(), reverse=True, key=lambda x: x[1])[0:10]
#         mess = f"Выводим ТОП-10 навыков и процент их встречаемости: {ans_1}"
#         bot.send_message(message.chat.id, mess)
#     else:
#         bot.send_message(message.chat.id, 'я не понял', parse_mode='html')
#
#
# bot.polling(none_stop=True)


rostec_all = []
url_rostec = "http://www.rostec.ru"
r_rostec = requests.get(url_rostec, headers=headers)
soup_rostec = BeautifulSoup(r_rostec.content, "html.parser")
headlines_rostec = soup_rostec.find_all('span', class_='text')
for i in range(len(headlines_rostec)):
    rostec_all.append(headlines_rostec[i].text)

# news = rostec_all..splitlines( )

print(rostec_all)
# print(news)