msg = "I love football and watching videos."

# split()
print(msg.split(" "))

msg = "I-love-football-and-watching-videos."
print(msg.split("-"))

# rsplit()
print(msg.rsplit("-", 3))

# center()
name = "Atif"

print(name.center(10))
print(name.center(10, "*"))
print(name.center(20, "-"))

# count()
msg = "I love football and watching videos. I love watching football matches."

print(len(msg))
print(msg.count("football"))
print(msg.count("videos"))
print(msg.count("I"))
print(msg.count("football", 0, 62))

# swapcase()
msg = "I love football and watching videos. I love watching football matches."

print(msg.swapcase())

# startswith()
msg = "I love football and watching videos. I love watching football matches."

print(msg.startswith("football", 7, 69))

# endswith()
msg = "I love football and watching videos. I love watching football matches."

print(msg.endswith("matches."))
print(msg.endswith("l", 7, 15))