def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

def add_matrices(A, B):
    n = len(A)
    return [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]

def multiply_matrices(A, B):
    n = len(A)
    result = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]

    return result

# Define two square matrices
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

print("Matrix 1:")
print_matrix(matrix1)
print("\nMatrix 2:")
print_matrix(matrix2)

# Matrix Addition
sum_matrix = add_matrices(matrix1, matrix2)
print("\nMatrix Addition Result:")
print_matrix(sum_matrix)

# Matrix Multiplication
product_matrix = multiply_matrices(matrix1, matrix2)
print("\nMatrix Multiplication Result:")
print_matrix(product_matrix)