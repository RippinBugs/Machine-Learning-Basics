import csv
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from collections import Counter

plt.style.use('fivethirtyeight')

# data = pd.read_csv('data.csv')
# ids = data['Respnder_id']
# lang_respones = data['LanguagesWorkedWith']
# lang_counter = Counter()
# for response in lang_respones:
#     lang_counter.update(response.split(';'))
    

with open('data.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    language_counter = Counter()
    
    #row = next(csv_reader)
    #print(row)
    #print(row['LanguagesWorkedWith'].split(';'))  #returns a list of programming languages
    
    for row in csv_reader:
        language_counter.update(row['LanguagesWorkedWith'].split(';'))
        

#print(language_counter.most_common(15))     
languages = []
popularity = []
for item in language_counter.most_common(15):    #list of tuples
    languages.append(item[0])
    popularity.append(item[1])
    
    
# print(languages)
# print(popularity)

languages.reverse()     
popularity.reverse()    #this reverse() method works in-place meaning we don't need to assign it to languages or popularity list again

#plt.bar(languages,popularity)   #there is a great number of languages and the x-axis is overwhelmed with the names. so use horizontal bar method instead
plt.barh(languages,popularity,height=0.4)   #barh(y,x)
plt.xlabel('Popularity')
#plt.ylabel('Languages')
plt.title('Developers Favorite Languages')
plt.tight_layout()
plt.grid(False)
plt.show()