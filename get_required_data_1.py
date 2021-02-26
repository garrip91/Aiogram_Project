import requests

from bs4 import BeautifulSoup as BS



URL = 'https://zen.yandex.ru/id/601d76de40f32972e4d8ce59?clid=101&country_code=ru'

HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36', 'accept': '*/*'}



def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r
    
def get_content(html):
    soup = BS(html, 'html.parser')
    items = soup.find_all('span', class_='card-text-clamp__text-content')
    
    titles_and_descriptions = []
    for item in items:
        item = str(item).replace('<span class="card-text-clamp__text-content">', '').replace('<span class="card-text-clamp__text-content _is-ellipsis-needed">', '').replace('</span>', '').replace('\n', ' ')
        if item not in titles_and_descriptions:
            titles_and_descriptions.append(item)
    #print(titles_and_descriptions)
    
    del titles_and_descriptions[1::2]
    print(titles_and_descriptions)
    
    zipped = list(zip(titles_and_descriptions[::2], titles_and_descriptions[1::2]))
    #print(zipped)
    
def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print("Error!")
    
    
    
parse()