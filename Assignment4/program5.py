#Write a Python program that adds two lists element-wise using
#  the map() function.
# Input:
#    list1 = [1, 2, 3, 4, 5]
#    list2 = [5, 4, 3, 2, 1]
# Expected Output:
#   [6, 6, 6, 6, 6]


list1 = [1, 2, 3, 4, 5]
list2 = [5, 4, 3, 2, 1]

result = list(map(lambda x, y: x + y, list1, list2))

print("Element-wise sum:", result)