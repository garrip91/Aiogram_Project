import requests, json

url = 'https://zen.yandex.ru/id/601d76de40f32972e4d8ce59?clid=101&country_code=ru'

response = requests.get(url, json={'key': 'value'})
s_c = response.status_code
#response.json()
print(response.json())