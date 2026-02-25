# Strings Formatting New Ways 
name = "Atif"
age = 24
rank = 10

print("My Name is: " + name)
# print("My Name is: " + name + " and My Age is: " + age)  # Type Error

print("My name is: {}".format("Atif"))
print("My name is: {}".format(name))
print("I am: {}".format(age))
print("My rank is: {}".format(rank))
print("My Name is: {} My Age: {}".format(name, age))
print("My Name is: {:s} Age: {:d} & Rank is: {:f}".format(name, age, rank))

# {:s} => String
# {:d} => Number
# {:f} => Float

n = "Atif"
l = "Python"
y = 10
print("My Name is {} Iam {} Developer With {:d} Years Exp".format(n, l, y))


myNumber = 10
print("My Number is: {:d}".format(myNumber))
print("My Number is: {:f}".format(myNumber))
print("My Number is: {:.2f}".format(myNumber))


# Truncate String
myLongString = "Hello Peoples of Elzero Web School I Love You All"
print("Message is {}".format(myLongString))
print("Message is {:.5s}".format(myLongString))
print("Message is {:.13s}".format(myLongString))

hugeNumber = 239472983749823749823757823478
print("My number is: {:d}".format(hugeNumber))
print("My number is: {:_d}".format(hugeNumber))
print("My number is: {:,d}".format(hugeNumber))

# Rearrange Items 
a, b, c = "One", "Two", "Three"
print("Hello {} {} {}".format(a, b, c))  # Hello One Two Three
print("Hello {1} {2} {0}".format(a, b, c))  # Hello Two Three One
print("Hello {2} {0} {1}".format(a, b, c))  # Hello Three One Two

x, y, z = 10, 20, 30
print("Hello {} {} {}".format(x, y, z))
print("Hello {1:d} {2:d} {0:d}".format(x, y, z))
print("Hello {2:f} {0:f} {1:f}".format(x, y, z))
print("Hello {2:.2f} {0:.4f} {1:.5f}".format(x, y, z))


myName = "Atif Yasser"
myAge = 24

print(f"Hello, My name is {myName} and I am {myAge} years old.")