import requests
import pprint

#https://github.com/hhru/api/blob/master/docs/vacancies.md#search
#https://github.com/hhru/api
#
# domain = 'https://api.hh.ru/'
#
# url_vac = f'{domain}vacancies'
#
# params = {
#     'text': 'python developer',
#     # page
#     'page': 100
# }
#
# result = requests.get(url_vac, params=params)
#
# # items = result['items']
# #
# # first = items[0]
#
# #print(result.status_code)
#
# # data = result.json()
# pprint.pprint(result.json())
# # pprint.pprint(first)
# # print(first['name'])
# # print(first['schedule'])
# # print(first['salary'])
"""
1. Используя HH API, рассчитать среднюю зарплату в Москве по запросу "Python"
2. Составить список релевантных навыков по вакансиям Python-разработчик.
Алгоритм решения примерно следующий:
● получаем список вакансий;
● очищаем тексты описания вакансий и требования вакансий;
● составляем список релевантных навыков (python, django, sql и т.д.);
● считаем частоту появления ключевых слов в текстах вакансий;
● выводим ТОП-10 навыков и процент их встречаемости пользователю."""

list_of_vacancies = []
all_salaries = 0
all_num = 0

for i in range(100):
    url = 'https://api.hh.ru/vacancies'
    result = requests.get(url, params={'text': 'python developer', 'area': '1', 'page' : i})
    list_of_vacancies.append(result.json())

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


print(average_salary)
pprint.pprint(list_of_vacancies[0])