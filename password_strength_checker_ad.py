# Password Strength Checker

import re

# Password Strength Check Conditions (each contributes to an overall score):
# Length >= 8, Length >= 12, digit, uppercase, lowercase, special character, no common patterns


def check_password_strength(password):
    """
    Analyzes a password and returns:
        - score (int): points earned out of max_score
        - percentage (int): strength as a percentage (0-100)
        - label (str): Weak / Medium / Strong / Very Strong
        - recommendations (list[str]): tips to improve the password
    """
    recommendations = []
    score = 0
    max_score = 7

    # 1. Minimum length
    if len(password) >= 8:
        score += 1
    else:
        recommendations.append("Use at least 8 characters.")

    # 2. Good length (bonus for longer passwords)
    if len(password) >= 12:
        score += 1
    else:
        recommendations.append("Use 12+ characters for stronger protection.")

    # 3. Contains a digit
    if any(char.isdigit() for char in password):
        score += 1
    else:
        recommendations.append("Add at least one number (0-9).")

    # 4. Contains an uppercase letter
    if any(char.isupper() for char in password):
        score += 1
    else:
        recommendations.append("Add at least one uppercase letter (A-Z).")

    # 5. Contains a lowercase letter
    if any(char.islower() for char in password):
        score += 1
    else:
        recommendations.append("Add at least one lowercase letter (a-z).")

    # 6. Contains a special character
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        recommendations.append("Add at least one special character (!@#$%^&* etc).")

    # 7. Avoids common/predictable patterns
    common_patterns = [
        "password", "123456", "qwerty", "letmein", "admin",
        "welcome", "abc123", "111111", "iloveyou"
    ]
    if not any(pattern in password.lower() for pattern in common_patterns):
        score += 1
    else:
        recommendations.append("Avoid common words or predictable sequences (e.g. 'password', '123456').")

    percentage = round((score / max_score) * 100)

    if percentage < 40:
        label = "Weak"
    elif percentage < 70:
        label = "Medium"
    elif percentage < 100:
        label = "Strong"
    else:
        label = "Very Strong"

    return {
        "score": score,
        "max_score": max_score,
        "percentage": percentage,
        "label": label,
        "recommendations": recommendations,
    }


def print_strength_meter(percentage, bar_length=30):
    """
    Prints a simple text-based strength meter bar.
    """
    filled_length = int(bar_length * percentage // 100)
    bar = "█" * filled_length + "-" * (bar_length - filled_length)
    print(f"[{bar}] {percentage}%")


def password_checker():
    """
    Main function to take user input and check password strength.
    """
    print("Welcome! TO THE PASSWORD STRENGTH CHECKER <3")

    while True:
        password = input("\nEnter your password (or type 'exit' to quit): ")

        if password.lower() == "exit":
            print("Thank you for using the Password Strength Checker! Goodbye!")
            break

        result = check_password_strength(password)

        print(f"\nStrength: {result['label']} ({result['percentage']}%)")
        print_strength_meter(result["percentage"])

        if result["recommendations"]:
            print("\nRecommendations to improve your password:")
            for tip in result["recommendations"]:
                print(f"  - {tip}")
        else:
            print("\nGreat job! Your password meets all strength criteria.")


# Run the password checker
if __name__ == "__main__":
    password_checker()