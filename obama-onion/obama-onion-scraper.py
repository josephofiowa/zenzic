# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 15:45:04 2017

@author: JosephNelson
"""

# standard imports
from bs4 import BeautifulSoup
import requests

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

'''
Using the links to collect data
'''

# load csv
onion = pd.read_csv('onion_links.csv')
onion.head()

# drop all graphics and videos from dataset
for i, x in enumerate(onion.links):
    if '/graphic/' in x:
        onion.drop(i, inplace=True)
    elif '/video/' in x:
        onion.drop(i, inplace=True)

# confirm drops
onion.shape

# fix index
onion.reset_index(inplace=True)

# drop re-indexed columns
onion.drop('Unnamed: 0', axis=1, inplace=True)

# build df
stories = pd.DataFrame(columns=['link','title','date','tag0','tag1','tag2','tag3','tag4','body'])

# grab these to be nice to The Onion
from time import sleep
import random 

for j, slug in enumerate(onion.links):    
    # request main feature page each time to be legit
    requests.get('http://www.theonion.com/interactive/obama')
    # wait ~3 seconds to grab a link
    sleep(random.uniform(.1,6))    
    
    # begin the real process
    link_to_visit = 'http://theonion.com'+ slug
    r = requests.get(link_to_visit)
    soup = BeautifulSoup(r.text)
    
    # grab article title      
    title = soup.find('header', attrs={'class':'content-header electoral-retro'}).find('h1').text
    # grab article date
    date = soup.find('span', attrs={'class':'content-published'}).text.strip()
    # inelegantly reset tags each iteration
    tags ={'tag0':None,
           'tag1':None,
           'tag2':None,
           'tag3':None,
           'tag4':None
           }
    # grab tags for article - but only as many tags (<=4) as appear for an article
    for i, x in enumerate(soup.find('span', attrs={'class':'content-tags'}).find_all('a')):
        tags['tag{0}'.format(i)]=x.text.strip()
    
    # body - inelegantly ignore Copyright and spam filtering p text tags
    body = []
    for para in soup.find_all('p'):
        if 'Copyright 2017 Onion' in para.text:
            pass
        elif 'Give your spam filter something to do.' in para.text:
            pass
        else:
            body.append(para.text)
    
    # add to df
    stories.loc[len(stories)]=[link_to_visit, title, date, tags['tag0'], tags['tag1'], tags['tag2'], tags['tag3'], tags['tag4'], body]    
    # pause a random amount of time - about a 35 seconds each
    
    print 'Completed ' + str(j)
    sleep(random.uniform(.1,70))

# stories.to_csv('obama_final.csv')