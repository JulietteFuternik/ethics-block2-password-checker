# ---- Juliette's Password Strength Checker ----

# Juliette Futernik
# u1189692
# CS 3090, Spring 2026
# 2/7/2026

# What this checks:
# 1. Long enough (8+ characters)
# 2. Not a common password
# 3. Has a number
# 4. Has an uppercase letter
# 5. Has a special character
# Each rule = 1 point
# Total score = 0-5

# How to run it:
# Open terminal and run: python password_checker.py

def load_bad_passwords(filename):
    """
    Loads a list of common bad passwords from a file.

    :param filename: Name of the text file containing bad passwords
    :return: A set of bad passwords for fast lookup
    """
    bad_passwords = set()

    with open(filename, "r") as file:
        for line in file:
            bad_passwords.add(line.strip().lower())

    return bad_passwords


def check_password(password, bad_passwords):
    """
    Checks a password against several simple strength rules.

    :param password: The password entered by the user
    :param bad_passwords: A set of known common passwords
    :return: A score (0–5) and a list of explanations
    """
    score = 0
    reasons = []

    # Rule 1: length
    if len(password) >= 8:
        score += 1
        reasons.append("Password is at least 8 characters long.")
    else:
        reasons.append("Password is too short (needs at least 8 characters).")

    # Rule 2: common / bad passwords
    if password.lower() in bad_passwords:
        reasons.append("Password is too common.")
    else:
        score += 1
        reasons.append("Password is not a common password.")

    # Rule 3: has at least one number
    has_number = False
    for char in password:
        if char.isdigit():
            has_number = True

    if has_number:
        score += 1
        reasons.append("Password has a number.")
    else:
        reasons.append("Password needs at least one number.")

    # Rule 4: has at least one uppercase letter
    has_upper = False
    for char in password:
        if char.isupper():
            has_upper = True

    if has_upper:
        score += 1
        reasons.append("Password has an uppercase letter.")
    else:
        reasons.append("Password needs at least one uppercase letter.")

    # Rule 5: has at least one special character
    special_chars = "!@#$%^&*()-_+="
    has_special = False

    for char in password:
        if char in special_chars:
            has_special = True

    if has_special:
        score += 1
        reasons.append("Password has a special character.")
    else:
        reasons.append("Password needs at least one special character.")

    return score, reasons


def main():
    """
    Runs the password strength checker program.

    Asks the user for a password, checks it,
    and prints the results to the screen.
    """
    bad_passwords = load_bad_passwords("bad_passwords.txt")
    password = input("Enter a password: ")

    score, reasons = check_password(password, bad_passwords)

    print("\nResults:")
    for reason in reasons:
        print("-", reason)

    print("\nScore:", score, "/ 5")

    if score <= 2:
        print("Overall strength: WEAK")
    elif score <= 4:
        print("Overall strength: OK")
    else:
        print("Overall strength: STRONG")


# This runs main() when we run the file
if __name__ == "__main__":
    main()
