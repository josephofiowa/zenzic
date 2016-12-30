# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 22:55:03 2016

@author: JosephNelson
"""

from bs4 import BeautifulSoup
import requests
from time import sleep

r = requests.get('https://www.hillaryclinton.com/speeches/page/1/')
soup = BeautifulSoup(r.text, 'html.parser', from_encoding="utf-8")

# show one snippet of a speech post
print soup.find_all('div', {'class': 'o-wrap-post'})[0]

# there are 12 pages of speeches
# grab relevant links
links = []
for page in range(1,13):
    r = requests.get('https://www.hillaryclinton.com/speeches/page/' + str(page))
    soup = BeautifulSoup(r.text, 'html.parser', from_encoding="utf-8")
    for link in soup.find_all('a'):
        if link.has_attr('href'):
            if '/speeches/' in link.attrs['href']:
                links.append(link.attrs['href'])
    sleep(1)

set(links)