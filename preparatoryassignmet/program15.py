

# Program to count occurrences of each alphabet (case-insensitive)

text = input("Enter a string: ")

text = text.lower()

alphabet_count = {}

for char in text:
    if char.isalpha():  
        if char in alphabet_count:
            alphabet_count[char] += 1
        else:
            alphabet_count[char] = 1

print("\nAlphabet Occurrences:")
for letter in sorted(alphabet_count):
    print(f"{letter}: {alphabet_count[letter]}")