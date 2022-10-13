"""1. Создайте во Flask-проекте новую ветку.
2. Настройте связь проекта с SqLite бд.
Результаты активной работы веб-приложения (например, результаты парсинга, результаты запроса к API) сохраняйте в бд.
3. Создайте форму, позволяющую добавлять новые данные в бд.


2. Сделайте выборку данных (пользователь, просматривая результаты, уже выбирает данные из базы)
3. Также можно добавить любой дополнительный функционал по желанию

"""
import pprint
import requests
from flask import Flask, render_template, request
import json
import sqlite3
from sqlite3 import Error
'''
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
'''




app = Flask(__name__)


@app.route('/')
@app.route('/main')
def hello_world():
     #return 'Hello, World!'
     return render_template('main.html')


@app.route('/contacts')
def motos():
     return render_template('contacts.html')



@app.route('/form', methods = ['POST'])
def form():
    ses = requests.Session()
    ses.headers = {'HH-User-Agent': "Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/10.0"}
    all_salaries = 0
    all_num = 0
    all_words = 0
    request_hh = request.form['request_HH']
    list_of_vacancies = []
    for i in range(500):
        url = 'https://api.hh.ru/vacancies'
        result = requests.get(url, params={'text': request_hh, 'area': '1', 'per_page': 1, 'page' : i})
        if i == result:
            list_of_vacancies.append(result.json())
        else:
            pass
    # добавляем данные в базу
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
            # print(id, name, area, created_at, published_at, employer, salary, schedule, snippet, url)
            # Opens a file called
            connect = sqlite3.connect('test_staff.db')
            cursor = connect.cursor()
            # Insert the values into the table
            cursor.execute(
                '''INSERT OR IGNORE INTO staff(id, name, area, created_at, published_at, employer, salary, schedule, snippet, url ) VALUES(?,?,?,?,?,?,?,?,?,?)''',
                (id, name, area, created_at, published_at, employer, salary, schedule, snippet, url))
            # Commit the change
            connect.commit()
            connect.close()
    for i in list_of_vacancies:
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
    average_salary = all_salaries/all_num
    average_salary = float('{:.2f}'.format(average_salary))
    tags_list_vac = []
    for i in list_of_vacancies:
        for i in i['items']:
            vac_id = i['id']
            vac_res = ses.get(f'https://api.hh.ru/vacancies/{vac_id}')
            if len(vac_res.json()["key_skills"]) > 0:  # at least one skill present
                tags = [v for v_dict in vac_res.json()["key_skills"] for _, v in v_dict.items()]
                tags_list_vac.append(tags)
    counts = dict()
    for sublist in tags_list_vac:
        for x in sublist:
            if x in counts:
                counts[x] += 1
            else:
                counts[x] = 1
    top_skills = sorted(counts.items(), reverse=True, key=lambda x: x[1])[0:10]
    data = {
            'user_request': request_hh,
            'model': average_salary,
            'user_skills': top_skills}
    return render_template('form.html', data=data)


if __name__ == "__main__":
    app.run(debug = False)

