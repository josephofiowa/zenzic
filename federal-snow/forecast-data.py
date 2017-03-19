import pandas as pd
import forecastio
from datetime import *
import numpy as np

'''
Three steps here
1) Create list of dates for which we want historical weather forecast data
2) Use Dark Sky API to grab data for those dates
3) Export data
'''


'''
1) Create list of dates for which we want historical weather forecast data
'''
# function to produce all dates between a start and end
# thanks, StackOverflow http://stackoverflow.com/questions/1060279/iterating-through-a-range-of-dates-in-python
def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

# set defaults (we only have good Google weekly data for these dates)
start_date = date(2012, 3, 25)
end_date = date(2017, 3, 19)

# create date list
dates = []
for single_date in daterange(start_date, end_date):
    dates.append(datetime.datetime.combine(single_date, datetime.time.min))

'''
2) Use Dark Sky API to grab data for those dates
https://darksky.net/dev/docs
https://github.com/ZeevG/python-forecast.io
'''

# set defaults - this is for the White House
lat  = 38.8977
lng  = -77.0365

# if you didn't set an env variable...
api_key = ''

# make df
weather = pd.DataFrame(columns=['date','summary', 'temp','precip', 'precip_intensity', 'precip_type', 'wind', 'visibility'])

# get data
for date in dates:
    forecast = forecastio.load_forecast(api_key, lat, lng, time=date)
    # make hourly
    byHour = forecast.hourly()
    # get 23rd hour data (last for that calendar date - 11PM) 
    try:  
        summary = byHour.data[23].summary
        temp = byHour.data[23].temperature
        precip = byHour.data[23].precipProbability
        precipIntensity = byHour.data[23].precipIntensity
        if precipIntensity!=0:
            precipType = byHour.data[23].precipType
        else:
            precipType = np.nan
        wind = byHour.data[23].windSpeed
        visibility = byHour.data[23].visibility
    except:
        pass
    # add to df    
    weather.loc[len(weather)]=[date, summary, temp, precip, precipIntensity, precipType, wind, visibility]

'''
3) Export data
'''

# check it out
weather.shape
weather.head()
weather.tail()

# export it
weather.to_csv('forecasts.csv', encoding='utf-8')