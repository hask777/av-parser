import requests
from bs4 import BeautifulSoup

base_url = 'https://cars.av.by/'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}

r = requests.get('https://cars.av.by/acura')

soup = BeautifulSoup(r.content, 'html.parser')
carslist = soup.find_all('div', class_='listing-item')

carslinks = {}

finalcars = []

for item in carslist:
    photo = item.find('div', class_='listing-item__photo')
    image = photo.find('img')

    title = item.find('span', class_='link-text')

    params = item.find('div', class_='listing-item__params')

    link = item.find('a', href=True)
    # link = link['href']

    # print(image['data-src'])

    carslinks = {
        'image': image['data-src'],
        'title': title.text,
        'params': params.text,
        'link': link['href']
    }

    finalcars.append(carslinks)

    print(finalcars)
    
   