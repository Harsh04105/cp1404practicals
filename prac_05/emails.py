"""
Emails
Estimate: 30 minutes
Actual:   36 minutes
"""


def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        correct_name = input(f"Is your name {name}? (Y/n)")
        if correct_name.upper() != "Y" and correct_name != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def get_name_from_email(email: str) -> str:
    parts = email.split("@")[0].split(".")
    name = " ".join(parts).title()
    return name

main()