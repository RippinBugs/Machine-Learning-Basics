from name_function import get_formatted_name
print("Enter 'q' at anytime to quit")
while True:
    first = input("enter first name: ")
    if first == 'q':
        break
    mid_getter = input('do you want to enter a middle name? ("y/n")')
    if mid_getter == 'y':
        middle = input("enter middle name: ")
    else:
        pass
    last = input("enter last name: ")
    if last == 'q':
        break
    formatted_name = get_formatted_name(first,last,middle)
    print(formatted_name)