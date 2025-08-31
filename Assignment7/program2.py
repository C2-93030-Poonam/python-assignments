# Write a version of a palindrome recognizer that also accepts phrase palindromes such as
# "Go hanga salami I'm a lasagna hog.",
# "Was it a rat I saw?",
# "Step on no pets",
# "Sit on a potato pan, Otis",
# "Lisa Bonet ate no basil",
# "Satan, oscillate my metallic sonatas",
# "I roamed under it as a tired nude Maori",
# "Rise to vote sir", or the exclamation "Dammit, I'm mad!".
# Note: that punctuation, capitalization, and spacing are usually ignored

import string

def is_phrase_palindrome(text):
   
    cleaned = ''.join(char.lower() for char in text if char.isalpha())
    
    return cleaned == cleaned[::-1]


examples = [
    "Go hanga salami I'm a lasagna hog.",
    "Was it a rat I saw?",
    "Step on no pets",
    "Sit on a potato pan, Otis",
    "Lisa Bonet ate no basil",
    "Satan, oscillate my metallic sonatas",
    "I roamed under it as a tired nude Maori",
    "Rise to vote sir",
    "Dammit, I'm mad!"
]

for phrase in examples:
    print(f'"{phrase}" → {is_phrase_palindrome(phrase)}')