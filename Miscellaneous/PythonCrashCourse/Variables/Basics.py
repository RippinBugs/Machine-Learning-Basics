"""print('Hello world')
print("this is me amit. who's a computer programmer")
print('Hello "Amit"!')


#putting a message inside a variable
message = "this is amit"
print("\n" +message)

message = 'this is a new message which overrides the previous message'
print(message)

#in python there are few rules regarding the naming convention. You know most of them. So don't worry

#some methods of string(Data type).

name = 'monoarul islam'
#title() --> this method helps you to make the first letter of every word capital.
print(name.title())

#upper(), lower() --> these two methods make the whole string consisting of uppercase and lower case letters respectively.
print(name.upper())
print(name.lower())

# string concatenation can be done by "+" sign.
print("hello, "+name.title()+"!")

#adding whitespace to string with tabs and newlines.
print("we need to buy:\n\tCoffee\n\ttea\n\tsugar\n")

#stripping whitespace --> this strip out extra spaces in terms of your preferences.
#rstrip(),lstrip(),strip()

favorite_language = ' python '
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())
"""

#integer and floats
print(2+5)
a = 2.01 ** 4.03
print(a)

age = 23
name = 'amit'
print(name+"'s age is "+str(age)) #type casting or just transforming that integer value into a string

#  """    """  --> the format of multiple lines comment
#  hash(#) is used for single line comment

# The zen of python (import this, use it in terminal)
