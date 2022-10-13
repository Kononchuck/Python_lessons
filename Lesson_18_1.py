"""1. Создайте во Flask-проекте новую ветку.
2. Переписать backend с использованием моделей SQLAlchemy.
3. Сдать дз в виде ссылки на PullRequest.
"""
import requests
import sqlalchemy
from sqlalchemy import Column, Integer, String, Float, create_engine, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pprint
import requests
from flask import Flask, render_template, request
import json
import sqlite3
from sqlite3 import Error
import sys


"""
# 2.- Create your connection.
cnx = sqlite3.connect('/Users/den/PycharmProjects/Python_lessons/test_staff.db')
cursor = cnx.cursor()
# 3.- Query and print all the tables in the database engine
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())
# 4.-  READ TABLE OF SQLITE CALLED staff
dfN_check = pd.read_sql_query("SELECT * FROM staff", cnx) # we need real name of table
print(dfN_check)
# 7.- Close the connection with the database
cnx.close()

# создадим таблицу с уникальным столбцом
cur.execute("CREATE TABLE staff(id INTEGER UNIQUE, name TEXT, area TEXT, created_at TEXT,"
            " published_at TEXT, employer TEXT,salary TEXT, schedule TEXT, snippet TEXT, url TEXT)")
"""

from sqlalchemy import Column, Integer, String, Float, create_engine, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


ses = requests.Session()
ses.headers = {'HH-User-Agent': "Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/10.0"}

all_salaries = 0
all_num = 0
all_words = 0

"""Закомментированный код используется один раз для получения информации с HH"""
list_of_vacancies = []
for i in range(100):
    url = 'https://api.hh.ru/vacancies'
    result = requests.get(url, params={'text': 'специалист по качеству', 'area': '1', 'per_page': 1, 'page' : i})
    list_of_vacancies.append(result.json())
print(type(list_of_vacancies))


engine = create_engine('sqlite:///staff.db', echo=False)
Base = declarative_base()

class Staff(Base):
    __tablename__ = 'staff'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    area = Column(String)
    created_at = Column(String)
    published_at = Column(String)
    employer = Column(String)
    salary = Column(String)
    schedule = Column(String)
    snippet = Column(String)
    url = Column(String)

    def __init__(self, id, name, area, created_at, published_at, employer, salary, schedule, snippet, url):
        self.id = id
        self.name = name
        self.area = area
        self.created_at = created_at
        self.published_at = published_at
        self.employer = employer
        self.salary = salary
        self.schedule = schedule
        self.snippet = snippet
        self.url = url

    def __str__(self):
        return f'{self.name}, {self.area}, {self.created_at}, {self.published_at}, {self.schedule}, {self.snippet}, {self.url}'



if __name__ == '__main__':
    # Base.metadata.create_all(engine)
    Session_SQL = sessionmaker(bind=engine)
    session_SQL = Session_SQL()


#
# """Открываем с локального ресурса"""
# with open('vacancies.txt') as json_file:
#     list_of_vacancies = json.load(json_file)


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
        test = Staff(id, name, area, created_at, published_at, employer, salary, schedule, snippet, url)
        print(test)
        session_SQL.merge(test) # ignore and merge the same id
        session_SQL.commit()



# test = Staff(
#     id= 4646,
#     name = 'wrefgt',
#     area = 'wrefgt',
#     created_at = 'wrefgt',
#     published_at = 'wrefgt',
#     employer = 'wrefgt',
#     salary = 'wrefgt',
#     schedule = 'wrefgt',
#     snippet = 'wrefgt',
#     url = 'wrefgt')



#
# question = session.query(Staff)
#
# print(question)
#
# for i in question:
#     print(i)