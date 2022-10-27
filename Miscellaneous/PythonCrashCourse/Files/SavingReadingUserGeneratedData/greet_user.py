import json
filename ='SavingReadingUserGeneratedData\save_and_read.txt'

with open(filename,'r') as f_obj:
    username = json.load(f_obj)
    print(f"welcome back {username}!")