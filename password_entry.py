"""
Brodie Windle
"""


MIN_LENGTH = 2
MAX_LENGTH = 15

password = input("Please enter a Password: ")

while MIN_LENGTH > len(password) < MAX_LENGTH:
    password = input("Please enter a Password: ")

print(len(password)*"*")
