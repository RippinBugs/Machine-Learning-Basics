import json

username = input("what's your name?")
filename = 'SavingReadingUserGeneratedData/save_and_read.txt'
with open(filename,'w') as f_obj:
    json.dump(username,f_obj)
    print(f"we will remember you when you come back {username}")
    
