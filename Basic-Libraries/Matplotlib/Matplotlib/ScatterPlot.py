"""
Scatter plots are great for determining whether two sets of data are correlated. If there is a correlation, 
scatter plots allow us to spot these trends. 
"""
from turtle import color
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('seaborn')


#demo code
# x = [1,2,3,3,2,1,5,6,1,6,7,1]
# y = [12,12,15,51,53,62,6,3,7,10,111,67]

# colors = [2,1,5,18,3,6,0,13,17,10,11,7]   #think about this as intensity 

# sizes = [205,155,200,311,100,105,159,200,180,110,70,120]

# plt.scatter(x,y,s = sizes, c = colors,cmap = 'Greens',marker='p',edgecolor = 'k',linewidth=1,alpha = 1)

# cbar = plt.colorbar()
# cbar.set_label('Satisfaction level')
# #plt.scatter(x,y,s = 150,c = 'green',marker='*',edgecolor = 'k',alpha= 0.75,linewidth= 1)       #s means size,linwidth is the width of the edge of the markers

data = pd.read_csv('YoutubeData.csv')
print(data.head())

viewsX = data['view_count']
likesY = data['likes']
ratio_bar = data['ratio']

#plt.scatter(viewsX,likesY,c=ratio_bar,cmap='Greens',edgecolor='orange',linewidth=1,alpha=1)
#to make it look a bit better use logarithmic scaling
plt.scatter(viewsX,likesY,c=ratio_bar,cmap='summer',edgecolor='orange',linewidth=1,alpha=1)
plt.xscale('log')
plt.yscale('log')

cbar = plt.colorbar()
cbar.set_label('Like/Dislike Ratio')

plt.title("Scatter Plot")
plt.xlabel('Views')
plt.ylabel('Likes')
plt.tight_layout()
plt.show()