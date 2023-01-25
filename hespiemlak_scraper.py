from bs4 import BeautifulSoup
import requests
import pandas as pd
import _pickle
import time
#cengiz github push check
class HepsiemlakScraper(object):
    
    def __init__(self, config_file_name):
        with open(config_file_name, 'rb') as f:
            config = _pickle.load(f)
            
        self.advertisements = config['advertisements']
        self.page_index_start, self.page_index_end = config['page_index']['start'], config['page_index']['end']
        
        
    def export(self, config_file_name):
        config = {'advertisements':self.advertisements,
                  'page_index':{'start':self.page_index_start,
                                'end':self.page_index_end}}
        with open(config_file_name, 'wb') as f:
            _pickle.dump(config, f)
    
    
    def run(self):
        for page_index in range(self.page_index_start, self.page_index_end):
            
            try:
                url = f"https://www.hepsiemlak.com/istanbul-kiralik?page={page_index}"

                payload={}
                headers = {
                  'Cookie': 'i18n_redirected=tr'
                }

                response = requests.request("GET", url, headers=headers, data=payload)

                all_page = response.text
                soup = BeautifulSoup(all_page, 'html.parser')

                ul = soup.find('ul', class_='list-items-container')

                link_lis = ul.findAll('li')
 
                for link_li in link_lis:

                    adv = link_li.find('div', class_='list-view-img-wrapper')
                    if not adv:
                        continue

                    advertisement_info = {}

                    adv_url = 'https://www.hepsiemlak.com' + adv.a['href']
                    if adv_url in self.advertisements:
                        continue

                    advertisement_info['url'] = adv_url

                    payload={}
                    headers = {
                      'Cookie': 'i18n_redirected=tr'
                    }

                    adv_response = requests.request("GET", adv_url, headers=headers, data=payload)

                    adv_page = adv_response.text
                    adv_soup = BeautifulSoup(adv_page, 'html.parser')

                    # details
                    adv_details = adv_soup.find('div', class_='det-adv-info')
                    details_uls = adv_details.findAll('ul', class_='adv-info-list')
                    for details_ul in details_uls:
                        details = details_ul.findAll('li', class_='spec-item')

                        for li in details:
                            spans = li.findAll('span')
                            if len(spans) < 2:
                                advertisement_info[spans[0].text] = li.a.text
                            elif len(spans) == 2:
                                advertisement_info[spans[0].text] = spans[1].text
                            elif len(spans) == 3:
                                advertisement_info[spans[0].text] = f'{spans[1].text.replace(" ", "")} {spans[2].text.replace(" ", "")}'
                            else:
                                print('here: ', adv_url)

                    # short details
                    short_info_ul = adv_soup.find('ul', class_='short-info-list')
                    short_info_lis = short_info_ul.findAll('li')
                    short_info = [li.text.replace(' ', '').replace('\n', '') for li in short_info_lis]
                    advertisement_info['short_info'] = short_info

                    # rent
                    rent = adv_soup.find('p', class_='fontRB fz24 price').text.replace(' ', '').replace('\n', '')
                    advertisement_info['rent'] = rent

                    self.advertisements[adv_url] = advertisement_info
                    time.sleep(2)

                print(page_index)
                time.sleep(2)
            
            except:
                self.page_index_start = page_index + 1
        

