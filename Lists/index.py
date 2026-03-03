# --- Lists --- 
names = ["Ahmed", "Mohamed", "Salim"] # method 1

print(names) # []
print(type(names)) # <class 'list'>

names = list(("Ahmed", "Mohamed", "Zeyad", "Mosa", "Maher", "Mostafa")) # method 2
print(names)

# String
myName = "Atif"
myName = str("Atif")
print(myName)

myAge = 24
myAge = int(24)
print(myAge)

myFAge = 24.0
print(myName)
myFAge = float(myFAge)

# Multiple Values 
container = [1, 1.0, -1, -1.0, False, True, "Orange", "Mouse", "Ahmed"]
print(container)

print(container[1])
print(container[6])

print(container[1: 7])
print(container[: 4])
print(container[4: ])

print(container[::1])
print(container[1::2])

# Changeable 
container[0] = "Hello"
print(container)

container[-1] = "Last element"
print(container)

container[0: 3] = ["A"]
print(container)

