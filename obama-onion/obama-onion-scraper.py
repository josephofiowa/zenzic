# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 15:45:04 2017

@author: JosephNelson
"""

# standard imports
from bs4 import BeautifulSoup
import requests
from time import sleep

# grab the full text of the feature page
r = requests.get('http://www.theonion.com/interactive/obama/2008/28')
soup1 = BeautifulSoup(r.text)

# check an individual link
soup1.find('div', attrs={'class':'article-link'}).find('a')['href']

# loop through all inks, add to list called links
links = []
for x in soup1.find_all('div', attrs={'class':'article-link'}):
    links.append(x.find('a')['href'])

# save as csv
import pandas as pd
onion = pd.DataFrame(data=links, columns=['links'])
onion.head()
onion.to_csv('onion_links.csv')

# load csv
onion = pd.read_csv('onion_links.csv')
onion.head()

link_to_visit = 'http://theonion.com'+ onion.links[1]
r = requests.get(link_to_visit)
soup = BeautifulSoup(r.text)

# article body
for para in soup.find_all('p'):
    if 'Copyright 2017 Onion' in para.text:
        pass
    elif 'Give your spam filter something to do.' in para.text:
        pass
    else:
        print para.text

# article title
soup.find('header', attrs={'class':'electoral-retro-promo-header'}).find('a').text.strip()

# date
soup.find('span', attrs={'class':'content-published'}).text.strip()

# content tags
for tag in soup.find('span', attrs={'class':'content-tags'}).find_all('a'):
    print tag.text.strip()

# drop 
for x in enumerate(onion.links):
    
    
    
    if '/graphic/' in x:
        print True


