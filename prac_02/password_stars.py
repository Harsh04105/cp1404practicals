min_length = 5
password = input(f"Enter your password of atleast {min_length} characters: ")
while len(password) < min_length:
    print("Needs to be minimum of 5 characters.")
    password = input(f"Enter your password of atleast {min_length} characters: ")

print("*" * len(password))