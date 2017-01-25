# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 15:45:04 2017

@author: JosephNelson
"""

# standard imports
from bs4 import BeautifulSoup
import requests
import pandas as pd

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
onion = pd.DataFrame(data=links, columns=['links'])
onion.head()
onion.to_csv('onion_links.csv')

'''
Using the links to collect data
'''

# load csv
onion = pd.read_csv('onion_links.csv')

# drop re-indexed columns
onion.drop('Unnamed: 0', axis=1, inplace=True)

# good to go
onion.head()

# find graphic and video indexes
non_text = []

for i, x in enumerate(onion.links):
    if '/graphic/' in x:
        non_text.append(i)
        # print i
    elif '/video/' in x:
        non_text.append(i)
        # print i
        
# drop graphics/videos
onion.drop(non_text, inplace=True)

# how many non-text stories did The Onion feautre?
len(non_text)

# see how many dropped
onion.shape

# fix index
onion.index

# fix index
onion.reset_index(inplace=True)

# check fixed index
onion.index

# drop old index
onion.drop('index', axis=1, inplace=True)

# check df - good to go
onion.index
onion.head()

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
    # grab tags for article - but only as many tags (<=5) as appear for an article
    try:
        for i, x in enumerate(soup.find('span', attrs={'class':'content-tags'}).find_all('a')):
            tags['tag{0}'.format(i)]=x.text.strip()
    except:
        pass
    
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

stories.to_csv('obama_scraped.csv', encoding='utf-8')
