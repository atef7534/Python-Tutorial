# clear()
a = {1, 2, 3}
a.clear()
print(a)

# union()
set1 = {"Mohamed", "Ahmed"}
set2 = {"Atif", "Ebrahim"}
set3 = {1.0, 25}
print(set1.union(set2, a))
print(set1 | set2 | set3)

# add()
set1.add("Reda")
set1.add(1)
set1.add(1)
print(set1)

# copy()
set2 = set1.copy()
set2.add("Welcome")
print(set2)
print(set1)

# remove()
set1.remove("Reda")
# set1.remove("Reda") 
print(set1)

# discard()
set1.discard(1)
set1.discard(1)
print(set1)

# pop()
set1.pop()
print(set1)

# update()
set1.update(["My name is Atif 😊"])
print(set1)
