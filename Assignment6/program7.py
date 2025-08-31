#List all consonants in the string “Yellow Yaks like yelling and yawning and yesterday they 
#yodeled while eating yuky yams”.

text = "Yellow Yaks like yelling and yawning and yesterday they yodeled while eating yuky yams"
consonants = [char for char in text.lower() if char.isalpha() and char not in 'aeiou']
print(consonants)
 