# 2. Extract vowels from a string using list comprehension. 
#(Input: "education")


input_str = "education"
vowels = [char for char in input_str if char.lower() in 'aeiou']
print(vowels)