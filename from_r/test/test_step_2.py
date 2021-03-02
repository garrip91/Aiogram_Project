import json

path = 'DATA.json'



dict_example_for_add = {
                        'title': 'Лидер – кто может им стать и что для этого нужно',
                        'desc': None,
                        'url': 'https://zen.yandex.ru/media/id/601d76de40f32972e4d8ce59/lider--kto-mojet-im-stat-i-chto-dlia-etogo-nujno-603d289abdd71022a29d3b10'
                       }



path_list = []
path_dict_id = 1
with open(path, 'a', encoding='UTF-8') as f:
    path_json_read = json.load(f)
    for i in path_json_read:
        path_dict = {}
        if i['title'] != dict_example_for_add['title']:
                    
#print(path_list[3])

with open(path, 'w', encoding='UTF-8') as f:
    path_json_write = json.dump(path_list, f, ensure_ascii=False, indent=4)

#result = [x for x in path_list + temp_list if x not in path_list or x not in temp_list]
#print(result)