# Write a program that reads a string from keyboard and display:
# a) The number of uppercase letters in the string
# b) The number of lowercase letters in the string
# d) The number of whitespace characters in the string

text = input("Enter a string: ")

uppercase_count = sum(1 for char in text if char.isupper())
lowercase_count = sum(1 for char in text if char.islower())
digit_count     = sum(1 for char in text if char.isdigit())
space_count     = sum(1 for char in text if char.isspace())

print("Uppercase letters:", uppercase_count)
print("Lowercase letters:", lowercase_count)
print("Digits:", digit_count)
print("Whitespace characters:", space_count)