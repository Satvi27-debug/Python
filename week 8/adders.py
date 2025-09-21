def half_adder(a, b):
    sum_bit = a ^ b  # XOR operation
    carry_bit = a & b  # AND operation
    return sum_bit, carry_bit

def full_adder(a, b, carry_in):
    sum1, carry1 = half_adder(a, b)
    sum2, carry2 = half_adder(sum1, carry_in)
    carry_out = carry1 | carry2  # OR operation to get final carry
    return sum2, carry_out

def parallel_adder(A, B):
    n = len(A)  # Assuming A and B have the same length
    carry = 0
    result = []

    for i in range(n - 1, -1, -1):  # Perform bit-wise addition from LSB to MSB
        sum_bit, carry = full_adder(A[i], B[i], carry)
        result.insert(0, sum_bit)  # Insert at the beginning to maintain order

    result.insert(0, carry)  # Final carry bit
    return result

# Example usage
a, b = 1, 1
sum_bit, carry_bit = half_adder(a, b)
print(f"Half Adder: {a} + {b} -> Sum: {sum_bit}, Carry: {carry_bit}")

x, y, c_in = 1, 1, 0
sum_bit, carry_out = full_adder(x, y, c_in)
print(f"Full Adder: {x} + {y} + Carry In {c_in} -> Sum: {sum_bit}, Carry Out: {carry_out}")

A = [1, 0, 1, 1]  # 4-bit binary number
B = [1, 1, 0, 1]  # 4-bit binary number
print("Parallel Adder Result:", parallel_adder(A, B))