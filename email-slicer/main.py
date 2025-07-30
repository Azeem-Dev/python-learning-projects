"""THIS IS THE SIMPLEST VERSION WITHOUT METHODS AND VALIDATION"""

# email = input("Enter your email")

# index = email.index("@")

# username = email[:index]

# domain = email[index+1:]

# print(f"Your username is {username} and domain is www.{domain}")

"""END"""


"""BELOW IS THE REFINED VERSION OF THE EMAIL SLICE"""


def validateEmail(email: str) -> bool:
    if "@" in email:
        return True
    else:
        return False


def SliceEmailToUserNameAndDomain(email: str) -> list[str]:
    return email.split("@")


def main():
    email = input("Enter your email: ")
    if validateEmail(email):
        username, domain = SliceEmailToUserNameAndDomain(email)
        print(f"Your username is: {username} and domain is www.{domain}")
    else:
        print("Your email is not valid. Please enter a valid email address.")


main()
