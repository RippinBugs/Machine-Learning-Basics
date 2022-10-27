# #print(5/0)
# #exception handling
# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("you can't divide by Zero")

#Using exceptions to prevent crashes
print('Give me two numbers and i\'ll divide them')
print('Enter "q" to quit')
i = 0
while True:
    first = input('first number: ')
    if first == 'q':
        break
    second = input('second number: ')
    if second == 'q':
        break
    try:
        answer = int(first)/int(second)
    except ZeroDivisionError:
        print('You can\'t divide a number by zero')
    else:
        print(f'the result is: {answer}')
    i+=1

print(f'you have divide {i} times')