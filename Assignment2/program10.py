# write a function to return compound interest.
# CI = P (1 + r/n) ^ nt
# P - Principal Amount
# r - Rate of interest
# n - Number of times interest compounds in a year
# t - Number of years

def calculate_compound_interest(P, r, n, t):
    amount = P * (1 + r / n) ** (n * t)
    compound_interest = amount - P
    return compound_interest


P = float(input("Enter the principal amount (Rs): "))
r_percent = float(input("Enter the annual interest rate (%): "))
n = int(input("Enter number of times interest compounds per year: "))
t = float(input("Enter the number of years: "))

r = r_percent / 100

CI = calculate_compound_interest(P, r, n, t)
print(f"\nCompound Interest: Rs {CI:.2f}")