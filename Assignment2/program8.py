# Write a program that prompts the user to input a character and determine the character is vowel or
# consonant

def isLowercaseVowel(c):
    return c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u'


def isUppercaseVowel(c):
    
    return c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U'


c = input("Enter a alphabet:")

if not c.isalpha():
    print("Non alphabet")
elif isLowercaseVowel(c) or isUppercaseVowel(c):
    print(f"{c} is a Vowel")
else:
    print(f"{c} is a consonant")