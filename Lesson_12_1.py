import time
import requests
import json
import csv


ses = requests.Session()
ses.headers = {'HH-User-Agent': "Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/10.0"}

phrase_to_search = 'python'
url = f'https://api.hh.ru/vacancies?text={phrase_to_search}&per_page=100'
res = ses.get(url)

# # getting a list of all responses
# res_all = []
# for p in range(res.json()['pages']):
#     print(f'scraping page {p}')
#     url_p = url + f'&page={p}'
#     res = ses.get(url_p)
#     res_all.append(res.json())
#     time.sleep(0.2)
#
# """Сохраняем данные для локальной работы"""
# with open('res_all.json', 'w') as outfile:
#     json.dump(res_all, outfile)

"""Открываем с локального ресурса"""
with open('res_all.txt') as json_file:
    res_all = json.load(json_file)



# parcing vacancies ids, getting vacancy page and scraping tags from each vacancy
tags_list = []
for i in res_all:
    for i in i['items']:
        vac_id = i['id']
        vac_res = ses.get(f'https://api.hh.ru/vacancies/{vac_id}')
        if len(vac_res.json()["key_skills"]) > 0:  # at least one skill present
            print(vac_id)
            tags = [v for v_dict in vac_res.json()["key_skills"] for _, v in v_dict.items()]
            print(' '.join(tags))
            tags_list.append(tags)
            print()
            """Сохраняем данные для локальной работы"""
            with open('tags_list.txt', 'w') as outfile:
                json.dump(tags_list, outfile)
        time.sleep(0.1)




# res = {'phrase': phrase_to_search, 'items_number': len(tags_list), 'items': tags_list}
# with open(f'./data/raw-tags_{phrase_to_search}.json', 'w') as fp:  # Serializing
#     json.dump(res, fp)

#
# tags_list['items'] = [[i.lower() for i in line] for line in tags_list['items']]
#
# # counting words occurrences
# flattened_list = [i for line in tags_list for i in line]
# nodes_dict_all = {i: flattened_list.count(i) for i in set(flattened_list)}
# nodes_dict = {k:v for k, v in nodes_dict_all.items() if v > del_nodes_count}



#
# # tags connection dict initialization
# formatted_tags = {(tag1, tag2): 0 for tag1, tag2 in itertools.permutations(set(nodes_dict.keys()), 2)}
#
# # count tags connection
# for line in tags_list:
#     for tag1, tag2 in itertools.permutations(line, 2):
#         if (tag1, tag2) in formatted_tags.keys():
#             formatted_tags[(tag1, tag2)] += 1
#
# # filtering pairs with zero count
# for k, v in formatted_tags.copy().items():
#     if v == 0:
#         del formatted_tags[k]
#
# nodes = []
# links = []
# for pair, count in formatted_tags.items():
#     links.append({"source": pair[0], "target": pair[1], "value": count})
#
# max_count = max(list(nodes_dict.values()))
# count_step = max_count // 7
# for node, count in nodes_dict.items():
#     nodes.append({"id": node, "group": count // count_step, "popularity": count})
#
# data_to_dump = in_json.copy()
# data_to_dump['items'] = {"nodes": nodes, "links": links}