def AND_gate(a, b):
    return a & b

def OR_gate(a, b):
    return a | b

def NOT_gate(a):
    return 1 - a  # Assuming binary values (0 or 1)

def XOR_gate(a, b):
    return a ^ b

# Example usage
print("AND Gate: 1 AND 1 =", AND_gate(1, 1))
print("AND Gate: 1 AND 0 =", AND_gate(1, 0))
print("OR Gate: 1 OR 0 =", OR_gate(1, 0))
print("OR Gate: 0 OR 0 =", OR_gate(0, 0))
print("NOT Gate: NOT 1 =", NOT_gate(1))
print("NOT Gate: NOT 0 =", NOT_gate(0))
print("XOR Gate: 1 XOR 0 =", XOR_gate(1, 0))
print("XOR Gate: 1 XOR 1 =", XOR_gate(1, 1))