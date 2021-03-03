import json

path = 'DATA.json'



data_example_for_add = [{
                        'title': 'Лидер – кто может им стать и что для этого нужно',
                        'desc': None,
                        'url': 'https://zen.yandex.ru/media/id/601d76de40f32972e4d8ce59/lider--kto-mojet-im-stat-i-chto-dlia-etogo-nujno-603d289abdd71022a29d3b10'
                       }]

# ====== Заполняем основной список данными из JSON: ====== #
# ======================================================== #
json_list = []
with open(path, 'r', encoding='UTF-8') as f:
    path_json_read = json.load(f)
    for i in path_json_read:
        json_list.append(i)       
# ======================================================== #        

# ...и объявляем переменную с первым значением ID #
new_id = json_list[-1]['id'] + 1
# =============================================== #

# Добавляем всем новым элементам по ID-ключу и сами элементы в виде словарей добавляем в новый список: #
new_list = []
for i in data_example_for_add:
    path_dict = {}
    path_dict['id'] = new_id
    path_dict['title'] = i['title']
    try:
        path_dict['desc'] = i['desc']
    except KeyError:
        pass
    path_dict['url'] = i['url']
    new_list.append(path_dict)
    new_id += 1
# ==================================================================================================== #

# Проверяем наши списки на предмет наличия одинаковых элементов и в случае их отсутствия добавляем элементы из нового списка в основной: #
'''
json_tuples_list = []
for i in json_list.items():
    json_tuples_list_tuple = ()
    for k,v in i['id']:
        json_dicts_list.append()
'''
#json_tuples_list = [tuple(k,v) for k,v in i.items() for i in json_list]
result = [print(F"\n{tuple((i,))}\n") for i in json_list]
#result=list(set(json_list)-set(new_list))
print(result)
# ====================================================================================================================================== #

'''
with open(path, 'w', encoding='UTF-8') as f:
    path_json_write = json.dump(json_list, f, ensure_ascii=False, indent=4)
'''
#result = [x for x in json_list + temp_list if x not in json_list or x not in temp_list]
#print(result)

# tuple(x for x in some_list)