import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')
data = pd.read_csv('fill.csv')
#print(data.head())

ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

plt.plot(ages,dev_salaries,color = '#444444',linestyle = '--',label = 'All Devs')
plt.plot(ages,py_salaries,color = 'r',linestyle = '-.',label = 'Python Devs')
#plt.plot(ages,js_salaries,color='b',linestyle = '-',label = 'js Devs')

overall_median = 57287

# plt.fill_between(ages,py_salaries,alpha=0.6)
# plt.fill_between(ages,py_salaries,overall_median,
#                  where = (py_salaries > overall_median),
#                  interpolate = True, alpha=0.25)   #alpha works as opacity  (x,y1,y2)

# plt.fill_between(ages,py_salaries,overall_median,
#                  where = (py_salaries <= overall_median),
#                  interpolate = True, color = 'k', alpha=0.25)

plt.fill_between(ages,dev_salaries,py_salaries,alpha = 0.4, label = 'Python - Above avg',
                 where=(py_salaries > dev_salaries),interpolate=True)
plt.fill_between(ages,dev_salaries,py_salaries,alpha = 0.4, label = 'Python - Below avg',
                 where=(py_salaries <= dev_salaries),interpolate=True)

plt.legend()

plt.title('Median Salary (USD) by age')
plt.grid(True)
plt.ylabel('salary')
plt.xlabel('Age')
plt.tight_layout()
plt.show()