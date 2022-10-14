import json
import time
import requests
import pprint


ses = requests.Session()
ses.headers = {'HH-User-Agent': "Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/10.0"}

all_salaries = 0
all_num = 0
all_words = 0

"""Закомментированный код используется один раз для получения информации с HH"""
list_of_vacancies = []
for i in range(100):
    url = 'https://api.hh.ru/vacancies'
    result = requests.get(url, params={'text': 'Специалист в области качества', 'area': '1', 'per_page': 1, 'page' : i})
    list_of_vacancies.append(result.json())
print(type(list_of_vacancies))


"""Сохраняем данные для локальной работы"""
with open('vacancies.txt', 'w') as outfile:
    json.dump(list_of_vacancies, outfile)


"""Открываем с локального ресурса"""
with open('vacancies.txt') as json_file:
    list_of_vacancies = json.load(json_file)


"""                                                                          
1. Используя HH API, рассчитать среднюю зарплату в Москве по запросу "Python"
2. Составить список релевантных навыков по вакансиям Python-разработчик.     
Алгоритм решения примерно следующий:                                         
● получаем список вакансий;                                                  
● очищаем тексты описания вакансий и требования вакансий;                    
● составляем список релевантных навыков (python, django, sql и т.д.);        
● считаем частоту появления ключевых слов в текстах вакансий;                
● выводим ТОП-10 навыков и процент их встречаемости пользователю."""


for i in list_of_vacancies:
    y = i['items']
    num = 0
    sum_salaries = 0
    for i in y:
        if i['salary'] !=None:
            salary = i['salary']
            if salary['from'] !=None:
                num += 1
                salary['from']
                sum_salaries += salary['from']
    all_salaries += sum_salaries
    all_num += num
average_salary = all_salaries/all_num
average_salary = float('{:.2f}'.format(average_salary))
print("Средняя заработная плата по Москве (рубли): ", average_salary)


tags_list_vac = []
for i in list_of_vacancies:
    for i in i['items']:
        vac_id = i['id']
        vac_res = ses.get(f'https://api.hh.ru/vacancies/{vac_id}')
        if len(vac_res.json()["key_skills"]) > 0:  # at least one skill present
            # print(vac_id)
            tags = [v for v_dict in vac_res.json()["key_skills"] for _, v in v_dict.items()]
            # print(' '.join(tags))
            tags_list_vac.append(tags)
            # print()
            """Сохраняем данные для локальной работы"""
            with open('tags_list_vac.txt', 'w') as outfile:
                json.dump(tags_list_vac, outfile)
        time.sleep(0.1)

# with open('tags_list_vac.txt') as json_file:
#     tags_list_vac = json.load(json_file)


counts = dict()
for sublist in tags_list_vac:
    for x in sublist:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1

print("Выводим ТОП-10 навыков и процент их встречаемости: ", sorted(counts.items(), reverse=True, key=lambda x: x[1])[0:20])