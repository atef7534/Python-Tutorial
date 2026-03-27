# Set methods 
a = {1, 2, 3, 4, 5}
b = {1, 2, 3, "Atif", "Ali"}

# Difference 
print(a.difference(b))
print(b.difference(a))
print(b - a)

print("=" * 40)  # Separator

# Difference Update 
a.difference_update(b)
print(a)
a = {1, 2, 3, 4, 5}
b.difference_update(a)
print(b)

# Intersection 
a = {1, 2, 3, 4, 5}
b = {1, 2, 3, "Atif", "Ali"}

print("=" * 40)  # Separator

# Intersection Update
print(a.intersection(b))
print("Middle:", a & b)
a.intersection_update(b)
print(a)

print("=" * 40)  # Separator

# Symmetric Difference 
i = {1, 2, 3, 4, 5, "X"}
j = {"Osama", "Zero", 1, 2, 4, "X"}
print(i.symmetric_difference(j))
print(i ^ j)

# Symmetric Difference Update
i.symmetric_difference_update(j)
print(i)

# issuperset()
# issubset()
# isdisjoint()

# Try them out 😊

