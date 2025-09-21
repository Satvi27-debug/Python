def palindrome(s):
    s = s.lower().replace(" ", "")  # Convert to lowercase & remove spaces
    return s == s[::-1]  # Compare the string with its reverse

# Example usage
word = input("Enter a word or phrase: ")

# Checking if it's a palindrome
if palindrome(word):
    print("The given string is a palindrome.")
else:
    print("The given string is not a palindrome.")