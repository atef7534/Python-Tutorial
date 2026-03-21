mytuple1 = ("Atif",)
mytuple2 = "Atif",

print(mytuple1)
print(mytuple2)

print(len(mytuple1))
print(len(mytuple2))

a = (1, 2, 3, 4, 5)
b = (6, 7)
c = a + b
d = a + ("A", "B", True) + b 

print(c)
print(d)

myString = "Osama"
myList = [1, 2]
myTuple = ("A", "B")

print(myString * 6)
print(myList * 6)
print(myTuple * 6)

myTuple = ("A", "C", "D", "E", "A", "B", "A", "D")
print(myTuple.count("B")) # 2
print(myTuple.index("B")) # 1


print("The Position of Index Is: {:d}".format(myTuple.index("E")))
print(f"The Position of Index Is: {myTuple.index('C')}")

a = ("A", "B", 4, "C")
x, y, z, w = a 

print(x)
print(y)
print(z)
print(w)

mylist = [1, 2, 3]
mytuple = tuple(mylist)