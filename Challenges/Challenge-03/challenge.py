# 🧠 Challenge 1 — Sentence Analyzer
# Objective:
# Write a Python program that asks the user for a sentence then prints:
## The original sentence
## The reversed sentence
## How many uppercase letters the sentence has
## How many lowercase letters the sentence has
## How many words are in the sentence

# --------------------------------------------------------------------

### Output
# Original: Hello World
# Reversed: dlroW olleH
# Uppercase Count: 2
# Lowercase Count: 8
# Word Count: 2

# Ask the user to enter the sentence 
userSentence = input("Enter your sentence: ")

# Print the original sentence 
print("Original: " + userSentence)

# Print the reversed sentence 
print("Reversed: " + userSentence[::-1])

# Print the number of uppercase letters 
# My name is Atif 
cnt = 0

for letter in userSentence:
    if letter.isupper(): # True | False 
        cnt = cnt + 1 

print("Uppercase Count: " + str(cnt))

# Print the number of lowercase letters 
cnt = 0
for letter in userSentence:
    if letter.islower(): # True | False 
        cnt = cnt + 1 
        
print("Lowercase Count: " + str(cnt))

# Print how many words
words = len(userSentence.split(" "))
print("Word Count: " + str(words))