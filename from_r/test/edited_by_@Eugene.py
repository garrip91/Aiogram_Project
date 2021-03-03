import json
from typing import Any, Dict, Generator, List, Tuple
 
path = 'DATA.json'
 
Entry = Dict[str, Any]
EntryTuple = Tuple[Tuple[str, Any]]
 
example_data_to_add = [{
    'title': 'Лидер – кто может им стать и что для этого нужно',
    'desc': None,
    'url': 'https://zen.yandex.ru/media/id/601d76de40f32972e4d8ce59/lider--kto-mojet-im-stat-i-chto-dlia-etogo-nujno-603d289abdd71022a29d3b10'
}]
 
def transform_json_to_tuples(json_data: List[Entry]) -> Generator[EntryTuple]:
    for record in json_data:
        yield transform_entry(record)
 
 
def transform_entry(entry_dict: Entry) -> EntryTuple:
    return tuple((k, v) for k, v in entry_dict.items())
 
 
def load_data(filename) -> List[Entry]:
    with open(filename) as f:
        return json.load(f)
 
 
def ids_gen(initial: int) -> Generator[int]:
    while True:
        initial += 1
        yield initial
 
 
json_data = load_data(path)
initial_id = json_data[-1]['id']
get_new_id = ids_gen(initial_id)
set_of_tuples = set(transform_json_to_tuples(json_data))
 
 
# Добавляем всем новым элементам по ID-ключу и сами элементы в виде словарей добавляем в новый список: #
for d in example_data_to_add:
    new_data = dict(d)
 
    if transform_entry(d) in set_of_tuples:
        continue
 
    new_data['id'] = next(get_new_id)
    json_data.append(new_data)