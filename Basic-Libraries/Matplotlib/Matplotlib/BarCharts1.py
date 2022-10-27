import numpy as np
from matplotlib import pyplot as plt

#print(plt.style.available)   #this will output a list of built-in style 
plt.style.use('fivethirtyeight')


age_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
x_indices = np.arange(len(age_x))                          #np.arange returns ndarray indices. here, 0-9 (Array of evenly spaced values)
width = 0.25                                      #how much distance away from the middle bar the others bar will stand

dev_y = [38496, 42000, 46752, 49320, 53200,           
         56000, 62316, 64928, 67317, 68748, 73752]
plt.bar(x_indices - width, dev_y,label = 'All Devs',width=width)


py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]
plt.bar(x_indices,py_dev_y,label = 'Python Devs',width=width)


js_dev_y = [37810, 43515, 46823, 49293, 53437,
             56373, 62375, 66674, 68745, 68746, 74583]
plt.bar(x_indices + width,js_dev_y,label = 'javascript Devs',width=width)


plt.title('Median salary(USD) by age ')
plt.xlabel('Age')
plt.ylabel('Median Salary (USD)')
plt.xticks(ticks=x_indices, labels=age_x)         #renames the indices of the x-axis by age values. 

plt.legend()

plt.grid(True)        #for adding grid.
plt.tight_layout()    #for padding 

plt.show()
