import string 
import random
import getpass

def check_password_strength(password):
    issues = []
    if len(password) < 8:
        issues.append("Password is too short. it should be minimum 8 characters")
    if not any(c.islower() for c in password):
        issues.append("Missing lowercase letter")
    if not any(c.isupper() for c in password):
        issues.append("Missing uppercase letter")
    if not any(c in string.punctuation for c in password):
        issues.append("Missing special character")
    return issues

def generate_strong_password(lenght = 12):
    chars = string.ascii_letters + string.digits + string.punctuation
    
    return "".join(random.choice(chars) for _ in range(lenght))

password = getpass.getpass("Enter your password: ")
issues = check_password_strength(password)

if not issues:
    print("Your password is strong. You are good to go...")
else:
    print("You got a weak password")
    for issue in issues:
        print(f" - {issue}")

yes_or_no = input("Do you need a password suggestion?(y/n) ")
if(yes_or_no == "y"): 
    suggestion = generate_strong_password()
    print("Suggesting you a password...")
    print(suggestion)
    print("Thank you...")
else:
    print("Thank you...")


