# Count the number of spaces in a string

#(using comprehension)

text = "jkasjdk kjdi jdk kjei jiwj"
space_count = sum([1 for char in text if char == ' '])
print(space_count)