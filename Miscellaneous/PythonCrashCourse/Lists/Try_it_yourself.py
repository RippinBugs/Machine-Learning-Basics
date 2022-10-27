"""
#3.1,3.2,3.3(easy)
friends_name = ['nileem', 'pasha', 'sakib']
print(friends_name[0])
print(friends_name[1])
print("welcom to the club " +friends_name[2].title())

#3.4,3.5,3.6,3.7(in brief)
guests = ['mayen','pasha','sakib']
print("come to the dinner "+ guests[0].title())
not_attending = guests[0]
print("He won't be able to come to dinner " + not_attending+" so i'm invitin nileem")
guests.pop(0)
guests.append('nileem')
print("these are my final list of guests")
print(guests)

print("i found a bigger table so im gonna invite some more of my freinds")
guests.insert(0,'hafiz')
guests.insert(2,'rameez')
guests.append('mahian')

print(guests)
guests.pop()
guests.pop()
del guests[1]
print(guests)

"""
#3.8,3.9,3.10
tour = ['USA','UK','Germany','France','Nepal']
print(tour)
print(sorted(tour))
print(tour)
print(sorted(tour,reverse=True))

print(tour)
tour.reverse()
print(tour)
tour.reverse()
tour.sort()
print(tour)
tour.sort(reverse=True)
print(tour)