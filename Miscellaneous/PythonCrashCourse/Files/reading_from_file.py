# #we need open to access the file first
# #with open() python will know when it is time to close the file
# #that's the magic of it.
# with open ('read.txt') as file_object:
#     contents = file_object.read()
#     print(contents)

# #but with this above code read() returns an empty string when it reaches the end of the line
# #to get a output without a new line at the end of the string we can use rstrip()
# file_name = 'read.txt'
# with open(file_name) as f_obj:
#     contents = f_obj.read()
#     print(contents.rstrip())

#on windows if your file doesn't exist inside the working folder you need to specify a file_path
#a demo is given below
# file_path = 'C:\Users\User\Desktop\PythonCrashCourse\demo.txt'

''' #reading line by line
file_name = 'read.txt'
with open(file_name) as file_object:
    for line in file_object:
        print(line.strip()) '''

# #making a list of lines from a file
# file_name = 'read.txt'
# with open(file_name) as file_object:
#     lines = file_object.readlines()

# for line in lines:
#     print(line.strip())

# pi_string = ''
# for line in lines:
#     pi_string += line.strip()

# print(pi_string)
# print(len(pi_string))


#is my birthday in pi
def birthday_in_pi(birthday):
    file_name = 'pi_million_digits.txt'
    with open(file_name) as file_object:
        lines = file_object.readlines()
        contents = ' '
        #print(contents.strip())
        for line in lines:
            contents += line.strip()
        if birthday in contents.strip():
            print("yeah")
        else:
            print("naah")
        

birthday_in_pi(birthday='120372')
