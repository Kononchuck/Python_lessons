import json
import time
import requests
import pprint


ses = requests.Session()
ses.headers = {'HH-User-Agent': "Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/10.0"}

all_salaries = 0
all_num = 0
all_words = 0
search_num = 0

"""Закомментированный код используется один раз для получения информации с HH"""
list_of_vacancies_qms = []
for i in range(100):
    url = 'https://api.hh.ru/vacancies'
    result = requests.get(url, params={'text': 'Quality manager', 'area': '1', 'per_page': 1, 'page' : i})
    list_of_vacancies_qms.append(result.json())
    search_num += 1

print(type(list_of_vacancies_qms))
print("Всего найдено анкет: ", search_num)

"""Сохраняем данные для локальной работы"""
with open('vacancies_qms.txt', 'w') as outfile:
    json.dump(list_of_vacancies_qms, outfile)


"""Открываем с локального ресурса"""
with open('vacancies_qms.txt') as json_file:
    list_of_vacancies_qms = json.load(json_file)


for i in list_of_vacancies_qms:
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
print("Средняя заработная плата специалистов по качеству в Москве (рубли): ", average_salary)

all_qms = 0
tags_list_vac_qms = []
for i in list_of_vacancies_qms:
    for i in i['items']:
        vac_id = i['id']
        vac_res = ses.get(f'https://api.hh.ru/vacancies/{vac_id}')
        if len(vac_res.json()["key_skills"]) > 0:  # at least one skill present
            all_qms += 1
            # print(vac_id)
            tags = [v for v_dict in vac_res.json()["key_skills"] for _, v in v_dict.items()]
            # print(' '.join(tags))
            tags_list_vac_qms.append(tags)
            # print()
            """Сохраняем данные для локальной работы"""
            with open('tags_list_vac_qms.txt', 'w') as outfile:
                json.dump(tags_list_vac_qms, outfile)
        time.sleep(0.1)

with open('tags_list_vac_qms.txt') as json_file:
    tags_list_vac_qms = json.load(json_file)


counts = dict()
for sublist in tags_list_vac_qms:
    for x in sublist:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1


print("Выводим ТОП-10 навыков и процент их встречаемости: ", sorted(counts.items(), reverse=True, key=lambda x: x[1])[0:10])
print("Всего анкет: ", all_qms)