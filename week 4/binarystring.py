def generate_binary_strings(n, current=""):
    if len(current) == n:
        print(current)  # Print the binary string when length reaches n
        return
    
    # Recursive calls: Append '0' and '1' to generate all possible combinations
    generate_binary_strings(n, current + "0")
    generate_binary_strings(n, current + "1")

# Taking user input
n = int(input("Enter the length of binary strings: "))

print(f"All {n}-bit binary strings:")
generate_binary_strings(n)