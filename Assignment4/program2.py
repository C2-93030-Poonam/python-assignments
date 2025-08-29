#Write a Python program to double all numbers in a given list of integers. Use Python map, lambda
# function.
# list1 = [1,2,3,4,5,6,7,8,9]

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

doubled_numbers = list(map(lambda x: x * 2, list1))

print("Doubled numbers:", doubled_numbers)