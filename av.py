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

    ''' Find car image '''
    photo = item.find('div', class_='listing-item__photo')
    image = photo.find('img')['data-src']

    ''' Find car title '''
    title = item.find('span', class_='link-text').text

    ''' Find car link '''
    params = item.find('div', class_='listing-item__params').text

    ''' Find car link '''
    link = item.find('a', href=True)['href']
 
    carslinks = {
        'image': image,
        'title': title,
        'params': params,
        'link': link
    }

    finalcars.append(carslinks)

print(finalcars[1])
    
   