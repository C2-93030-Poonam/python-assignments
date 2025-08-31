# Generate all possible pairs from two strings using list comprehension.
# Input: "ab" and "cd"

str1 = "ab"
str2 = "cd"
pairs = [(a, b) for a in str1 for b in str2]
print(pairs)