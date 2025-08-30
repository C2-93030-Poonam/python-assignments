#Define a function subtract() that takes two lists and returns difference 
#(i.e. excess elements from list1).
# If list1 = [10, 20, 30, 40] and
# list2 = [30, 40, 50, 60], then result should be [10, 20].


def subtract(list1, list2):
    result = [item for item in list1 if item not in list2]
    return result

list1 = [10 , 20 , 30 , 40]
list2 = [30 , 40 , 50 , 60]

print(subtract(list1, list2))