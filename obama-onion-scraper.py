# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 15:45:04 2017

@author: JosephNelson
"""

from bs4 import BeautifulSoup
import requests
from time import sleep

r = requests.get('http://www.theonion.com/article/black-guy-asks-nation-for-change-2409')
soup = BeautifulSoup(r.text)
soup.find_all('p')

r = requests.get('http://www.theonion.com/interactive/obama/2008/28')
soup1 = BeautifulSoup(r.text)

soup1.find('div', attrs={'class':'article-link'}).find('a')['href']

links = []
for x in soup1.find_all('div', attrs={'class':'article-link'}):
    links.append(x.find('a')['href'])

len(set(links)) 