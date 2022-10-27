file_name = 'programming.txt'
with open(file_name,'w') as file_object:
    file_object.write('I love programming')
    #writing multiple lines
    file_object.write(' I want to write code for the rest of my life.\n')
    #the problem with this that python doesn't add new line 
    #to add a new line use \n
    file_object.write('I hate debugging xD')

#'w' -> write
#'r' -> read also default 
#'r+' -> read and write
#'a' -> appending

#appending to a file
with open(file_name,'a') as file_object:
    file_object.write('\nThis is appending :3')
