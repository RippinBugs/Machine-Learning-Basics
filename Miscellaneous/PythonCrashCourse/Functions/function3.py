#passing arbitrary number of arguments.
#the asterisk * in the parameter tells python to make an empty "tuple" and pack every value it recieves into the tuple.
def make_pizza(*toppings):
    "print the list of toppings that have been requested"
    print("making a pizza with following toppings ")
    for topping in toppings:
        print("\t - " + topping)

make_pizza('black olive')
make_pizza('mushrooms','tomato','fries','pineapple')

#mixing positional and arbitrary arguments
def make_pizza(size , *toppings):
    "print the list of toppings that have been requested"
    print(f"making a {size} inch pizza with following toppings ")
    for topping in toppings:
        print("\t - " + topping)

make_pizza(12, 'black olive')
make_pizza(16, 'mushrooms','tomato','fries','pineapple')

#Using arbitrary keyword arguments
#the double asterisk creates a dictionary and store all the key=value argument in it.
def build_profile(first,last,**user_info):
    full_name = first + " " +last
    bp_dict={'first_name' : first,'last_name' : last}
    for key,value in user_info.items():
        bp_dict[key] = value
    return full_name,bp_dict

f_name, user_profile = build_profile('monoarul','islam',location = 'Khulna',field = "CSE",age = 24)
print(f"{f_name}'s user infos are given below {user_profile}")