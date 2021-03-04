import json



path = 'DATA.json'
# ================== #
temp = 'TEMP.json'

################# https://github.com/xlwings/jsondiff #################

json_list_1_for_check = []
with open(path, 'r', encoding='UTF-8') as f:  
    path_json_read = json.load(f)
    for i in path_json_read:
        json_list_1_for_check.append(i)
json_list_2_for_check = []
with open(temp, 'r', encoding='UTF-8') as f:  
    temp_json_read = json.load(f)
    for i in temp_json_read:
        json_list_2_for_check.append(i)
        
for i in json_list_1_for_check:
    for j in json_list_2_for_check:
        if (i['title'] == j['title']) and (i['url'] == j['url']):
            print(F"В ДАННОМ СЛУЧАЕ ВСЕ ПОЛЯ ***{i}*** ПОЛНОСТЬЮ СОВПАДАЮТ С ПОЛЯМИ ***{j}***")
        elif (i['title'] != j['title']) and (i['url'] == j['url']):
            print(F"В ДАННОМ СЛУЧАЕ ЗАГОЛОВОК ***{i['title']}*** НЕ СОВПАДАЕТ С ЗАГОЛОВКОМ ***{j['title']}***")
        elif (i['title'] == j['title']) and (i['url'] != j['url']):
            print(F"В ДАННОМ СЛУЧАЕ ССЫЛКА ***{i['url']}*** НЕ СОВПАДАЕТ СО ССЫЛКОЙ ***{j['url']}***")
        elif (i['title'] != j['title']) and (i['url'] != j['url']):
            print(F"В ДАННОМ СЛУЧАЕ НИКАКИЕ ПОЛЯ ***{i}*** НЕ СОВПАДАЮТ С ПОЛЯМИ ***{j}***")
    

#######################################################################