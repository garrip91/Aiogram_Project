import json

import sqlite3



path = 'DATA.json'
temp = 'TEMP.json'
'''
path_list = []
with open(path, 'r', encoding='UTF-8') as f1:
    path_json = json.loads(f1.read())
    for i in path_json:
        path_list.append(i)
        
temp_list = []
with open(temp, 'r', encoding='UTF-8') as f2:
    temp_json = json.loads(f2.read())
    for i in temp_json:
        temp_list.append(i)

result = [x for x in path_list + temp_list if x not in path_list or x not in temp_list]



#with open(filename + '.json', 'w', encoding='UTF-8') as file:
with open('DATA.json', 'w', encoding='UTF-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=4)
    print("F{result} - ЭТИ ДАННЫЕ ЗАПИСАНЫ В ФАЙЛ DATA.json...")
with open('TEMP.json', 'w', encoding='UTF-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=4)
    print("F{result} - ...И ПРОДУБЛИРОВАНЫ В ФАЙЛ TEMP.json...")
'''    
    
    
db = sqlite3.connect('server.db')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS DATA (
    id INT,
    title TEXT,
    desc TEXT,
    url TEXT
)""")

db.commit()

title = input('Title: ')
description = input('Description: ')

sql.execute('SELECT title FROM DATA')
if sql.fetchone() is None:
    sql.execute(F"INSERT INTO DATA VALUES ('{title}', '{description}', '{0}')")
else:
    print("Такая запись уже имеется!")

db.close()