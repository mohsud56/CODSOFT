import random
# List of characters avaliable in the password
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789#&-_()@%/*^!"
# Ask the user for password length
length = int(input("Enter password length: "))
# Initialize empty password string
password = ""
for a in range(length):
    password += random.choice(chars)
# Print the generated password
print("Generated password:", password)
