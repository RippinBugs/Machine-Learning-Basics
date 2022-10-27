"""
#simple program with a while loop
current_number = 1
while current_number <= 5:
    print(current_number,end=" ")
    current_number+=1

#letting the user choose when to quit
prompt = "\nTell me something, and i will repeat after you"
prompt+="\nEnter 'quit' to end the program "
message = ""
while message.lower() != 'quit':
    message = input(prompt)
    if message.lower() != 'quit':
        print(message)
"""

"""
#The same program but this time by using a flag
prompt = "\nTell me something, and i will repeat after you"
prompt+="\nEnter 'quit' to end the program "
flag = True
message = ""
while flag:
    message = input(prompt)
    if message.lower() != 'quit':
        print(message)
    else:
        flag = False
"""

"""
#using break and continue
#for break, this will print from 1 to 5
#for continue, this will go back to looping 
i = 1
while i < 30:
    if i == 6:
        break
    elif i == 3:
        i+=1
        continue
    else:
        print(i,end=" ")
        i+=1
"""

"""
#removing all instances of specific values from a list
pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']
while 'cat' in pets:
    pets.remove('cat')

print(pets)
"""

#filling a dictionary with user inputs
responses = {}
polling_active = True
while polling_active:
    name = input("Enter the name: ")
    response = input("where do you wanna go next: ")

    responses[name] = response
    poll_taker = input('would you like to let another person respond?(y/n)')
    if poll_taker == 'n':
        polling_active = False
for name, response in responses.items():
    print(f"{name} wants to go to {responses[name]}")
