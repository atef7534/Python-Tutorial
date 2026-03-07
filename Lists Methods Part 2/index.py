# clear()
a = list(range(1, 5))
print(a)
a.clear()
print(a)

# copy()
b = [1, 2, 3, 4]
c = b.copy()
print(c)
b.append(5)
print(c)


# count()
print(b.count(1))

# index()
print(b.index(3))

# insert()
b.insert(1, "Atif")
print(b)

# pop()
b.pop("Atif")
print(b)