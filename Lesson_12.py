import json

import requests
import pprint

# #https://github.com/hhru/api/blob/master/docs/vacancies.md#search
# #https://github.com/hhru/api
"""
1. Используя HH API, рассчитать среднюю зарплату в Москве по запросу "Python"
2. Составить список релевантных навыков по вакансиям Python-разработчик.
Алгоритм решения примерно следующий:
● получаем список вакансий;
● очищаем тексты описания вакансий и требования вакансий;
● составляем список релевантных навыков (python, django, sql и т.д.);
● считаем частоту появления ключевых слов в текстах вакансий;
● выводим ТОП-10 навыков и процент их встречаемости пользователю."""


all_salaries = 0
all_num = 0
all_words = 0


# list_of_vacancies = []
# for i in range(100):
#     url = 'https://api.hh.ru/vacancies'
#     result = requests.get(url, params={'text': 'Python', 'area': '1', 'per_page': 1, 'page' : i})
#     list_of_vacancies.append(result.json())
# with open('vacancies.txt', 'w') as outfile:
#     json.dump(list_of_vacancies, outfile)

"""Сохраняем данные для локальной работы"""
with open('vacancies.txt') as json_file:
    list_of_vacancies = json.load(json_file)



# for i in list_of_vacancies:
#     y = i['items']
#     num = 0
#     sum_salaries = 0
#     for i in y:
#         if i['salary'] !=None:
#             salary = i['salary']
#             if salary['from'] !=None:
#                 num += 1
#                 salary['from']
#                 sum_salaries += salary['from']
#     all_salaries += sum_salaries
#     all_num += num
# average_salary = all_salaries/all_num

for i in list_of_vacancies:
    y = i['items']
    num = 0
    sum_salaries = 0
    for i in y:
        if i['snippet'] == 'MongoDB':
            num += 1
    all_words += num
print(all_words)




# print(average_salary)
#pprint.pprint(list_of_vacancies[20])


#
# for i in list_of_vacancies['items']:
#     print('requirement': + 'Django')
#
#
# for p in data['people']:
#         print('Name: ' + p['name'])
#         print('Website: ' + p['website'])
#         print('From: ' + p['from'])
#         print('')