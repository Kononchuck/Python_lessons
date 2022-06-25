import re
import pymorphy2
#методами строк очистить текст от знаков препинания;

text = open('text.txt', 'r')
text = text.read()
text = re.sub(r'[?|$|.|! — 1] ',r'', text)


#сформировать list со словами(split);
text = text.split(' ')

#привести все слова к нижнему регистру(map);

text = list(map(str.lower, text))
for_lemm_text = text

#получить из list пункта 3 dict, ключами которого являются слова, а значениями их количество появлений в тексте;

counts = dict()
for i in text:
    if i in counts:
        counts[i] += 1
    else:
        counts[i] = 1
print(counts)

#вывести 5 наиболее часто встречающихся слов(sort)

print(text.sort())
'''метод (sort)  дает None - не смог разобраться почему'''

print(sorted(counts.items(), reverse=True, key=lambda x: x[1])[0:5])

#вывести количество разных слов в тексте(set)
differ_words = len(set(counts))
print("Всего разных слов: ", differ_words)


#в пункте 3 дополнительно к приведению к нижнему регистру выполнить лемматизацию
morph = pymorphy2.MorphAnalyzer()
show_lemm = list()
for i in for_lemm_text:
    p=morph.parse(i)[0]
    show_lemm.append(p.normal_form)
print(for_lemm_text)
print(show_lemm)