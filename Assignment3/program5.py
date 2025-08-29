# Define a function overlapping() that takes two lists and returns True if they have at least one member in
# common, False otherwise

 
def overlapping(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False

list_a = [1, 2, 3, 4]
list_b = [5, 6, 3, 7]

result = overlapping(list_a, list_b)
print("List are overlapping or not???", result)