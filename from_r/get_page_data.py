import json

from bs4 import BeautifulSoup
from funcs import del_space
import re
from out import write_xlsx



#old_path = 'EXISTING_DATA.json'
path = 'DATA.json'
temp = 'TEMP.json'

# Убираем все символы из url, начиная с "?" и далее:
def remove_trash(data: str):
    if el := re.findall(r'\?.+', data):
        data = data.replace(el[0], '')
	
    return data

# Собираем данные всех статей из скаченной html-страницы:
def get_page_data(filename_html: str, filename: str):
    # Загружаем сформированную html-страницу:
    with open(filename_html, 'r', encoding='UTF-8') as file:
        html_data = file.read()
	
    # Переводим html-страницу в объект, понятный для Python:
    soup = BeautifulSoup(html_data, 'lxml')
    # Получаем из html-страницы все статьи:
    cards = soup.find_all('div', class_='card-wrapper')
	
    # Создаём список с данными в виде - [{'title', 'desc'(при его наличии), 'url'}, ...]:
    data_list = []
    for card in cards:
        # Cоздаем словарь в виде - {'title', 'desc'(при его наличии), 'url'}, куда добавляем заголовки, описания и ссылки соответственно:
        data_dict = {}

        # Находим заголовок статьи по атрибуту соответствующего html-тега С ПРИМЕНЕНИЕМ ФУНКЦИИ УДАЛЕНИЯ ЛИШНИХ ПРОБЕЛОВ И ПЕРЕНОСОВ СТРОК и добавляем его в наш словарь:
        data_dict['title'] = del_space(card.find('div', class_='card-content__title').find('span').text)

        try:
            # Находим описание статьи по атрибуту соответствующего html-тега С ПРИМЕНЕНИЕМ ФУНКЦИИ УДАЛЕНИЯ ЛИШНИХ ПРОБЕЛОВ И ПЕРЕНОСОВ СТРОК и добавляем его в наш словарь:
            data_dict['desc'] = del_space(card.find('div', class_='card-content__text').find('span').text)
        except AttributeError:
            pass

        # Находим ссылку по атрибуту соответствующего html-тега С ПРИМЕНЕНИЕМ ФУНКЦИИ УДАЛЕНИЯ ЛИШНИХ СИМВОЛОВ НАЧИНАЯ С "?" и добавляем его в наш словарь:
        data_dict['url'] = remove_trash(card.find('a', class_='card-image-view-by-metrics__clickable').get('href'))        
        # Добавляем словарь, содержащий заголовок, описание(при его наличии) и ссылку на статью, в наш список:
        data_list.append(data_dict)
        
        # ...и проходим циклом по всем статьям...
	
    # Записываем все наши статьи в Excel-таблицу:
    write_xlsx(data_list, filename + '.xlsx')
    
    # Записываем все наши статьи в json:
    with open(filename + '.json', 'w', encoding='UTF-8') as file:
        json.dump(data_list[::-1], file, ensure_ascii=False, indent=4)
    # Также записываем содержимое нашего JSON-файла в отдельный временный файл:
#    with open('TEMP.json', 'r+', encoding='UTF-8') as f:
#        json_data = json.loads(f.read())
#        print(json_data)
        #for i_1 in data_list:
            #for i_2 in file:
                #if i != 
#        if len(data_list) == len(json_data):
#            print(True)
        #json.dump(data_list[::-1], file, ensure_ascii=False, indent=4)



# if __name__ == '__main__':
	# get_page_data(input("Filename (html): "), input("Filename (xlsx): "))