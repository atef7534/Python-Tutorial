# -- String methods --

# index()
msg = "My name is Atif."
print(msg.index("i"))
# print(msg.index("At", 3, 11)) # Throw Error
print(msg.index("At", 3, 13))

# find()
msg = "My name is Atif."
print(msg.find("i"))
print(msg.find("At", 3, 11)) # -1
print(msg.find("At", 3, 13))

# rjust()
name = "Atif"
print(name.rjust(10))
print(name.rjust(10, '#'))

# ljust()
name = "Atif"
print(name.ljust(10))
print(name.ljust(10, '-'))

# splitlines()
letter = """First line
Second Line
Third Line"""

print(letter)
print(letter.splitlines())

f = "First Line\nSecond Line\nThird Line"
print(f.splitlines())

one = "I Love Python And 3G"
two = "I Love Python And 3g"

# istitle()
# islower()
# isupper()

print(one.istitle()) # True
print(two.istitle()) # False 

three = " "
four = ""
print(three.isspace())
print(four.isspace())

five = 'i love python'
six = 'I Love Python'
print(five.islower()) # True
print(six.islower()) # False

five = 'I LOVE PYTHON'
six = 'I Love Python'
print(five.isupper()) # True
print(six.isupper()) # False

# isidentifier()
seven = "osama_elzero"
eight = "OsamaElzero100"
nine = "Osama--Elzero100"

print(seven.isidentifier()) # True
print(eight.isidentifier()) # True
print(nine.isidentifier()) # False 

# isalpha()
x = "AaaaaBbbbbb"
y = "AaaaaBbbbbb111"
print(x.isalpha()) # True
print(y.isalpha()) # False

# isalnum()
u = "AaaaaBbbbbb"
z = "AaaaaBbbbbb111"
print(u.isalnum()) # True
print(z.isalnum()) # True

# replace()
a = "Hello One Two Three One One"
print(a.replace("One", "1"))
print(a.replace("One", "1", 1))
print(a.replace("One", "1", 2))

# join()
print(", ".join(["My", "name", "is", "Atif"]))
