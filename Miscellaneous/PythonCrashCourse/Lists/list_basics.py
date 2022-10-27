#creating a list
bicycles = ['trek','cannondale','redine','specialized']
print(bicycles)

#a list can also be empty
empty_list = []
print(empty_list)

#accessing elements in a list (first and last one)
#index position starts at 0, not 1.
#That's why sometimes you may encounter "off by one Error"
print(bicycles[0])
print(bicycles[-1])

message = 'my first bycylce was ' + bicycles[0].title()
print(message)

#modifying elements in a list
#As lists are mutable you can override informations.
bicycles[0] = 'road'
print(bicycles)

#adding elements to a list
#Using append() method to add another data in the list
bicycles.append('trek')
print(bicycles)

#inserting elements into the list
#Using insert() method we can specify the location and what to insert in that location.
bicycles.insert(1,'olympic')
print(bicycles)

#removing an element using del statement, it deletes completely
del bicycles[1]
print(bicycles)

#also we can use the pop method. But in pop() it lets you work with it later
last_item = bicycles.pop()
print("The last one I bought is " + last_item.title())
print(bicycles)

#popping items from any position in the list.
#also one can use pop() to remove element from certain location. In that case, just give a value to the attribute
bicycles.pop(2)
print(bicycles)

#removing an item by value. if the value appears several times, only the first occurrence will be removed.
#remove() method lets you do this.
bicycles.remove('road')
print(bicycles)

#organizing a list(permanently)
ls = [1,2,5,3,5,7,8]
ls.sort()
print(ls)
#reversing a list
ls.sort(reverse=True)
print(ls)

#Sorting a list temporarily with sorted() function
print(sorted(ls))
print(ls)

#printing a list in reverse order,it doesn't sort, it just print in the reverse direction
ls.reverse()
print(ls)

#finding the length of a list,using len() function.
print(len(ls))