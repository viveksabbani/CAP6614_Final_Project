# false negative case in bandit

import re

def check_username(username):
    """
    Validate username with a regex that could be vulnerable to ReDoS.
    """
    pattern = r"^(a+)+$"
    if re.match(pattern, username):
        print("Valid username")
    else:
        print("Invalid username")

if __name__ == "__main__":
    user_input = input("Enter your username: ")
    check_username(user_input)
