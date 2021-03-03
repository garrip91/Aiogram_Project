import json



path = 'DATA.json'

path_list = []
path_dict_id = 1
with open(path, 'r', encoding='UTF-8') as f:
    path_json_read = json.load(f)
    for i in path_json_read:
        path_dict = {}
        #================================#
        path_dict['id'] = path_dict_id
        path_dict_id += 1
        #================================#
        path_dict['title'] = i['title']
        #================================#
        try:
            path_dict['desc'] = i['desc']
        except KeyError:
            pass
        #================================#
        path_dict['url'] = i['url']
        #================================#
        path_list.append(path_dict)
#print(path_list[3])

with open(path, 'w', encoding='UTF-8') as f:
    path_json_write = json.dump(path_list, f, ensure_ascii=False, indent=4)

#result = [x for x in path_list + temp_list if x not in path_list or x not in temp_list]
#print(result)