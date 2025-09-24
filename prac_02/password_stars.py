min_length = 5


def main():
    password = get_password()
    print_password(password)


def print_password(password: str):
    print("*" * len(password))


def get_password() -> str:
    password = input(f"Enter your password of atleast {min_length} characters: ")
    while len(password) < min_length:
        print("Needs to be minimum of 5 characters.")
        password = input(f"Enter your password of atleast {min_length} characters: ")
    return password


main()
