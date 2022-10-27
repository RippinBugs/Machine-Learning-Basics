file_name = 'alicee.txt'

try:
    with open(file_name,'r') as file_object:
        contents = file_object.read()
except FileNotFoundError:
    msg = 'sorry, the file ' + file_name + 'doesn\'t exit'
    print(msg)
else:
    #count the approximate number of words in the file
    words = contents.split()
    num_of_words = len(words)
    print(f"Total no of words is {num_of_words}")
    

title = 'my name is amit'
x = title.split()
print(x)