#Write a Python program that calculates the sum of the squares of all
#  odd numbers in a list of integers
# using map() and filter().
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

squared_odds = list(map(lambda x: x ** 2, odd_numbers))
print(f"square of odd numbers:", squared_odds)

sum_of_squares_of_odd_numbers = sum(squared_odds)

print("Sum of squares of odd numbers:", sum_of_squares_of_odd_numbers)