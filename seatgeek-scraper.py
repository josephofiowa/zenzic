# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 20:57:58 2016

@author: JosephNelson
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

# get our webpage
r = requests.get('https://seatgeek.com/washington-capitals-tickets')
soup = BeautifulSoup(r.text)

# event listings
print soup.find_all(name='div', attrs={'class':'page-event-listing'})

# date
print soup.find(name='div', attrs={'class':'event-listing-date'}).get('content')

# datetime
print soup.find(name='div', attrs={'class':'event-listing-time'}).get('title')

# day of week
print soup.find(name='div', attrs={'class':'event-listing-time'}).text.strip()[:3]

# teams
print soup.find(name='a', attrs={'class':'event-listing-title'}).find(name='span').text

# price
print soup.find(name='a', attrs={'class':'event-listing-button'}).text.strip()[5:]


tix = pd.DataFrame(columns=["date","time","day_of_week","home","away","price"])


# programmatic
for game in soup.find_all(name='div', attrs={'class':'page-event-listing'}):
    # print game.find(name='div', attrs={'class':'event-listing-date'}).get('content')    # date
    print game.find(name='a', attrs={'class':'event-listing-button'}).text.strip()[5:]


