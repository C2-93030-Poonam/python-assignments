#. Write a program in Python to read a string from the keyboard. Replace each ‘This’ word with ‘That’
# word in this String.
# Example:
# Input: This is me and This is my python program.
# Output: That is me and That is my python program


text = input("Enter a sentence: ")

updated_text = text.replace("This", "That")

print("Updated sentence:", updated_text)
