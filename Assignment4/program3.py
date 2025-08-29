#Write a Python program to convert a given list of integers and a tuple
#  of integers into a list of strings.
# Use Python map

int_list = [1, 2, 3, 4, 5]
int_tuple = (6, 7, 8, 9, 10)

string_list = list(map(str, int_list))

string_tuple = list(map(str, int_tuple))

print("List converted to strings:", string_list)
print("Tuple converted to strings:", string_tuple)