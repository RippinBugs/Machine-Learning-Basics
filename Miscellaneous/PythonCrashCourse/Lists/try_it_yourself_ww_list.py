#4.3
for i in range(1,21):
    print(i)

#4.4,4.5
numbers = list(range(1,1000001))
print("the sum is "+str(sum(numbers)))
print('the min is '+str(min(numbers)))
print("the max is "+str(max(numbers)))

#printing without newline in python
for i in range(1,50,2):
    print(i,end=" ")

print('\n')
#using list comprehension to get a list of cubes
cubes = [value**3 for value in range(1,11)]
print(cubes)