import numpy as np
import pandas as pd
import json


from collections import Counter


with open('tags_list.txt') as json_file:
    tags_list = json.load(json_file)


# with open('tags_list.txt') as file:
#     tags_list = file.read()


pd.value_counts(np.array(tags_list[0]))

print(pd.value_counts(np.array(tags_list[0])))

# counts = dict()
# # for i in tags_list[0]:
# #     if i in counts:
# #         counts[i] += 1
# #     else:
# #         counts[i] = 1
# # print(counts)

count = Counter(x for sublist in tags_list for x in sublist)
print(count)

counts = dict()
for sublist in tags_list:
    for x in sublist:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1

print(counts)
print(sorted(counts.items(), reverse=True, key=lambda x: x[1])[0:5])