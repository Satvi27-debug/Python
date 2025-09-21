def gcd(a, b):
    while b:
        a, b = b, a % b  # Replace a with b, and b with a % b
    return a

# Example usage
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Calling the function
result = gcd(num1, num2)

# Displaying result
print(f"GCD of {num1} and {num2} is: {result}")