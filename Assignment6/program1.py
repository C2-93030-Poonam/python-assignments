# Extract all odd numbers from a given list using list comprehension.
# numbers = [1, 2, 3, 4, 5, 6, 7]



numbers = [1, 2, 3, 4, 5, 6, 7]
odd_numbers = [num for num in numbers if num % 2 != 0]
print(odd_numbers)