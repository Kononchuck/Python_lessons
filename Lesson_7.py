import pandas as pd
import random
import csv

#df = pd.read_csv('Auto.csv')
with open ('Auto.csv', 'r') as f:
    reader = csv.reader(f, delimiter = '&')
    print(random.choice(list(reader)))



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
def get_context(mpg, cylinders, displacement, horsepower, weight, acceleration, year, origin, name):
    return {
        'mpg': mpg,
        'cylinders': cylinders,
        'displacement': displacement,
        'horsepower': horsepower,
        'weight': weight,
        'acceleration': acceleration,
        'year': year,
        'origin': origin,
        'name': name,

    }
print(get_context(18,8,307,130,3504,12,70,1,"chevrolet chevelle malibu"))

