# User Input

# Wallet system 

# Get a phone number from the user 
# print("Enter your phone number: ", end="")
phone_number = input("Enter your phone number: ").strip()

RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
ENDC = '\033[0m'

print(f"{GREEN}User phone number = {phone_number}{ENDC}")
print(len(phone_number))

temp_number = input("Enter your temporary number: ").strip()
print(f"{GREEN}Your temporary number = {temp_number}{ENDC}")

money_needed = input("Enter your amount of money: ").strip()
print(f"{GREEN}Your needed money = {money_needed}{ENDC}")
