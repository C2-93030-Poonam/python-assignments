# Write a function translate() that will translate a text into "rövarspråket" (Swedish for "robber's
# language"). That is, double every consonant and place an occurrence of "o" in between. For example,
# translate("this is fun") should return the string "tothohisos isos fofunon".
 #Rule: Double every consonant, place "o" in between

def translate(text):
    vowels = 'aeiouAEIOU'
    result = ''
    for char in text:
        if char.isalpha() and char not in vowels:
            result += char + 'o' + char
        else:
            result += char
    return result

print(translate("this is fun"))