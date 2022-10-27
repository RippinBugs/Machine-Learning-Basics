"""
We will learn how to monitor a CSV file that is constantly being updated, and plot the values from that CSV file as they are coming in. 
This can be extremely useful for plotting data coming from APIs or sensors or any other source that will have frequent updates. 
"""

import random 
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

# x_vals = []
# y_vals = []

# index = count()

# """
# This frame number argument can be given a simple parameter like i. 
# That parameter does not have to be used in the function that draws the plot
# """
# def animate(i):
#     x_vals.append(next(index))   #increase the index number by one simultaneously
#     y_vals.append(random.randint(0,5))
    
#     """
#     The matplotlib.pyplot.cla() function clears the current Axes state without closing the Axes. The elements within the Axes 
#     are not dropped, however the current Axes can be redrawn with commands in the same script.
#     """
#     plt.cla()  
#     plt.plot(x_vals,y_vals)

# ani = FuncAnimation(plt.gcf(),animate,interval = 200)    #interval = 1s = 1000ms
    
def animate(i):
    data = pd.read_csv('LiveData.csv')
    x = data['x_val']
    y1 = data['total_1']
    y2 = data['total_2']
    
    plt.cla()
    
    plt.plot(x,y1,label = 'channel 1')
    plt.plot(x,y2,label = 'channel 2')
    
    plt.legend(loc = 'upper left')
    plt.tight_layout()
    
ani = FuncAnimation(plt.gcf(),animate,interval = 1000)
plt.tight_layout()
plt.show()