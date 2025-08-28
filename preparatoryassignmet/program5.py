# Write a program to check the input characters for uppercase, 
#lowercase, number of digits and other characters. Display appropriate 
#message.

text = input("Enter a string: ")

uppercase = 0
lowercase = 0
digits = 0
others = 0

for char in text:
    if char.isupper():
        uppercase += 1
    elif char.islower():
        lowercase += 1
    elif char.isdigit():
        digits += 1
    else:
        others += 1

print("\nCharacter Classification:")
print(f"Uppercase letters: {uppercase}")
print(f"Lowercase letters: {lowercase}")
print(f"Digits: {digits}")
print(f"Other characters: {others}")