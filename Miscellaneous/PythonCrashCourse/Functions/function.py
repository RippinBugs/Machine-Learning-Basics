"""
def greet_user():
    message = input("name: ")
    print("Hello " + message)

greet_user()
"""

"""
#passing information to a function
#here user_name is a parameter and 'amit' is an argument
def greet_user(user_name):
    print("Hello " + user_name)

greet_user('amit')
"""

"""
#passing arguments
#this is an example of positional arguments. In this case, order matters.
def describe_pet(animal_type,pet_name):
    
    #This is a function which displayes a pet name of a certain type of an animal
    
    print(f"my {animal_type}'s name is {pet_name}")

describe_pet('hamster','harry')
describe_pet('dog','wilie')
"""

#keyword argument
#in this process there will be less confusion regarding parameters and arguments.
"""
def describe_pet(animal_type,pet_name):
     print(f"my {animal_type}'s name is {pet_name}")

describe_pet(animal_type = 'hamster',pet_name = 'harry')
"""

#default values
#put the default value parameter in the last always.
"""
def describe_pet(pet_name,animal_type='dog'):
    print(f"my {animal_type}'s name is {pet_name}")

describe_pet('harry')
describe_pet('mike','cat')
"""

#equivalent fn calls
#a hamster named harry.

#describe_pet('harry','hamster')
#describe_pet(pet_name='harry',animal_type="hamster")
#describe_pet(animal_type='hamster',pet_name="harry")

#Return values
def get_formatted_name(first,last,middle_name = ''):
    "return a full name, neatly formatted"
    if middle_name:
        full_name = first + ' ' + middle_name + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name

name = get_formatted_name('monoarul','amit','islam')
print(name)
name = get_formatted_name('monoarul','islam')
print(name)

#returning a dictionary
def build_person(first_name,last_name,age=''):
    bp_dict = {'first':first_name, 'last':last_name}
    if age:
        bp_dict['age'] = age
    return bp_dict
print(build_person('monoarul','islam',24))