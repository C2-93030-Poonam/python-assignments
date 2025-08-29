# Using for loop, write and run a Python program to find factorial from 0 to 10.



for n in range(0, 11):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    print(f"Factorial of {n} is {factorial}")