"""1. Создайте во Flask-проекте новую ветку.
2. Переписать backend с использованием моделей SQLAlchemy.
3. Сдать дз в виде ссылки на PullRequest.

"""

import requests
from flask import Flask, render_template, request
from sqlalchemy import Column, Integer, String, Float, create_engine, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

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
    Session = sessionmaker(bind=engine)
    session_SQL = Session()


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
    for i in range(100):
        url = 'https://api.hh.ru/vacancies'
        result = requests.get(url, params={'text': request_hh, 'area': '1', 'per_page': 1, 'page' : i})
        list_of_vacancies.append(result.json())
        list_for_db = list_of_vacancies
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

    for i in list_for_db:
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
            session_SQL.merge(test)  # ignore and merge the same id
            session_SQL.commit()

    return render_template('form.html', data=data)


if __name__ == "__main__":
    app.run(debug = False)

