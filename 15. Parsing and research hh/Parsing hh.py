import json
import re
import requests as req
import tqdm
from bs4 import BeautifulSoup

data = {
    'data': []
}

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
headers= {'accept': '*/*', 'user-agent': USER_AGENT}
for page in tqdm.tqdm(range(0, 41)):
    session = req.Session()
    url = f'https://hh.ru/search/vacancy?search_field=name&search_field=company_name&search_field=description&text=python+%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA&from=suggest_post&page={page}&hhtmFrom=vacancy_search_list'
    resp = session.get(url, headers = headers)
    if resp.status_code !=200:
        print('Error:', resp.status_code)
    
    soup = BeautifulSoup(resp.text, 'lxml')
    tags = soup.find_all(attrs={'data-qa': 'serp-item__title'})
    
    for tag in tqdm.tqdm(tags):
        url_inner = tag.attrs['href']
        resp_inner = session.get(url_inner, headers = headers)
        soup_inner = BeautifulSoup(resp_inner.text, 'lxml')
        
        try:
            tag_name = tag.text
        except:
            tag_name = 'Ошибка'
                
        try:
            tag_price = soup_inner.find(attrs={'data-qa': 'vacancy-salary'}).text
        except:
            tag_price = 'Не указана'
            
        try:
            tag_background = soup_inner.find(attrs={'data-qa': 'vacancy-experience'}).text
        except:
            tag_background = 'Не указан'
            
        try:
            tag_region = (re.split(r',', soup_inner.find(attrs={'data-qa': 'vacancy-view-raw-address'}).text))[0]
        except:
            tag_region = 'Неизвестен'
        #tag_region = (re.split(r',', soup_inner.find(attrs={'data-qa': 'vacancy-view-raw-address'}).text))[0]
        
        data['data'].append(
            {'title': tag_name,
            'work experience': tag_background, 
            'salary': tag_price, 
            'region': tag_region
            })
        
        with open('data.json', 'w') as file:
            json.dump(data, file, ensure_ascii=False,)
            
        