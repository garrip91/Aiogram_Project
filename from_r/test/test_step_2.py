import json

data = 'DATA.json'
# ================== #
temp = 'TEMP.json'



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

# ====== Объявляем функцию заполнения основного списка данными из JSON: ====== #
def json_list_1_func(data=data):
    json_list_1 = []
    with open(data, 'r', encoding='UTF-8') as f:  
        data_json_read = json.load(f)
        for i in data_json_read:
            json_list_1.append(i)  
    return json_list_1
#print(json_list_1_func()[0])
# ============================================================================ #

# Добавляем всем новым элементам по ID-ключу и сами элементы в виде словарей добавляем в новый список: #
def json_list_2_func(data_example_for_add_list=data_example_for_add_list):
    json_list_2 = []
    new_id = json_list_1_func()[-1]['id'] + 1
    for i in data_example_for_add_list:
        dict_in_json_list_2 = {}
        dict_in_json_list_2['id'] = new_id
        dict_in_json_list_2['title'] = i['title']
        try:
            dict_in_json_list_2['desc'] = i['desc']
        except KeyError:
            pass
        dict_in_json_list_2['url'] = i['url']
        json_list_2.append(dict_in_json_list_2)
        new_id += 1
    return json_list_2
#print(json_list_2_func())
# ==================================================================================================== #

# Добавляем готовые новые данные (с ключами ID) во второй JSON-файл:
def add_to_temp_json(temp=temp, json_list_2_func=json_list_2_func):
    with open(temp, 'w', encoding='UTF-8') as f:    
        json.dump(json_list_2_func(), f, ensure_ascii=False, indent=4)
    return "Ваши данные успешно загружены!"
#print(add_to_temp_json())
# ================================================================ #

# Проверяем наши списки на предмет наличия одинаковых элементов: #
def check_jsons_func(json_list_1_func=json_list_1_func(), json_list_2_func=json_list_2_func()):
    # Получаем данные из готовых JSON-файлов для сравнения:
    json_list_1_for_check = []
    with open(data, 'r', encoding='UTF-8') as f:  
        data_json_read_for_check = json.load(f)
        for i in data_json_read_for_check:
            json_list_1_for_check.append(i)
    json_list_2_for_check = []
    with open(temp, 'r', encoding='UTF-8') as f:  
        path_json_read_for_check = json.load(f)
        for i in path_json_read_for_check:
            json_list_2_for_check.append(i)
    # Проходим циклом по полученным данным для их сравнения:
    full_flag = False
    url_flag = False
    title_flag = False
    nothing_flag = False
    for i in json_list_1_for_check:
        for j in json_list_2_for_check:
            if (i['title'] == j['title']) and (i['url'] == j['url']):
                full_flag = True
            elif (i['title'] != j['title']) and (i['url'] == j['url']):
                url_flag = True
            elif (i['title'] == j['title']) and (i['url'] != j['url']):
                title_flag = True
            elif (i['title'] != j['title']) and (i['url'] != j['url']):
                nothing_flag = True
                
    if full_flag == True:
        return F"В ДАННОМ СЛУЧАЕ ВСЕ ПОЛЯ ИЗ DATA.json ПОЛНОСТЬЮ СОВПАДАЮТ С ПОЛЯМИ ИЗ TEMP.json"
    if url_flag == True:
        return F"В ДАННОМ СЛУЧАЕ ЗАГОЛОВОК ИЗ DATA.json НЕ СОВПАДАЕТ С ЗАГОЛОВКОМ ИЗ TEMP.json"
    if title_flag == True:
        return F"В ДАННОМ СЛУЧАЕ ССЫЛКА ИЗ DATA.json НЕ СОВПАДАЕТ СО ССЫЛКОЙ ИЗ TEMP.json"
    if nothing_flag == True:
        return F"В ДАННОМ СЛУЧАЕ НИКАКИЕ ПОЛЯ ИЗ DATA.json НЕ СОВПАДАЮТ НИ С КАКИМИ ПОЛЯМИ ИЗ TEMP.json"
        
print(check_jsons_func())
# ====================================================================================================================================== #

'''
with open(data, 'w', encoding='UTF-8') as f:
    data_json_write = json.dump(json_list, f, ensure_ascii=False, indent=4)
'''
#result = [x for x in json_list + temp_list if x not in json_list or x not in temp_list]
#print(result)