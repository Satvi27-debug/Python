# Taking user input
char = input("Enter a single character: ")

# Checking the type of character
if char.isdigit():
    print("The input is a Digit.")
elif char.islower():
    print("The input is a Lowercase Letter.")
elif char.isupper():
    print("The input is an Uppercase Letter.")
else:
    print("The input is a Special Character.")