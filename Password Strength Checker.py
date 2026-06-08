#Decode Labs Project 1: Password Strength Checker
#Author: [Karan]

import string
def check_password_strength(password):
    common_passwords = ['password', '123456', '12345678', 'qwerty', 'abc123', 'monkey', 'letmein', 'dragon', '111111', 'baseball']
    score = 0
    feedback = []
    if len(password) < 8:
        print("Password is too short. It should be at least 8 characters.")
        return
    elif len(password) < 12:
        score += 1
    else:
        score += 2
    
    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("Password should include lowercase letters.")

    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Password should include uppercase letters.")

    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Password should include numbers.")

    if any(char in string.punctuation for char in password):
        score += 1
    else:
        feedback.append("Password should include special characters.")
    
    if password in common_passwords:
        feedback.append("Password is too common. Please choose a more unique password.")

    if len(set(password)) <= 2:
        feedback.append("Password contains too many repeated characters.")
        score -= 1

    if score < 0:
        score = 0
    
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    elif score <= 6:
        strength = "Strong"
    else:
        strength = "Very Strong"

    print(f"Password Strength: {strength}")
    print(f"Password Score: {score}/6")
    if feedback:
        print("Suggestions for improvement:")
        for suggestion in feedback:
            print(f" - {suggestion}")
    else:
        print("Your password is strong. No suggestions for improvement.")
    

print("=======Password Strength Checker=======\n\n")

password = input("Enter your password:\t")
check_password_strength(password)
