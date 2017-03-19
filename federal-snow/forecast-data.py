import darksky as ds
import forecastio
import datetime

# Haven't saved your API key as an environment variable?
ds.key('545461fdd9504a9342a3f4c7d40173b7')


# Look up interesting storms
ds.interesting()

# Get a brief forecast for a latitude/longitude
ds.brief(38.8977, -77.0365)
38.8977,-77.0365

# Or for a given address
ds.brief('155 9th St San Francisco, CA')

# Alternatively, get the full forecast
ds.forecast(37.775002, -122.418297)

# Same goes for an address
ds.forecast('155 9th St San Francisco, CA')

# Fetch the latitude/longitude manually
ds.location('155 9th St San Francisco, CA')

r = requests.get('https://api.darksky.net/forecast/545461fdd9504a9342a3f4c7d40173b7/38.8977,-77.0365?time=[2017]-[03]-[13]T[12]:[00]:[00]')
data = json.loads(r.content)

data['daily']['data']

import forecastio
forecast = forecastio.load_forecast('545461fdd9504a9342a3f4c7d40173b7', 38.8977, -77.0365)
forecast.hourly().summary

lat  = 38.8977
lng  = -77.0365
now = datetime.datetime(2017, 3, 13, 0, 0, 0)
api_key = ''
forecast = forecastio.load_forecast(api_key, lat, lng, time=now)
forecast.daily()

byHour = forecast.hourly()
byHour.temperature

for hourlyData in byHour.data:
    print hourlyData.precipProbability
    print hourlyData.temperature

for hourlyData in byHour.data:
    print hourlyData.precipProbability


byHour.data[23].precipProbability

forecast.currently().temperature

# StackOverflow http://stackoverflow.com/questions/1060279/iterating-through-a-range-of-dates-in-python
from datetime import timedelta, date

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

dates = []
start_date = date(2012, 3, 25)
end_date = date(2017, 3, 19)
for single_date in daterange(start_date, end_date):
    dates.append(datetime.datetime.combine(single_date, datetime.time.min))

len(dates)
