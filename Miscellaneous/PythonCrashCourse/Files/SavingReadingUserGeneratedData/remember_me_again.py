import json

filename = 'SavingReadingUserGeneratedData/save_and_read.json'
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    with open(filename,'w') as f_obj:
        username = input("what's your name? ")
        json.dump(username,f_obj)
        print(f"we'll remember you when you come back! {username}")
else:
    print(f"welcome back! {username}")