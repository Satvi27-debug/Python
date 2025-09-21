def is_sorted(lst):
    return lst == sorted(lst)  # Compare the list with its sorted version

# Example usage
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Checking if the list is sorted
if is_sorted(numbers):
    print("The list is sorted in ascending order.")
else:
    print("The list is not sorted.")