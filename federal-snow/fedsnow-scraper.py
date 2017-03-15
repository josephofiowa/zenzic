import requests
from bs4 import BeautifulSoup
import pandas as pd

class LetItSnow:  
    """

    This module is used to scrape the OPM federal snow advisory website for snow-
    related events available at:
    https://www.opm.gov/policy-data-oversight/snow-dismissal-procedures/status-archives/

    Example:
    Call this script with simply:
        $ python federalsnow-scraper.py
    """
    
    def scrapeOPM(self):
        """
        Runs the scraper. Returns a dataframe that has three columns: 'year', 
        'date', and 'notice' (the snow advisory text) and also saves that df as 
        csv called opm_snow_data.csv to your current working directory 
        """     
        snow_data = self.buildDataframe()
        r = requests.get('https://www.opm.gov/policy-data-oversight/snow-dismissal-procedures/status-archives/')
        soup = BeautifulSoup(r.text)
        items = soup.find(name='ul', attrs={'class':'StatusYearContainer'}).find_all('li')
        for item in items:
            try:
                year = item.find('div', {'class':'StatusYear'}).text
                events = item.find('ul', {'class':'StatusUpdateContainer'}).find_all('li')
                for event in events:         
                    date = event.find('div', {'class':'StatusDateContainer'}).text.strip()
                    notice = event.find('div', {'class':'StatusNameContainer'}).text.strip()  
                    snow_data.loc[len(snow_data)]=[year, date, notice]
                    if len(snow_data)%25 == 0:
                        print('Scraped '+ str(len(snow_data)) + ' snow-related events. . .')
            except:
                pass
        snow_data.to_csv('opm_snow_data.csv', encoding='utf-8')
        print('Finished. Scraped ' + str(len(snow_data)) + ' snow-related events')
        return snow_data

    def buildDataframe(self):
        """
        Returns an empty dataframe with three columns: year, date, notice
        """
        return pd.DataFrame(columns=['year','date','notice'])

scraper = LetItSnow()
snow_days = scraper.scrapeOPM()
print(snow_days.head())