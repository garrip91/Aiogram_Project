from selenium import webdriver



URL = 'https://zen.yandex.ru/id/601d76de40f32972e4d8ce59?clid=101&country_code=ru'

HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36', 'accept': '*/*'}



def main():
    driver = webdriver.Chrome()
    driver.get(URL)
    elems = driver.find_element_by_class_name('card-image-view-by-metrics__clickable')
    #elems.click()
    #print(type(elems))
    #print(str(elems))
    #a_tags = driver.find_element_by_tag_name('a')
    #a_tags.click()
    #print(a_tags.text)
    #print(driver.page_source)
    
    f = open('RESULT.html', 'w', encoding='utf8')
    f.write(driver.page_source)
    f.close()
    
    
if __name__ == '__main__':
    main()