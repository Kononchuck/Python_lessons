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
