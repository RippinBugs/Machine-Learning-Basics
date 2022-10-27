"""
#how the input() works
message = input("Enter your name: ")
print(message)

#using int()
number = int(input("enter a number : "))
print(number)
"""

"""
#when your prompt is big you can divide it into separate lines
prompt = "Hello there, how are you."
prompt+= "Enter something"
message = input(prompt)
print(message)
"""

#a small program
age = int(input("enter your age: "))
if age < 18:
    print("you are a kid, amit")
else:
    print("OH no, you are an adult")