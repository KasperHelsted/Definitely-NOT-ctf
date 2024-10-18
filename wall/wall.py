import uuid

import requests
from bs4 import BeautifulSoup
from urllib3.connection import port_by_scheme

base_url = 'https://the-wall.4j.dk/auth_cache/'

data = BeautifulSoup(requests.get(base_url).text, "lxml")

for url in data.find_all('a'):
    if '..' in url['href']:
        continue
    url = base_url + url['href']
    data2 = BeautifulSoup(requests.get(url).text, "lxml")

    for url2 in data2.find_all('a'):
        if '..' in url2['href']:
            continue
        url2 = url + url2['href']

        print(url2)
        data3 = BeautifulSoup(requests.get(url2).text, "lxml")

        for url3 in data3.find_all('a'):
            if '..' in url3['href']:
                continue
            url3 = url2 + url3['href']

            print(url3)
            data = requests.get(url3).text
            with open(f'./files/{uuid.uuid4().hex}.txt', 'w', encoding='utf-8') as f:
                print("Write file")
                f.write(data)
