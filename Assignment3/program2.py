# Write a program that accepts a list from user and print the alternate element of list.

user_input = input("Enter list elements separated by spaces: ")

elements = user_input.split()

print("\nAlternate elements of the list:")
for i in range(0, len(elements), 2):
    print(elements[i])