import string

def password_strength(password):
    # Conditions check
    length = len(password) >= 8
    upper = any(c.isupper() for c in password)
    lower = any(c.islower() for c in password)
    digit = any(c.isdigit() for c in password)
    special = any(c in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/~`" for c in password)

    # Result
    if all([length, upper, lower, digit, special]):
        return "✅ Strong Password"
    else:
        issues = []
        if not length:
            issues.append("- Password must be at least 8 characters")
        if not upper:
            issues.append("- Include at least one uppercase letter (A-Z)")
        if not lower:
            issues.append("- Include at least one lowercase letter (a-z)")
        if not digit:
            issues.append("- Include at least one number (0-9)")
        if not special:
            issues.append("- Include at least one special character (!@#$%^&*)")
        return "❌ Weak Password:\n" + "\n".join(issues)

def main():
    print("🔒 Password Strength Checker 🔒")
    password = input("Enter your password: ")
    result = password_strength(password)
    print("\n" + result)

if __name__ == "__main__":
    main()
