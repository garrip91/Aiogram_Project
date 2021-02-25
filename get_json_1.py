import requests

from bs4 import BeautifulSoup as BS



# URL = 'https://auto.ria.com/newauto/marka-jeep/'
URL = 'https://zen.yandex.ru/id/601d76de40f32972e4d8ce59?clid=101&country_code=ru'

HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36', 'accept': '*/*'}



def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r
    
def get_content(html):
    soup = BS(html, 'html.parser')
    #items = soup.find_all('div', class_='clamp__text-expand')
    #items = soup.find_all('div', class_='desktop-channel-2-layout')
    items = soup.find_all('div', class_='clamp__text-expand')
    
    print(items)
    
    # articles = []
    # for item in items:
        # articles.append({
            # 'title': item.find('div', class_='clamp__text-expand').get_text(strip=True)
        # })
    # print(articles)
    titles = []
    n = 1
    for item in items:
        titles.append({
            F'title-{n}': item.find('div', class_='clamp__text-expand')
            #.get_text(strip=True)
        })
        n += 1
    #print(titles)
    
def parse():
    html = get_html(URL)
    #print(html)
    #print(html.status_code)
    if html.status_code == 200:
        #print(html.text)
        get_content(html.text)
    else:
        print("Error!")
    
    
    
parse()

# Заголовок блога(статьи): <span class="card-text-clamp__text-content">Soft skills - что это такое и зачем они нужны</span> 