import requests
from bs4 import BeautifulSoup

r = requests.get('https://washingtondc.craigslist.org/search/bik')
soup = BeautifulSoup(r.text)

test = []
for row in soup.find_all('li', 'result-row'):
    # print row
    print row
    row.find('a')
    break

for x in soup.find_all('li', 'result-row'):
    x.find('a')['href']
    break

soup.find('li', 'result-row').find('a')

soup.find('p', 'result-info').find('span', 'result-price').text

for x in soup.find_all('p', 'result-info'):
    print x
    x.find('span', 'result-price')