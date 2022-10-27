#linePlots
from matplotlib import pyplot as plt

#print(plt.style.available)   #this will output a list of built-in style 
plt.style.use('fivethirtyeight')
#plt.xkcd()                   #based on the comic page

age_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]  #x-axis values

dev_y = [38496, 42000, 46752, 49320, 53200,           #y-axis values
         56000, 62316, 64928, 67317, 68748, 73752]


plt.plot(age_x, dev_y,color = '#444444',linestyle = '--',marker = '*' ,label = 'All Devs',linewidth = 4)

#plt.plot(age_x, dev_y,'--k' ,label = 'All Devs')  #plotting the values 
#format string [marker][line][color]   ex. '--k'
#default is solid line

# plt.title('Median salary(USD) by age ')
# plt.xlabel('Age')
# plt.ylabel('Median Salary (USD)')
# plt.show()               #to show the plot


# Median Python Developer Salaries by Age
#py_dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
# as the age range is similar we will just work on with age_x  list 

py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]


# Median JavaScript Developer Salaries by Age
js_dev_y = [37810, 43515, 46823, 49293, 53437,
             56373, 62375, 66674, 68745, 68746, 74583]

plt.plot(age_x,js_dev_y,color = '#5abf23',label = 'javascript Devs',marker = '*',linestyle = '-.',linewidth = 3)

plt.plot(age_x,py_dev_y,color  = 'r',label = 'Python Devs',linewidth = 2)
plt.title('Median salary(USD) by age ')
plt.xlabel('Age')
plt.ylabel('Median Salary (USD)')

#legend method 1 is error prone because you have to know the order they were added
#plt.legend(['All devs','python'])  #we can pass on a list of labels by the order they were added to the plot

#legend method 2 is more suitable
#which is we can add a label while plotting the data. in that way we don't have to remember the order. and lastly we just need to call the legend method
plt.legend()

plt.grid(True)        #for adding grid.
plt.tight_layout()    #for padding 


plt.savefig('plot.png')         #this will create a .png image in my current directory
plt.show()
