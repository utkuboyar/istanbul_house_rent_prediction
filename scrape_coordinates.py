from selenium import webdriver
from selenium.webdriver.common.by import By

import _pickle

with open('recorded_ads', 'rb') as f:
    recorded_ads = _pickle.load(f)
urls = {}

driver = webdriver.Chrome()


for url in recorded_ads.keys():

    driver.get(url)
    driver.implicitly_wait(30)

    interactive_ul = driver.find_element(By.CLASS_NAME, 'interactive-list')
    lis = interactive_ul.find_elements(By.TAG_NAME, 'li')

    for li in lis:
        a = li.find_element(By.TAG_NAME, 'a')
        if 'Harita / Sokak' in a.get_attribute('innerHTML'):
            anchor = a
            break

    anchor.click()
    map_block_section = driver.find_element(By.ID, 'mapBlock')
    map_anchor = map_block_section.find_element(By.TAG_NAME, 'a')
    
    map_url = map_anchor.get_attribute('href')
    print(map_url)
    urls[url] = map_url
    
    
driver.close()
