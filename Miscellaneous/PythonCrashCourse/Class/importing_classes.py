from collections import OrderedDict
#this import helps the dictionary values to execute in order
favorite_languages = OrderedDict()
favorite_languages['jen'] = 'python'
favorite_languages['amit'] = 'c++'
favorite_languages['mahi'] = 'javascript'

for key,value in favorite_languages.items():
    print(f"{key}'s favorite language is {value}")