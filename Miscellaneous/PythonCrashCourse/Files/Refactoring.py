import json

def get_stored_username():
    filename = 'name.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username
    
def get_new_user():
    username = input("What is your name? ")
    filename = 'name.json'
    with open(filename,'w') as f_obj:
        json.dump(username,f_obj)
        return username
        
def greet_user():
    username = get_stored_username()
    if username:
        print(f"the name of the user is {username}")
    else:
        username = get_new_user()
        print(f"the name of the user is {username}")
        
greet_user()