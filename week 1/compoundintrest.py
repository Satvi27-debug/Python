# Function to calculate compound interest
def compound_interest(principal, rate, time):
    amount = principal * (1 + rate / 100) ** time
    interest = amount - principal
    return amount, interest

# Taking user input
P = float(input("Enter the principal amount: "))
R = float(input("Enter the annual interest rate (in %): "))
T = int(input("Enter the number of periods (years): "))

# Calculating compound interest
final_amount, interest_earned = compound_interest(P, R, T)

# Displaying results
print(f"Final Amount after {T} years: {final_amount:.2f}")
print(f"Total Interest Earned: {interest_earned:.2f}")