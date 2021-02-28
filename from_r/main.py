from get_page_data import get_page_data
from get_whole_page import get_whole_page

if __name__ == '__main__':
    #link = input('Link: ')
    link = 'https://zen.yandex.ru/id/601d76de40f32972e4d8ce59?clid=101'
    #filename = input('Filename without extension: ')
    filename = 'DATA'
	
    #get_whole_page(link, filename + '.html')
    get_whole_page(link, F'{filename}.html')
    #get_page_data(filename + '.html', filename)
    get_page_data(F'{filename}.html', filename)