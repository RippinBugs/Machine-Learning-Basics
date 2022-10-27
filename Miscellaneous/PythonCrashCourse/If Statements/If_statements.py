#simple if problem
cars = ['audi','bmw','subaru','toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

#checking for inequalities
requested_toppings = 'mushrooms'
if requested_toppings != 'anchovies':
    print("hold the anchovies")

#checking whether a value is in the list or not
# we use "in" for the value which is in the list 
print('audi' in cars)

#we use "not in" for value which is not in the list
print('audi' not in cars)

#if-elif-else chain
age = 17
if age < 4:
    price = 0
elif age < 12:
    price = 5
else:
    price = 10
print("you need to pay "+str(price))

#this code is nice
available_toppings = ['mushrooms','olives','green peppers',
'pepperoni','pineapple','extra cheese']
requested_toppings = ['mushrooms','fries','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("adding "+requested_topping +".")
    else:
        print("sorry, we don't have " + requested_topping + '.')
    
print("Finished making your pizza")

