# REQUIRED: 'pip install jsondiff'
import json
from jsondiff import diff



path = 'DATA.json'
temp = 'TEMP.json'

# # ВТОРОЙ НАБОР ДАННЫХ ЯВЛЯЕТСЯ ВЕДУЩИМ:
# t1 = {1:1, 2:2, 3:3, 4:{"a":"hello", "b":[1, 2, 3]}}
# t2 = {1:1, 2:2, 3:3, 4:{"a":"hello", "b":[1, 3, 2, 3]}}

path_list = []
result_path_list = [None]
with open(path, 'r', encoding='UTF-8') as f1:
    path_json = json.loads(f1.read())
    for i in path_json:
        path_tuple_i = () # здесь было path_list_i = []
        for v in i.values():
            path_list_i.append(v)
            path_list.append(path_list_i)
    for i in path_list:
        if i != result_path_list[-1]:
            result_path_list.append(i)
        else:
            continue
    del result_path_list[0]
print(result_path_list[:10])

temp_list = []
result_temp_list = [None]
with open(temp, 'r', encoding='UTF-8') as f2:
    temp_json = json.loads(f2.read())
    for i in temp_json:
        temp_tuple_i = () # здесь было temp_list_i = []
        for v in i.values():
            temp_list_i.append(v)
            temp_list.append(temp_list_i)
    for i in temp_list:
        if i != result_temp_list[-1]:
            result_temp_list.append(i)
        else:
            continue
    del result_temp_list[0]
#print(result_temp_list[:10])

#if (result_path_list > result_temp_list):
    #print(list(set(path_list) - set(temp_list)))
    #print(len(path_list - temp_list))