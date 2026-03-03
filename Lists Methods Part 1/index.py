# -- Lists Methods ---

# append()
myFriends = ["Ahmed", "Mohamed", "Reda"]
myOldFriends = ["Seif", "Mahmoud", "Mohamed"]
myFriends.append("Ebrahim")
print(myFriends)

myFriends.append(100)
myFriends.append(True)
myFriends.append(myOldFriends)
print(myFriends)
print(myFriends[6][0][0])

mylist = [[1, 2, 3, 4]]
print(mylist[0][0])

# extend()
myFriends = ["Ahmed", "Mohamed", "Reda"]
myOldFriends = ["Seif", "Mahmoud", "Mohamed"]

myFriends.extend(myOldFriends)
print(myFriends)
print(myFriends[3][0], myFriends[3][1], myFriends[3][2])

# remove()
myFriends.remove("Ahmed") 
myFriends.remove("Seif") 
print(myFriends)

# sort()
y = [1, 2, 100, 120, -10, 17, 29]
y.sort(reverse=True)
print(y)

# reverse()
z = [10, 1, 9, 80, 100, "Atif", 100]
z.reverse()
print(z)