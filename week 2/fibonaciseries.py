# Taking user input for number of terms
n = int(input("Enter the number of terms: "))

# Initializing first two terms
a, b = 0, 1
count = 0

# Printing Fibonacci sequence using while loop
print("Fibonacci Sequence:")
while count < n:
    print(a, end=" ")  # Print the current term
    temp = a + b  # Compute next term
    a = b  # Update 'a' to next
    b = temp  # Update 'b' to next
    count += 1  # Increment count