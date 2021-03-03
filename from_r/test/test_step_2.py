import json

from jsondiff import diff

path = 'DATA.json'
# ================== #
temp = 'TEMP.json'

################# https://github.com/xlwings/jsondiff #################
json1 = []
with open(path, 'r', encoding='UTF-8') as f:  
    path_json_read = json.load(f)
    for i in path_json_read:
        json1.append(i)
json2 = []
with open(temp, 'r', encoding='UTF-8') as f:  
    temp_json_read = json.load(f)
    for i in temp_json_read:
        json2.append(i)
    
#diff({'a': 1, 'b': 2}, {'b': 3, 'c': 4})
# print(diff(json1, json2))
#diff({'a': 1, 'b': 2}, {'b': 3, 'c': 4}, syntax='explicit')
# print(diff(json1, json2, syntax='explicit'))
#diff({'a': 1, 'b': 2}, {'b': 3, 'c': 4}, syntax='symmetric')
print(diff(json1, json2, syntax='symmetric'))
#print(diff('["a", "b", "c"]', '["a", "c", "d"]', load=True, dump=True))
# print(diff(json1, json2, dump=True))
#######################################################################

data_example_for_add_list = [
                                {
                                    'title': 'Лидер – кто может им стать и что для этого нужно',
                                    'desc': None,
                                    'url':'https://zen.yandex.ru/media/id/601d76de40f32972e4d8ce59/lider--kto-mojet-im-stat-i-chto-dlia-etogo-nujno-603d289abdd71022a29d3b10'
                                },
                                {
                                    'title': 'Гармония – как найти себя и что для это нужно',
                                    'desc': None,
                                    'url':'https://zen.yandex.ru/media/id/601d76de40f32972e4d8ce59/garmoniia--kak-naiti-sebia-i-chto-dlia-eto-nujno-603e2ee15f6b8d26fec3e4af'
                                }
                            ]
'''                       
with open(temp, 'w', encoding='UTF-8') as f:  
    json.dump(data_list[::-1], f, ensure_ascii=False, indent=4)
'''                       
# Test:
#print(diff(path, data_example_for_add_list))

# ====== Объявляем функцию заполнения основного списка данными из JSON: ====== #
def json_list_func(path=path):
    json_list = []
    with open(path, 'r', encoding='UTF-8') as f:  
        path_json_read = json.load(f)
        for i in path_json_read:
            json_list.append(i)  
    return json_list
#print(json_list_func()[0])
# ============================================================================ #

# Добавляем всем новым элементам по ID-ключу и сами элементы в виде словарей добавляем в новый список: #
def new_list_func(data_example_for_add_list=data_example_for_add_list):
    new_list = []
    new_id = json_list_func()[-1]['id'] + 1
    for i in data_example_for_add_list:
        dict_in_new_list = {}
        dict_in_new_list['id'] = new_id
        dict_in_new_list['title'] = i['title']
        try:
            dict_in_new_list['desc'] = i['desc']
        except KeyError:
            pass
        dict_in_new_list['url'] = i['url']
        new_list.append(dict_in_new_list)
        new_id += 1
    return new_list
#print(new_list_func())
# ==================================================================================================== #

# Добавляем готовые новые данные (с ключами ID) во второй JSON-файл:
def add_to_temp_json(temp=temp, new_list_func=new_list_func):
    with open(temp, 'w', encoding='UTF-8') as f:    
        json.dump(new_list_func(), f, ensure_ascii=False, indent=4)
    return "Ваши данные успешно загружены!"
#print(add_to_temp_json())
# ================================================================ #

# Проверяем наши списки на предмет наличия одинаковых элементов и в случае их отсутствия добавляем элементы из нового списка в основной: #
'''
json_tuples_list = []
for i in json_list.items():
    json_tuples_list_tuple = ()
    for k,v in i['id']:
        json_dicts_list.append()
'''
#json_tuples_list = [tuple(k,v) for k,v in i.items() for i in json_list]
#result = [F"\n{tuple((i))}\n" for i in data_example_for_add_list]
#result=list(set(json_list)-set(new_list))
#print(result)
def check_lists_func(json_list_func=json_list_func(), new_list_func=new_list_func()):
    # Преобразовываем наш основной список в список кортежей кортежей:
    json_list_new = []
    for i in json_list_func:
        json_list_new.append(tuple(i.items()))
    
    # Преобразовываем наш новый список в список кортежей кортежей:    
    new_list_new = []
    for i in new_list_func:
        new_list_new.append(tuple(i.items()))
        
    # Сравниваем наши полученные кортежи (списки):
    result = list(set(json_list_new) & set(new_list_new))
            
    #return (json_list_new[0], new_list_new[0])
    return result
#print(check_lists_func())
# ====================================================================================================================================== #

'''
with open(path, 'w', encoding='UTF-8') as f:
    path_json_write = json.dump(json_list, f, ensure_ascii=False, indent=4)
'''
#result = [x for x in json_list + temp_list if x not in json_list or x not in temp_list]
#print(result)