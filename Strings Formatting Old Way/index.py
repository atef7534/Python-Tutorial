# Strings Formatting 

name = "Atif"
age = 24
rank = 10

print("My name is: " + name) 
print("My name is:", name) 

# print("My name is: " + age) # Type Error

# %s => String
# %d => Number
# %f => Float

print("My name is: %s" % "Atif")
print("My name is: %s" % name)
print("I am: %d" % 24)
print("I am: %d" % age)

print("My Name is: %s and My Age is: %d and My Rank is: %f" % (name, age, rank))

num = 10
print("My number is: %d" % num)    # My number is: 10
print("My number is: %f" % num)    # My number is: 10.000000
print("My number is: %.12f" % num) # My number is: 10.00

# Truncate String 
myLongString = "Hello Peoples of Elzero Web School I Love You All"
print("Message is %s" % myLongString)
print("Message is %.5s" % myLongString)

