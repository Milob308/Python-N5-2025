password = input("Please enter your password: ")
while len(password) < 8:
    print("Error, try a password with over 8 characters.")
    password = input("Please enter your password: ")
print("Password accepted.")
