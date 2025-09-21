# Printing the triangle pattern
for i in range(5, 0, -1):  # Loop from 5 to 1
    print((str(i) + " ") * (6 - i))  # Print i, (6-i) times

print(" ")

n = int(input("Enter a value for n:"))
for i in range(n, 0, -1):
    for j in range(n - i + 1):
        print(i, end = " ")
    print()