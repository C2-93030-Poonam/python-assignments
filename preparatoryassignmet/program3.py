# Program to generate Fibonacci Series up to n numbers

n = int(input("Enter the number of terms: "))

if n <= 0:
    print("Please enter a positive integer.")
else:
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b

    print("Fibonacci Series:")
    print(fib_series)