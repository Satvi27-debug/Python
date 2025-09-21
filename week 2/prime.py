import math

# Function to print prime numbers in a given range
def print_primes(start, end):
    print(f"Prime numbers between {start} and {end}:")
    for num in range(start, end + 1):
        if num > 1:  # Prime numbers are greater than 1
            is_prime = True
            for i in range(2, int(math.sqrt(num)) + 1):  # Check divisibility
                if num % i == 0:
                    is_prime = False
                    break  # Exit loop if a divisor is found
            if is_prime:
                print(num, end=" ")

# Taking user input for range
start = int(input("Enter the start of the interval: "))
end = int(input("Enter the end of the interval: "))

# Calling function to print prime numbers
print_primes(start, end)