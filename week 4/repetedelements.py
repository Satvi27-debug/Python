# 1. Check for Duplicates
def has_duplicates(lst):
    return len(lst) != len(set(lst))

# 2. Remove Duplicates
def remove_duplicates(lst):
    return list(set(lst))

# 3. Add "I", "a", and "" to a Given Word List
def add_missing_words(word_list):
    word_list.update({"I", "a", ""})
    return word_list

# 4. Invert Dictionary
def invert_dict(d):
    return {v: k for k, v in d.items()}

# User Inputs
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Checking for duplicates
if has_duplicates(numbers):
    print("The list contains duplicates.")
else:
    print("The list has all unique elements.")

# Removing duplicates and displaying unique list
unique_numbers = remove_duplicates(numbers)
print("List with unique elements:", unique_numbers)

# Word List Modification
words = {"hello", "world", "python"}  # Example word list
modified_words = add_missing_words(words)
print("Modified word list:", modified_words)

# Dictionary Inversion
user_dict = {}
n = int(input("Enter the number of dictionary elements: "))
for _ in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    user_dict[key] = value

inverted_dict = invert_dict(user_dict)
print("Inverted Dictionary:", inverted_dict)