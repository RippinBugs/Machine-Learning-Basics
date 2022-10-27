"""
#aliencolor 5.3-5.6
alien_color = 'red'
if alien_color == 'green':
    print('player just earned 5 points')
else:
    pass #this is like a null statement in python.


#5.8
user_names = ['admin','amit','fizz','sifat','alvi']
for user in user_names:
    if user == 'admin':
        print("Hello admin,would you like to see the status report?")
    else:
        print(f"Hello {user}, thank you for logging in again")
"""
#5.9
user_names = []
if user_names:
    for user in user_names:
        if user == 'admin':
            print("Hello admin,would you like to see the status report?")
        else:
            print(f"Hello {user}, thank you for logging in again")
else:
    print("we need some users.") 

#5.10
current_users = ['amit','mayen','fizz','sakib','adel','sifat','alvi']
new_users = ['amit','mahian','fizz','abid','fardin']
for username in new_users:
    if username.lower() in current_users:
        print(f"{username} needs to enter a new user name")
    else:
        print("The username is available")


