def count_words(filenames):
    for filename in filenames:
        try:
            with open(filename,'r') as file_object:
                contents = file_object.read()
        except FileNotFoundError:
            print("unfortunately, the file "+ filename +" doesn't exist ")
            #to fail silently use pass statement 
        else:
            words = contents.split()
            length = len(words)
            print(f"The file {filename} has {length} words")
        
filenames = ['alicee.txt','amit.txt','programming.txt']
count_words(filenames)