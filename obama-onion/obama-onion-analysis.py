# import
import pandas as pd
import matplotlib as plt
plt.rcParams['figure.figsize'] = (8, 6)
plt.rcParams['font.size'] = 14
matplotlib.style.use('ggplot')

# read in data
onion = pd.read_csv('obama_scraped.csv')

onion.head()

# format date
onion['date'] = pd.to_datetime(onion['date'])

'''
METHODOLOGY NOTE: my rows =/= unique links: scraper errored on 49 stories
'''
# links are my unique ID
onion.link.nunique()
onion.shape

# drop duplicates -- scraped data integrity has been compromised
onion.drop_duplicates(subset='link',inplace=True)

# verify drops
onion.link.nunique()
onion.shape

'''
END METHODOLOGY ADJUSTMENT
'''

onion.groupby('date').plot()
onion.pivot_table(rows=['date'], cols=['tag0']).plot()

ols=['Group'], values=['Data']).plot()


# plot stories over time
ts = onion.set_index('date')
ts.drop('Unnamed: 0',axis=1).count(ts.link).plot()

ts.groupby('')

.plot()
ts.plot()
ts['Unnamed: 0']

