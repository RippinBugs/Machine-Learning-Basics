"""
Time series data consists of data that contains dates. For example, in this video, we will be plotting BitCoin prices
over the last few weeks. We will learn how to format dates in different ways so that they work better with our graphs 
"""

import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime, timedelta
from matplotlib import dates as mpl_dates

plt.style.use('seaborn')

# dates = [
#     datetime(2019, 5, 24),
#     datetime(2019, 5, 25),
#     datetime(2019, 5, 26),
#     datetime(2019, 5, 27),
#     datetime(2019, 5, 28),
#     datetime(2019, 5, 29),
#     datetime(2019, 5, 30),
#     datetime(2019, 5, 31)
# ]

# y = [0,1,3,4,7,5,8,2]

# plt.plot_date(dates,y,linestyle = '-')
# plt.gcf().autofmt_xdate()            #gcf - get current format 

# date_format = mpl_dates.DateFormatter('%b, %d %Y')
# plt.gca().xaxis.set_major_formatter(date_format)   #gca - get current

data = pd.read_csv('BitcoinData.csv')
# print(data.head())
data['Date'] = pd.to_datetime(data['Date'])  #to convert string values into date
data.sort_values('Date',inplace = True)

price_date = data['Date']
price_close = data['Close']

plt.plot_date(price_date,price_close,linestyle = '-')

date_format = mpl_dates.DateFormatter('%b, %d %Y')   #formatting the date by my choice
plt.gca().xaxis.set_major_formatter(date_format)

plt.gcf().autofmt_xdate()
plt.title('Bitcoin Prices')
plt.xlabel('Date')
plt.ylabel('Closing Prices')
plt.tight_layout()
plt.show() 