#write a function to return simple interest.
# 1 / 2
# To calculate simple interest, you can use the formula: SI = (P × R × T) / 100
# SI: Stands for simple interest
# P: Represents the principal amount
# R: Represents the interest rate per year
# T: Represents the time in year

def calculate_simple_interest(principal, rate, time):
    
    simple_interest = (principal * rate * time) / 100
    return simple_interest

P = float(input("Enter the principal amount (Rs): "))
R = float(input("Enter the annual interest rate (%): "))
T = float(input("Enter the time in years: "))

SI = calculate_simple_interest(P, R, T)
print(f"\nSimple Interest: Rs {SI:.2f}")