password = input("Enter your password: ")

score = 0
feedback = []

if len(password) < 8:
    feedback.append("Password too short — minimum 8 characters.")
elif len(password) >= 12:
    score += 2
else:
    score += 1

has_upper = False
for ch in password:
    if ch >= 'A' and ch <= 'Z':
        has_upper = True
        break
if has_upper:
    score += 1
else:
    feedback.append("Add at least one uppercase letter.")

has_lower = False
for ch in password:
    if ch >= 'a' and ch <= 'z':
        has_lower = True
        break
if has_lower:
    score += 1
else:
    feedback.append("Add at least one lowercase letter.")

has_number = False
for ch in password:
    if ch >= '0' and ch <= '9':
        has_number = True
        break
if has_number:
    score += 1
else:
    feedback.append("Include at least one number.")

specials = "!@#$%^&*(),.?\":{}|<>"
has_special = False
for ch in password:
    if ch in specials:
        has_special = True
        break
if has_special:
    score += 1
else:
    feedback.append("Use at least one special character (!, @, #, etc.).")

if score <= 2:
    strength = "Weak"
elif score == 3 or score == 4:
    strength = "Moderate"
else:
    strength = "Strong"

print("\nPassword Strength:", strength)

if feedback:
    print("Suggestions:")
    for tip in feedback:
        print("-", tip)
