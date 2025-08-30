# In following text count occurrence of each letter 
# (irrespective of case).
# Hint: convert string to same case e.g. text.lower(). Do not use Counter collection.
 #text = """Python is a high-level general-purpose programming language. Its design philosophy
 #emphasizes code readability with the use of significant indentation. Python is dynamically typed and
 #garbage-collected. It supports multiple programming paradigms, including structured, object-oriented
 #and functional programming.""""



text = """Python is a high-level general-purpose programming language. Its design philosophy
emphasizes code readability with the use of significant indentation. Python is dynamically typed and
garbage-collected. It supports multiple programming paradigms, including structured, object-oriented
and functional programming."""

#text = text.upper()
text=text.lower()

letter_count = {}

for char in text:
    if char.isalpha():
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1

for letter in sorted(letter_count):
 print(f"{letter} : {letter_count[letter]}")





       


