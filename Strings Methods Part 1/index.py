a = "          I Love Python and CPlusPlus.           "

# strip()
# rstrip()
# lstrip()

print(a.strip())
print(a.rstrip())
print(a.lstrip())

a = "#####I Love Python####"
print(a.strip("#"))
print(a.lstrip("#")) 
print(a.rstrip("#")) 

a = "@#@#@#I Love Python@#@#@#"
print(a.strip("#@"))
print(a.lstrip("#@")) 
print(a.rstrip("#@")) 

# title()
b = "I Love 2d Graphics and 3g Technology and python"
print(b.title())
print("my name is mohamed.".title())

# capitalize()
print(b.capitalize())

# upper()
print(b.upper())

# lower()
print(b.lower())

# zfill()
c, d, e, f = "1", "11", "111", "1111"
print(c.zfill(5))
print(d.zfill(5))
print(e.zfill(5))
print(f.zfill(5))

print("Osama".zfill(15))