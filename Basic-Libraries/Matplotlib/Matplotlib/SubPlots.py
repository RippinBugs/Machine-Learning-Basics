import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('seaborn')

data = pd.read_csv('fill.csv')
#print(data.head())

ages = data['Age']
dev_sal = data['All_Devs']
py_sal = data['Python']
js_sal = data['JavaScript']

fig, (ax1,ax2) = plt.subplots(nrows=2,ncols=1, sharex=True)   #unpacking list of values
#sharex will only label the x axis ticks once

# fig1, ax1 = plt.subplots()
# fig2, ax2 = plt.subplots()
# #This will create create two figures

ax1.plot(ages,dev_sal,label = 'All Devs',linestyle = '-.')
ax2.plot(ages,py_sal,label = 'Python Devs')
ax2.plot(ages,js_sal,label = 'JS Devs',linestyle = '--',color = 'orange')

ax1.legend()
ax1.set_title("All Devs")
ax1.set_ylabel('Median Salary(USD)')

ax2.legend()
ax2.set_xlabel('Ages')
ax2.set_ylabel('Median Salary(USD)')

plt.tight_layout()

plt.show()

# fig1.savefig('fig1.png')
# fig2.savefig('fig2.png')