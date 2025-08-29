# Write a Python program that finds the longest word in a list of strings. Use map() to calculate the length
# of each word, and filter() to get the word with the maximum length.
#    words = ["python", "functional", "programming", "is", "powerful"



words = ["python" , "functional" , "programming" , "is" , "powerful"]

lenghts = list(map(len, words))
print("lenght of words:" , lenghts)

max_lenght = max(lenghts)

max_lenght_words = list(filter(lambda x:len(x) == max_lenght, words))

print("Maximum lenght words are:", max_lenght_words)





