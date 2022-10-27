#a simple dictionary.
#consists of a key-value pair
alien_0 = {'color':'green','point':5}
print(alien_0['color'])
print(alien_0['point'])

#adding new key-value pairs
#in dictionaries we don't append. Instead we insert a value for a certain key using []
alien_0['x_position'] = 120
alien_0['y_position'] = 30

print(alien_0)

#modifying value in a dictionary
alien_0['color'] = 'yellow'
print(alien_0)

#removing a key-value pair. Use del statement
del alien_0['color']
print(alien_0)

#looping through a dictionary
#the method items return a list of key-value pairs
user_0 = {'username': 'amit','first':'monoarul','last':'islam'}
for key,value in user_0.items():
    print('key : '+key)
    print('value:'+value)

#looping through all the keys in dictionary
#by default to loop through you don't need to call the method keys() for the key values
#for key in user_0:       ##both are same
for key in user_0.keys():
    print(f"key is {key}")

#for looping through all the values call the method values()

#a small program for fun.
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'python',
    'phil':'ruby'
}

friends = ['jen','sarah']
for friend in friends:
    print("friend's name is :"+friend)
    if friend in favorite_languages:
        print("Hi! " + friend +" ,i See your favorite language is "+favorite_languages[friend])


#looping through a dictinary keys in order
for key in sorted(favorite_languages.keys()):
    print(key)

#a set is list which contains only unique values.
#here we use set() function to do this.
print(set(favorite_languages.values()))

#Nesting
#a list of dictionaries.
aliens = []
for new_alien in range(30):
    new_alien = {'color':'green','points':5}
    aliens.append(new_alien)

#that's tricky but ezz
for i in aliens[0:5]:
    for x in i.keys():
        print(i[x])

#another short program.
users = {
    'aEinstein':{
        'first' : 'albert',
        'last' : 'einstein',
        'location' : 'princeton'
    },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris'
    }
}

for username,user_info in users.items():
    print(username + "'s full name is "+user_info['first'] +" "+user_info['last']+"!")
    print("he lived in " + user_info['location'])
    