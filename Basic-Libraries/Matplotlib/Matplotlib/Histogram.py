"""
Histograms are great for breaking your data into bins and seeing where your data falls based on those bins.
when the number of possible items are larger then using bar chart might not be efficacious. Thus try to use 
histogram.
"""
import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('fivethirtyeight')

# ages = [18,19,21,25,26,26,30,38,39,50,40,58]
# bins = [10,20,30,40,50,60]    #five bins with interval of 10 years
# bins = [20,30,40,50]          #this will include the values which lies only in those intervals.

data = pd.read_csv('dataAge.csv')
#print(data.head())
ids = data['Responder_id']
ages = data['Age']

median_age = 29
color = '#fc4f30'

plt.axvline(median_age,color = color,label = 'Age median',linewidth = 2)
plt.legend()

plt.hist(ages, bins=10, edgecolor = 'black',log = True)  #using log to scale values
plt.title('Ages of Responders')
plt.xlabel('Age')
plt.ylabel('Total Responders')
plt.tight_layout()
plt.show()

