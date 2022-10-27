"""
#for loop
magicians = ['alice','david','carolina']
for magician in magicians:
    print("Hello " +magician.title()+"!")
    print("your tricks are cool\n")
print("Done with for loop")

#making numerical lists
for number in range(1,6):
    print(number)

#using range() to make a list of numbers
numbers = list(range(1,7)) #this list will have values from 1 to 6 
for number in numbers:
    print(number)
"""

squares = []
for value in range(1,6):
    squares.append(value**2)
print(squares)

#this above using list comprehension
squares = [value**2 for value in range(1,6)]

#slicing a list
print(squares[:])
print(squares[2:7])
print(squares[-3:])
print(squares[-1:])

#looping through a slice
for i in squares[2:6]:
    print(i,end=" ")
print('\n')
#copying squares into another list
newsquares = squares[:]
#Don't use newsquares = squares because it will set both the variables point to same location. 

#Tuple
#it's immutable. 
dimensions =(200,50,8)
print(dimensions[0])

for dimension in dimensions:
    print(dimension,end=" ")
print('\n')

#but you can completely override the tuples value. this is not worth mentioning.
dimensions = (100,3,4)
print(dimensions)