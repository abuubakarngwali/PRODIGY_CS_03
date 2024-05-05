import re

def password_strength(password):
    # Criteria
    length_criteria = len(password) >= 8
    uppercase_criteria = any(char.isupper() for char in password)
    lowercase_criteria = any(char.islower() for char in password)
    digit_criteria = any(char.isdigit() for char in password)
    special_char_criteria = bool(re.search(r'[!@#$%^&*()_+{}[\]:;"\'|\\<,>.?/]', password))

    # Score
    score = sum([length_criteria, uppercase_criteria, lowercase_criteria, digit_criteria, special_char_criteria])

    # Feedback
    if score >= 5:
        return "Strong password! Fantastic "
    elif score >= 3:
        return "Medium strength password. please add more complexity."
    elif score >= 1:
        return "Weak password. Please consider adding more characters and complexity."
    else:
        return "Very weak password. you are in the risk of being attacked."

def main():
    password = input("Enter your password: ")
    strength = password_strength(password)
    print(strength)

if __name__ == "__main__":
    main()
