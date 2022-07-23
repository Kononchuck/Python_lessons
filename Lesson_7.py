import random
import csv
import json
import time
from docxtpl import DocxTemplate

#начинаем замерять время на выполнение задач
start = time.process_time()

#Создайте csv-файл с данными о машине.
def get_context():
    dict_new = []
    with open('Auto.csv', 'r') as data:
        for i in csv.DictReader(data):
            dict_new.append(i)
        return random.choice(list(dict_new))

#Создайте шаблон документа doc
doc = DocxTemplate('auto_tpl.docx')

content = get_context()

#подсчитываем время на выполнение задач
content['time'] = time.process_time() - start

# подставляем затраченное время в шаблон
doc.render(content)

# Вносим данные из файла в шаблон
doc.save("generated_docx.docx")

#Создайте json-файл с данными о машине.
dict_to_json = json.dumps(get_context())
print(type(dict_to_json), dict_to_json)

