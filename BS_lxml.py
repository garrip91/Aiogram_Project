import requests
import lxml.html
from lxml import etree
from bs4 import BeautifulSoup as BS



def lxml_title(html_text):
    tree = lxml.html.document_fromstring(html_text)
    text_original = tree.xpath('/html/head/title/text()')
    print(text_original)
    
def main():
    url = 'https://zen.yandex.ru/id/601d76de40f32972e4d8ce59?clid=101&country_code=ru'
    html_text = requests.get(url).text
    lxml_title(html_text)
    
    
    
if __name__ == '__main__':
    main()