"""1. Создать 3 html формы (можно взять из выполненного дз к 13-му вебинару): главная
страницы, страница с парсером, данные о вас.
2. Наполнение главной страницы и страницы с данными оставить на Ваше усмотрение.
3. На странице с парсером реализовать интерфейс с пользователем. Например, по
нажатию кнопки осуществляется парсинг выбранного Вами портала, после чего
выводится некоторая информация о результатах парсинга.

Выполнить Light со следующим изменением: вместо страницы с парсером
реализовать страницу определения основных навыков по определенным
вакансиям (взаимодействие с hh api). Например, на странице представлена форма:
город, название вакансии, кнопка. По нажатию пользователю будет показана
средняя ЗП по данной вакансии в этом городе и список релевантных навыков
(бекэнд взять из 12-го вебинара).
"""
from pprint import pprint
import time
import requests
import json
import sqlite3
from sqlite3 import Error



# Подключаемся к базе (создаем базу)
connect = None

try:
    connect = sqlite3.connect('test_staff.db')
    cur = connect.cursor()
except sqlite3.Error as e:
    print(f"Error {e.args[0]}:")


# создадим таблицу с уникальным столбцом
cur.execute("CREATE TABLE staff(id INTEGER UNIQUE, name TEXT, area TEXT, created_at TEXT,"
            " published_at TEXT, employer TEXT,salary TEXT, schedule TEXT, snippet TEXT, url TEXT)")



ses = requests.Session()
ses.headers = {'HH-User-Agent': "Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/10.0"}
all_salaries = 0
all_num = 0
all_words = 0

list_of_vacancies = []
for i in range(500):
    url = 'https://api.hh.ru/vacancies'
    result = requests.get(url, params={'text': 'специалист по качеству', 'area': '1', 'per_page': 1, 'page' : i})
    list_of_vacancies.append(result.json())

# with open('list_of_vacancies.json', 'w') as f:
#     json.dump(list_of_vacancies, f)

# pprint(list_of_vacancies[0])

# list_of_vacancies = json.load(open('list_of_vacancies.json'))

for i in list_of_vacancies:
    for i in i['items']:
        id = i['id']
        name = str(i['name'])
        area = str(i['area'])
        created_at = str(i['created_at'])
        published_at = str(i['published_at'])
        employer = str(i['employer'])
        salary = str(i['salary'])
        schedule = str(i['schedule'])
        snippet = str(i['snippet'])
        url = str(i['url'])
        print(id, name, area, created_at, published_at, employer, salary, schedule, snippet, url)
        # Opens a file called measurements
        connect = sqlite3.connect('test_staff.db')
        cursor = connect.cursor()
        # Insert the values into the table
        cursor.execute('''INSERT OR IGNORE INTO staff(id, name, area, created_at, published_at, employer, salary, schedule, snippet, url ) VALUES(?,?,?,?,?,?,?,?,?,?)''',
                       (id, name, area, created_at, published_at, employer, salary, schedule, snippet, url ))
        # Commit the change
        connect.commit()
        connect.close()



def get_last_data():
    while True:
        try:
            db = sqlite3.connect('/home/pi/measurements_v2')
            cursor = db.cursor()
            cursor.execute("SELECT * FROM My_all ORDER BY ROWID DESC LIMIT 1")
            rows = cursor.fetchall()
            for row in rows:
                dtg = row[0]
                sun = row[1]
                temp = row[2]
                hum = row[3]
                vibro = row[4]
                co_gas = row[5]
                h2_gas = row[6]
                ch4_gas = row[7]
                lpg_gas = row[8]
                propane_gas = row[9]
                alcohol_gas = row[10]
                smoke_gas = row[11]
            time.sleep(1)
            return dtg, sun, temp, hum, vibro, co_gas, h2_gas, ch4_gas, lpg_gas, propane_gas, alcohol_gas, smoke_gas
        except (RuntimeError, TypeError, NameError):
            pass
