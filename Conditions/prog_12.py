#This program checks multiple passwords and generates a detailed security report.
def audit_password(password: str) -> dict:
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special_character = False
    special_characters = "!@#$%^&*()_+-=[]{}|;:,.<>?"

    for character in password:
        if character.isupper():
            has_uppercase = True
        elif character.islower():
            has_lowercase = True
        elif character.isdigit():
            has_digit = True
        elif character in special_characters:
            has_special_character = True

    issues = []

    if len(password) < 10:
        issues.append("Password must contain at least 10 characters.")

    if not has_uppercase:
        issues.append("An uppercase letter is required.")

    if not has_lowercase:
        issues.append("A lowercase letter is required.")

    if not has_digit:
        issues.append("A number is required.")

    if not has_special_character:
        issues.append("A special character is required.")

    return {
        "is_secure": len(issues) == 0,
        "issues": issues
    }


user_passwords = {
    "admin": "Admin123",
    "manager": "Manager@2026",
    "developer": "pythondeveloper",
    "auditor": "Secure#Audit90"
}

print("\nPASSWORD SECURITY AUDIT")
print("=" * 65)

for username, password in user_passwords.items():
    result = audit_password(password)

    print(f"Username : {username}")

    if result["is_secure"]:
        print("Status   : Secure password")
    else:
        print("Status   : Weak password")

        for issue_number, issue in enumerate(
            result["issues"],
            start=1
        ):
            print(f"  {issue_number}. {issue}")

    print("-" * 65)