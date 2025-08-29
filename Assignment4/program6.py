#Write a Python program that filters out all strings that have 
# more than 5 characters from a list of strings
# using the filter() function.
# Input:
#   words = ['Red', 'Green', 'Yellow', 'Purple', 'Orange']
# Output:
#    ['Yellow', 'Purple', 'Orange']



words = ['red' , 'green' , 'yellow' , 'purple' , 'orange' ,]

longer_words = list(filter(lambda x: len(x) > 5, words))

print("longer words are:" , longer_words)