# Write a function filter_long_words() that takes a list of words and an integer len and returns the list of
# words that are longer than len


def filter_long_words():
    
    words_input = input("Enter words separated by spaces: ")
    length = int(input("Enter the minimum length: "))

    words = words_input.split()

    long_words = [word for word in words if len(word) > length]

    return long_words

result = filter_long_words()
print("Words longer than the given length:", result)