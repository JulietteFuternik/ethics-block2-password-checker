# ethics-block2-password-checker
Password strength checker for CS 3090 ethics project

## Password Strength Checker
This project is a Python program that checks the strength of a password
using a set of clear rules. The program returns a score (0–5), an overall
rating (WEAK, OK, or STRONG), and explanations for why the password received
that score.

# ---- What the program does ----
The program checks a password against five rules. Each rule is worth one point:
1. The password is at least 8 characters long  
2. The password is not a common password  
3. The password contains at least one number  
4. The password contains at least one uppercase letter  
5. The password contains at least one special character

# ---- How to run the program ----
## Requirements
- Python 3  
- No external libraries are required

## Run instructions
From the project folder, run:
python password_checker.py

When prompted, enter a password to see its score and strength rating.
"Enter a password: "

## Files in this repository
password_checker.py - the main program
bad_passwords.txt - a small list of common passwords used for comparison

# ---- Warnings and limitations ----
!!!! This tool is for educational use only and should not be used for securing sensitive information. !!!!
- This tool is for educational purposes only and should not be used to secure real accounts.
- The list of common passwords is very limited and does not represent real-world breach databases.
- The scoring system is simplistic and does not reflect real-world password security.
- A password rated as “STRONG” by this tool may still be insecure in practice.

# ---- Ethical considerations and responsible use ----
This tool is intended to demonstrate basic password security concepts in an educational context.
Potential risks include giving users a false sense of security or being modified to collect or store
passwords, which would be unethical.

Responsible use guidelines:
- Only test passwords that you own or have permission to test.
- Do not store, log, or transmit passwords entered into the program.
- Treat the results as guidance, not a guarantee of security.


