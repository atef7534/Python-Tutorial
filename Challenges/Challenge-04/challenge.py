# 🧠 Python Challenge — Strings Only (Until Lesson 18)

# You have the following text variable
# And you need to solve the tasks next to it
text = "  eLzErO wEb sChOoL  "

# Tasks

# Task 1: Remove spaces
# Expected Output: 'eLzErO wEb sChOoL'
# WRITE YOUR CODE HERE 
text = text.strip(" ")
print(text)

# Task 2: Fix the case
# Expected Output: 'Elzero web school'
# WRITE YOUR CODE HERE 
text = text.capitalize()
print(text)

# Task 3: Get Specific Letters
# Expected Output: 'E' then 'l' in a new line.
# WRITE YOUR CODE HERE
print(text[0])
print(text[1])

# Task 4: Slice the word
# Expected Output: 'web'
# WRITE YOUR CODE HERE 
print(text[7: 10])

# Task 5: Count letters
# Expected Output: '17'
# WRITE YOUR CODE HERE 
print(len(text))

# Task 6: Replace
# Expected Output: 'Elzero web academy'
# WRITE YOUR CODE HERE
text = text.replace("school", "academy")
print(text)

# Task 7: String formatting
# Expected Output: 'Welcome to Elzero Web Academy'
# WRITE YOUR CODE HERE
print(f"Welcome to {text}")
print("Welcome to {}".format(text))

# END 🥳