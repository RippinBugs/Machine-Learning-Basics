""" stack plots in Matplotlib. Sometimes these are called Area Charts. These are similar to pie charts, 
but instead of showing us the proportions at a single instant, these allow us to see the proportions over a series of points
"""

import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

minutes = [1,2,3,4,5,6,7,8,9]

# player1 = [1,2,3,3,4,4,4,4,5]
# player2 = [1,1,1,1,2,2,2,3,4]
# player3 = [1,1,1,2,2,2,3,3,3]

# labels = ['player 1','player 2','player 3']
colors = ['#6d904f','#fc4f30','#008fd5']

# plt.stackplot(minutes,player1,player2,player3,labels=labels,colors=colors)
# plt.legend(loc = (0.07,0.1))    #we need to call legend() method to show the labels
#loc(0-1,0-1)  that's the range

amit =   [8,3,1,6,0,0,2,2,8]
nileem = [0,3,6,0,2,5,3,4,0]
pasha =  [0,2,1,2,6,3,3,2,0]
labels = ['amit','nileem','pasha']

plt.stackplot(minutes,amit,nileem,pasha,colors=colors,labels=labels)
plt.legend(loc = (0.5,0.7))

plt.title('My Cool Stack Plot')
plt.tight_layout()
plt.show()