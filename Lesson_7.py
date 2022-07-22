import pandas as pd
import random
import csv

# with open ('Auto.csv', 'r') as f:
#     reader = csv.reader(f, delimiter = '&')
#     next(reader) #пропускаем заголовок
#     df_auto = random.choice(list(reader))#выбираем случаную строку
#     df_auto = ''.join(df_auto)#убираем скобы

dict_new = []
with open('Auto.csv', 'r') as data:
    for line in csv.DictReader(data):
        dict_new.append(line)

print(random.choice(dict_new))





import datetime

from docx.shared import Cm
from docxtpl import DocxTemplate, InlineImage

"""
# определяем словарь переменных контекста,
# которые определены в шаблоне документа DOCX
context = {}
context['company_name'] = 'Mechantica, Inc.'

doc = DocxTemplate("word_tpl.docx")
#img = InlineImage(doc, image_descriptor='python_logo.png', width=Mm(20), height=Mm(10))

# подставляем контекст в шаблон
doc.render(context)
# сохраняем и смотрим, что получилось
doc.save("generated_docx.docx")
"""

# возвращает словарь аргуменов
# def get_context(mpg, cylinders, displacement, horsepower, weight, acceleration, year, origin, name):
#     return {
#         'mpg': mpg,
#         'cylinders': cylinders,
#         'displacement': displacement,
#         'horsepower': horsepower,
#         'weight': weight,
#         'acceleration': acceleration,
#         'year': year,
#         'origin': origin,
#         'name': name,
#
#     }


