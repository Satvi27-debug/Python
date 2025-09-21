import re

def validate_phone(phone):
    pattern = r"^\+?[0-9]{10,15}$"  # Supports optional '+' and 10-15 digits
    return re.match(pattern, phone) is not None

def validate_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA0-9.-]+\.[a-zA-Z]{2,}$"  # Standard email pattern
    return re.match(pattern, email) is not None

# Read input from user
phone = input("Enter phone number: ")
email = input("Enter email ID: ")

# Validate phone number and email
if validate_phone(phone):
    print("Valid phone number")
else:
    print("Invalid phone number")

if validate_email(email):
    print("Valid email ID")
else:
    print("Invalid email ID")