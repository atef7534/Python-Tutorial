# -----------------------------
# -- Tuple --
# -----------
# [1] Tuple Items Are Enclosed in Parentheses
# [2] You Can Remove The Parentheses If You Want
# [3] Tuple Are Ordered, To Use Index To Access Item
# [4] Tuple Are Immutable => You Cant Add or Delete
# [5] Tuple Items Is Not Unique
# [6] Tuple Can Have Different Data Types
# [7] Operators Used in Strings and Lists Available In Tuples
# -----------------------------

# Tuple Syntax & Type Test

# Create your first tuple 
mytuple = ("one", "two", "three")
print(mytuple)
print(type(mytuple))

mylist = [1, 2, 3]
mylist[0] = 70
print(mylist)

mytuple = list(mytuple)
mytuple[0] = "seventy"
mytuple = tuple(mytuple)
print(mytuple)

print(mytuple[-1])

differentData = (1, True, "True", [24.03, -27, 27], "Ahmed", "Juice")
print(differentData)

mytuple2 = "one", "two", "three", "four"
print(mytuple2)