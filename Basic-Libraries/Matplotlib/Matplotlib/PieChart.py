import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
#print(plt.style.available)
plt.style.use('fast')

data = pd.read_csv('data.csv')
ids = data['Responder_id']
Lang = data['LanguagesWorkedWith']

lang_counter = Counter()
for responses in Lang:
    lang_counter.update(responses.split(';'))

print(lang_counter)

language_name = []
language_occured = []

for i in lang_counter.most_common(7):
    language_name.append(i[0])
    language_occured.append(i[1])

# print(language_name)
# print(language_occured)
explode = [0,0,0,0.1,0,0,0]  #0 means as it is. and whichever we want to explode we put a value ranging from 0-1. it will be of that much of the length of the radius
plt.pie(language_occured, labels = language_name,explode = explode,
        shadow = True,startangle=90,autopct='%1.1f%%', wedgeprops={'edgecolor':'blue'})




# slices = [60,40,30,20]
# labels = ['Sixty','Fourty','ex1','ex2']
# colors = ['red','green','blue','yellow']

# plt.pie(slices,labels=labels,colors = colors,wedgeprops={'edgecolor':'black'})

plt.title('My cool pychart')
plt.tight_layout()
plt.show()

 